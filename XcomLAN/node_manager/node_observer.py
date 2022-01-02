#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file contains definition/implementation of a NodeObserver Class that Receives device notifications if NodeManager
finds Studer devices.
Inspired from and Based on hesso-valais/scom : devicesubscriber.py
<https://github.com/hesso-valais/scom/blob/0.7.3/src/sino/scom/dman/devicesubscriber.py>
"""
import logging

from ..device import BSP_DEVICE_ID
from ..device import RCC_1_DEVICE_ID
from ..device import XCOM232i_DEVICE_ID
from ..device import RCC_2_DEVICE_ID
from ..device import RCC_3_DEVICE_ID
from ..device import RCC_4_DEVICE_ID
from ..device import RCC_5_DEVICE_ID
from ..device import RCC_GROUP_DEVICE_ID
from ..device import VS_10_DEVICE_ID
from ..device import VS_11_DEVICE_ID
from ..device import VS_12_DEVICE_ID
from ..device import VS_13_DEVICE_ID
from ..device import VS_14_DEVICE_ID
from ..device import VS_15_DEVICE_ID
from ..device import VS_1_DEVICE_ID
from ..device import VS_2_DEVICE_ID
from ..device import VS_3_DEVICE_ID
from ..device import VS_4_DEVICE_ID
from ..device import VS_5_DEVICE_ID
from ..device import VS_6_DEVICE_ID
from ..device import VS_7_DEVICE_ID
from ..device import VS_8_DEVICE_ID
from ..device import VS_9_DEVICE_ID
from ..device import VS_GROUP_DEVICE_ID
from ..device import VT_10_DEVICE_ID
from ..device import VT_11_DEVICE_ID
from ..device import VT_12_DEVICE_ID
from ..device import VT_13_DEVICE_ID
from ..device import VT_14_DEVICE_ID
from ..device import VT_15_DEVICE_ID
from ..device import VT_1_DEVICE_ID
from ..device import VT_2_DEVICE_ID
from ..device import VT_3_DEVICE_ID
from ..device import VT_4_DEVICE_ID
from ..device import VT_5_DEVICE_ID
from ..device import VT_6_DEVICE_ID
from ..device import VT_7_DEVICE_ID
from ..device import VT_8_DEVICE_ID
from ..device import VT_9_DEVICE_ID
from ..device import VT_GROUP_DEVICE_ID
from ..device import XT_1_DEVICE_ID
from ..device import XT_2_DEVICE_ID
from ..device import XT_3_DEVICE_ID
from ..device import XT_4_DEVICE_ID
from ..device import XT_5_DEVICE_ID
from ..device import XT_6_DEVICE_ID
from ..device import XT_7_DEVICE_ID
from ..device import XT_8_DEVICE_ID
from ..device import XT_9_DEVICE_ID
from ..device import XT_GROUP_DEVICE_ID


# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------  NodeObserver Class  ----------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class NodeObserver(object):
    """
    Receives device notifications if NodeManager finds Studer devices.
    (get notified about an SCOM device of interest.)
    """

    def __init__(self, node_manager):
        super(NodeObserver, self).__init__()
        assert node_manager, 'To create NodeObserver object, node_manager must be giving!'
        self._node_manager = node_manager
        self.log = logging.getLogger(__name__ + ":" + self.node_name)
        self._connected_devices = {}
        self._node_manager.subscribe(self)

    def __del__(self):
        self._node_manager.unsubscribe(self)

    @property
    def node_manager(self):
        """Returns the NodeManager object related to this observer"""
        return self._node_manager

    @property
    def node_name(self):
        """
        Returns the Node Name.

        :return:
        """
        return self.node_manager.node_name

    @property
    def connected_devices(self):
        """
        Returns list of the currently connected device.

        :return:
        """
        return self._connected_devices

    # ---------------------------------------------------------------------------------------------------------------- #
    # ---------------------------------  Subscriber's Notification Functions/Methods  -------------------------------- #
    # ---------------------------------------------------------------------------------------------------------------- #
    def on_device_connected(self, device):
        """
        Called whenever the DeviceManager detects a new SCOM device (of interest).

        :param device:
        :type device ScomDevice
        :return: None
        """
        self._connected_devices[device.device_address] = device

    def on_device_disconnected(self, device):
        """
        Called whenever the DeviceManager detects the disappearance of an SCOM device (of interest).

        :param device:
        :type device ScomDevice
        :return: None
        """
        self._connected_devices.pop(device.device_address)

    # ---------------------------------------------------------------------------------------------------------------- #
    # --------------------------------------  Getters Properties for Xtenders   -------------------------------------- #
    # ---------------------------------------------------------------------------------------------------------------- #
    @property
    def xt_all(self):
        """Returns the All Xtenders (Multicast) device if exist else returns None"""
        return self._connected_devices.get(XT_GROUP_DEVICE_ID)

    @property
    def xt1(self):
        """Returns the 1st Xtender device if exist else returns None"""
        return self._connected_devices.get(XT_1_DEVICE_ID)

    @property
    def xt2(self):
        """Returns the 2nd Xtender device if exist else returns None"""
        return self._connected_devices.get(XT_2_DEVICE_ID)

    @property
    def xt3(self):
        """Returns the 3rd Xtender device if exist else returns None"""
        return self._connected_devices.get(XT_3_DEVICE_ID)

    @property
    def xt4(self):
        """Returns the 4th Xtender device if exist else returns None"""
        return self._connected_devices.get(XT_4_DEVICE_ID)

    @property
    def xt5(self):
        """Returns the 5th Xtender device if exist else returns None"""
        return self._connected_devices.get(XT_5_DEVICE_ID)

    @property
    def xt6(self):
        """Returns the 6th Xtender device if exist else returns None"""
        return self._connected_devices.get(XT_6_DEVICE_ID)

    @property
    def xt7(self):
        """Returns the 7th Xtender device if exist else returns None"""
        return self._connected_devices.get(XT_7_DEVICE_ID)

    @property
    def xt8(self):
        """Returns the 8th Xtender device if exist else returns None"""
        return self._connected_devices.get(XT_8_DEVICE_ID)

    @property
    def xt9(self):
        """Returns the 9th Xtender device if exist else returns None"""
        return self._connected_devices.get(XT_9_DEVICE_ID)

    # ---------------------------------------------------------------------------------------------------------------- #
    # -------------------------------------  Getters Properties for VarioTracks   ------------------------------------ #
    # ---------------------------------------------------------------------------------------------------------------- #
    @property
    def vt_all(self):
        """Returns the All VarioTracks (Multicast) device if exist else returns None"""
        return self._connected_devices.get(VT_GROUP_DEVICE_ID)

    @property
    def vt1(self):
        """Returns the 1st VarioTrack device if exist else returns None"""
        return self._connected_devices.get(VT_1_DEVICE_ID)

    @property
    def vt2(self):
        """Returns the 2nd VarioTrack device if exist else returns None"""
        return self._connected_devices.get(VT_2_DEVICE_ID)

    @property
    def vt3(self):
        """Returns the 3rd VarioTrack device if exist else returns None"""
        return self._connected_devices.get(VT_3_DEVICE_ID)

    @property
    def vt4(self):
        """Returns the 4th VarioTrack device if exist else returns None"""
        return self._connected_devices.get(VT_4_DEVICE_ID)

    @property
    def vt5(self):
        """Returns the 5th VarioTrack device if exist else returns None"""
        return self._connected_devices.get(VT_5_DEVICE_ID)

    @property
    def vt6(self):
        """Returns the 6th VarioTrack device if exist else returns None"""
        return self._connected_devices.get(VT_6_DEVICE_ID)

    @property
    def vt7(self):
        """Returns the 7th VarioTrack device if exist else returns None"""
        return self._connected_devices.get(VT_7_DEVICE_ID)

    @property
    def vt8(self):
        """Returns the 8th VarioTrack device if exist else returns None"""
        return self._connected_devices.get(VT_8_DEVICE_ID)

    @property
    def vt9(self):
        """Returns the 9th VarioTrack device if exist else returns None"""
        return self._connected_devices.get(VT_9_DEVICE_ID)

    @property
    def vt10(self):
        """Returns the 9th VarioTrack device if exist else returns None"""
        return self._connected_devices.get(VT_10_DEVICE_ID)

    @property
    def vt11(self):
        """Returns the 9th VarioTrack device if exist else returns None"""
        return self._connected_devices.get(VT_11_DEVICE_ID)

    @property
    def vt12(self):
        """Returns the 9th VarioTrack device if exist else returns None"""
        return self._connected_devices.get(VT_12_DEVICE_ID)

    @property
    def vt13(self):
        """Returns the 9th VarioTrack device if exist else returns None"""
        return self._connected_devices.get(VT_13_DEVICE_ID)

    @property
    def vt14(self):
        """Returns the 9th VarioTrack device if exist else returns None"""
        return self._connected_devices.get(VT_14_DEVICE_ID)

    @property
    def vt15(self):
        """Returns the 9th VarioTrack device if exist else returns None"""
        return self._connected_devices.get(VT_15_DEVICE_ID)

    # ---------------------------------------------------------------------------------------------------------------- #
    # ------------------------------------  Getters Properties for VarioStrings   ------------------------------------ #
    # ---------------------------------------------------------------------------------------------------------------- #
    @property
    def vs_all(self):
        """Returns the All VarioStrings (Multicast) device if exist else returns None"""
        return self._connected_devices.get(VS_GROUP_DEVICE_ID)

    @property
    def vs1(self):
        """Returns the 1st VarioString device if exist else returns None"""
        return self._connected_devices.get(VS_1_DEVICE_ID)

    @property
    def vs2(self):
        """Returns the 2nd VarioString device if exist else returns None"""
        return self._connected_devices.get(VS_2_DEVICE_ID)

    @property
    def vs3(self):
        """Returns the 3rd VarioString device if exist else returns None"""
        return self._connected_devices.get(VS_3_DEVICE_ID)

    @property
    def vs4(self):
        """Returns the 4th VarioString device if exist else returns None"""
        return self._connected_devices.get(VS_4_DEVICE_ID)

    @property
    def vs5(self):
        """Returns the 5th VarioString device if exist else returns None"""
        return self._connected_devices.get(VS_5_DEVICE_ID)

    @property
    def vs6(self):
        """Returns the 6th VarioString device if exist else returns None"""
        return self._connected_devices.get(VS_6_DEVICE_ID)

    @property
    def vs7(self):
        """Returns the 7th VarioString device if exist else returns None"""
        return self._connected_devices.get(VS_7_DEVICE_ID)

    @property
    def vs8(self):
        """Returns the 8th VarioString device if exist else returns None"""
        return self._connected_devices.get(VS_8_DEVICE_ID)

    @property
    def vs9(self):
        """Returns the 9th VarioString device if exist else returns None"""
        return self._connected_devices.get(VS_9_DEVICE_ID)

    @property
    def vs10(self):
        """Returns the 9th VarioString device if exist else returns None"""
        return self._connected_devices.get(VS_10_DEVICE_ID)

    @property
    def vs11(self):
        """Returns the 9th VarioString device if exist else returns None"""
        return self._connected_devices.get(VS_11_DEVICE_ID)

    @property
    def vs12(self):
        """Returns the 9th VarioString device if exist else returns None"""
        return self._connected_devices.get(VS_12_DEVICE_ID)

    @property
    def vs13(self):
        """Returns the 9th VarioString device if exist else returns None"""
        return self._connected_devices.get(VS_13_DEVICE_ID)

    @property
    def vs14(self):
        """Returns the 9th VarioString device if exist else returns None"""
        return self._connected_devices.get(VS_14_DEVICE_ID)

    @property
    def vs15(self):
        """Returns the 9th VarioString device if exist else returns None"""
        return self._connected_devices.get(VS_15_DEVICE_ID)

    # ---------------------------------------------------------------------------------------------------------------- #
    # ----------------------------------------  Getters Properties for BSPs   ---------------------------------------- #
    # ---------------------------------------------------------------------------------------------------------------- #
    @property
    def bsp(self):
        """Returns the only BSP device if exist else returns None"""
        return self._connected_devices.get(BSP_DEVICE_ID)

    # ---------------------------------------------------------------------------------------------------------------- #
    # -----------------------------  Getters Properties for (RCC, Xcom-232i, Xcom-CAN)s   ---------------------------- #
    # ---------------------------------------------------------------------------------------------------------------- #
    @property
    def rcc_all(self):
        """Returns the All (RCC, Xcom-232i, Xcom-CAN)s (Multicast) device if exist else returns None"""
        return self._connected_devices.get(RCC_GROUP_DEVICE_ID)

    @property
    def rcc1(self):
        """Returns the 1st (RCC, Xcom-232i, Xcom-CAN) device if exist else returns None"""
        return self._connected_devices.get(RCC_1_DEVICE_ID)

    @property
    def xcom232i(self):
        """Returns the Xcom-232i device to which you speak with RS-232 if exist else returns None"""
        return self._connected_devices.get(XCOM232i_DEVICE_ID)

    @property
    def rcc2(self):
        """Returns the 2nd (RCC, Xcom-232i, Xcom-CAN) device if exist else returns None"""
        return self._connected_devices.get(RCC_2_DEVICE_ID)

    @property
    def rcc3(self):
        """Returns the 3rd (RCC, Xcom-232i, Xcom-CAN) device if exist else returns None"""
        return self._connected_devices.get(RCC_3_DEVICE_ID)

    @property
    def rcc4(self):
        """Returns the 4th (RCC, Xcom-232i, Xcom-CAN) device if exist else returns None"""
        return self._connected_devices.get(RCC_4_DEVICE_ID)

    @property
    def rcc5(self):
        """Returns the 5th (RCC, Xcom-232i, Xcom-CAN) device if exist else returns None"""
        return self._connected_devices.get(RCC_5_DEVICE_ID)

# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------  End of NodeObserver Class  ------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
