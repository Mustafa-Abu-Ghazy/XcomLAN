#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file contains Enum represents all the types of different devices:
    - 0: Unknown
    - 1: Xtender
    - 2: Compact
    - 3: VarioTrack
    - 4: VarioString
    - 5: RCC, Xcom-232i, Xcom-CAN
    - 6: BSP
"""
# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------  Types Of Devices  ------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
from enum import Enum

from ..appendix import BSP_INFOS
from ..appendix import RCC_PARAMETERS
from ..appendix import VARIO_STRING_INFOS
from ..appendix import VARIO_TRACK_INFOS
from ..appendix import XTENDER_INFOS


class DeviceType(Enum):
    """
    Enum represents all the types of different devices:
        - 0: Unknown
        - 1: Xtender
        - 2: Compact
        - 3: VarioTrack
        - 4: VarioString
        - 5: RCC, Xcom-232i, Xcom-CAN
        - 6: BSP
    usage like:
        print(DeviceType.XTENDER) # <DeviceType.XTENDER: 1>
        print(DeviceType.XTENDER.value) # 1
        print(DeviceType.XTENDER.name) # "XTENDER"
    """

    UNKNOWN = 0  # Unknown Device

    # ---------------------------------------------------------------------------------------------------------------- #
    # --------------------------------------------------- Xtender  --------------------------------------------------- #
    # ---------------------------------------------------------------------------------------------------------------- #
    XTENDER = 1  # Off-Grid Inverter / Battery Charger / Current Injector / Support To An AC Source
    """
    A series of products allowing for system capacities from 0.5kVA to 72kVA that allow for the optimal use of available
     energy, either as an off-grid inverter, battery charger, current injector, or support to an AC source. 
    The Xtender is a high-tech device and a key player in the management of an energy system.
    <https://www.studer-innotec.com/en/products/xtender-series/>
    """

    # ---------------------------------------------------------------------------------------------------------------- #
    # --------------------------------------------------- Compact  --------------------------------------------------- #
    # ---------------------------------------------------------------------------------------------------------------- #
    COMPACT = 2  # Off-Grid Inverter / Battery Charger / Solar Charge Controller
    """
    The Compact series includes devices with a power level ranging from 1.1kVA to 4kVA that allow for optimal use of 
    available energy, either as an off-grid inverter, battery charger or solar charge controller. 
    This range of robust products ready to be used offers an excellent price/efficiency relationship. 
    For 12, 24, or 48V battery banks.
    <https://www.studer-innotec.com/en/products/compact-series/>
    """

    # ---------------------------------------------------------------------------------------------------------------- #
    # -------------------------------------------------- VarioTrack  ------------------------------------------------- #
    # ---------------------------------------------------------------------------------------------------------------- #
    VARIO_TRACK = 3  # MPPT Solar Charge Controller
    """
    The VarioTrack family consists of 3 models of MPPT solar charge controllers for systems with solar PV capacity 
    from 0.6 - 75kWp (with 15 in parallel), a PV input voltage up to 150Vdc, and 12, 24 or 48V battery banks.
    <https://www.studer-innotec.com/en/products/variotrack-series/>
    """

    # ---------------------------------------------------------------------------------------------------------------- #
    # ------------------------------------------------- VarioString  ------------------------------------------------- #
    # ---------------------------------------------------------------------------------------------------------------- #
    VARIO_STRING = 4  # MPPT Solar Charge Controller
    """
    The VarioString family consists of 2 models of MPPT solar charge controllers with 70A or 120A battery charge current 
    for 48V batteries.
    <https://www.studer-innotec.com/en/products/variostring-series/>
    """

    # ---------------------------------------------------------------------------------------------------------------- #
    # ------------------------------------------- RCC, Xcom-232i, Xcom-CAN  ------------------------------------------ #
    # ---------------------------------------------------------------------------------------------------------------- #
    RCC = 5  # Remote Control and Programming Centre
    """
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
    
    Multi-protocol communication module Xcom-CAN
    This tool enables the communication between BMS, Lithium Battery Management Systems, and products of the Xtender / 
    VarioTrack / VarioString family. The list of batteries (manufacturers) compatible is available on request at 
    Studer-Innotec. The Xcom-CAN makes it also possible for any device with a CAN bus (PC, PLC and microcontroller) to 
    interact with all products of the Xtender / Vario family via a proprietary protocol. 
    Like having the system controlled by a supervisor (SCADA) while giving the third system an access to all data 
    (configuration parameters and datalog).
    <https://www.studer-innotec.com/en/accessoires/xtender-series/multi-protocol-communication-module-xcom-can-5345>
    <https://www.studer-innotec.com/en/accessoires/variotrack-series/multi-protocol-communication-module-xcom-can-5345>
    <https://www.studer-innotec.com/en/accessoires/variostring-series/multi-protocol-communication-module-xcom-can-5345>
    """

    # ---------------------------------------------------------------------------------------------------------------- #
    # ----------------------------------------------------- BSP  ----------------------------------------------------- #
    # ---------------------------------------------------------------------------------------------------------------- #
    BSP = 6  # Battery Status Processor
    """
    One of the most important information for a safe and effective operating of an energy system with batteries is their 
    state of charge. The BSP offers, for Xtender, VarioTrack and VarioString systems, a highly precise measuring and an 
    extremely efficient algorithm that calculates the state of charge in the most accurate way.
    <https://www.studer-innotec.com/en/accessoires/xtender-series/battery-status-processor-bsp-769>
    <https://www.studer-innotec.com/en/accessoires/variotrack-series/battery-status-processor-bsp-769>
    <https://www.studer-innotec.com/en/accessoires/variostring-series/battery-status-processor-bsp-769>
    """

    # ---------------------------------------------------------------------------------------------------------------- #
    # ------------------------------------------------- classmethods  ------------------------------------------------ #
    # ---------------------------------------------------------------------------------------------------------------- #
    @classmethod
    def has_value(cls, value):
        """
        Check if the Enum has the provided value or not
        :param value: value to be checked
        :type value: int
        :rtype: bool
        """
        return value in cls._value2member_map_

    @classmethod
    def get_reference_search_object_id(cls, device_type):
        """
        Returns the reference object id to be used to search for a device based on its type.
        """
        assert type(device_type) == cls, 'Unsupported Device Type'

        if device_type == DeviceType.XTENDER:
            search_object_id = list(XTENDER_INFOS.keys())[0]
        elif device_type == DeviceType.COMPACT:
            assert False, 'No Implementation of Device-Class for the Compact device type.'
        elif device_type == DeviceType.VARIO_TRACK:
            search_object_id = list(VARIO_TRACK_INFOS.keys())[0]
        elif device_type == DeviceType.VARIO_STRING:
            search_object_id = list(VARIO_STRING_INFOS.keys())[0]
        elif device_type == DeviceType.RCC:
            # TODO: Add support for reading parameters
            search_object_id = list(RCC_PARAMETERS.keys())[0]
        elif device_type == DeviceType.BSP:
            search_object_id = list(BSP_INFOS.keys())[0]
        else:
            assert False, 'Not Supported device type.'

        return search_object_id

# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------  End of Types Of Devices  -------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
