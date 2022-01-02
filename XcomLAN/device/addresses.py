#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file contains all the addresses of different devices:
    - Xtender
    - VarioTrack
    - RCC, Xcom-232i, Xcom-CAN
    - BSP
    - VarioString
Inspired from studer-innotec/xcomcan : addresses.py
<https://github.com/studer-innotec/xcomcan/blob/master/xcomcan/addresses.py>

And refined based on '3.5 ADDRESSING THE DEVICES' section from the Xtender serial protocol document
4O3C\\Technical specification - Xtender serial protocol.pdf
Date : 04.12.17
Version : V1.6.30 (R644)
"""
# -------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------  Addresses Of Devices  ---------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
"""
WARNINGS
----------
This file **MUST NOT** be edited.
Please read the complete documentation available on : `Studer Innotec SA <https://www.studer-innotec.com>`_ *->
Support -> Download Center -> Software and Updates -> Communication protocols Xcom-232i*
!!! DO NOT CHANGE CONFIGURATIONS BELOW !!!
"""
# -------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------- Xtender  ----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
XT_GROUP_DEVICE_ID = 100  # All Xtenders
"""
Virtual address to access all XTH, XTM and XTS (Multicast), used in:\n
    - Read User Info\n
    - Read Parameter\n
    - Write Parameter\n
"""
XT_1_DEVICE_ID = XT_GROUP_DEVICE_ID + 1  # 1st Xtender
"""
First Xtender device address, up to 9 XT allowed, ordered by the index displayed on the RCC (Unicast), used in:\n
    - Read User Info\n
    - Read Parameter\n
    - Write Parameter\n
    - Message as source address\n
"""
XT_2_DEVICE_ID = XT_GROUP_DEVICE_ID + 2  # 2nd Xtender
XT_3_DEVICE_ID = XT_GROUP_DEVICE_ID + 3  # 3rd Xtender
XT_4_DEVICE_ID = XT_GROUP_DEVICE_ID + 4  # 4th Xtender
XT_5_DEVICE_ID = XT_GROUP_DEVICE_ID + 5  # 5th Xtender
XT_6_DEVICE_ID = XT_GROUP_DEVICE_ID + 6  # 6th Xtender
XT_7_DEVICE_ID = XT_GROUP_DEVICE_ID + 7  # 7th Xtender
XT_8_DEVICE_ID = XT_GROUP_DEVICE_ID + 8  # 8th Xtender
XT_9_DEVICE_ID = XT_GROUP_DEVICE_ID + 9  # 9th Xtender
XT_DEVICE_ID_RANGE = [XT_GROUP_DEVICE_ID, XT_9_DEVICE_ID]  # Range of IDs for Xtender devices [start, end]
XT_DEVICE_ID_DEFAULT_SCAN_RANGE = [XT_1_DEVICE_ID, XT_9_DEVICE_ID]

XT_L1 = 191  # 1st Phase L1
"""
virtual address to access properties on all inverters on a phase :\n
    - 191 for L1\n
    - 192 for L2\n
    - 193 for L3\n
A read access return the value of the master of the phase.
"""
XT_L2 = 192  # 2nd Phase L2
XT_L3 = 193  # 3rd Phase L3

# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------- VarioTrack  --------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
VT_GROUP_DEVICE_ID = 300  # All VarioTracks
"""
Virtual address to access all VarioTrack (Multicast), used in:\n
    - Read User Info\n
    - Read Parameter\n
    - Write Parameter\n
"""
VT_1_DEVICE_ID = VT_GROUP_DEVICE_ID + 1  # 1st VarioTrack
"""
First VarioTrack device address, up to 15 VarioTrack allowed, ordered by the index displayed on the RCC (Unicast), 
used in:\n
    - Read User Info\n
    - Read Parameter\n
    - Write Parameter\n
    - Message as source address\n
"""
VT_2_DEVICE_ID = VT_GROUP_DEVICE_ID + 2  # 2nd VarioTrack
VT_3_DEVICE_ID = VT_GROUP_DEVICE_ID + 3  # 3rd VarioTrack
VT_4_DEVICE_ID = VT_GROUP_DEVICE_ID + 4  # 4th VarioTrack
VT_5_DEVICE_ID = VT_GROUP_DEVICE_ID + 5  # 5th VarioTrack
VT_6_DEVICE_ID = VT_GROUP_DEVICE_ID + 6  # 6th VarioTrack
VT_7_DEVICE_ID = VT_GROUP_DEVICE_ID + 7  # 7th VarioTrack
VT_8_DEVICE_ID = VT_GROUP_DEVICE_ID + 8  # 8th VarioTrack
VT_9_DEVICE_ID = VT_GROUP_DEVICE_ID + 9  # 9th VarioTrack
VT_10_DEVICE_ID = VT_GROUP_DEVICE_ID + 10  # 10th VarioTrack
VT_11_DEVICE_ID = VT_GROUP_DEVICE_ID + 11  # 11th VarioTrack
VT_12_DEVICE_ID = VT_GROUP_DEVICE_ID + 12  # 12th VarioTrack
VT_13_DEVICE_ID = VT_GROUP_DEVICE_ID + 13  # 13th VarioTrack
VT_14_DEVICE_ID = VT_GROUP_DEVICE_ID + 14  # 14th VarioTrack
VT_15_DEVICE_ID = VT_GROUP_DEVICE_ID + 15  # 15th VarioTrack
VT_DEVICE_ID_RANGE = [VT_GROUP_DEVICE_ID, VT_15_DEVICE_ID]  # Range of IDs for VarioTrack devices [start, end]
VT_DEVICE_ID_DEFAULT_SCAN_RANGE = [VT_GROUP_DEVICE_ID, VT_15_DEVICE_ID]

# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------- RCC, Xcom-232i, Xcom-CAN  -------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
RCC_GROUP_DEVICE_ID = 500  # All (RCC, Xcom-232i, Xcom-CAN)s
"""
Virtual address to access all RCC (Multicast), used in:\n
"""
RCC_1_DEVICE_ID = RCC_GROUP_DEVICE_ID + 1  # 1st RCC, Xcom-232i, Xcom-CAN
XCOM232i_DEVICE_ID = RCC_1_DEVICE_ID
"""
Based on (studer-innotec/xcomcan : addresses.py):
    First RCC device (RCC, Xcom-232i, Xcom-CAN), up to 5 allowed, ordered by the index displayed on the RCC (Unicast), 
    used in:\n
        - Message as source address\n
Based on (4O3C\\Technical specification - Xtender serial protocol.pdf):\n
    It only mentioned this address as XCOM232i_DEVICE_ID \n
    As alias for the gateway that the DTE uses to communicate (the Xcom-232i to which you speak with RS-232)\n
"""
RCC_2_DEVICE_ID = RCC_GROUP_DEVICE_ID + 2  # 2nd RCC, Xcom-232i, Xcom-CAN
RCC_3_DEVICE_ID = RCC_GROUP_DEVICE_ID + 3  # 3rd RCC, Xcom-232i, Xcom-CAN
RCC_4_DEVICE_ID = RCC_GROUP_DEVICE_ID + 4  # 4th RCC, Xcom-232i, Xcom-CAN
RCC_5_DEVICE_ID = RCC_GROUP_DEVICE_ID + 5  # 5th RCC, Xcom-232i, Xcom-CAN
RCC_DEVICE_ID_RANGE = [RCC_GROUP_DEVICE_ID, RCC_5_DEVICE_ID]  # Range of IDs for RCC devices [start, end]
RCC_DEVICE_ID_DEFAULT_SCAN_RANGE = [XCOM232i_DEVICE_ID, XCOM232i_DEVICE_ID]

# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------- BSP  ------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
BSP_GROUP_DEVICE_ID = 600  # All BSPs
"""
Virtual address to access the BSP (Multicast, but only one BSP per installation), used in:\n
    - Read User Info\n
    - Read Parameter\n
    - Write Parameter\n
"""
BSP_DEVICE_ID = BSP_GROUP_DEVICE_ID + 1  # 1st BSP
"""
A single BSP (Unicast), used in:\n
    - Read User Info\n
    - Read Parameter\n
    - Write Parameter\n
    - Message as source address\n
"""
BSP_DEVICE_ID_RANGE = [BSP_GROUP_DEVICE_ID, BSP_DEVICE_ID]  # Range of IDs for BSP devices [start, end]
BSP_DEVICE_ID_DEFAULT_SCAN_RANGE = [BSP_DEVICE_ID, BSP_DEVICE_ID]

# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------- VarioString  --------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
VS_GROUP_DEVICE_ID = 700  # All VarioStrings
"""
Virtual address to access all VarioString (Multicast), used in:\n
    - Read User Info\n
    - Read Parameter\n
    - Write Parameter\n
"""
VS_1_DEVICE_ID = VS_GROUP_DEVICE_ID + 1  # 1st VarioString
"""
First VarioString device address, up to 15 VarioString allowed, ordered by the index displayed on the RCC (Unicast), 
used in:\n
    - Read User Info\n
    - Read Parameter\n
    - Write Parameter\n
    - Message as source address\n
"""
VS_2_DEVICE_ID = VS_GROUP_DEVICE_ID + 2  # 2nd VarioString
VS_3_DEVICE_ID = VS_GROUP_DEVICE_ID + 3  # 3rd VarioString
VS_4_DEVICE_ID = VS_GROUP_DEVICE_ID + 4  # 4th VarioString
VS_5_DEVICE_ID = VS_GROUP_DEVICE_ID + 5  # 5th VarioString
VS_6_DEVICE_ID = VS_GROUP_DEVICE_ID + 6  # 6th VarioString
VS_7_DEVICE_ID = VS_GROUP_DEVICE_ID + 7  # 7th VarioString
VS_8_DEVICE_ID = VS_GROUP_DEVICE_ID + 8  # 8th VarioString
VS_9_DEVICE_ID = VS_GROUP_DEVICE_ID + 9  # 9th VarioString
VS_10_DEVICE_ID = VS_GROUP_DEVICE_ID + 10  # 10th VarioString
VS_11_DEVICE_ID = VS_GROUP_DEVICE_ID + 11  # 11th VarioString
VS_12_DEVICE_ID = VS_GROUP_DEVICE_ID + 12  # 12th VarioString
VS_13_DEVICE_ID = VS_GROUP_DEVICE_ID + 13  # 13th VarioString
VS_14_DEVICE_ID = VS_GROUP_DEVICE_ID + 14  # 14th VarioString
VS_15_DEVICE_ID = VS_GROUP_DEVICE_ID + 15  # 15th VarioString
VS_DEVICE_ID_RANGE = [VS_GROUP_DEVICE_ID, VS_15_DEVICE_ID]  # Range of IDs for VarioString devices [start, end]
VS_DEVICE_ID_DEFAULT_SCAN_RANGE = [VS_GROUP_DEVICE_ID, VS_15_DEVICE_ID]

# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------- ALL MULTICAST_ADDRESSES  --------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
MULTICAST_ADDRESSES = [XT_GROUP_DEVICE_ID,
                       VT_GROUP_DEVICE_ID,
                       RCC_GROUP_DEVICE_ID,
                       BSP_GROUP_DEVICE_ID,
                       VS_GROUP_DEVICE_ID]

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------  End of Addresses Of Devices  ------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
