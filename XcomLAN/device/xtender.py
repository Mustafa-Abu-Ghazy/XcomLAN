# -*- coding: utf-8 -*-
#
"""
Implementation of Device-Class for the Xtender device type.
"""
import logging

from .base_device import BaseDevice
from .device_type import DeviceType
from ..appendix import XTENDER_INFOS


# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------  Xtender Class  ------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class Xtender(BaseDevice):
    """
    Provides access to a Xtender device.

    A series of products allowing for system capacities from 0.5kVA to 72kVA that allow for the optimal use of available
    energy, either as an off-grid inverter, battery charger, current injector, or support to an AC source.
    The Xtender is a high-tech device and a key player in the management of an energy system.
    <https://www.studer-innotec.com/en/products/xtender-series/>
    """

    def __init__(self, device_address, scom=None, user_infos_table=XTENDER_INFOS):
        """
        :param device_address The device number on the SCOM interface. Own address of the device.
        :type device_address int
        """
        super(Xtender, self).__init__(device_address, scom)
        self.log = logging.getLogger(__name__ + ":" + self.node_name)
        self._deviceType = DeviceType.XTENDER
        self.set_user_infos_table(user_infos_table)

# -------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------  End of Xtender Class  ---------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
