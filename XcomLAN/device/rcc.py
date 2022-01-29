# -*- coding: utf-8 -*-
#
"""
Implementation of Device-Class for the RCC device type.
"""
import logging

from .base_device import BaseDevice
from .device_type import DeviceType


# -------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------  RCC Class  --------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class RCC(BaseDevice):
    """
    Provides access to a RCC, Xcom-232i device.

    The RCC enables the user to supervise the system and to completely adapt it to the needs through the many parameter
    settings available on the Xtenders, on the VarioTracks and on the VarioStrings.
    <https://www.studer-innotec.com/en/accessoires/compact-series/rcc-01-remote-control-1061>
    <https://www.studer-innotec.com/en/accessoires/xtender-series/rcc-02-remote-control-and-programming-centre-767>
    <https://www.studer-innotec.com/en/accessoires/xtender-series/rcc-03-remote-control-and-programming-centre-768>
    <https://www.studer-innotec.com/en/accessoires/variotrack-series/rcc-02-remote-control-and-programming-centre-767>
    <https://www.studer-innotec.com/en/accessoires/variotrack-series/rcc-03-remote-control-and-programming-centre-768>
    <https://www.studer-innotec.com/en/accessoires/variostring-series/rcc-02-remote-control-and-programming-centre-767>
    <https://www.studer-innotec.com/en/accessoires/variostring-series/rcc-03-remote-control-and-programming-centre-768>

    Communication module Xcom-232i
    The communication module Xcom-232i, equipped with a serial port RS-232, enables to be informed of the state of
     a system consisting of one or several Xtenders, VarioTracks or VarioStrings.
    <https://www.studer-innotec.com/en/accessoires/xtender-series/communication-module-xcom-232i-770>
    <https://www.studer-innotec.com/en/accessoires/xtender-series/communication-sets-by-internet-with-xcom-lan--xcom-gsm-771>
    <https://www.studer-innotec.com/en/accessoires/variotrack-series/communication-module-xcom-232i-770>
    <https://www.studer-innotec.com/en/accessoires/variotrack-series/communication-sets-by-internet-with-xcom-lan--xcom-gsm-771>
    <https://www.studer-innotec.com/en/accessoires/variostring-series/communication-module-xcom-232i-770>
    <https://www.studer-innotec.com/en/accessoires/variostring-series/communication-sets-by-internet-with-xcom-lan--xcom-gsm-771>
    """

    def __init__(self, device_address, scom=None):
        """
        :param device_address The device number on the SCOM interface. Own address of the device.
        :type device_address int
        """
        super(RCC, self).__init__(device_address, scom)
        self.log = logging.getLogger(__name__ + ":" + self.node_name)
        self._deviceType = DeviceType.RCC

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------  End of RCC Class  ----------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
