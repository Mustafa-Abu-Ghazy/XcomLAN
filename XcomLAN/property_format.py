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
# ----------------------------------------------  Formats Of Properties  --------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
from enum import Enum


class PropertyFormat(Enum):
    """
    Enum represents all the formats of different properties:
    used as value for 'Format' in INFOS, and as 'Scom format' in PARAMETERS
        - 0: Not supported
        - 1: BOOL
        - 2: FLOAT
        - 3: INT32
        - 4: INT32 (Signal)
        - 5: SHORT ENUM
        - 6: LONG ENUM
        - 7: ONLY LEVEL
    usage like:
        print(PropertyFormat.FLOAT) # <PropertyFormat.FLOAT: 2>
        print(PropertyFormat.FLOAT.value) # 2
        print(PropertyFormat.FLOAT.name) # "FLOAT"
    """

    NOT_SUPPORTED = 0
    BOOL = 1
    FLOAT = 2
    INT32 = 3
    INT32_SIGNAL = 4
    SHORT_ENUM = 5
    LONG_ENUM = 6
    ONLY_LEVEL = 7

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

# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------  End of Formats Of Properties  ------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
