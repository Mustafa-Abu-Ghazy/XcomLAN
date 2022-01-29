# -*- coding: utf-8 -*-
"""
This file contains definition/implementation of a DeviceFactory Class responsible for creating all the different devices
    - Xtender
    - VarioTrack
    - VarioString
    - RCC, Xcom-232i
    - Xcom-CAN
    - BSP
Inspired from and Based on hesso-valais/scom : devicefactory.py
<https://github.com/hesso-valais/scom/blob/0.7.3/src/sino/scom/device/devicefactory.py>
"""

from .addresses import *
from .bsp import BSP
from .device_type import DeviceType
from .rcc import RCC
from .vario_string import VarioString
from .vario_track import VarioTrack
from .xtender import Xtender


# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------  DeviceFactory Class  ---------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class DeviceFactory(object):
    """
    Creates Studer device representations.
    """

    @classmethod
    def create(cls, device_type, device_address, scom):
        """
        Creates a new studer device according to the category given.
        """

        if device_type == DeviceType.XTENDER:
            assert XT_DEVICE_ID_RANGE[0] <= device_address <= XT_DEVICE_ID_RANGE[1], \
                'This Address {0} is not a Valid address for Xtender device'.format(device_address)
            new_device = Xtender(device_address, scom)
        elif device_type == DeviceType.COMPACT:
            assert False, 'No Implementation of Device-Class for the Compact device type.'
        elif device_type == DeviceType.VARIO_TRACK:
            assert VT_DEVICE_ID_RANGE[0] <= device_address <= VT_DEVICE_ID_RANGE[1], \
                'This Address {0} is not a Valid address for VarioTrack device'.format(device_address)
            new_device = VarioTrack(device_address, scom)
        elif device_type == DeviceType.VARIO_STRING:
            assert VS_DEVICE_ID_RANGE[0] <= device_address <= VS_DEVICE_ID_RANGE[1], \
                'This Address {0} is not a Valid address for VarioString device'.format(device_address)
            new_device = VarioString(device_address, scom)
        elif device_type == DeviceType.RCC:
            assert RCC_DEVICE_ID_RANGE[0] <= device_address <= RCC_DEVICE_ID_RANGE[1], \
                'This Address {0} is not a Valid address for RCC, Xcom-232i device'.format(device_address)
            new_device = RCC(device_address, scom)
        elif device_type == DeviceType.BSP:
            assert BSP_DEVICE_ID_RANGE[0] <= device_address <= BSP_DEVICE_ID_RANGE[1], \
                'This Address {0} is not a Valid address for BSP device'.format(device_address)
            new_device = BSP(device_address, scom)
        else:
            assert False, 'Not Supported device type.'
        return new_device

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------  End of DeviceFactory Class  ------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
