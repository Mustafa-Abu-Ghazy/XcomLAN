# -*- coding: utf-8 -*-
"""
This file contains definition/implementation of a NodeManager Class that Manages the Devices found on the SCOM bus.
Inspired from and Based on hesso-valais/scom : devicemanager.py
<https://github.com/hesso-valais/scom/blob/0.7.3/src/sino/scom/dman/devicemanager.py>
"""

import gc
import logging
import sys
import time
from threading import Thread

import serial
from sino.scom import defines
from sino.scom.baseframe import BaseFrame
from sino.scom.property import Property

from ..device import BaseDevice
from ..device import DeviceFactory
from ..device import DeviceType
from ..scom import Scom


# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------  NodeManager Class  ----------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class NodeManager(object):
    """
    Manages the Devices found on the SCOM bus.

    Requirements:
    - The NodeManager scans regularly for Devices on the SCOM bus of the Xcom-232i node and notifies
      the NodeObservers about changes.
    - The NodeManager is responsible to create an instance for every SCOM device found.
    - The Node Manager needs to hold a list of present devices.
    - In case a device appears on the SCOM bus it notifies the concerning observers with on_device_connected.
    - In case a device disappears, it notifies the observers with onDeviceDisconnect.
    - Scom RX errors are checked regularly and after too many errors the application gets terminated.
    """

    DEFAULT_RX_BUFFER_SIZE = 1024

    def __init__(self, node_name, scom=None, config=None, address_scan_info=None,
                 control_interval_in_seconds=5.0, thread_monitor=None):
        # Attribute initialization
        self._node_name = node_name
        self.log = logging.getLogger(__name__ + ":" + self._node_name)
        self._thread_should_run = True
        self._thread_left_run_loop = False  # Set to true when _thread is leaving run loop
        self._control_interval_in_seconds = control_interval_in_seconds
        self._subscribers = []  # type: [dict]
        self._devices = {}  # type: {int: BaseDevice}
        self._scom_rx_error_message_send = False  # type: bool

        if scom:
            self._scom = scom
            self._scom.node_name = self._node_name
        else:
            assert config, 'In case \'scom\' is not set the parameter config must be given!'

            studer_com = Scom(node_name=self._node_name)

            studer_com.initialize(
                com_port=config['scom']['interface'],
                baudrate=config['scom']['baudrate'] if 'baudrate' in config['scom'] else 115200,
                parity=config['scom']['parity'] if 'parity' in config['scom'] else serial.PARITY_NONE,
            )

            self._scom = studer_com

        if address_scan_info:
            self._address_scan_info = address_scan_info
        else:
            assert config, 'In case \'address_scan_info\' is not set the parameter config must be given!'
            assert config.get('scom-device-address-scan'), 'Missing section \'scom-device-address-scan\' in config'

            # Load device address to scan
            self._address_scan_info = {}
            for device_type in config['scom-device-address-scan']:
                if True or DeviceType.has_value(device_type):
                    self._address_scan_info[device_type] = config['scom-device-address-scan'][device_type]

        # Do some checks on 'self._address_scan_info'
        assert isinstance(self._address_scan_info, dict), 'Address scan info must be a dictionary'
        for device_type, scan_info in self._address_scan_info.items():
            assert len(scan_info) == 2, 'Need two values for scan info'

        self._thread = Thread(target=self._run_with_exception_logging)
        self._thread.name = self.__class__.__name__ + self._thread.name
        self._thread.setDaemon(True)  # Close thread as soon as main thread exits
        if thread_monitor:
            # Register thread for later monitor of itself. Thread monitor allows to take action
            # in case the thread crashes.
            thread_monitor.register(self._thread)
        self._thread.start()

    @property
    def node_name(self):
        """
        Returns the Node Name.

        :return:
        """
        return self._node_name

    # ---------------------------------------------------------------------------------------------------------------- #
    # -----------------------------------------  Notifier Functions/Methods  ----------------------------------------- #
    # ---------------------------------------------------------------------------------------------------------------- #
    def subscribe(self, node_subscriber, filter_policy=('all',)):
        """
        Adds the given subscriber to the list.

        :param node_subscriber Subscriber to be added to the list
        :type node_subscriber DeviceSubscriber
        :param filter_policy The list of device types of interest
        :type filter_policy tuple[string]
        :return True if subscriber could be added, otherwise False
        """
        # Subscribe the info about the new subscriber
        self._subscribers.append({'subscriber': node_subscriber, 'filterPolicy': filter_policy})

        # Notify already present devices to new subscriber
        self._notify_subscriber(node_subscriber, filter_policy=filter_policy)
        return True

    def unsubscribe(self, node_subscriber):
        """
        Removes the given subscriber from the list.

        :param node_subscriber Subscriber to be removed from the list
        :type node_subscriber DeviceSubscriber
        :return True if subscriber could be removed, otherwise False
        """

        for index, subscriber in enumerate(self._subscribers):
            if subscriber['subscriber'] == node_subscriber:
                self._subscribers.pop(index)
                return True
        return False

    def _notify_subscriber(self, node_subscriber, filter_policy=('all',)):
        """
        Used to notify new subscribers about already present devices.
        """
        subscriber_info = {'subscriber': node_subscriber, 'filter_policy': filter_policy}

        for deviceAddress, the_device in self._devices.items():
            device_type = the_device.device_type
            if device_type in subscriber_info['filter_policy'] or 'all' in subscriber_info['filter_policy']:
                # Notify subscriber
                subscriber_info['subscriber'].on_device_connected(the_device)

    def _notify_subscribers(self, device, connected=True):
        """
        Notifies connect/disconnect of a device to all subscribers with the according filter policy.
        """
        # Notify subscribers about the device found
        for subscriberInfo in self._subscribers:
            device_type = device.device_type
            # Apply subscribers filter policy
            if device_type in subscriberInfo['filterPolicy'] or 'all' in subscriberInfo['filterPolicy']:
                # Notify subscriber
                if connected:
                    subscriberInfo['subscriber'].on_device_connected(device)
                else:
                    subscriberInfo['subscriber'].on_device_disconnected(device)

    # ---------------------------------------------------------------------------------------------------------------- #

    def stop_thread(self):
        """

        :return:
        """
        self._thread_should_run = False

    def get_number_of_instances(self, device_type):
        """

        :param device_type:
        :return:
        """
        return len([device for address, device in self._devices.items() if device.device_type == device_type])

    def get_instances_of_category(self, device_type):
        """

        :param device_type:
        :return:
        """
        return {address: device for address, device in self._devices.items() if device.device_type == device_type}

    def _run_with_exception_logging(self):
        """Same as _run but logs exceptions to the console or log file.

        This is necessary when running in testing/production environment.
        In case of an exception thrown, the stack trace can be seen in the
        log file. Otherwise there is no info why the thread did stop.
        """
        try:
            self._run()
        except Exception as e:
            logging.error(e, exc_info=True)
        finally:
            # Wait here for a while. If leaving the method directly, the thread
            # gets deleted and the is_alive() method won't work any more!
            time.sleep(5)
            return

    def _run(self):
        self.log.info(type(self).__name__ + ' thread running...')

        while self._thread_should_run:

            self._search_devices()

            self._check_scom_rx_errors()

            # Wait until next interval begins
            if self._thread_should_run:
                self._thread_sleep_interval(self._control_interval_in_seconds)

        if self._scom:
            self._scom.close()
            self._scom = None

        self.remove_all_devices()

        self._thread_left_run_loop = True

    def _thread_sleep_interval(self, sleep_interval_in_seconds, decr_value=0.2):
        """Tells the executing thread how long to sleep while being still reactive on _threadShouldRun attribute.
        """
        wait_time = sleep_interval_in_seconds

        while wait_time > 0:
            time.sleep(decr_value)
            wait_time -= decr_value
            # Check if thread should leave run loop
            if not self._thread_should_run:
                break

    def _search_devices(self):
        """Searches on the SCOM bus for devices.
        """
        assert len(self._address_scan_info), 'No device categories to scan found!'
        need_garbage_collect = False

        for device_type, addressScanRange in self._address_scan_info.items():
            device_list = self._search_device_type(device_type, addressScanRange)

            nbr_of_devices_found = len(device_list) if device_list else 0

            if device_list:
                for device_address in device_list:
                    # Check if device is present in device dict
                    if device_address in self._devices:
                        pass
                    else:
                        self._add_new_device(device_type, device_address)

            # Compare number of instantiated devices (per category/group) and remove disappeared devices from list
            if nbr_of_devices_found < self.get_number_of_instances(device_type):
                self.log.warning(u'Some ScomDevices seem to be disappeared!')
                missing_device_address_list = self._get_missing_device_addresses(device_type, device_list)

                for missingDeviceAddress in missing_device_address_list:
                    missing_device = self._devices[
                        missingDeviceAddress] if missingDeviceAddress in self._devices else None
                    assert missing_device

                    self.log.info('Studer device disappeared: %s #%d' % (device_type, missingDeviceAddress))

                    # Notify subscribers about the disappeared device
                    self._notify_subscribers(device=missing_device, connected=False)

                    # Remove studer device from list
                    self._devices.pop(missingDeviceAddress)
                    need_garbage_collect = True

        if need_garbage_collect:  # Garbage collect to update WeakValueDictionaries
            gc.collect()

    def _add_new_device(self, device_type, device_address):
        """Adds a new ScomDevice an notifies subscribers.
        """
        # Let the factory create a new SCOM device representation
        self._devices[device_address] = DeviceFactory.create(device_type, device_address, self._scom)
        self.log.info('Found new studer device: %s #%d' % (device_type, device_address))

        # Notify subscribers about the device found
        self._notify_subscribers(device=self._devices[device_address])

    def _search_device_type(self, device_type, address_scan_range) -> [int]:
        """Searches for devices of a specific category on the SCOM interface.

        :return A list of device address found.
        """
        device_list = []
        device_start_address = int(address_scan_range[0])
        device_stop_address = int(address_scan_range[1])

        self.log.info('Searching devices in group \'%s\'...' % device_type)

        request_frame = BaseFrame(self.DEFAULT_RX_BUFFER_SIZE)

        device_index = device_start_address
        while device_index <= device_stop_address:
            request_frame.initialize(src_addr=1, dest_addr=device_index)

            prop = Property(request_frame)
            # TODO For some devices 'parameter' value must be read instead of 'user info' (ex. RCC device)
            prop.set_object_read(defines.OBJECT_TYPE_READ_USER_INFO,
                                 DeviceType.get_reference_search_object_id(device_type),
                                 defines.PROPERTY_ID_READ)

            if request_frame.is_valid():
                response_frame = self._scom.write_frame(request_frame, 0.5)  # Set a short timeout during search

                if response_frame and response_frame.is_valid():
                    self.log.info('Found device on address: ' + str(device_index))
                    device_list.append(device_index)
            else:
                self.log.warning('Frame with error: ' + request_frame.last_error())

            device_index += 1

        if len(device_list) == 0:
            self.log.warning('No devices in group \'%s\' found' % device_type)

        return device_list

    def _get_missing_device_addresses(self, device_type, device_address_list):
        """"Searches in actually instantiated devices list (of a category) for devices not found in given device list.

        :param device_type The device category in which to search for devices
        :type device_type str
        :param device_address_list List containing device address (which are still present and not missed)
        :type device_address_list
        """
        missing_device_address_list = []

        device_list = self.get_instances_of_category(device_type)

        for internal_id, device in device_list.items():
            if device.device_address not in device_address_list:
                missing_device_address_list.append(device.device_address)

        return missing_device_address_list

    def _check_scom_rx_errors(self):
        """Checks how many times there was an RX error on the SCOM bus.

        After a few RX errors are detected, first a message is send (logged) and
        after still more errors the application gets terminated.
        """
        msg = u'Scom bus no more responding!'
        if self._scom.rxErrors > 50 and not self._scom_rx_error_message_send:
            self.log.critical(msg)
            self._scom_rx_error_message_send = True

        if self._scom.rxErrors > 100:
            sys.exit(msg)

    def remove_all_devices(self):
        """Cleans up all SCOM devices and notifies subscribers about the removal.
        """
        for device_address, device in self._devices.items():
            # Notify subscribers that device is going to disappear
            self._notify_subscribers(device=device, connected=False)
        self._devices.clear()
        gc.collect()

    def wait_on_manager_to_leave(self, timeout=3):
        """
        Can be called to wait for the NodeManager until it left the run loop.
        """
        wait_time = timeout
        decr_value = 0.2

        if self._thread_left_run_loop:
            return

        while wait_time > 0:
            time.sleep(decr_value)
            wait_time -= decr_value
            if self._thread_left_run_loop:
                break

    def destroy(self):
        """
        Destroys the running NodeManager object
        """
        self.stop_thread()
        self.wait_on_manager_to_leave()  # Wait thread to leave loop

# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------  End of NodeManager Class  -------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
