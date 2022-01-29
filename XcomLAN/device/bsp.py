# -*- coding: utf-8 -*-
#
"""
Implementation of Device-Class for the BSP device type.
"""
import logging

from .base_device import BaseDevice
from .device_type import DeviceType
from ..appendix import BSP_INFOS


# -------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------  BSP Class  --------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class BSP(BaseDevice):
    """
    Provides access to a BSP device.

    One of the most important information for a safe and effective operating of an energy system with batteries is their
    state of charge. The BSP offers, for Xtender, VarioTrack and VarioString systems, a highly precise measuring and an
    extremely efficient algorithm that calculates the state of charge in the most accurate way.
    <https://www.studer-innotec.com/en/accessoires/xtender-series/battery-status-processor-bsp-769>
    <https://www.studer-innotec.com/en/accessoires/variotrack-series/battery-status-processor-bsp-769>
    <https://www.studer-innotec.com/en/accessoires/variostring-series/battery-status-processor-bsp-769>
    """

    def __init__(self, device_address, scom=None, user_infos_table=BSP_INFOS):
        """
        :param device_address The device number on the SCOM interface. Own address of the device.
        :type device_address int
        """
        super(BSP, self).__init__(device_address, scom)
        self.log = logging.getLogger(__name__ + ":" + self.node_name)
        self._deviceType = DeviceType.BSP
        self.set_user_infos_table(user_infos_table)

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------  End of BSP Class  ----------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
