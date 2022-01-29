# -*- coding: utf-8 -*-
#
"""
Implementation of Device-Class for the VarioTrack device type.
"""
import logging

from .base_device import BaseDevice
from .device_type import DeviceType
from ..appendix import VARIO_TRACK_INFOS


# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------  VarioTrack Class  ------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
class VarioTrack(BaseDevice):
    """
    Provides access to a VarioTrack device.

    The VarioTrack family consists of 3 models of MPPT solar charge controllers for systems with solar PV capacity
    from 0.6 - 75kWp (with 15 in parallel), a PV input voltage up to 150Vdc, and 12, 24 or 48V battery banks.
    <https://www.studer-innotec.com/en/products/variotrack-series/>
    """

    def __init__(self, device_address, scom=None, user_infos_table=VARIO_TRACK_INFOS):
        """
        :param device_address The device number on the SCOM interface. Own address of the device.
        :type device_address int
        """
        super(VarioTrack, self).__init__(device_address, scom)
        self.log = logging.getLogger(__name__ + ":" + self.node_name)
        self._deviceType = DeviceType.VARIO_TRACK
        self.set_user_infos_table(user_infos_table)

# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------  End of VarioTrack Class  -------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
