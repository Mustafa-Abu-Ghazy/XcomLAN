# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
This file contains definition/implementation of a ThingsBoardClient Class
that Manages dealing with / pushing data to ThingsBoard server.
"""

import csv
import logging
import re
import threading
from datetime import datetime
from queue import Queue
from time import sleep
from time import time

from tb_device_mqtt import TBPublishInfo
from tb_gateway_mqtt import TBGatewayMqttClient


# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------  ThingsBoardClient Class  -------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class ThingsBoardClient(TBGatewayMqttClient):
    """
    ThingsBoardClient Class
    """

    def __init__(self, host, token=None, port=1883,
                 gateway=None, quality_of_service=1,
                 node_profile='Studer Xcom-LAN Node'):
        super(ThingsBoardClient, self).__init__(host, token, port, gateway, quality_of_service)
        self._node_profile = node_profile
        self.log = logging.getLogger(__name__ + ":" + self._node_profile)

        # Initializing a Telemetry Queue
        self._telemetry_queue = Queue()
        self._telemetry_restored_queue = Queue()

        # Initializing and Start a Thread to server the stored telemetry information
        self._thread = threading.Thread(target=self._send_nodes_telemetry_loop)
        self._thread.name = self.__class__.__name__ + self._thread.name
        self._thread.setDaemon(True)
        self._thread.start()

    def __del__(self):
        self.disconnect()

    @property
    def node_profile(self):
        """
        Returns the Node Profile.
        """
        return self._node_profile

    def node_telemetry_enqueue(self, node_name, timestamp, telemetry_values):
        """
        enqueue method add the telemetry's information to the _telemetry_queue queue to be served in order by
        the _send_nodes_telemetry_loop method thread.
        """
        valid_node_name = type(node_name) is str
        valid_timestamp = type(timestamp) is int
        valid_telemetry_values = type(telemetry_values) is dict and len(telemetry_values)
        if not (valid_node_name and valid_timestamp and valid_telemetry_values):
            self.log.error("Invalid telemetry information to be added to the queue. (" +
                           "node_name= " + str(node_name) + ", " +
                           "timestamp= " + str(timestamp) + ", " +
                           "telemetry_values= " + str(telemetry_values) + ")"
                           )
            return

        self._telemetry_queue.put({
            "node_name": node_name,
            "timestamp": timestamp,
            "telemetry_values": telemetry_values
        })

    def _send_nodes_telemetry_loop(self):
        """
        This method designed to be executed as a separate thread
        """
        log = logging.getLogger(__name__ + ":" + "send_nodes_telemetry_loop")
        while True:
            if self._telemetry_restored_queue.qsize():
                telemetry = self._telemetry_restored_queue.get()
            else:
                telemetry = self._telemetry_queue.get()
            try:
                # Try to connect to the Server if not connected yet
                if not self.is_connected():
                    self.connect()
                # Try sending telemetry to the server
                self.send_node_telemetry(
                    node_name=telemetry["node_name"],
                    timestamp=telemetry["timestamp"],
                    telemetry_values=telemetry["telemetry_values"]
                )
            except Exception as e:
                self._telemetry_restored_queue.put(telemetry)  # Restore the telemetry back to the restored_queue
                log.exception(e)  # log the exception
                sleep(30)  # Sleep 30 Seconds

    # telemetry === UserInfo
    def send_node_telemetry(self, node_name, timestamp, telemetry_values):
        """
        Sending Telemetry of node to TB Server
        """
        log = logging.getLogger(__name__ + ":" + self.node_profile + ":" + node_name)

        # Connect The Device: ThingsBoard will publish updates for this particular device to this Gateway.
        # Used only to ensure creating the device with the proper device_type if not exist.
        # device_type: will be used only when creating not existing device
        self.gw_connect_device(node_name, device_type=self.node_profile)

        # Sending Telemetry Data (UserInfo) to TB Device
        telemetry = {  # Contains JSON/Dict
            'ts': timestamp,
            'values': telemetry_values
        }
        result = self.gw_send_telemetry(node_name, telemetry)
        result_status = result.get() == TBPublishInfo.TB_ERR_SUCCESS
        log.info('Send to Node: ' + node_name + ' Telemetry Content: ' + str(telemetry) +
                 ' Sending Telemetry Result Status: ' + str(result_status))

        self.gw_disconnect_device(node_name)

    # attribute === Parameter
    def send_node_attributes(self, node_name, attributes_values):
        """
        Sending Attributes of node to TB Server
        """
        log = logging.getLogger(__name__ + ":" + self.node_profile + ":" + node_name)

        # Connect The Device: ThingsBoard will publish updates for this particular device to this Gateway.
        # Used only to ensure creating the device with the proper device_type if not exist.
        # device_type: will be used only when creating not existing device
        self.gw_connect_device(node_name, device_type=self.node_profile)

        # Sending Attributes Data (Parameter) to TB Device
        attributes = attributes_values  # Contains JSON/Dict
        result = self.gw_send_attributes(node_name, attributes)
        result_status = result.get() == TBPublishInfo.TB_ERR_SUCCESS
        log.info('Send to Node: ' + node_name + ' Attributes Content: ' + str(attributes) +
                 ' Sending Attributes Result Status: ' + str(result_status))

        self.gw_disconnect_device(node_name)

    @classmethod
    def _generate_dict_header_for_csv_log_file(cls, csv_log_file_path):
        # supports only nodes with single Xtender device
        first_row, second_row, third_row = list(csv.reader(open(csv_log_file_path, 'r')))[0:3]
        header = ['ts'] + [''] * (len(first_row) - 2)

        for idx in range(1, len(first_row) - 1):
            if first_row[idx] == '':
                first_row[idx] = first_row[idx - 1]

            if first_row[idx].startswith('XT') or first_row[idx].startswith('DEV XT'):
                header[idx] = 'XT' + '1' + second_row[idx]
            elif first_row[idx].startswith('VS') or first_row[idx].startswith('DEV VS'):
                header[idx] = 'VS' + third_row[idx] + second_row[idx]
            elif first_row[idx].startswith('VT') or first_row[idx].startswith('DEV VT'):
                header[idx] = 'VT' + third_row[idx] + second_row[idx]
            elif first_row[idx].startswith('BSP'):
                header[idx] = 'BSP' + second_row[idx]
            elif first_row[idx].startswith('DEV'):
                header[idx] = 'DEV' + second_row[idx]
            elif first_row[idx] == 'Solar power (ALL) [kW]':
                header[idx] = 'SolarPowerALL' + second_row[idx]
            else:
                header[idx] = re.sub('[^0-9a-zA-Z]+', '', first_row[idx]) + third_row[idx] + second_row[idx]
        return header

    @classmethod
    def _parse_value_from_csv_log_file(cls, value):
        if value.isdigit():
            return int(value)
        elif len(value) > 1 and value[0] in ('-', '+') and value[1:].isdigit():
            return int(value)
        elif value.replace('.', '', 1).isdigit():
            return float(value)
        elif len(value) > 1 and value[0] in ('-', '+') and value.replace('.', '', 1)[1:].isdigit():
            return float(value)
        else:
            return value

    def push_csv_input_to_tb(self, node_name, csv_log_file_path, feed_as_realtime=False):
        """
        Read Telemetry from CSV file of node and Push them  to TB Server

        :param feed_as_realtime: if set the Telemetry will be parsed and send as a realtime
         neglecting the stored timestamp
        """
        log = logging.getLogger(__name__ + ":" + self.node_profile + ":" + node_name)

        # Connect The Device
        # device_type: will be used only when creating not existing device
        self.gw_connect_device(node_name, device_type=self.node_profile)

        telemetry = {}
        attributes = {}

        # Define Fields Names
        fieldnames = self._generate_dict_header_for_csv_log_file(csv_log_file_path)

        # Creating A CSV DictReader object
        csv_dict_reader = list(csv.DictReader(open(csv_log_file_path, 'r'), fieldnames=fieldnames))

        # Read (CSVDictReader), Skip First 3 Rows. Focus on Telemetries
        for index, row in enumerate(csv_dict_reader[3:1443]):
            try:
                logging.info('CSV ROW Number: ' + str(index + 4))
                date_time_str = row['ts']
                date_time_obj = datetime.strptime(date_time_str, '%d.%m.%Y %H:%M')
                timestamp = date_time_obj.timestamp()
                telemetry['ts'] = int(timestamp * 1000) if not feed_as_realtime else int(round(time() * 1000))
                telemetry['values'] = {i: self._parse_value_from_csv_log_file(row[i]) for i in fieldnames[1:]}

                result = self.gw_send_telemetry(node_name, telemetry)
                result_status = result.get() == TBPublishInfo.TB_ERR_SUCCESS
                log.info('Node: ' + node_name + ' Telemetry Content: ' + str(telemetry))
                log.info('Node: ' + node_name + ' File: ' + csv_log_file_path +
                         ' Send Telemetry Result Status: ' + str(result_status))
            except Exception as e:
                logging.exception(e)

        # Read (CSVDictReader), Skip First 1443 Rows. Focus on Attributes
        for index, row in enumerate(csv_dict_reader[1443:]):
            if re.match(r'[PI][0-9]+', row[fieldnames[0]]):
                attributes[row[fieldnames[0]]] = self._parse_value_from_csv_log_file(row[fieldnames[1]])

        result = self.gw_send_attributes(node_name, attributes)
        result_status = result.get() == TBPublishInfo.TB_ERR_SUCCESS
        log.info('Node: ' + node_name + ' File: ' + csv_log_file_path + ' Attributes Content: ' + str(attributes))
        log.info('Node: ' + node_name + ' Send Attributes Result Status: ' + str(result_status))

        # Disconnect The Device
        self.gw_disconnect_device(node_name)

        if feed_as_realtime:
            sleep(60)

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------  End of ThingsBoardClient Class  ----------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
