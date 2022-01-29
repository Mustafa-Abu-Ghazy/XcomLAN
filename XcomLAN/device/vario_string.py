# -*- coding: utf-8 -*-
#
"""
Implementation of Device-Class for the VarioString device type.
"""
import logging

from .base_device import BaseDevice
from .device_type import DeviceType
from ..appendix import VARIO_STRING_INFOS


# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------  VarioString Class  ----------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class VarioString(BaseDevice):
    """
    Provides access to a VarioString device.

    The VarioString family consists of 2 models of MPPT solar charge controllers with 70A or 120A battery charge current
    for 48V batteries.
    <https://www.studer-innotec.com/en/products/variostring-series/>
    """

    def __init__(self, device_address, scom=None, user_infos_table=VARIO_STRING_INFOS):
        """
        :param device_address The device number on the SCOM interface. Own address of the device.
        :type device_address int
        """
        super(VarioString, self).__init__(device_address, scom)
        self.log = logging.getLogger(__name__ + ":" + self.node_name)
        self._deviceType = DeviceType.VARIO_STRING
        self.set_user_infos_table(user_infos_table)

# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------  End of VarioString Class  -------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
