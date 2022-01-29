# -*- coding: utf-8 -*-
"""
This file contains definition/implementation of a Base-Class for all the different devices
    - Xtender
    - VarioTrack
    - VarioString
    - RCC, Xcom-232i
    - Xcom-CAN
    - BSP
Inspired from and Based on hesso-valais/scom : scomdevice.py
<https://github.com/hesso-valais/scom/blob/0.7.3/src/sino/scom/device/scomdevice.py>
"""

import logging
import re
import struct

from sino.scom.defines import *
from sino.scom.frame import Frame as ScomFrame
from sino.scom.property import Property

from .addresses import *
from .device_type import DeviceType
from ..property_format import PropertyFormat


# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------  BaseDevice Class  ------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
class BaseDevice(object):
    """
    Base-Class for all the different devices
        - Xtender
        - VarioTrack
        - VarioString
        - RCC, Xcom-232i
        - Xcom-CAN
        - BSP
    Inspired from and Based on hesso-valais/scom : scomdevice.py
    <https://github.com/hesso-valais/scom/blob/0.7.3/src/sino/scom/device/scomdevice.py>
    """

    log = logging.getLogger(__name__)

    def __init__(self, device_address, scom=None):
        super(BaseDevice, self).__init__()
        self._scom = scom
        assert self._scom, "In order to create Device, scom object must be given!"
        self.log = logging.getLogger(__name__ + ":" + self.node_name)

        self._userInfosTable = {}
        self._deviceAddress = device_address
        self._deviceType = DeviceType.UNKNOWN

    @property
    def node_name(self):
        """
        Returns the Node Name.

        :return:
        """
        return self._scom.node_name

    @property
    def device_type(self):
        """
        Returns the device type.

        See 'DeviceType'

        :return The device type.
        :rtype enumerate
        """
        return self._deviceType

    @property
    def device_address(self):
        """
        Returns the device address.

        :return The device address
        :rtype int
        """
        return self._deviceAddress

    @property
    def is_multicast_device(self):
        """
        Returns True if the device address is a Multicast device address

        :return The device address
        :rtype: bool
        """
        return self._deviceAddress in MULTICAST_ADDRESSES

    def _get_scom(self):
        """
        Returns the SCOM interface on which the device can be reached.

        There may be more then on SCOM interface connected to the system.
        This method is used by the base class (BaseDevice) to receive the right
        SCOM interface.
        """
        return self._scom

    @property
    def software_version(self):
        """
        Returns the software version.

        :return The Software version as dict {major, minor, patch}, zeros for the device types haven't related UserInfo
        :rtype dict or None
        """
        id_soft_msb = id_soft_lsb = None
        if hasattr(self, 'read_user_info_smsb'):
            id_soft_msb = getattr(self, 'read_user_info_smsb')()
        if hasattr(self, 'read_user_info_slsb'):
            id_soft_lsb = getattr(self, 'read_user_info_slsb')()
        if id_soft_msb and id_soft_lsb:
            id_soft_major_version = int(id_soft_msb) >> 8
            id_soft_minor_version = int(id_soft_lsb) >> 8
            id_soft_revision = int(id_soft_lsb) & 0xFF
            return {'major': id_soft_major_version, 'minor': id_soft_minor_version, 'patch': id_soft_revision}
        return {'major': 0, 'minor': 0, 'patch': 0}

    def _read_user_info_by_parameter_id(self, parameter_id):
        """
        Reads a user info on the device.

        :param parameter_id
        :type parameter_id int
        :return The parameter read
        :type return bytearray
        """
        value = bytearray()
        request_frame = ScomFrame()

        request_frame.initialize(src_addr=1, dest_addr=self.device_address, data_length=99)

        prop = Property(request_frame)
        prop.set_object_read(OBJECT_TYPE_READ_USER_INFO, parameter_id, PROPERTY_ID_READ)

        if request_frame.is_valid():
            response_frame = self._get_scom().write_frame(request_frame)  # Method call is blocking

            if response_frame:
                if response_frame.is_valid():
                    value_size = response_frame.response_value_size()
                    value = response_frame[24:24 + value_size]
                elif response_frame.is_data_error_flag_set():
                    self.log.warning('Warning: Error flag set in response frame! will reading UserInfo %d' %
                                     parameter_id)
            else:
                self.log.warning('No response frame received!')
        else:
            self.log.warning('Request frame not valid')

        return value

    def read_user_info(self, user_info_id):
        """
        Uses the userInfoTable to access the needed user info. and get it's value.

        :return The value received from the device
        :rtype:  float, (enum), None.
        """
        user_info = self._userInfosTable.get(user_info_id)

        if not user_info:
            self.log.warning("Could not read UserInfo %d It's UnSupported UserInfo" % (user_info_id,))
            return None
        value = self._read_user_info_by_parameter_id(user_info_id)
        if value:
            if user_info["Format"] == PropertyFormat.FLOAT:
                assert len(value) == 4, 'Length of Value: Expected 4 got %d' % len(value)
                value = struct.unpack('f', value[0:4])[0]
            elif user_info["Format"] == PropertyFormat.SHORT_ENUM:
                assert len(value) == 2, 'Length of Value: Expected 2 got %d' % len(value)
                value = struct.unpack('H', value[0:2])[0]  # Read 'ENUM' format as unsigned int (H)
            else:
                assert False, 'Unsupported format for this UserInfo'
            return value
        else:
            self.log.warning("Could not read UserInfo %d '%s'" % (user_info_id, user_info["Short desc."]))
            return None

    def read_user_infos_as_telemetry(self, list_of_user_infos_of_interest):
        """
        Read Values for all the user_infos in the _userInfosTable and returns telemetry_values dict
        contains user_info_id as a key and the received value from read_user_info(user_info_id) as a value
        :return:
        """

        _prefix = ''
        if self.device_type == DeviceType.XTENDER:
            _prefix += 'XT'
            if self.device_address == XT_GROUP_DEVICE_ID:
                _prefix += 'ALL'
            elif self.device_address == XT_1_DEVICE_ID:
                _prefix += str(1)
            elif self.device_address == XT_2_DEVICE_ID:
                _prefix += str(2)
            elif self.device_address == XT_3_DEVICE_ID:
                _prefix += str(3)
            elif self.device_address == XT_4_DEVICE_ID:
                _prefix += str(4)
            elif self.device_address == XT_5_DEVICE_ID:
                _prefix += str(5)
            elif self.device_address == XT_6_DEVICE_ID:
                _prefix += str(6)
            elif self.device_address == XT_7_DEVICE_ID:
                _prefix += str(7)
            elif self.device_address == XT_8_DEVICE_ID:
                _prefix += str(8)
            elif self.device_address == XT_9_DEVICE_ID:
                _prefix += str(9)
        elif self.device_type == DeviceType.VARIO_TRACK:
            _prefix += 'VT'
            if self.device_address == VT_GROUP_DEVICE_ID:
                _prefix += 'ALL'
            elif self.device_address == VT_1_DEVICE_ID:
                _prefix += str(1)
            elif self.device_address == VT_2_DEVICE_ID:
                _prefix += str(2)
            elif self.device_address == VT_3_DEVICE_ID:
                _prefix += str(3)
            elif self.device_address == VT_4_DEVICE_ID:
                _prefix += str(4)
            elif self.device_address == VT_5_DEVICE_ID:
                _prefix += str(5)
            elif self.device_address == VT_6_DEVICE_ID:
                _prefix += str(6)
            elif self.device_address == VT_7_DEVICE_ID:
                _prefix += str(7)
            elif self.device_address == VT_8_DEVICE_ID:
                _prefix += str(8)
            elif self.device_address == VT_9_DEVICE_ID:
                _prefix += str(9)
            elif self.device_address == VT_10_DEVICE_ID:
                _prefix += str(10)
            elif self.device_address == VT_11_DEVICE_ID:
                _prefix += str(11)
            elif self.device_address == VT_12_DEVICE_ID:
                _prefix += str(12)
            elif self.device_address == VT_13_DEVICE_ID:
                _prefix += str(13)
            elif self.device_address == VT_14_DEVICE_ID:
                _prefix += str(14)
            elif self.device_address == VT_15_DEVICE_ID:
                _prefix += str(15)
        elif self.device_type == DeviceType.VARIO_STRING:
            _prefix += 'VS'
            if self.device_address == VS_GROUP_DEVICE_ID:
                _prefix += 'ALL'
            elif self.device_address == VS_1_DEVICE_ID:
                _prefix += str(1)
            elif self.device_address == VS_2_DEVICE_ID:
                _prefix += str(2)
            elif self.device_address == VS_3_DEVICE_ID:
                _prefix += str(3)
            elif self.device_address == VS_4_DEVICE_ID:
                _prefix += str(4)
            elif self.device_address == VS_5_DEVICE_ID:
                _prefix += str(5)
            elif self.device_address == VS_6_DEVICE_ID:
                _prefix += str(6)
            elif self.device_address == VS_7_DEVICE_ID:
                _prefix += str(7)
            elif self.device_address == VS_8_DEVICE_ID:
                _prefix += str(8)
            elif self.device_address == VS_9_DEVICE_ID:
                _prefix += str(9)
            elif self.device_address == VS_10_DEVICE_ID:
                _prefix += str(10)
            elif self.device_address == VS_11_DEVICE_ID:
                _prefix += str(11)
            elif self.device_address == VS_12_DEVICE_ID:
                _prefix += str(12)
            elif self.device_address == VS_13_DEVICE_ID:
                _prefix += str(13)
            elif self.device_address == VS_14_DEVICE_ID:
                _prefix += str(14)
            elif self.device_address == VS_15_DEVICE_ID:
                _prefix += str(15)
        elif self.device_type == DeviceType.BSP and self.device_address == BSP_DEVICE_ID:
            _prefix += 'BSP'
        _prefix += 'I'

        telemetry_values = {
            _prefix + str(user_info_id): self.read_user_info(user_info_id)
            for user_info_id
            in self._userInfosTable
            if user_info_id in list_of_user_infos_of_interest
        }
        print(telemetry_values)
        return telemetry_values

    @classmethod
    def _generate_short_desc_string_as_function_name(cls, short_desc_string):
        """
        Converters the UserInfo 'Short desc.' string to a string compatible to be used as part of function name

        :param short_desc_string:
        :return the new_short_desc_string
        :rtype: str
        """
        new_short_desc_string = None
        if short_desc_string.strip():
            new_short_desc_string = short_desc_string.strip()
            new_short_desc_string = new_short_desc_string.replace("+", "_plus")
            new_short_desc_string = new_short_desc_string.replace("-", "_minus")
            new_short_desc_string = re.sub("[^0-9a-zA-Z]+", "_", new_short_desc_string)
            new_short_desc_string = re.sub("[_]*$", "", new_short_desc_string)
        return new_short_desc_string.lower()

    def _create_read_user_info_function(self, user_info_id):
        """
        Use the provided user_info_id to dynamically generate function implementation as a wrapper for the
        read_user_info(user_info_id) function.

        :param user_info_id:
        :return:
        """

        def function_template():
            """
            Temp docstring for the function should be replaced using (function_template.__doc__=)
            after generating the function
            """
            return self.read_user_info(user_info_id)

        function_template.__doc__ = "\n\tUses the userInfoTable to access the needed user info ({0}). " \
                                    "and get it's value.\n".format(user_info_id)
        return function_template

    def set_user_infos_table(self, user_infos_table):
        """
        Sets the _userInfosTable to the passed dict and dynamically generates getters functions for all the infos
        contains in it.
        like:
            -  read_user_info_i3000()                       --> for the Xtender Info 3001
            - read_user_info_i3001(), read_user_info_tbat() --> for the Xtender Info 3001
        The wrapper function with the 'Short desc.' in the name will be produced only if the 'Short desc.' is unique.

        :param user_infos_table:
        :return:
        """

        self._userInfosTable = user_infos_table

        _list_of_all_short_desc_strings = [_user_info_dict["Short desc."]
                                           for _, _user_info_dict
                                           in self._userInfosTable.items()]

        for user_info_id, user_info_dict in self._userInfosTable.items():
            exec("setattr(self, 'read_user_info_i{0}', self._create_read_user_info_function({0}))".format(user_info_id))
            if _list_of_all_short_desc_strings.count(user_info_dict["Short desc."]) == 1:
                short_desc_string = self._generate_short_desc_string_as_function_name(user_info_dict["Short desc."])
                if short_desc_string:
                    # print(user_info_id, "\t", user_info_dict["Short desc."], "\t", short_desc_string)
                    exec("setattr(self, 'read_user_info_{0}', self._create_read_user_info_function({1}))".format(
                        short_desc_string, user_info_id))


# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------  End of BaseDevice Class  -------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
