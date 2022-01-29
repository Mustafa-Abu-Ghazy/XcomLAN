# coding=utf-8
"""
This file contains all the information within the  Xtender serial protocol appendix document
4O3C\\Technical specification - Xtender serial protocol appendix
Date : 01.07.21
Version : V1.6.28 (R676)
"""

from .property_format import PropertyFormat

# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------- 1. Appendix --------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# The information in the appendices is valid for the latest software release. For a detailed changelog,
# please see the document Release_Rxxx.pdf in the latest “Studer system update” available on www.studer-innotec.com.
# A major release (from R5xx to R6xx, for example) can imply significant changes that should be validated.

S = None  # A Place Holder for the INT32 (Signal) Scom format value, used as Default, Min, Max for the parameter.

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------- 1.1 Xtender 120Vac specific parameters -------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# While using Xtenders -01 (120Vac), some parameters have specific values.
# The following list contain them. The others are the same for all Xtender types.
# Contains 7 Parameters
XTENDER_120VAC_SPECIFIC_PARAMETERS = {
    1286: {
        "Level": "Expert",
        "Nr": 1286,
        "parameter description": "AC Output voltage",
        "Unit": "Vac",
        "Default": 120,
        "Min": 55,
        "Max": 140,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1560: {
        "Level": "Expert",
        "Nr": 1560,
        "parameter description": "Max AC voltage increase with battery voltage",
        "Unit": "Vac",
        "Default": 5,
        "Min": 2,
        "Max": 8,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1309: {
        "Level": "Expert",
        "Nr": 1309,
        "parameter description": "AC input low limit voltage to allow charger function",
        "Unit": "Vac",
        "Default": 90,
        "Min": 50,
        "Max": 115,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1433: {
        "Level": "Expert",
        "Nr": 1433,
        "parameter description": "Adaptation range of the input current according to the input voltage",
        "Unit": "Vac",
        "Default": 5,
        "Min": 2,
        "Max": 15,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1199: {
        "Level": "Expert",
        "Nr": 1199,
        "parameter description": "Input voltage giving an opening of the transfer relay with delay",
        "Unit": "Vac",
        "Default": 100,
        "Min": 40,
        "Max": 115,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1200: {
        "Level": "Expert",
        "Nr": 1200,
        "parameter description": "Input voltage giving an immediate opening of the transfer relay (UPS)",
        "Unit": "Vac",
        "Default": 90,
        "Min": 40,
        "Max": 115,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1432: {
        "Level": "Inst.",
        "Nr": 1432,
        "parameter description": "Absolute max limit for input voltage",
        "Unit": "Vac",
        "Default": 135,
        "Min": 117.5,
        "Max": 145,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
}

# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------- 1.2 Xtender parameters ---------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Contains 406 Parameters
XTENDER_PARAMETERS = {
    1100: {
        "Level": "Basic",
        "Nr": 1100,
        "parameter description": "BASIC SETTINGS",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1551: {
        "Level": "Basic",
        "Nr": 1551,
        "parameter description": "Basic parameters set by means of the potentiomenter in the XTS",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1107: {
        "Level": "Basic",
        "Nr": 1107,
        "parameter description": "Maximum current of AC source (Input limit)",
        "Unit": "Aac",
        "Default": 32,
        "Min": 2,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1138: {
        "Level": "Basic",
        "Nr": 1138,
        "parameter description": "Battery charge current",
        "Unit": "Adc",
        "Default": 60,
        "Min": 0,
        "Max": 200,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1126: {
        "Level": "Basic",
        "Nr": 1126,
        "parameter description": "Smart-Boost allowed",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1124: {
        "Level": "Basic",
        "Nr": 1124,
        "parameter description": "Inverter allowed",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1125: {
        "Level": "Expert",
        "Nr": 1125,
        "parameter description": "Charger allowed",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1552: {
        "Level": "Basic",
        "Nr": 1552,
        "parameter description": "Type of detection of the grid loss (AC-In)",
        "Unit": "",
        "Default": 2,
        "Min": 1,
        "Max": 4,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Slow 2:Tolerant 4:Fast"
    },
    1187: {
        "Level": "Basic",
        "Nr": 1187,
        "parameter description": "Standby level",
        "Unit": "%",
        "Default": 10,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    1395: {
        "Level": "Basic",
        "Nr": 1395,
        "parameter description": "Restore default settings",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    1287: {
        "Level": "Inst.",
        "Nr": 1287,
        "parameter description": "Restore factory settings",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    1137: {
        "Level": "Expert",
        "Nr": 1137,
        "parameter description": "BATTERY MANAGEMENT AND CYCLE",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1646: {
        "Level": "Inst.",
        "Nr": 1646,
        "parameter description": "Charger uses only power from AC-Out",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1139: {
        "Level": "Expert",
        "Nr": 1139,
        "parameter description": "Temperature compensation",
        "Unit": "mV/°C/cell",
        "Default": -3,
        "Min": -8,
        "Max": 0,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1615: {
        "Level": "QSP",
        "Nr": 1615,
        "parameter description": "Fast charge/inject regulation",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1645: {
        "Level": "QSP",
        "Nr": 1645,
        "parameter description": "Pulses cutting regulation for XT (Not XTS)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1568: {
        "Level": "Expert",
        "Nr": 1568,
        "parameter description": "Undervoltage",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1108: {
        "Level": "Expert",
        "Nr": 1108,
        "parameter description": "Battery undervoltage level without load",
        "Unit": "Vdc",
        "Default": 46.3,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1531: {
        "Level": "Expert",
        "Nr": 1531,
        "parameter description": "Battery undervoltage dynamic compensation",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1191: {
        "Level": "Expert",
        "Nr": 1191,
        "parameter description": "Battery undervoltage dynamic compensation",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1532: {
        "Level": "Expert",
        "Nr": 1532,
        "parameter description": "Kind of dynamic compensation",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 0:Manual 1:Automatic"
    },
    1632: {
        "Level": "QSP",
        "Nr": 1632,
        "parameter description": "Automatic adaptation of dynamic compensation",
        "Unit": "%",
        "Default": 65,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1109: {
        "Level": "Expert",
        "Nr": 1109,
        "parameter description": "Battery undervoltage level at full load",
        "Unit": "Vdc",
        "Default": 42,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1190: {
        "Level": "Expert",
        "Nr": 1190,
        "parameter description": "Battery undervoltage duration before turn off",
        "Unit": "min",
        "Default": 3,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1110: {
        "Level": "Expert",
        "Nr": 1110,
        "parameter description": "Restart voltage after batteries undervoltage",
        "Unit": "Vdc",
        "Default": 48,
        "Min": 37.9,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1194: {
        "Level": "Expert",
        "Nr": 1194,
        "parameter description": "Battery adaptive low voltage (B.L.O)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1195: {
        "Level": "Expert",
        "Nr": 1195,
        "parameter description": "Max voltage for adaptive low voltage",
        "Unit": "Vdc",
        "Default": 49.9,
        "Min": 37.9,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1307: {
        "Level": "Expert",
        "Nr": 1307,
        "parameter description": "Reset voltage for adaptive correction",
        "Unit": "Vdc",
        "Default": 52.8,
        "Min": 37.9,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1298: {
        "Level": "Expert",
        "Nr": 1298,
        "parameter description": "Increment step of the adaptive low voltage",
        "Unit": "Vdc",
        "Default": 0.5,
        "Min": 0,
        "Max": 1.4,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.01"
    },
    1121: {
        "Level": "Expert",
        "Nr": 1121,
        "parameter description": "Battery overvoltage level",
        "Unit": "Vdc",
        "Default": 68.2,
        "Min": 37.9,
        "Max": 74.4,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1122: {
        "Level": "Expert",
        "Nr": 1122,
        "parameter description": "Restart voltage level after an battery overvoltage",
        "Unit": "Vdc",
        "Default": 64.8,
        "Min": 37.9,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1140: {
        "Level": "Expert",
        "Nr": 1140,
        "parameter description": "Floating voltage",
        "Unit": "Vdc",
        "Default": 54.4,
        "Min": 37.9,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1467: {
        "Level": "Expert",
        "Nr": 1467,
        "parameter description": "Force phase of floating",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    1141: {
        "Level": "Expert",
        "Nr": 1141,
        "parameter description": "New cycle menu",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1142: {
        "Level": "Expert",
        "Nr": 1142,
        "parameter description": "Force a new cycle",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    1608: {
        "Level": "Inst.",
        "Nr": 1608,
        "parameter description": "Use dynamic compensation of battery level (new cycle)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1143: {
        "Level": "Expert",
        "Nr": 1143,
        "parameter description": "Voltage level 1 to start a new cycle",
        "Unit": "Vdc",
        "Default": 49.9,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1144: {
        "Level": "Expert",
        "Nr": 1144,
        "parameter description": "Time period under voltage level 1 to start a new cycle",
        "Unit": "min",
        "Default": 30,
        "Min": 0,
        "Max": 240,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1145: {
        "Level": "Expert",
        "Nr": 1145,
        "parameter description": "Voltage level 2 to start a new cycle",
        "Unit": "Vdc",
        "Default": 49.2,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1146: {
        "Level": "Expert",
        "Nr": 1146,
        "parameter description": "Time period under voltage level 2 to start a new cycle",
        "Unit": "sec",
        "Default": 60,
        "Min": 0,
        "Max": 600,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "2"
    },
    1149: {
        "Level": "Expert",
        "Nr": 1149,
        "parameter description": "New cycle priority on absorption and equalization phases",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1147: {
        "Level": "Expert",
        "Nr": 1147,
        "parameter description": "Cycling restricted",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1148: {
        "Level": "Expert",
        "Nr": 1148,
        "parameter description": "Minimal delay between cycles",
        "Unit": "hours",
        "Default": 3,
        "Min": 0,
        "Max": 540,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1451: {
        "Level": "Expert",
        "Nr": 1451,
        "parameter description": "Absorption phase",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1155: {
        "Level": "Expert",
        "Nr": 1155,
        "parameter description": "Absorption phase allowed",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1156: {
        "Level": "Expert",
        "Nr": 1156,
        "parameter description": "Absorption voltage",
        "Unit": "Vdc",
        "Default": 57.6,
        "Min": 37.9,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1157: {
        "Level": "Expert",
        "Nr": 1157,
        "parameter description": "Absorption duration",
        "Unit": "hours",
        "Default": 2,
        "Min": 0,
        "Max": 18,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    1158: {
        "Level": "Expert",
        "Nr": 1158,
        "parameter description": "End of absorption triggered with current",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1159: {
        "Level": "Expert",
        "Nr": 1159,
        "parameter description": "Current limit to quit the absorption phase",
        "Unit": "Adc",
        "Default": 4,
        "Min": 1,
        "Max": 200,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1160: {
        "Level": "Expert",
        "Nr": 1160,
        "parameter description": "Maximal frequency of absorption control",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1161: {
        "Level": "Expert",
        "Nr": 1161,
        "parameter description": "Minimal delay since last absorption",
        "Unit": "hours",
        "Default": 2,
        "Min": 0,
        "Max": 540,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1452: {
        "Level": "Expert",
        "Nr": 1452,
        "parameter description": "Equalization phase",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1163: {
        "Level": "Expert",
        "Nr": 1163,
        "parameter description": "Equalization allowed",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1162: {
        "Level": "Expert",
        "Nr": 1162,
        "parameter description": "Force equalization",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    1291: {
        "Level": "Expert",
        "Nr": 1291,
        "parameter description": "Equalization before absorption phase",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1290: {
        "Level": "Expert",
        "Nr": 1290,
        "parameter description": "Equalization current",
        "Unit": "Adc",
        "Default": 60,
        "Min": 1,
        "Max": 200,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1164: {
        "Level": "Expert",
        "Nr": 1164,
        "parameter description": "Equalization voltage",
        "Unit": "Vdc",
        "Default": 62.4,
        "Min": 37.9,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1165: {
        "Level": "Expert",
        "Nr": 1165,
        "parameter description": "Equalization duration",
        "Unit": "hours",
        "Default": 0.5,
        "Min": 0.2,
        "Max": 10,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    1166: {
        "Level": "Expert",
        "Nr": 1166,
        "parameter description": "Number of cycles before an equalization",
        "Unit": "",
        "Default": 25,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1284: {
        "Level": "Expert",
        "Nr": 1284,
        "parameter description": "Equalization with fixed interval",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1285: {
        "Level": "Expert",
        "Nr": 1285,
        "parameter description": "Weeks between equalizations",
        "Unit": "weeks",
        "Default": 26,
        "Min": 1,
        "Max": 104,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1168: {
        "Level": "Expert",
        "Nr": 1168,
        "parameter description": "End of equalization triggered with current",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1169: {
        "Level": "Expert",
        "Nr": 1169,
        "parameter description": "Current threshold to end equalization phase",
        "Unit": "Adc",
        "Default": 4,
        "Min": 1,
        "Max": 30,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1453: {
        "Level": "Expert",
        "Nr": 1453,
        "parameter description": "Reduced floating phase",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1170: {
        "Level": "Expert",
        "Nr": 1170,
        "parameter description": "Reduced floating allowed",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1171: {
        "Level": "Expert",
        "Nr": 1171,
        "parameter description": "Floating duration before reduced floating",
        "Unit": "days",
        "Default": 1,
        "Min": 0,
        "Max": 31,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1172: {
        "Level": "Expert",
        "Nr": 1172,
        "parameter description": "Reduced floating voltage",
        "Unit": "Vdc",
        "Default": 52.8,
        "Min": 37.9,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1454: {
        "Level": "Expert",
        "Nr": 1454,
        "parameter description": "Periodic absorption phase",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1173: {
        "Level": "Expert",
        "Nr": 1173,
        "parameter description": "Periodic absorption allowed",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1174: {
        "Level": "Expert",
        "Nr": 1174,
        "parameter description": "Periodic absorption voltage",
        "Unit": "Vdc",
        "Default": 57.6,
        "Min": 37.9,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1175: {
        "Level": "Expert",
        "Nr": 1175,
        "parameter description": "Reduced floating duration before periodic absorption",
        "Unit": "days",
        "Default": 7,
        "Min": 0,
        "Max": 31,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1176: {
        "Level": "Expert",
        "Nr": 1176,
        "parameter description": "Periodic absorption duration",
        "Unit": "hours",
        "Default": 0.5,
        "Min": 0,
        "Max": 10,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    1186: {
        "Level": "Expert",
        "Nr": 1186,
        "parameter description": "INVERTER",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1286: {
        "Level": "Expert",
        "Nr": 1286,
        "parameter description": "AC Output voltage",
        "Unit": "Vac",
        "Default": 230,
        "Min": 110,
        "Max": 280,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1548: {
        "Level": "Expert",
        "Nr": 1548,
        "parameter description": "AC voltage increase according to battery voltage",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1560: {
        "Level": "Expert",
        "Nr": 1560,
        "parameter description": "Max AC voltage increase with battery voltage",
        "Unit": "Vac",
        "Default": 10,
        "Min": 4,
        "Max": 16,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1112: {
        "Level": "Expert",
        "Nr": 1112,
        "parameter description": "Inverter frequency",
        "Unit": "Hz",
        "Default": 50,
        "Min": 45,
        "Max": 65,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1536: {
        "Level": "Expert",
        "Nr": 1536,
        "parameter description": "Inverter frequency increase when battery full",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1549: {
        "Level": "Expert",
        "Nr": 1549,
        "parameter description": "Inverter frequency increase according to battery voltage",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1546: {
        "Level": "Expert",
        "Nr": 1546,
        "parameter description": "Max frequency increase",
        "Unit": "Hz",
        "Default": 4,
        "Min": 0,
        "Max": 10,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1534: {
        "Level": "Expert",
        "Nr": 1534,
        "parameter description": "Speed of voltage or frequency change in function of battery",
        "Unit": "",
        "Default": 0,
        "Min": -4,
        "Max": 3,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1420: {
        "Level": "Expert",
        "Nr": 1420,
        "parameter description": "Standby and turn on",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1189: {
        "Level": "Expert",
        "Nr": 1189,
        "parameter description": "Time delay between standby pulses",
        "Unit": "sec",
        "Default": 0.8,
        "Min": 0.2,
        "Max": 10,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.2"
    },
    1188: {
        "Level": "Expert",
        "Nr": 1188,
        "parameter description": "Standby number of pulses",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 10,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1599: {
        "Level": "Expert",
        "Nr": 1599,
        "parameter description": "Softstart duration",
        "Unit": "sec",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    1438: {
        "Level": "Expert",
        "Nr": 1438,
        "parameter description": "Solsafe presence Energy source at AC-Out side",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1572: {
        "Level": "QSP",
        "Nr": 1572,
        "parameter description": "Modulator ru_soll",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1197: {
        "Level": "Expert",
        "Nr": 1197,
        "parameter description": "AC-IN AND TRANSFER",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1128: {
        "Level": "Expert",
        "Nr": 1128,
        "parameter description": "Transfer relay allowed",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1580: {
        "Level": "Expert",
        "Nr": 1580,
        "parameter description": "Delay before closing transfer relay",
        "Unit": "min",
        "Default": 0,
        "Min": 0,
        "Max": 30,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    1607: {
        "Level": "Inst.",
        "Nr": 1607,
        "parameter description": "Limitation of the power Boost",
        "Unit": "%",
        "Default": 100,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1471: {
        "Level": "Expert",
        "Nr": 1471,
        "parameter description": "Max input current modification",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1566: {
        "Level": "Expert",
        "Nr": 1566,
        "parameter description": "Using a secondary value for the maximum current of the AC source",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1567: {
        "Level": "Expert",
        "Nr": 1567,
        "parameter description": "Second maximum current of the AC source (Input limit)",
        "Unit": "Aac",
        "Default": 16,
        "Min": 2,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1527: {
        "Level": "Expert",
        "Nr": 1527,
        "parameter description": "Decrease max input limit current with AC-In voltage",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1554: {
        "Level": "Expert",
        "Nr": 1554,
        "parameter description": "Decrease of the max. current of the source with input voltage activated by "
                                 "remote entry",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1309: {
        "Level": "Expert",
        "Nr": 1309,
        "parameter description": "AC input low limit voltage to allow charger function",
        "Unit": "Vac",
        "Default": 180,
        "Min": 100,
        "Max": 230,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1433: {
        "Level": "Expert",
        "Nr": 1433,
        "parameter description": "Adaptation range of the input current according to the input voltage",
        "Unit": "Vac",
        "Default": 10,
        "Min": 4,
        "Max": 30,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1553: {
        "Level": "Expert",
        "Nr": 1553,
        "parameter description": "Speed of input limit increase",
        "Unit": "",
        "Default": 50,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "2"
    },
    1295: {
        "Level": "Expert",
        "Nr": 1295,
        "parameter description": "Charge current decrease coef. at voltage limit to turn back in inverter mode",
        "Unit": "%",
        "Default": 100,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1436: {
        "Level": "Expert",
        "Nr": 1436,
        "parameter description": "Overrun AC source current limit without opening the transfer relay "
                                 "(Input limit)",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1510: {
        "Level": "Expert",
        "Nr": 1510,
        "parameter description": "Tolerance on detection of AC-input loss (tolerant UPS mode)",
        "Unit": "",
        "Default": 100,
        "Min": 2,
        "Max": 120,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "2"
    },
    1199: {
        "Level": "Expert",
        "Nr": 1199,
        "parameter description": "Input voltage giving an opening of the transfer relay with delay",
        "Unit": "Vac",
        "Default": 200,
        "Min": 80,
        "Max": 230,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1198: {
        "Level": "Expert",
        "Nr": 1198,
        "parameter description": "Time delay before opening of transfer relay",
        "Unit": "sec",
        "Default": 8,
        "Min": 0,
        "Max": 30,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1200: {
        "Level": "Expert",
        "Nr": 1200,
        "parameter description": "Input voltage giving an immediate opening of the transfer relay (UPS)",
        "Unit": "Vac",
        "Default": 180,
        "Min": 80,
        "Max": 230,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1432: {
        "Level": "Inst.",
        "Nr": 1432,
        "parameter description": "Absolute max limit for input voltage",
        "Unit": "Vac",
        "Default": 270,
        "Min": 235,
        "Max": 290,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1500: {
        "Level": "QSP",
        "Nr": 1500,
        "parameter description": "Standby of the charger allowed",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1505: {
        "Level": "Expert",
        "Nr": 1505,
        "parameter description": "Delta frequency allowed above the standard input frequency",
        "Unit": "Hz",
        "Default": 5,
        "Min": 0,
        "Max": 35,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1506: {
        "Level": "Expert",
        "Nr": 1506,
        "parameter description": "Delta frequency allowed under the standard input frequency",
        "Unit": "Hz",
        "Default": 5,
        "Min": 0,
        "Max": 15,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1507: {
        "Level": "Expert",
        "Nr": 1507,
        "parameter description": "Duration with frequency error before opening the transfer",
        "Unit": "sec",
        "Default": 2,
        "Min": 0,
        "Max": 5,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1575: {
        "Level": "Expert",
        "Nr": 1575,
        "parameter description": "AC-IN current active filtering (Not in parallel)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1557: {
        "Level": "Inst.",
        "Nr": 1557,
        "parameter description": "Use an energy quota on AC-input",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1559: {
        "Level": "Inst.",
        "Nr": 1559,
        "parameter description": "AC-In energy quota",
        "Unit": "kWh",
        "Default": 1,
        "Min": 0.5,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.5"
    },
    1201: {
        "Level": "Expert",
        "Nr": 1201,
        "parameter description": "AUXILIARY CONTACT 1",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1202: {
        "Level": "Expert",
        "Nr": 1202,
        "parameter description": "Operating mode (AUX 1)",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Automatic 2:Reversed automatic 4:Manual ON 8:Manual OFF"
    },
    1497: {
        "Level": "Expert",
        "Nr": 1497,
        "parameter description": "Combination of the events for the auxiliary contact (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 0:Any (Function OR) 1:All (Function AND)"
    },
    1203: {
        "Level": "Expert",
        "Nr": 1203,
        "parameter description": "Temporal restrictions (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1204: {
        "Level": "Expert",
        "Nr": 1204,
        "parameter description": "Program 1 (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1205: {
        "Level": "Expert",
        "Nr": 1205,
        "parameter description": "Day of the week (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1206: {
        "Level": "Expert",
        "Nr": 1206,
        "parameter description": "Start hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1207: {
        "Level": "Expert",
        "Nr": 1207,
        "parameter description": "End hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1208: {
        "Level": "Expert",
        "Nr": 1208,
        "parameter description": "Program 2 (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1209: {
        "Level": "Expert",
        "Nr": 1209,
        "parameter description": "Day of the week (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1210: {
        "Level": "Expert",
        "Nr": 1210,
        "parameter description": "Start hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1211: {
        "Level": "Expert",
        "Nr": 1211,
        "parameter description": "End hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1212: {
        "Level": "Expert",
        "Nr": 1212,
        "parameter description": "Program 3 (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1213: {
        "Level": "Expert",
        "Nr": 1213,
        "parameter description": "Day of the week (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1214: {
        "Level": "Expert",
        "Nr": 1214,
        "parameter description": "Start hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1215: {
        "Level": "Expert",
        "Nr": 1215,
        "parameter description": "End hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1216: {
        "Level": "Inst.",
        "Nr": 1216,
        "parameter description": "Program 4 (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1217: {
        "Level": "Inst.",
        "Nr": 1217,
        "parameter description": "Day of the week (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1218: {
        "Level": "Inst.",
        "Nr": 1218,
        "parameter description": "Start hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1219: {
        "Level": "Inst.",
        "Nr": 1219,
        "parameter description": "End hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1220: {
        "Level": "Inst.",
        "Nr": 1220,
        "parameter description": "Program 5 (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1221: {
        "Level": "Inst.",
        "Nr": 1221,
        "parameter description": "Day of the week (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1222: {
        "Level": "Inst.",
        "Nr": 1222,
        "parameter description": "Start hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1223: {
        "Level": "Inst.",
        "Nr": 1223,
        "parameter description": "End hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1269: {
        "Level": "Expert",
        "Nr": 1269,
        "parameter description": "Contact active with a fixed time schedule (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1270: {
        "Level": "Expert",
        "Nr": 1270,
        "parameter description": "Program 1 (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1271: {
        "Level": "Expert",
        "Nr": 1271,
        "parameter description": "Day of the week (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1272: {
        "Level": "Expert",
        "Nr": 1272,
        "parameter description": "Start hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1273: {
        "Level": "Expert",
        "Nr": 1273,
        "parameter description": "End hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1274: {
        "Level": "Expert",
        "Nr": 1274,
        "parameter description": "Program 2 (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1275: {
        "Level": "Expert",
        "Nr": 1275,
        "parameter description": "Day of the week (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1276: {
        "Level": "Expert",
        "Nr": 1276,
        "parameter description": "Start hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1277: {
        "Level": "Expert",
        "Nr": 1277,
        "parameter description": "End hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1278: {
        "Level": "Expert",
        "Nr": 1278,
        "parameter description": "Program 3 (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1279: {
        "Level": "Expert",
        "Nr": 1279,
        "parameter description": "Day of the week (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1280: {
        "Level": "Expert",
        "Nr": 1280,
        "parameter description": "Start hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1281: {
        "Level": "Expert",
        "Nr": 1281,
        "parameter description": "End hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1455: {
        "Level": "Expert",
        "Nr": 1455,
        "parameter description": "Contact active on event (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1225: {
        "Level": "Expert",
        "Nr": 1225,
        "parameter description": "Xtender is OFF (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1518: {
        "Level": "Expert",
        "Nr": 1518,
        "parameter description": "Xtender ON (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1543: {
        "Level": "Expert",
        "Nr": 1543,
        "parameter description": "Remote entry (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1226: {
        "Level": "Expert",
        "Nr": 1226,
        "parameter description": "Battery undervoltage alarm (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1227: {
        "Level": "Expert",
        "Nr": 1227,
        "parameter description": "Battery overvoltage (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1228: {
        "Level": "Expert",
        "Nr": 1228,
        "parameter description": "Inverter overload (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1229: {
        "Level": "Expert",
        "Nr": 1229,
        "parameter description": "Overtemperature (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1520: {
        "Level": "Expert",
        "Nr": 1520,
        "parameter description": "No overtemperature (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1231: {
        "Level": "Expert",
        "Nr": 1231,
        "parameter description": "Active charger (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1232: {
        "Level": "Expert",
        "Nr": 1232,
        "parameter description": "Active inverter (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1233: {
        "Level": "Expert",
        "Nr": 1233,
        "parameter description": "Active Smart-Boost (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1234: {
        "Level": "Expert",
        "Nr": 1234,
        "parameter description": "AC input presence but with fault (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1235: {
        "Level": "Expert",
        "Nr": 1235,
        "parameter description": "AC input presence (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1236: {
        "Level": "Expert",
        "Nr": 1236,
        "parameter description": "Transfer relay ON (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1237: {
        "Level": "Expert",
        "Nr": 1237,
        "parameter description": "AC out presence (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1238: {
        "Level": "Expert",
        "Nr": 1238,
        "parameter description": "Bulk charge phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1239: {
        "Level": "Expert",
        "Nr": 1239,
        "parameter description": "Absorption phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1240: {
        "Level": "Expert",
        "Nr": 1240,
        "parameter description": "Equalization phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1242: {
        "Level": "Expert",
        "Nr": 1242,
        "parameter description": "Floating (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1243: {
        "Level": "Expert",
        "Nr": 1243,
        "parameter description": "Reduced floating (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1244: {
        "Level": "Expert",
        "Nr": 1244,
        "parameter description": "Periodic absorption (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1601: {
        "Level": "Inst.",
        "Nr": 1601,
        "parameter description": "AC-In energy quota (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1245: {
        "Level": "Expert",
        "Nr": 1245,
        "parameter description": "Contact active according to battery voltage (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1288: {
        "Level": "Expert",
        "Nr": 1288,
        "parameter description": "Use dynamic compensation of battery level (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1246: {
        "Level": "Expert",
        "Nr": 1246,
        "parameter description": "Battery voltage 1 activate (AUX 1)",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1247: {
        "Level": "Expert",
        "Nr": 1247,
        "parameter description": "Battery voltage 1 (AUX 1)",
        "Unit": "Vdc",
        "Default": 46.8,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1248: {
        "Level": "Expert",
        "Nr": 1248,
        "parameter description": "Delay 1 (AUX 1)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1249: {
        "Level": "Expert",
        "Nr": 1249,
        "parameter description": "Battery voltage 2 activate (AUX 1)",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1250: {
        "Level": "Expert",
        "Nr": 1250,
        "parameter description": "Battery voltage 2 (AUX 1)",
        "Unit": "Vdc",
        "Default": 47.8,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1251: {
        "Level": "Expert",
        "Nr": 1251,
        "parameter description": "Delay 2 (AUX 1)",
        "Unit": "min",
        "Default": 10,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1252: {
        "Level": "Expert",
        "Nr": 1252,
        "parameter description": "Battery voltage 3 activate (AUX 1)",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1253: {
        "Level": "Expert",
        "Nr": 1253,
        "parameter description": "Battery voltage 3 (AUX 1)",
        "Unit": "Vdc",
        "Default": 48.5,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1254: {
        "Level": "Expert",
        "Nr": 1254,
        "parameter description": "Delay 3 (AUX 1)",
        "Unit": "min",
        "Default": 60,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1255: {
        "Level": "Expert",
        "Nr": 1255,
        "parameter description": "Battery voltage to deactivate (AUX 1)",
        "Unit": "Vdc",
        "Default": 54,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1256: {
        "Level": "Expert",
        "Nr": 1256,
        "parameter description": "Delay to deactivate (AUX 1)",
        "Unit": "min",
        "Default": 60,
        "Min": 0,
        "Max": 480,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1516: {
        "Level": "Expert",
        "Nr": 1516,
        "parameter description": "Deactivate if battery in floating phase (AUX 1)",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1257: {
        "Level": "Expert",
        "Nr": 1257,
        "parameter description": "Contact active with inverter power or Smart-Boost (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1258: {
        "Level": "Expert",
        "Nr": 1258,
        "parameter description": "Inverter power level 1 activate (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1259: {
        "Level": "Expert",
        "Nr": 1259,
        "parameter description": "Power level 1 (AUX 1)",
        "Unit": "% Pnom",
        "Default": 120,
        "Min": 20,
        "Max": 120,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    1260: {
        "Level": "Expert",
        "Nr": 1260,
        "parameter description": "Time delay 1 (AUX 1)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1644: {
        "Level": "QSP",
        "Nr": 1644,
        "parameter description": "Activated by AUX2 event partial overload",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1261: {
        "Level": "Expert",
        "Nr": 1261,
        "parameter description": "Inverter power level 2 activate (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1262: {
        "Level": "Expert",
        "Nr": 1262,
        "parameter description": "Power level 2 (AUX 1)",
        "Unit": "% Pnom",
        "Default": 80,
        "Min": 20,
        "Max": 120,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    1263: {
        "Level": "Expert",
        "Nr": 1263,
        "parameter description": "Time delay 2 (AUX 1)",
        "Unit": "min",
        "Default": 5,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1264: {
        "Level": "Expert",
        "Nr": 1264,
        "parameter description": "Inverter power level 3 activate (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1265: {
        "Level": "Expert",
        "Nr": 1265,
        "parameter description": "Power level 3 (AUX 1)",
        "Unit": "% Pnom",
        "Default": 50,
        "Min": 20,
        "Max": 120,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    1266: {
        "Level": "Expert",
        "Nr": 1266,
        "parameter description": "Time delay 3 (AUX 1)",
        "Unit": "min",
        "Default": 30,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1267: {
        "Level": "Expert",
        "Nr": 1267,
        "parameter description": "Inverter power level to deactivate (AUX 1)",
        "Unit": "% Pnom",
        "Default": 40,
        "Min": 20,
        "Max": 120,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    1268: {
        "Level": "Expert",
        "Nr": 1268,
        "parameter description": "Time delay to deactivate (AUX 1)",
        "Unit": "min",
        "Default": 5,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1503: {
        "Level": "Expert",
        "Nr": 1503,
        "parameter description": "Contact active according to battery temperature (AUX 1) With BSP or BTS",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1446: {
        "Level": "Expert",
        "Nr": 1446,
        "parameter description": "Contact activated with the temperature of battery (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1447: {
        "Level": "Expert",
        "Nr": 1447,
        "parameter description": "Contact activated over (AUX 1)",
        "Unit": "°C",
        "Default": 3,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1448: {
        "Level": "Expert",
        "Nr": 1448,
        "parameter description": "Contact deactivated below (AUX 1)",
        "Unit": "°C",
        "Default": 5,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1501: {
        "Level": "Expert",
        "Nr": 1501,
        "parameter description": "Contact active according to SOC (AUX 1) Only with BSP",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1439: {
        "Level": "Expert",
        "Nr": 1439,
        "parameter description": "Contact activated with the SOC 1 of battery (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1440: {
        "Level": "Expert",
        "Nr": 1440,
        "parameter description": "Contact activated below SOC 1 (AUX 1)",
        "Unit": "% SOC",
        "Default": 50,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1581: {
        "Level": "Expert",
        "Nr": 1581,
        "parameter description": "Delay 1 (AUX 1)",
        "Unit": "hours",
        "Default": 12,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    1582: {
        "Level": "Expert",
        "Nr": 1582,
        "parameter description": "Contact activated with the SOC 2 of battery (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1583: {
        "Level": "Expert",
        "Nr": 1583,
        "parameter description": "Contact activated below SOC 2 (AUX 1)",
        "Unit": "% SOC",
        "Default": 30,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1584: {
        "Level": "Expert",
        "Nr": 1584,
        "parameter description": "Delay 2 (AUX 1)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    1585: {
        "Level": "Expert",
        "Nr": 1585,
        "parameter description": "Contact activated with the SOC 3 of battery (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1586: {
        "Level": "Expert",
        "Nr": 1586,
        "parameter description": "Contact activated below SOC 3 (AUX 1)",
        "Unit": "% SOC",
        "Default": 20,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1587: {
        "Level": "Expert",
        "Nr": 1587,
        "parameter description": "Delay 3 (AUX 1)",
        "Unit": "hours",
        "Default": 0,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    1441: {
        "Level": "Expert",
        "Nr": 1441,
        "parameter description": "Contact deactivated over SOC (AUX 1)",
        "Unit": "% SOC",
        "Default": 90,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1588: {
        "Level": "Expert",
        "Nr": 1588,
        "parameter description": "Delay to deactivate (AUX 1)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 10,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    1589: {
        "Level": "Expert",
        "Nr": 1589,
        "parameter description": "Deactivate if battery in floating phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1512: {
        "Level": "Expert",
        "Nr": 1512,
        "parameter description": "Security, maximum time of contact (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1514: {
        "Level": "Expert",
        "Nr": 1514,
        "parameter description": "Maximum time of operation of contact (AUX 1)",
        "Unit": "min",
        "Default": 600,
        "Min": 10,
        "Max": 1200,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    1569: {
        "Level": "Expert",
        "Nr": 1569,
        "parameter description": "Reset all settings (AUX 1)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    1310: {
        "Level": "Expert",
        "Nr": 1310,
        "parameter description": "AUXILIARY CONTACT 2",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1311: {
        "Level": "Expert",
        "Nr": 1311,
        "parameter description": "Operating mode (AUX 2)",
        "Unit": "",
        "Default": 2,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Automatic 2:Reversed automatic 4:Manual ON 8:Manual OFF"
    },
    1498: {
        "Level": "Expert",
        "Nr": 1498,
        "parameter description": "Combination of the events for the auxiliary contact (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 0:Any (Function OR) 1:All (Function AND)"
    },
    1312: {
        "Level": "Expert",
        "Nr": 1312,
        "parameter description": "Temporal restrictions (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1313: {
        "Level": "Expert",
        "Nr": 1313,
        "parameter description": "Program 1 (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1314: {
        "Level": "Expert",
        "Nr": 1314,
        "parameter description": "Day of the week (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1315: {
        "Level": "Expert",
        "Nr": 1315,
        "parameter description": "Start hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1316: {
        "Level": "Expert",
        "Nr": 1316,
        "parameter description": "End hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1317: {
        "Level": "Expert",
        "Nr": 1317,
        "parameter description": "Program 2 (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1318: {
        "Level": "Expert",
        "Nr": 1318,
        "parameter description": "Day of the week (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1319: {
        "Level": "Expert",
        "Nr": 1319,
        "parameter description": "Start hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1320: {
        "Level": "Expert",
        "Nr": 1320,
        "parameter description": "End hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1321: {
        "Level": "Expert",
        "Nr": 1321,
        "parameter description": "Program 3 (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1322: {
        "Level": "Expert",
        "Nr": 1322,
        "parameter description": "Day of the week (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1323: {
        "Level": "Expert",
        "Nr": 1323,
        "parameter description": "Start hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1324: {
        "Level": "Expert",
        "Nr": 1324,
        "parameter description": "End hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1325: {
        "Level": "Inst.",
        "Nr": 1325,
        "parameter description": "Program 4 (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1326: {
        "Level": "Inst.",
        "Nr": 1326,
        "parameter description": "Day of the week (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1327: {
        "Level": "Inst.",
        "Nr": 1327,
        "parameter description": "Start hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1328: {
        "Level": "Inst.",
        "Nr": 1328,
        "parameter description": "End hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1329: {
        "Level": "Inst.",
        "Nr": 1329,
        "parameter description": "Program 5 (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1330: {
        "Level": "Inst.",
        "Nr": 1330,
        "parameter description": "Day of the week (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1331: {
        "Level": "Inst.",
        "Nr": 1331,
        "parameter description": "Start hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1332: {
        "Level": "Inst.",
        "Nr": 1332,
        "parameter description": "End hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1378: {
        "Level": "Expert",
        "Nr": 1378,
        "parameter description": "Contact active with a fixed time schedule (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1379: {
        "Level": "Expert",
        "Nr": 1379,
        "parameter description": "Program 1 (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1380: {
        "Level": "Expert",
        "Nr": 1380,
        "parameter description": "Day of the week (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1381: {
        "Level": "Expert",
        "Nr": 1381,
        "parameter description": "Start hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1382: {
        "Level": "Expert",
        "Nr": 1382,
        "parameter description": "End hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1383: {
        "Level": "Expert",
        "Nr": 1383,
        "parameter description": "Program 2 (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1384: {
        "Level": "Expert",
        "Nr": 1384,
        "parameter description": "Day of the week (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1385: {
        "Level": "Expert",
        "Nr": 1385,
        "parameter description": "Start hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1386: {
        "Level": "Expert",
        "Nr": 1386,
        "parameter description": "End hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1387: {
        "Level": "Expert",
        "Nr": 1387,
        "parameter description": "Program 3 (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1388: {
        "Level": "Expert",
        "Nr": 1388,
        "parameter description": "Day of the week (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 127,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Bit field"
    },
    1389: {
        "Level": "Expert",
        "Nr": 1389,
        "parameter description": "Start hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1390: {
        "Level": "Expert",
        "Nr": 1390,
        "parameter description": "End hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1456: {
        "Level": "Expert",
        "Nr": 1456,
        "parameter description": "Contact active on event (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1333: {
        "Level": "Expert",
        "Nr": 1333,
        "parameter description": "Xtender is OFF (AUX 2)",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1519: {
        "Level": "Expert",
        "Nr": 1519,
        "parameter description": "Xtender ON (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1544: {
        "Level": "Expert",
        "Nr": 1544,
        "parameter description": "Remote entry (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1334: {
        "Level": "Expert",
        "Nr": 1334,
        "parameter description": "Battery undervoltage alarm (AUX 2)",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1335: {
        "Level": "Expert",
        "Nr": 1335,
        "parameter description": "Battery overvoltage (AUX 2)",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1336: {
        "Level": "Expert",
        "Nr": 1336,
        "parameter description": "Inverter overload (AUX 2)",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1337: {
        "Level": "Expert",
        "Nr": 1337,
        "parameter description": "Overtemperature (AUX 2)",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1521: {
        "Level": "Expert",
        "Nr": 1521,
        "parameter description": "No overtemperature (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1339: {
        "Level": "Expert",
        "Nr": 1339,
        "parameter description": "Active charger (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1340: {
        "Level": "Expert",
        "Nr": 1340,
        "parameter description": "Active inverter (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1341: {
        "Level": "Expert",
        "Nr": 1341,
        "parameter description": "Active Smart-Boost (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1342: {
        "Level": "Expert",
        "Nr": 1342,
        "parameter description": "AC input presence but with fault (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1343: {
        "Level": "Expert",
        "Nr": 1343,
        "parameter description": "AC input presence (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1344: {
        "Level": "Expert",
        "Nr": 1344,
        "parameter description": "Transfer contact ON (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1345: {
        "Level": "Expert",
        "Nr": 1345,
        "parameter description": "AC out presence (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1346: {
        "Level": "Expert",
        "Nr": 1346,
        "parameter description": "Bulk charge phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1347: {
        "Level": "Expert",
        "Nr": 1347,
        "parameter description": "Absorption phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1348: {
        "Level": "Expert",
        "Nr": 1348,
        "parameter description": "Equalization phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1350: {
        "Level": "Expert",
        "Nr": 1350,
        "parameter description": "Floating (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1351: {
        "Level": "Expert",
        "Nr": 1351,
        "parameter description": "Reduced floating (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1352: {
        "Level": "Expert",
        "Nr": 1352,
        "parameter description": "Periodic absorption (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1602: {
        "Level": "Inst.",
        "Nr": 1602,
        "parameter description": "AC-In energy quota (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1643: {
        "Level": "QSP",
        "Nr": 1643,
        "parameter description": "Partial overload",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1353: {
        "Level": "Expert",
        "Nr": 1353,
        "parameter description": "Contact active according to battery voltage (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1354: {
        "Level": "Expert",
        "Nr": 1354,
        "parameter description": "Use dynamic compensation of battery level (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1355: {
        "Level": "Expert",
        "Nr": 1355,
        "parameter description": "Battery voltage 1 activate (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1356: {
        "Level": "Expert",
        "Nr": 1356,
        "parameter description": "Battery voltage 1 (AUX 2)",
        "Unit": "Vdc",
        "Default": 48,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1357: {
        "Level": "Expert",
        "Nr": 1357,
        "parameter description": "Delay 1 (AUX 2)",
        "Unit": "min",
        "Default": 5,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1358: {
        "Level": "Expert",
        "Nr": 1358,
        "parameter description": "Battery voltage 2 activate (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1359: {
        "Level": "Expert",
        "Nr": 1359,
        "parameter description": "Battery voltage 2 (AUX 2)",
        "Unit": "Vdc",
        "Default": 46.1,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1360: {
        "Level": "Expert",
        "Nr": 1360,
        "parameter description": "Delay 2 (AUX 2)",
        "Unit": "min",
        "Default": 5,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1361: {
        "Level": "Expert",
        "Nr": 1361,
        "parameter description": "Battery voltage 3 activate (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1362: {
        "Level": "Expert",
        "Nr": 1362,
        "parameter description": "Battery voltage 3 (AUX 2)",
        "Unit": "Vdc",
        "Default": 44.2,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1363: {
        "Level": "Expert",
        "Nr": 1363,
        "parameter description": "Delay 3 (AUX 2)",
        "Unit": "min",
        "Default": 5,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1364: {
        "Level": "Expert",
        "Nr": 1364,
        "parameter description": "Battery voltage to deactivate (AUX 2)",
        "Unit": "Vdc",
        "Default": 50.4,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1365: {
        "Level": "Expert",
        "Nr": 1365,
        "parameter description": "Delay to deactivate (AUX 2)",
        "Unit": "min",
        "Default": 5,
        "Min": 0,
        "Max": 480,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1517: {
        "Level": "Expert",
        "Nr": 1517,
        "parameter description": "Deactivate if battery in floating phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1366: {
        "Level": "Expert",
        "Nr": 1366,
        "parameter description": "Contact active with inverter power or Smart-Boost (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1367: {
        "Level": "Expert",
        "Nr": 1367,
        "parameter description": "Inverter power level 1 activate (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1368: {
        "Level": "Expert",
        "Nr": 1368,
        "parameter description": "Power level 1 (AUX 2)",
        "Unit": "% Pnom",
        "Default": 120,
        "Min": 20,
        "Max": 120,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    1369: {
        "Level": "Expert",
        "Nr": 1369,
        "parameter description": "Time delay 1 (AUX 2)",
        "Unit": "min",
        "Default": 0,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1370: {
        "Level": "Expert",
        "Nr": 1370,
        "parameter description": "Inverter power level 2 activate (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1371: {
        "Level": "Expert",
        "Nr": 1371,
        "parameter description": "Power level 2 (AUX 2)",
        "Unit": "% Pnom",
        "Default": 80,
        "Min": 20,
        "Max": 120,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    1372: {
        "Level": "Expert",
        "Nr": 1372,
        "parameter description": "Time delay 2 (AUX 2)",
        "Unit": "min",
        "Default": 5,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1373: {
        "Level": "Expert",
        "Nr": 1373,
        "parameter description": "Inverter power level 3 activate (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1374: {
        "Level": "Expert",
        "Nr": 1374,
        "parameter description": "Power level 3 (AUX 2)",
        "Unit": "% Pnom",
        "Default": 50,
        "Min": 20,
        "Max": 120,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    1375: {
        "Level": "Expert",
        "Nr": 1375,
        "parameter description": "Time delay 3 (AUX 2)",
        "Unit": "min",
        "Default": 30,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1376: {
        "Level": "Expert",
        "Nr": 1376,
        "parameter description": "Inverter power level to deactivate (AUX 2)",
        "Unit": "% Pnom",
        "Default": 40,
        "Min": 20,
        "Max": 120,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    1377: {
        "Level": "Expert",
        "Nr": 1377,
        "parameter description": "Time delay to deactivate (AUX 2)",
        "Unit": "min",
        "Default": 5,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1504: {
        "Level": "Expert",
        "Nr": 1504,
        "parameter description": "Contact active according to battery temperature (AUX 2) With BSP or BTS",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1457: {
        "Level": "Expert",
        "Nr": 1457,
        "parameter description": "Contact activated with the temperature of battery (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1458: {
        "Level": "Expert",
        "Nr": 1458,
        "parameter description": "Contact activated over (AUX 2)",
        "Unit": "°C",
        "Default": 3,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1459: {
        "Level": "Expert",
        "Nr": 1459,
        "parameter description": "Contact deactivated below (AUX 2)",
        "Unit": "°C",
        "Default": 5,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1502: {
        "Level": "Expert",
        "Nr": 1502,
        "parameter description": "Contact active according to SOC (AUX 2) Only with BSP",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1442: {
        "Level": "Expert",
        "Nr": 1442,
        "parameter description": "Contact activated with the SOC 1 of battery (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1443: {
        "Level": "Expert",
        "Nr": 1443,
        "parameter description": "Contact activated below SOC 1 (AUX 2)",
        "Unit": "% SOC",
        "Default": 50,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1590: {
        "Level": "Expert",
        "Nr": 1590,
        "parameter description": "Delay 1 (AUX 2)",
        "Unit": "hours",
        "Default": 12,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    1591: {
        "Level": "Expert",
        "Nr": 1591,
        "parameter description": "Contact activated with the SOC 2 of battery (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1592: {
        "Level": "Expert",
        "Nr": 1592,
        "parameter description": "Contact activated below SOC 2 (AUX 2)",
        "Unit": "% SOC",
        "Default": 30,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1593: {
        "Level": "Expert",
        "Nr": 1593,
        "parameter description": "Delay 2 (AUX 2)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    1594: {
        "Level": "Expert",
        "Nr": 1594,
        "parameter description": "Contact activated with the SOC 3 of battery (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1595: {
        "Level": "Expert",
        "Nr": 1595,
        "parameter description": "Contact activated below SOC 3 (AUX 2)",
        "Unit": "% SOC",
        "Default": 20,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1596: {
        "Level": "Expert",
        "Nr": 1596,
        "parameter description": "Delay 3 (AUX 2)",
        "Unit": "hours",
        "Default": 0,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    1444: {
        "Level": "Expert",
        "Nr": 1444,
        "parameter description": "Contact deactivated over SOC (AUX 2)",
        "Unit": "% SOC",
        "Default": 90,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1597: {
        "Level": "Expert",
        "Nr": 1597,
        "parameter description": "Delay to deactivate (AUX 2)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 10,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    1598: {
        "Level": "Expert",
        "Nr": 1598,
        "parameter description": "Deactivate if battery in floating phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1513: {
        "Level": "Expert",
        "Nr": 1513,
        "parameter description": "Security, maximum time of contact (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1515: {
        "Level": "Expert",
        "Nr": 1515,
        "parameter description": "Maximum time of operation of contact (AUX 2)",
        "Unit": "min",
        "Default": 600,
        "Min": 10,
        "Max": 1200,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    1570: {
        "Level": "Expert",
        "Nr": 1570,
        "parameter description": "Reset all settings (AUX 2)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    1489: {
        "Level": "Expert",
        "Nr": 1489,
        "parameter description": "AUXILIARY CONTACTS 1 AND 2 EXTENDED FUNCTIONS",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1491: {
        "Level": "Expert",
        "Nr": 1491,
        "parameter description": "Generator control active",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1493: {
        "Level": "Expert",
        "Nr": 1493,
        "parameter description": "Number of starting attempts",
        "Unit": "",
        "Default": 5,
        "Min": 0,
        "Max": 20,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1492: {
        "Level": "Expert",
        "Nr": 1492,
        "parameter description": "Starter pulse duration (with AUX2)",
        "Unit": "sec",
        "Default": 3,
        "Min": 1,
        "Max": 20,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1494: {
        "Level": "Expert",
        "Nr": 1494,
        "parameter description": "Time before a starter pulse",
        "Unit": "sec",
        "Default": 3,
        "Min": 1,
        "Max": 20,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1574: {
        "Level": "Expert",
        "Nr": 1574,
        "parameter description": "Main contact hold/interrupt time",
        "Unit": "sec",
        "Default": 0,
        "Min": 0,
        "Max": 30,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1101: {
        "Level": "Expert",
        "Nr": 1101,
        "parameter description": "SYSTEM",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1537: {
        "Level": "Expert",
        "Nr": 1537,
        "parameter description": "Remote entry (Remote ON/OFF)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1545: {
        "Level": "Expert",
        "Nr": 1545,
        "parameter description": "Remote entry active",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 0:Closed 1:Open"
    },
    1538: {
        "Level": "Expert",
        "Nr": 1538,
        "parameter description": "Prohibits transfert relay",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1539: {
        "Level": "Expert",
        "Nr": 1539,
        "parameter description": "Prohibits inverter",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1540: {
        "Level": "Expert",
        "Nr": 1540,
        "parameter description": "Prohibits charger",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1541: {
        "Level": "Expert",
        "Nr": 1541,
        "parameter description": "Prohibits Smart-Boost",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1542: {
        "Level": "Expert",
        "Nr": 1542,
        "parameter description": "Prohibits grid feeding",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1576: {
        "Level": "Expert",
        "Nr": 1576,
        "parameter description": "ON/OFF command",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1578: {
        "Level": "Expert",
        "Nr": 1578,
        "parameter description": "Activated by AUX 1 state",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1579: {
        "Level": "Expert",
        "Nr": 1579,
        "parameter description": "Prohibits battery priority",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1600: {
        "Level": "Inst.",
        "Nr": 1600,
        "parameter description": "Disable minigrid mode",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1640: {
        "Level": "QSP",
        "Nr": 1640,
        "parameter description": "Clear AUX2 event partial overload",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1647: {
        "Level": "Inst.",
        "Nr": 1647,
        "parameter description": "Prohibits charger using only power from AC-Out",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1296: {
        "Level": "Expert",
        "Nr": 1296,
        "parameter description": "Batteries priority as energy source (Not recommended in parallel)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1297: {
        "Level": "Expert",
        "Nr": 1297,
        "parameter description": "Battery priority voltage",
        "Unit": "Vdc",
        "Default": 51.6,
        "Min": 37.9,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1565: {
        "Level": "Expert",
        "Nr": 1565,
        "parameter description": "Buzzer alarm duration",
        "Unit": "min",
        "Default": 0,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1129: {
        "Level": "Expert",
        "Nr": 1129,
        "parameter description": "Auto restarts",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1130: {
        "Level": "Expert",
        "Nr": 1130,
        "parameter description": "After battery undervoltage",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1304: {
        "Level": "Expert",
        "Nr": 1304,
        "parameter description": "Number of batteries undervoltage allowed before definitive stop",
        "Unit": "",
        "Default": 3,
        "Min": 1,
        "Max": 20,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1404: {
        "Level": "Expert",
        "Nr": 1404,
        "parameter description": "Time period for batteries undervoltages counting",
        "Unit": "sec",
        "Default": 0,
        "Min": 0,
        "Max": 3000,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "60"
    },
    1305: {
        "Level": "Expert",
        "Nr": 1305,
        "parameter description": "Number of batteries critical undervoltage allowed before definitive stop",
        "Unit": "",
        "Default": 10,
        "Min": 1,
        "Max": 20,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1405: {
        "Level": "Expert",
        "Nr": 1405,
        "parameter description": "Time period for critical batteries undervoltages counting",
        "Unit": "sec",
        "Default": 10,
        "Min": 0,
        "Max": 3000,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1131: {
        "Level": "Expert",
        "Nr": 1131,
        "parameter description": "After battery overvoltage",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1132: {
        "Level": "Expert",
        "Nr": 1132,
        "parameter description": "After inverter or Smart-Boost overload",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1533: {
        "Level": "Expert",
        "Nr": 1533,
        "parameter description": "Delay to restart after an overload",
        "Unit": "sec",
        "Default": 5,
        "Min": 2,
        "Max": 120,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1134: {
        "Level": "Expert",
        "Nr": 1134,
        "parameter description": "After overtemperature",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1111: {
        "Level": "Expert",
        "Nr": 1111,
        "parameter description": "Autostart to the battery connection",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1484: {
        "Level": "Expert",
        "Nr": 1484,
        "parameter description": "System earthing (Earth - Neutral)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1485: {
        "Level": "Expert",
        "Nr": 1485,
        "parameter description": "Prohibited ground relay",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1486: {
        "Level": "Expert",
        "Nr": 1486,
        "parameter description": "Continuous neutral",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1628: {
        "Level": "Inst.",
        "Nr": 1628,
        "parameter description": "Xtender watchdog enabled (SCOM)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1629: {
        "Level": "Inst.",
        "Nr": 1629,
        "parameter description": "Xtender watchdog delay (SCOM)",
        "Unit": "sec",
        "Default": 60,
        "Min": 10,
        "Max": 300,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    1616: {
        "Level": "QSP",
        "Nr": 1616,
        "parameter description": "Use of functions limited to a number of days",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1391: {
        "Level": "QSP",
        "Nr": 1391,
        "parameter description": "Number of days without functionalitie's restrictions",
        "Unit": "days",
        "Default": 0,
        "Min": 0,
        "Max": 1300,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1617: {
        "Level": "QSP",
        "Nr": 1617,
        "parameter description": "Transfer relay disabled after timeout",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1618: {
        "Level": "QSP",
        "Nr": 1618,
        "parameter description": "Inverter disabled after timeout",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1619: {
        "Level": "QSP",
        "Nr": 1619,
        "parameter description": "Charger disabled after timeout",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1620: {
        "Level": "QSP",
        "Nr": 1620,
        "parameter description": "Smart-Boost disabled after timeout",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1621: {
        "Level": "QSP",
        "Nr": 1621,
        "parameter description": "Grid feeding disabled after timeout",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1550: {
        "Level": "Inst.",
        "Nr": 1550,
        "parameter description": "Parameters saved in flash memory",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1415: {
        "Level": "Inst.",
        "Nr": 1415,
        "parameter description": "ON of the Xtenders",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    1399: {
        "Level": "Inst.",
        "Nr": 1399,
        "parameter description": "OFF of the Xtenders",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    1468: {
        "Level": "Expert",
        "Nr": 1468,
        "parameter description": "Reset of all the inverters",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    1282: {
        "Level": "Expert",
        "Nr": 1282,
        "parameter description": "MULTI XTENDER SYSTEM",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1283: {
        "Level": "Expert",
        "Nr": 1283,
        "parameter description": "Integral mode",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1461: {
        "Level": "Expert",
        "Nr": 1461,
        "parameter description": "Multi inverters allowed",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1462: {
        "Level": "Expert",
        "Nr": 1462,
        "parameter description": "Multi inverters independents. Need reset {1468}",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1555: {
        "Level": "Expert",
        "Nr": 1555,
        "parameter description": "Battery cycle synchronized by the master",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1547: {
        "Level": "Expert",
        "Nr": 1547,
        "parameter description": "Allow slaves standby in multi-Xtender system",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1571: {
        "Level": "Expert",
        "Nr": 1571,
        "parameter description": "Splitphase: L2 with 180 degrees phaseshift",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1558: {
        "Level": "QSP",
        "Nr": 1558,
        "parameter description": "Separated Batteries",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1437: {
        "Level": "Inst.",
        "Nr": 1437,
        "parameter description": "Minigrid compatible",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1577: {
        "Level": "Inst.",
        "Nr": 1577,
        "parameter description": "Minigrid with shared battery energy",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1556: {
        "Level": "Inst.",
        "Nr": 1556,
        "parameter description": "Is the central inverter in distributed minigrid",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1522: {
        "Level": "Expert",
        "Nr": 1522,
        "parameter description": "GRID-FEEDING",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    1127: {
        "Level": "Expert",
        "Nr": 1127,
        "parameter description": "Grid feeding allowed",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1523: {
        "Level": "Expert",
        "Nr": 1523,
        "parameter description": "Max grid feeding current",
        "Unit": "Aac",
        "Default": 10,
        "Min": 0,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.2"
    },
    1524: {
        "Level": "Expert",
        "Nr": 1524,
        "parameter description": "Battery voltage target for forced grid feeding",
        "Unit": "Vdc",
        "Default": 48,
        "Min": 37.9,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1525: {
        "Level": "Expert",
        "Nr": 1525,
        "parameter description": "Forced grid feeding start time",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1526: {
        "Level": "Expert",
        "Nr": 1526,
        "parameter description": "Forced grid feeding stop time",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    1610: {
        "Level": "Inst.",
        "Nr": 1610,
        "parameter description": "Use of the defined phase shift curve for injection",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1622: {
        "Level": "Inst.",
        "Nr": 1622,
        "parameter description": "Cos phi at P = 0%  {Default [0: Cos phi 1],  Min [-0.1 : Inductive 0.90] , "
                                 "Max [+0.1: Capacitive 0.90]}",
        "Unit": "",
        "Default": 0,
        "Min": -0.1,
        "Max": 0.1,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.01"
    },
    1623: {
        "Level": "Inst.",
        "Nr": 1623,
        "parameter description": "Cos phi at the power defined by param {1613}  {Default [0: Cos phi 1],  "
                                 "Min [-0.1 : Inductive 0.90] , Max [+0.1: Capacitive 0.90]}",
        "Unit": "",
        "Default": 0,
        "Min": -0.1,
        "Max": 0.1,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.01"
    },
    1613: {
        "Level": "Inst.",
        "Nr": 1613,
        "parameter description": "Power of the second cos phi point in % of Pnom",
        "Unit": "%",
        "Default": 50,
        "Min": 20,
        "Max": 85,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    1624: {
        "Level": "Inst.",
        "Nr": 1624,
        "parameter description": "Cos phi at P = 100%  {Default [+0.1: Capacitive 0.90],  "
                                 "Min [-0.1 : Inductive 0.90] , Max [+0.1: Capacitive 0.90]}",
        "Unit": "",
        "Default": 0.1,
        "Min": -0.1,
        "Max": 0.1,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.01"
    },
    1627: {
        "Level": "Inst.",
        "Nr": 1627,
        "parameter description": "ARN4105 frequency control enabled",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    1630: {
        "Level": "Inst.",
        "Nr": 1630,
        "parameter description": "Delta from user frequency to start derating",
        "Unit": "Hz",
        "Default": 1,
        "Min": 0,
        "Max": 3.9,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1631: {
        "Level": "Inst.",
        "Nr": 1631,
        "parameter description": "Delta from user frequency to reach 100% derating",
        "Unit": "Hz",
        "Default": 2,
        "Min": 0,
        "Max": 3.9,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    1561: {
        "Level": "QSP",
        "Nr": 1561,
        "parameter description": "Correction for XTS saturation Reg U",
        "Unit": "",
        "Default": 0,
        "Min": -300,
        "Max": 300,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1562: {
        "Level": "QSP",
        "Nr": 1562,
        "parameter description": "Correction for XTS saturation Reg I",
        "Unit": "",
        "Default": 0,
        "Min": -300,
        "Max": 300,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1648: {
        "Level": "QSP",
        "Nr": 1648,
        "parameter description": "Imagnet INT level adjustment for correction",
        "Unit": "",
        "Default": 0,
        "Min": -300,
        "Max": 300,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    1649: {
        "Level": "QSP",
        "Nr": 1649,
        "parameter description": "Imagnet ERROR level adjustment for correction",
        "Unit": "",
        "Default": 0,
        "Min": -300,
        "Max": 300,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
}
# Note: The cos phi parameter range goes from -0.1 (Inductive 0.9) to +0.1 (Capacitive 0.9) by 0.01 steps.

# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------- 1.3 Xtender infos ------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
# Contains 114 Infos
XTENDER_INFOS = {
    3000: {
        "Nr": 3000,
        "information description": "Battery voltage",
        "Short desc.": "Ubat",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3001: {
        "Nr": 3001,
        "information description": "Battery temperature",
        "Short desc.": "Tbat",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "Value given by the external battery temperature sensor BTS-01, "
                                            "no sensor : return ~32767 °C"
    },
    3002: {
        "Nr": 3002,
        "information description": "Temperature compensation of battery voltage",
        "Short desc.": "Comp°C",
        "Unit on the RCC": "Ctmp",
        "Unit": "Ctmp",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3003: {
        "Nr": 3003,
        "information description": "Dynamic compensation of battery voltage",
        "Short desc.": "Comp P",
        "Unit on the RCC": "Cdyn",
        "Unit": "Cdyn",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3004: {
        "Nr": 3004,
        "information description": "Wanted battery charge current",
        "Short desc.": "Ibat",
        "Unit on the RCC": "Ausr",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3005: {
        "Nr": 3005,
        "information description": "Battery charge current",
        "Short desc.": "Ibat (m)",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3006: {
        "Nr": 3006,
        "information description": "Battery voltage ripple",
        "Short desc.": "Ubat ond",
        "Unit on the RCC": "Vrip",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3007: {
        "Nr": 3007,
        "information description": "State of charge",
        "Short desc.": "SOC",
        "Unit on the RCC": "%",
        "Unit": "%",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3008: {
        "Nr": 3008,
        "information description": "Low Voltage Disconect",
        "Short desc.": "LVD",
        "Unit on the RCC": "LVD",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3010: {
        "Nr": 3010,
        "information description": "Battery cycle phase",
        "Short desc.": "Phase",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "See parameter {1137} 0:Invalid value 1:Bulk 2:Absorpt. 3:Equalise "
                                            "4:Floating 5:R.float. 6:Per.abs. 7:Mixing 8:Forming"
    },
    3011: {
        "Nr": 3011,
        "information description": "Input voltage",
        "Short desc.": "U in",
        "Unit on the RCC": "Vac",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See parameter {1197}"
    },
    3012: {
        "Nr": 3012,
        "information description": "Input current",
        "Short desc.": "I in",
        "Unit on the RCC": "Aac",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3013: {
        "Nr": 3013,
        "information description": "Input power",
        "Short desc.": "P in",
        "Unit on the RCC": "kVA",
        "Unit": "kVA",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "Less accurate than info 3138"
    },
    3017: {
        "Nr": 3017,
        "information description": "Input limit value",
        "Short desc.": "I Limit Val",
        "Unit on the RCC": "ILim",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3018: {
        "Nr": 3018,
        "information description": "Input limite reached",
        "Short desc.": "P sharing",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "L*, see parameter {1107} 0:Off 1:On"
    },
    3019: {
        "Nr": 3019,
        "information description": "Boost active",
        "Short desc.": "Boost",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "B*, see parameter {1126} 0:Off 1:On"
    },
    3020: {
        "Nr": 3020,
        "information description": "State of transfer relay",
        "Short desc.": "Transfert",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Opened 1:Closed"
    },
    3021: {
        "Nr": 3021,
        "information description": "Output voltage",
        "Short desc.": "U out",
        "Unit on the RCC": "Vac",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See parameter {1286}"
    },
    3022: {
        "Nr": 3022,
        "information description": "Output current",
        "Short desc.": "I out",
        "Unit on the RCC": "Aac",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3023: {
        "Nr": 3023,
        "information description": "Output power",
        "Short desc.": "P out",
        "Unit on the RCC": "kVA",
        "Unit": "kVA",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "Less accurate than info 3139"
    },
    3028: {
        "Nr": 3028,
        "information description": "Operating state",
        "Short desc.": "Mode",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "Give the current working mode of the inverter. See {1107} for Boost, "
                                            "{1522} for Injection (grid-feeding), charger and inverter mode are "
                                            "oblivious. Only in CSV file, the value 6 indicate that the xtender is off."
                                            " 0:Invalid value 1:Inverter 2:Charger 3:Boost 4:Injection"
    },
    3030: {
        "Nr": 3030,
        "information description": "State of output relay",
        "Short desc.": "Rel out",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Opened 1:Closed"
    },
    3031: {
        "Nr": 3031,
        "information description": "State of auxiliary relay 1",
        "Short desc.": "Aux 1",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "See parameter {1201} 0:Opened 1:Closed"
    },
    3032: {
        "Nr": 3032,
        "information description": "State of auxiliary relay 2",
        "Short desc.": "Aux 2",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "See parameter {1201} 0:Opened 1:Closed"
    },
    3045: {
        "Nr": 3045,
        "information description": "Nbr. of overloads",
        "Short desc.": "n ovld",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3046: {
        "Nr": 3046,
        "information description": "Nbr. overtemperature",
        "Short desc.": "n ovtmp",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3047: {
        "Nr": 3047,
        "information description": "Nbr. batterie overvoltage",
        "Short desc.": "n ovvolt",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3049: {
        "Nr": 3049,
        "information description": "State of the inverter",
        "Short desc.": "XT state",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Off 1:On"
    },
    3050: {
        "Nr": 3050,
        "information description": "Number of battery elements",
        "Short desc.": "Bat cells",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3051: {
        "Nr": 3051,
        "information description": "Search mode state",
        "Short desc.": "SB state",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "See parameter {1187} 0:Off 1:On"
    },
    3054: {
        "Nr": 3054,
        "information description": "Relay aux 1 mode",
        "Short desc.": "Aux 1",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Invalid value 1:A 2:I 3:M 4:M 5:G "
                                            "0: Invalid value "
                                            "1: Automatic "
                                            "2: Reversed automatic "
                                            "3: Manual ON "
                                            "4: Manual OFF "
                                            "5: Coupled for generator start"
    },
    3055: {
        "Nr": 3055,
        "information description": "Relay aux 2 mode",
        "Short desc.": "Aux 2",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "See info (3055) 0:Invalid value 1:A 2:I 3:M 4:M 5:G"
    },
    3056: {
        "Nr": 3056,
        "information description": "Lockings flag",
        "Short desc.": "Lockings",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "Bit 0: forbidden inverter {1124} "
                                            "Bit 1: forbidden charger {1125} "
                                            "Bit 2: forbidden boost {1126} "
                                            "Bit 3: forbidden transfert {1128} "
                                            "Bit 4: forbidden injection {1127} "
                                            "Bit 8: forbidden multi {1461} "
                                            "Bit 9: multi independants allowed {1462} "
                                            "Bit 10: standy slave allowed {1547}"
    },
    3074: {
        "Nr": 3074,
        "information description": "State of the ground relay",
        "Short desc.": "Rel_gnd",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Opened 1:Closed"
    },
    3075: {
        "Nr": 3075,
        "information description": "State of the neutral transfer relay",
        "Short desc.": "Rel_neutral",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Opened 1:Closed"
    },
    3076: {
        "Nr": 3076,
        "information description": "Discharge of battery of the previous day",
        "Short desc.": "E out YD",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3078: {
        "Nr": 3078,
        "information description": "Discharge of battery of the current day",
        "Short desc.": "E out Day",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3080: {
        "Nr": 3080,
        "information description": "Energy AC-In from the previous day",
        "Short desc.": "Eac in YD",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3081: {
        "Nr": 3081,
        "information description": "Energy AC-In from the current day",
        "Short desc.": "Eac in Day",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3082: {
        "Nr": 3082,
        "information description": "Consumers energy of the previous day",
        "Short desc.": "Eac out YD",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3083: {
        "Nr": 3083,
        "information description": "Consumers energy of the current day",
        "Short desc.": "Eac out Dy",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3084: {
        "Nr": 3084,
        "information description": "Input frequency",
        "Short desc.": "F in",
        "Unit on the RCC": "Hz",
        "Unit": "Hz",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "Replace info 3014"
    },
    3085: {
        "Nr": 3085,
        "information description": "Output frequency",
        "Short desc.": "F out",
        "Unit on the RCC": "Hz",
        "Unit": "Hz",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "Replace info 3024"
    },
    3086: {
        "Nr": 3086,
        "information description": "Remote entry state",
        "Short desc.": "RME",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:RM EN 0 1:RM EN 1"
    },
    3087: {
        "Nr": 3087,
        "information description": "Output active power",
        "Short desc.": "Pout a",
        "Unit on the RCC": "W",
        "Unit": "W",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "Less accurate than info 3136"
    },
    3088: {
        "Nr": 3088,
        "information description": "Input active power",
        "Short desc.": "P in a",
        "Unit on the RCC": "W",
        "Unit": "W",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "Less accurate than info 3137"
    },
    3089: {
        "Nr": 3089,
        "information description": "Defined phase",
        "Short desc.": "",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1=L1, 2=L2, 4=L3"
    },
    3090: {
        "Nr": 3090,
        "information description": "Battery voltage (minute min)",
        "Short desc.": "Ubat-",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute minimum"
    },
    3091: {
        "Nr": 3091,
        "information description": "Battery voltage (minute max)",
        "Short desc.": "Ubat+",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute maximum"
    },
    3092: {
        "Nr": 3092,
        "information description": "Battery voltage (minute avg)",
        "Short desc.": "Ubat",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute average"
    },
    3093: {
        "Nr": 3093,
        "information description": "Battery charge current (minute min)",
        "Short desc.": "Ibat-",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute minimum"
    },
    3094: {
        "Nr": 3094,
        "information description": "Battery charge current (minute max)",
        "Short desc.": "Ibat+",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute maximum"
    },
    3095: {
        "Nr": 3095,
        "information description": "Battery charge current (minute avg)",
        "Short desc.": "Ibat",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute average"
    },
    3096: {
        "Nr": 3096,
        "information description": "Output power min (minute min)",
        "Short desc.": "Pout-",
        "Unit on the RCC": "kVA",
        "Unit": "kVA",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute minimum"
    },
    3097: {
        "Nr": 3097,
        "information description": "Output power (minute max)",
        "Short desc.": "Pout+",
        "Unit on the RCC": "kVA",
        "Unit": "kVA",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute maximum"
    },
    3098: {
        "Nr": 3098,
        "information description": "Output power (minute avg)",
        "Short desc.": "Pout",
        "Unit on the RCC": "kVA",
        "Unit": "kVA",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute average"
    },
    3099: {
        "Nr": 3099,
        "information description": "Output active power (minute min)",
        "Short desc.": "Pout-a",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute minimum"
    },
    3100: {
        "Nr": 3100,
        "information description": "Output active power (minute max)",
        "Short desc.": "Pout+a",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute maximum"
    },
    3101: {
        "Nr": 3101,
        "information description": "Output active power (minute avg)",
        "Short desc.": "Pout a",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute average"
    },
    3102: {
        "Nr": 3102,
        "information description": "Electronic temperature 1 (minute min)",
        "Short desc.": "Dev1-",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute minimum"
    },
    3103: {
        "Nr": 3103,
        "information description": "Electronic temperature 1 (minute max)",
        "Short desc.": "Dev1+",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute maximum"
    },
    3104: {
        "Nr": 3104,
        "information description": "Electronic temperature 1 (minute avg)",
        "Short desc.": "Dev1",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute average"
    },
    3105: {
        "Nr": 3105,
        "information description": "Electronic temperature 2 (minute min)",
        "Short desc.": "Dev2-",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute minimum"
    },
    3106: {
        "Nr": 3106,
        "information description": "Electronic temperature 2 (minute max)",
        "Short desc.": "Dev2+",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute maximum"
    },
    3107: {
        "Nr": 3107,
        "information description": "Electronic temperature 2 (minute avg)",
        "Short desc.": "Dev2",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute average"
    },
    3108: {
        "Nr": 3108,
        "information description": "Output frequency (minute min)",
        "Short desc.": "Fout-",
        "Unit on the RCC": "Hz",
        "Unit": "Hz",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute minimum"
    },
    3109: {
        "Nr": 3109,
        "information description": "Output frequency (minute max)",
        "Short desc.": "Fout+",
        "Unit on the RCC": "Hz",
        "Unit": "Hz",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute maximum"
    },
    3110: {
        "Nr": 3110,
        "information description": "Output frequency (minute avg)",
        "Short desc.": "Fout",
        "Unit on the RCC": "Hz",
        "Unit": "Hz",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute average"
    },
    3111: {
        "Nr": 3111,
        "information description": "Input voltage (minute min)",
        "Short desc.": "Uin-",
        "Unit on the RCC": "Vac",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute minimum"
    },
    3112: {
        "Nr": 3112,
        "information description": "Input voltage (minute max)",
        "Short desc.": "Uin+",
        "Unit on the RCC": "Vac",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute maximum"
    },
    3113: {
        "Nr": 3113,
        "information description": "Input voltage (minute avg)",
        "Short desc.": "Uin",
        "Unit on the RCC": "Vac",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute average"
    },
    3114: {
        "Nr": 3114,
        "information description": "Input current (minute min)",
        "Short desc.": "Iin-",
        "Unit on the RCC": "Aac",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute minimum"
    },
    3115: {
        "Nr": 3115,
        "information description": "Input current (minute max)",
        "Short desc.": "Iin+",
        "Unit on the RCC": "Aac",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute maximum"
    },
    3116: {
        "Nr": 3116,
        "information description": "Input current (minute avg)",
        "Short desc.": "Iin",
        "Unit on the RCC": "Aac",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute average"
    },
    3117: {
        "Nr": 3117,
        "information description": "Input active power (minute min)",
        "Short desc.": "Pin-a",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute minimum"
    },
    3118: {
        "Nr": 3118,
        "information description": "Input active power (minute max)",
        "Short desc.": "Pin+a",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute maximum"
    },
    3119: {
        "Nr": 3119,
        "information description": "Input active power (minute avg)",
        "Short desc.": "Pin a",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute average"
    },
    3120: {
        "Nr": 3120,
        "information description": "Input frequency (minute min)",
        "Short desc.": "Fin-",
        "Unit on the RCC": "Hz",
        "Unit": "Hz",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute minimum"
    },
    3121: {
        "Nr": 3121,
        "information description": "Input frequency (minute max)",
        "Short desc.": "Fin+",
        "Unit on the RCC": "Hz",
        "Unit": "Hz",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute maximum"
    },
    3122: {
        "Nr": 3122,
        "information description": "Input frequency (minute avg)",
        "Short desc.": "Fin",
        "Unit on the RCC": "Hz",
        "Unit": "Hz",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "1 minute average"
    },
    3124: {
        "Nr": 3124,
        "information description": "ID type",
        "Short desc.": "Idt",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "XTH family = 1, XTM family = 256 et XTS family = 512"
    },
    3125: {
        "Nr": 3125,
        "information description": "ID Power",
        "Short desc.": "Power",
        "Unit on the RCC": "VA",
        "Unit": "VA",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3126: {
        "Nr": 3126,
        "information description": "ID Uout",
        "Short desc.": "Uout",
        "Unit on the RCC": "Vac",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3127: {
        "Nr": 3127,
        "information description": "ID batt voltage",
        "Short desc.": "Idv",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3128: {
        "Nr": 3128,
        "information description": "ID Iout nom",
        "Short desc.": "Ionom",
        "Unit on the RCC": "Aac",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3129: {
        "Nr": 3129,
        "information description": "ID HW",
        "Short desc.": "HW",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3130: {
        "Nr": 3130,
        "information description": "ID SOFT msb",
        "Short desc.": "Smsb",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'Software version encoding'"
    },
    3131: {
        "Nr": 3131,
        "information description": "ID SOFT lsb",
        "Short desc.": "Slsb",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'Software version encoding'"
    },
    3132: {
        "Nr": 3132,
        "information description": "ID HW PWR",
        "Short desc.": "HWpwr",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3133: {
        "Nr": 3133,
        "information description": "Parameter number (in code)",
        "Short desc.": "pCod",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3134: {
        "Nr": 3134,
        "information description": "Info user number",
        "Short desc.": "iCod",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3135: {
        "Nr": 3135,
        "information description": "ID SID",
        "Short desc.": "SID",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3136: {
        "Nr": 3136,
        "information description": "Output active power",
        "Short desc.": "P out a",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "More accurate than info 3087"
    },
    3137: {
        "Nr": 3137,
        "information description": "Input active power",
        "Short desc.": "P in a",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "More accurate than info 3088"
    },
    3138: {
        "Nr": 3138,
        "information description": "Input power",
        "Short desc.": "P in",
        "Unit on the RCC": "kVA",
        "Unit": "kVA",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "More accurate than info 3013"
    },
    3139: {
        "Nr": 3139,
        "information description": "Output power",
        "Short desc.": "P out",
        "Unit on the RCC": "kVA",
        "Unit": "kVA",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "More accurate than info 3023"
    },
    3140: {
        "Nr": 3140,
        "information description": "System debug 1",
        "Short desc.": "DBG1",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3141: {
        "Nr": 3141,
        "information description": "System debug 2",
        "Short desc.": "DBG2",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3142: {
        "Nr": 3142,
        "information description": "System state machine",
        "Short desc.": "SSM",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3154: {
        "Nr": 3154,
        "information description": "Input frequency",
        "Short desc.": "F in",
        "Unit on the RCC": "Hz",
        "Unit": "Hz",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3155: {
        "Nr": 3155,
        "information description": "Desired AC injection current",
        "Short desc.": "Injc",
        "Unit on the RCC": "Aac",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3156: {
        "Nr": 3156,
        "information description": "ID FID msb",
        "Short desc.": "",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'FID encoding'"
    },
    3157: {
        "Nr": 3157,
        "information description": "ID FID lsb",
        "Short desc.": "",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'FID encoding'"
    },
    3158: {
        "Nr": 3158,
        "information description": "Actual freezed current in ARN4105 P(f)",
        "Short desc.": "",
        "Unit on the RCC": "Aac",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "ARN4105, maximum current that can be injected actually, "
                                            "grid frequency dependance"
    },
    3159: {
        "Nr": 3159,
        "information description": "AC injection current, type of limitation ARN4105 P(f)",
        "Short desc.": "Injt",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:No limit 1:FreezeOF 2:N_ImaxOF 3:FreezeUF 4:N_ImaxUF 5:N_IMaxST ARN4105,"
                                            " current limitation depending on grid frequency : "
                                            "0 : no limitation "
                                            "1 : Value was frozen, grid frequency is >= 50.2Hz "
                                            "2 : Value not frozen but not at maximum, grid frequency is < 50.2Hz "
                                            "3 : Value was frozen, grid frequency is <=49.8Hz "
                                            "4 : Value not frozen but not at maximum, grid frequency is >49.8Hz "
                                            "5 : Value not frozen but not at maximum, grid reconnection"
    },
    3160: {
        "Nr": 3160,
        "information description": "Source of limitation of the functions charger or injector",
        "Short desc.": "LimSrc",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Invalid value "
                                            "1:Ubatt "
                                            "2:Ubattp "
                                            "3:Ubattpp "
                                            "4:Ibatt "
                                            "5:Pchar "
                                            "6:UbattInj "
                                            "7:Iinj "
                                            "8:Imax "
                                            "9:Ilim "
                                            "10:Ithermal "
                                            "11:PchNeg "
                                            "12:ARN f "
                                            "Limitation source is :"
                                            " 0: Invalid value "
                                            "1: U batt (actual phase of charge cycle) "
                                            "2: U batt peak "
                                            "3: U batt peak peak "
                                            "4: I batt ({1138}) "
                                            "5: P charger "
                                            "6: U batt injection "
                                            "7: I injection ({1523}) "
                                            "8: I max "
                                            "9: I input limit ({1107}) "
                                            "10 : I thermal "
                                            "11 : Pcharger only neg ACout "
                                            "12 : Charger limited by grid frequency"
    },
    3161: {
        "Nr": 3161,
        "information description": "Battery priority active",
        "Short desc.": "batPr",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "Target voltage for charge/inject is battery priotrity "
                                            "(displayed on RCC with “BP”) (Only v1.6.x) 0:Off 1:On"
    },
    3162: {
        "Nr": 3162,
        "information description": "Forced grid feeding active",
        "Short desc.": "InjFo",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "Target voltage for charge/inject is forced injection "
                                            "(displayed on RCC with “IF”) (Only v1.6.x) 0:Off 1:On"
    },
    3164: {
        "Nr": 3164,
        "information description": "Battery voltage target for charger/injection",
        "Short desc.": "",
        "Unit on the RCC": "Vdc",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "DC voltage référence for charge and injection stage."
                                            " Higher battery voltage can result in injection and lower battery voltage "
                                            "can result in battery charge if allowed."
    },
    3165: {
        "Nr": 3165,
        "information description": "Allowed charge current in limited charger mode",
        "Short desc.": "",
        "Unit on the RCC": "Aac",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "AC max current allowed for charging stage to ensure power from Acout."
    },
    3166: {
        "Nr": 3166,
        "information description": "Current on converter output stage DC/AC",
        "Short desc.": "",
        "Unit on the RCC": "Aac",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3167: {
        "Nr": 3167,
        "information description": "Voltage on converter output stage DC/AC",
        "Short desc.": "",
        "Unit on the RCC": "Vac",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    3168: {
        "Nr": 3168,
        "information description": "Over temperature state",
        "Short desc.": "OvTempS",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:No Error 1:TR.Alarm 2:TR.Error 3:EL.Error 4:EL.Stop "
                                            "Thermal state : "
                                            "0 = thermal OK "
                                            "1 = Transformer alarm "
                                            "2 = Transformer error "
                                            "4 = Electronique error "
                                            "8 = Electronique error halted Acctual current limit in ARN4105 P(f)"
    },
    3169: {
        "Nr": 3169,
        "information description": "AC injection current limit ARN4105 P(f)",
        "Short desc.": "Injm",
        "Unit on the RCC": "Aac",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
}

# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------ 1.5 RCC parameters ------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
# Contains 94 Parameters
RCC_PARAMETERS = {
    5000: {
        "Level": "Basic",
        "Nr": 5000,
        "parameter description": "Language",
        "Unit": "",
        "Default": None,
        "Min": 0,
        "Max": 3,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    5036: {
        "Level": "Expert",
        "Nr": 5036,
        "parameter description": "OTHER LANGUAGES",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    5038: {
        "Level": "Basic",
        "Nr": 5038,
        "parameter description": "Choice of the second language",
        "Unit": "",
        "Default": 2,
        "Min": 1,
        "Max": 128,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:English 2:French 4:German 8:Spanish 16:Dutch 32:Latinoellinika 64:Italian 128:Slovak"
    },
    5039: {
        "Level": "Basic",
        "Nr": 5039,
        "parameter description": "Choice of the third language",
        "Unit": "",
        "Default": 4,
        "Min": 1,
        "Max": 128,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:English 2:French 4:German 8:Spanish 16:Dutch 32:Latinoellinika 64:Italian 128:Slovak"
    },
    5040: {
        "Level": "Basic",
        "Nr": 5040,
        "parameter description": "Choice of the fourth language",
        "Unit": "",
        "Default": 8,
        "Min": 1,
        "Max": 128,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:English 2:French 4:German 8:Spanish 16:Dutch 32:Latinoellinika 64:Italian 128:Slovak"
    },
    5002: {
        "Level": "Basic",
        "Nr": 5002,
        "parameter description": "Date",
        "Unit": "Seconds",
        "Default": 0,
        "Min": 0,
        "Max": 0,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    5012: {
        "Level": "V.O.",
        "Nr": 5012,
        "parameter description": "User level",
        "Unit": "",
        "Default": 16,
        "Min": 0,
        "Max": 111,
        "Scom format": PropertyFormat.NOT_SUPPORTED,
        "Increment": ""
    },
    5019: {
        "Level": "Expert",
        "Nr": 5019,
        "parameter description": "Force remote control to user BASIC level",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5057: {
        "Level": "Expert",
        "Nr": 5057,
        "parameter description": "DATALOGGER",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    5101: {
        "Level": "Expert",
        "Nr": 5101,
        "parameter description": "Datalogger enabled",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 4,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Automatic 2:Yes 4:No"
    },
    5059: {
        "Level": "Expert",
        "Nr": 5059,
        "parameter description": "Save today's datas",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5109: {
        "Level": "Inst.",
        "Nr": 5109,
        "parameter description": "Datalogger reset when modifying the installation",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    5120: {
        "Level": "Inst.",
        "Nr": 5120,
        "parameter description": "Erase the 30 oldest log files from the SD card",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5123: {
        "Level": "Expert",
        "Nr": 5123,
        "parameter description": "Activation of R&D tracks",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    5076: {
        "Level": "QSP",
        "Nr": 5076,
        "parameter description": "Track 1: device",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:XT 2:BSP/BMS 4:VarioTrack 8:VarioString"
    },
    5063: {
        "Level": "QSP",
        "Nr": 5063,
        "parameter description": "Track 1: UID",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 15,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    5077: {
        "Level": "QSP",
        "Nr": 5077,
        "parameter description": "Track 1: reference",
        "Unit": "",
        "Default": 140,
        "Min": 0,
        "Max": 255,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    5078: {
        "Level": "QSP",
        "Nr": 5078,
        "parameter description": "Track 2: device",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": " Only 1 bit 1:XT 2:BSP/BMS 4:VarioTrack 8:VarioString"
    },
    5064: {
        "Level": "QSP",
        "Nr": 5064,
        "parameter description": "Track 2: UID",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 15,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    5079: {
        "Level": "QSP",
        "Nr": 5079,
        "parameter description": "Track 2: reference",
        "Unit": "",
        "Default": 141,
        "Min": 0,
        "Max": 255,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    5080: {
        "Level": "QSP",
        "Nr": 5080,
        "parameter description": "Track 3: device",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:XT 2:BSP/BMS 4:VarioTrack 8:VarioString"
    },
    5065: {
        "Level": "QSP",
        "Nr": 5065,
        "parameter description": "Track 3: UID",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 15,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    5081: {
        "Level": "QSP",
        "Nr": 5081,
        "parameter description": "Track 3: reference",
        "Unit": "",
        "Default": 142,
        "Min": 0,
        "Max": 255,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    5082: {
        "Level": "QSP",
        "Nr": 5082,
        "parameter description": "Track 4: device",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:XT 2:BSP/BMS 4:VarioTrack 8:VarioString"
    },
    5066: {
        "Level": "QSP",
        "Nr": 5066,
        "parameter description": "Track 4: UID",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 15,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    5083: {
        "Level": "QSP",
        "Nr": 5083,
        "parameter description": "Track 4: reference",
        "Unit": "",
        "Default": 160,
        "Min": 0,
        "Max": 255,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    5013: {
        "Level": "Basic",
        "Nr": 5013,
        "parameter description": "SAVE AND RESTORE FILES",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    5041: {
        "Level": "Basic",
        "Nr": 5041,
        "parameter description": "Save all files (system backup)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5068: {
        "Level": "Basic",
        "Nr": 5068,
        "parameter description": "Restore all files (system recovery)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5070: {
        "Level": "Basic",
        "Nr": 5070,
        "parameter description": "Apply configuration files (masterfile)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5032: {
        "Level": "Expert",
        "Nr": 5032,
        "parameter description": "Separator of the .csv files",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 4,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Automatic 2:; 4:,"
    },
    5069: {
        "Level": "Expert",
        "Nr": 5069,
        "parameter description": "Advanced backup functions",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    5030: {
        "Level": "Expert",
        "Nr": 5030,
        "parameter description": "Save messages",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5049: {
        "Level": "Expert",
        "Nr": 5049,
        "parameter description": "Save and restore RCC files",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    5015: {
        "Level": "Expert",
        "Nr": 5015,
        "parameter description": "Save RCC parameters",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5016: {
        "Level": "Expert",
        "Nr": 5016,
        "parameter description": "Load RCC parameters",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5097: {
        "Level": "Inst.",
        "Nr": 5097,
        "parameter description": "Create RCC configuration file (masterfile)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5098: {
        "Level": "Expert",
        "Nr": 5098,
        "parameter description": "Load RCC configuration file (masterfile)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5050: {
        "Level": "Expert",
        "Nr": 5050,
        "parameter description": "Save and restore Xtender files",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    5017: {
        "Level": "Expert",
        "Nr": 5017,
        "parameter description": "Save Xtender parameters",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5018: {
        "Level": "Expert",
        "Nr": 5018,
        "parameter description": "Load Xtender parameters",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5033: {
        "Level": "Inst.",
        "Nr": 5033,
        "parameter description": "Create Xtender configuration file (masterfile)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5034: {
        "Level": "Expert",
        "Nr": 5034,
        "parameter description": "Load Xtender configuration file (masterfile)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5045: {
        "Level": "Expert",
        "Nr": 5045,
        "parameter description": "Load Xtender parameters preset",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 1,
        "Scom format": PropertyFormat.NOT_SUPPORTED,
        "Increment": ""
    },
    5051: {
        "Level": "Expert",
        "Nr": 5051,
        "parameter description": "Save and restore BSP files",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    5052: {
        "Level": "Expert",
        "Nr": 5052,
        "parameter description": "Save BSP parameters",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5053: {
        "Level": "Expert",
        "Nr": 5053,
        "parameter description": "Load BSP parameters",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5054: {
        "Level": "Inst.",
        "Nr": 5054,
        "parameter description": "Create BSP configuration file (masterfile)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5055: {
        "Level": "Expert",
        "Nr": 5055,
        "parameter description": "Load BSP configuration file (masterfile)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5084: {
        "Level": "Expert",
        "Nr": 5084,
        "parameter description": "Save and restore VarioTrack files",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    5085: {
        "Level": "Expert",
        "Nr": 5085,
        "parameter description": "Save VarioTrack parameters",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5086: {
        "Level": "Expert",
        "Nr": 5086,
        "parameter description": "Load VarioTrack parameters",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5087: {
        "Level": "Inst.",
        "Nr": 5087,
        "parameter description": "Create VarioTrack configuration file (masterfile)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5088: {
        "Level": "Expert",
        "Nr": 5088,
        "parameter description": "Load VarioTrack configuration file (masterfile)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5114: {
        "Level": "Expert",
        "Nr": 5114,
        "parameter description": "Save and restore VarioString files",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    5115: {
        "Level": "Expert",
        "Nr": 5115,
        "parameter description": "Save VarioString parameters",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5116: {
        "Level": "Expert",
        "Nr": 5116,
        "parameter description": "Load VarioString parameters",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5117: {
        "Level": "Inst.",
        "Nr": 5117,
        "parameter description": "Create VarioString configuration file (masterfile)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5118: {
        "Level": "Expert",
        "Nr": 5118,
        "parameter description": "Load VarioString configuration file (masterfile)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5047: {
        "Level": "Inst.",
        "Nr": 5047,
        "parameter description": "Format the SD card",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5061: {
        "Level": "Expert",
        "Nr": 5061,
        "parameter description": "Start update",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5042: {
        "Level": "Inst.",
        "Nr": 5042,
        "parameter description": "MODIFICATION OF ACCESS LEVELS OF MANY PARAMETERS",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    5043: {
        "Level": "Inst.",
        "Nr": 5043,
        "parameter description": "Change all parameters access level to:",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Choose 2:BASIC 4:EXPERT 8:INSTALLER"
    },
    5044: {
        "Level": "Inst.",
        "Nr": 5044,
        "parameter description": "Restore default access level of all parameters",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5007: {
        "Level": "Basic",
        "Nr": 5007,
        "parameter description": "BACKLIGHT",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    5093: {
        "Level": "Basic",
        "Nr": 5093,
        "parameter description": "Backlight mode",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 4,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Delayed 2:OFF 4:ON"
    },
    5009: {
        "Level": "Basic",
        "Nr": 5009,
        "parameter description": "Backlight switch off after",
        "Unit": "sec",
        "Default": 120,
        "Min": 5,
        "Max": 120,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    5026: {
        "Level": "Expert",
        "Nr": 5026,
        "parameter description": "Red backlight flashing on Xtender off and faulty",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    5021: {
        "Level": "Basic",
        "Nr": 5021,
        "parameter description": "EXTENDED AND SPECIAL FUNCTIONS",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    5006: {
        "Level": "Basic",
        "Nr": 5006,
        "parameter description": "Display contrast",
        "Unit": "%",
        "Default": 50,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    5073: {
        "Level": "Expert",
        "Nr": 5073,
        "parameter description": "Choice of standard display",
        "Unit": "",
        "Default": 2,
        "Min": 1,
        "Max": 16,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Clock 2:Xtender 4:BSP 8:VarioTrack 16:VarioString"
    },
    5111: {
        "Level": "Inst.",
        "Nr": 5111,
        "parameter description": "Displaying of configuration assistant on startup",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 4,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Automatic 2:Hidden menu 4:By default {5073}"
    },
    5010: {
        "Level": "Expert",
        "Nr": 5010,
        "parameter description": "Come back to standard display after",
        "Unit": "sec",
        "Default": 600,
        "Min": 5,
        "Max": 600,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    5011: {
        "Level": "Expert",
        "Nr": 5011,
        "parameter description": "Visibility of the transitory messages",
        "Unit": "sec",
        "Default": 60,
        "Min": 0,
        "Max": 180,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    5027: {
        "Level": "Basic",
        "Nr": 5027,
        "parameter description": "Acoustic alarm active",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    5031: {
        "Level": "Expert",
        "Nr": 5031,
        "parameter description": "Remote control acoustic alarm duration",
        "Unit": "sec",
        "Default": 120,
        "Min": 5,
        "Max": 120,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    5056: {
        "Level": "Expert",
        "Nr": 5056,
        "parameter description": "Switching ON and OFF of system on level 'VIEW ONLY'",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    5071: {
        "Level": "Expert",
        "Nr": 5071,
        "parameter description": "Reset of all the remotes control",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5121: {
        "Level": "Expert",
        "Nr": 5121,
        "parameter description": "Reset all devices of the system",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5090: {
        "Level": "QSP",
        "Nr": 5090,
        "parameter description": "Update FID (only 1 device)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    5091: {
        "Level": "QSP",
        "Nr": 5091,
        "parameter description": "Choose device type",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:XT 2:BSP 4:VarioTrack 8:VarioString"
    },
    5092: {
        "Level": "QSP",
        "Nr": 5092,
        "parameter description": "Choose device id (UID)",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 30,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    5062: {
        "Level": "QSP",
        "Nr": 5062,
        "parameter description": "Update device FID (only 1 device)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5094: {
        "Level": "Expert",
        "Nr": 5094,
        "parameter description": "XCOM AND SCOM",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    5105: {
        "Level": "Expert",
        "Nr": 5105,
        "parameter description": "Test of the modem's GPRS signal level (Xcom-GSM)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5067: {
        "Level": "Inst.",
        "Nr": 5067,
        "parameter description": "Clear info {17019} Maximum time interval between two scom requests",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5072: {
        "Level": "Inst.",
        "Nr": 5072,
        "parameter description": "Xcom Portal watchdog activation",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 4,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Automatic 2:Yes 4:No"
    },
    5113: {
        "Level": "Inst.",
        "Nr": 5113,
        "parameter description": "Delay before Xcom Portal watchdog forces reconnection",
        "Unit": "minutes",
        "Default": 15,
        "Min": 5,
        "Max": 1440,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    5119: {
        "Level": "QSP",
        "Nr": 5119,
        "parameter description": "Device identification (LEDs) with the SCOM address",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 831,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    5095: {
        "Level": "QSP",
        "Nr": 5095,
        "parameter description": "Enable SCOM watchdog",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    5096: {
        "Level": "QSP",
        "Nr": 5096,
        "parameter description": "SCOM watchdog delay before reset of Xcom-232i",
        "Unit": "sec",
        "Default": 60,
        "Min": 10,
        "Max": 300,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    5103: {
        "Level": "QSP",
        "Nr": 5103,
        "parameter description": "Activation of the watchdog hardware (deactivation restarts the Xcom-232i)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    5104: {
        "Level": "QSP",
        "Nr": 5104,
        "parameter description": "Clears the restart flag of Xcom-232i",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    5035: {
        "Level": "QSP",
        "Nr": 5035,
        "parameter description": "Erase messages",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
}

# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------ 1.6 BSP parameters ------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
# Contains 27 Parameters
BSP_PARAMETERS = {
    6000: {
        "Level": "Basic",
        "Nr": 6000,
        "parameter description": "BASIC SETTINGS (BSP)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    6057: {
        "Level": "Basic",
        "Nr": 6057,
        "parameter description": "Voltage of the system",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Automatic 2:12V 4:24V 8:48V"
    },
    6001: {
        "Level": "Basic",
        "Nr": 6001,
        "parameter description": "Nominal capacity",
        "Unit": "Ah",
        "Default": 110,
        "Min": 20,
        "Max": 20000,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    6002: {
        "Level": "Basic",
        "Nr": 6002,
        "parameter description": "Nominal discharge duration (C-rating)",
        "Unit": "h",
        "Default": 20,
        "Min": 1,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    6017: {
        "Level": "Basic",
        "Nr": 6017,
        "parameter description": "Nominal shunt current",
        "Unit": "A",
        "Default": 500,
        "Min": 10,
        "Max": 10000,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    6018: {
        "Level": "Basic",
        "Nr": 6018,
        "parameter description": "Nominal shunt voltage",
        "Unit": "mV",
        "Default": 50,
        "Min": 10,
        "Max": 200,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    6003: {
        "Level": "Expert",
        "Nr": 6003,
        "parameter description": "Reset of battery history",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    6004: {
        "Level": "Basic",
        "Nr": 6004,
        "parameter description": "Restore default settings",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    6005: {
        "Level": "Inst.",
        "Nr": 6005,
        "parameter description": "Restore factory settings",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    6016: {
        "Level": "Expert",
        "Nr": 6016,
        "parameter description": "ADVANCED SETTINGS (BSP)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    6031: {
        "Level": "Expert",
        "Nr": 6031,
        "parameter description": "Reset of user counters",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    6055: {
        "Level": "Expert",
        "Nr": 6055,
        "parameter description": "Manufacturer SOC for 0% displayed",
        "Unit": "%",
        "Default": 30,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    6056: {
        "Level": "Expert",
        "Nr": 6056,
        "parameter description": "Manufacturer SOC for 100% displayed",
        "Unit": "%",
        "Default": 100,
        "Min": 80,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    6042: {
        "Level": "Expert",
        "Nr": 6042,
        "parameter description": "Activate the end of charge synchronization",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    6024: {
        "Level": "Expert",
        "Nr": 6024,
        "parameter description": "End of charge voltage level",
        "Unit": "V",
        "Default": 52.8,
        "Min": 31.9,
        "Max": 70.1,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    6025: {
        "Level": "Expert",
        "Nr": 6025,
        "parameter description": "End of charge current level",
        "Unit": "%cap",
        "Default": 2,
        "Min": 0,
        "Max": 500,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    6065: {
        "Level": "Expert",
        "Nr": 6065,
        "parameter description": "Minimum duration before end of charge",
        "Unit": "min",
        "Default": 5,
        "Min": 5,
        "Max": 300,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    6048: {
        "Level": "Expert",
        "Nr": 6048,
        "parameter description": "Temperature correction of the end of charge voltage",
        "Unit": "mV/°C/cell",
        "Default": 0,
        "Min": -8,
        "Max": 0,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    6044: {
        "Level": "Expert",
        "Nr": 6044,
        "parameter description": "Activate the state of charge correction by the open circuit voltage",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    6058: {
        "Level": "Expert",
        "Nr": 6058,
        "parameter description": "Battery charge current centralized regulation activated",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    6059: {
        "Level": "Expert",
        "Nr": 6059,
        "parameter description": "Max battery charge current",
        "Unit": "A",
        "Default": 60,
        "Min": 0,
        "Max": 10000,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    6019: {
        "Level": "Expert",
        "Nr": 6019,
        "parameter description": "Self-discharge rate",
        "Unit": "%/month",
        "Default": 3,
        "Min": 0,
        "Max": 25,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    6020: {
        "Level": "Expert",
        "Nr": 6020,
        "parameter description": "Nominal temperature",
        "Unit": "°C",
        "Default": 20,
        "Min": 0,
        "Max": 40,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    6021: {
        "Level": "Expert",
        "Nr": 6021,
        "parameter description": "Temperature coefficient",
        "Unit": "%cap/°C",
        "Default": 0.5,
        "Min": 0,
        "Max": 3,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.0999756"
    },
    6022: {
        "Level": "Expert",
        "Nr": 6022,
        "parameter description": "Charge efficiency factor",
        "Unit": "%",
        "Default": 90,
        "Min": 50,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    6023: {
        "Level": "Expert",
        "Nr": 6023,
        "parameter description": "Peukert's exponent",
        "Unit": "",
        "Default": 1.2,
        "Min": 1,
        "Max": 1.5,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.0100098"
    },
    6049: {
        "Level": "Expert",
        "Nr": 6049,
        "parameter description": "Use C20 Capacity as reference value",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
}

# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------- 1.7 BSP infos -------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Contains 34 Infos
BSP_INFOS = {
    7000: {
        "Nr": 7000,
        "information description": "Battery voltage",
        "Short desc.": "Ubat",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7001: {
        "Nr": 7001,
        "information description": "Battery current",
        "Short desc.": "Ibat",
        "Unit on the RCC": "Adc",
        "Unit": "Adc",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7002: {
        "Nr": 7002,
        "information description": "State of Charge",
        "Short desc.": "SOC",
        "Unit on the RCC": "%",
        "Unit": "%",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7003: {
        "Nr": 7003,
        "information description": "Power",
        "Short desc.": "Pbat",
        "Unit on the RCC": "W",
        "Unit": "W",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7004: {
        "Nr": 7004,
        "information description": "Remaining autonomy",
        "Short desc.": "Trem",
        "Unit on the RCC": "",
        "Unit": "minutes",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "in discharge, number of minutes before 0 % between -60000 and 0, in charge"
                                            ", always NAN"
    },
    7006: {
        "Nr": 7006,
        "information description": "Relative capacity",
        "Short desc.": "Crel",
        "Unit on the RCC": "%",
        "Unit": "%",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "deprecated, return 100 % in version >= 1.5.6"
    },
    7007: {
        "Nr": 7007,
        "information description": "Ah charged today",
        "Short desc.": "0d<",
        "Unit on the RCC": "Ah",
        "Unit": "Ah",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7008: {
        "Nr": 7008,
        "information description": "Ah discharged today",
        "Short desc.": "0d>",
        "Unit on the RCC": "Ah",
        "Unit": "Ah",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7009: {
        "Nr": 7009,
        "information description": "Ah charged yesterday",
        "Short desc.": "-1d<",
        "Unit on the RCC": "Ah",
        "Unit": "Ah",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7010: {
        "Nr": 7010,
        "information description": "Ah discharged yesterday",
        "Short desc.": "-1d>",
        "Unit on the RCC": "Ah",
        "Unit": "Ah",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7011: {
        "Nr": 7011,
        "information description": "Total Ah charged",
        "Short desc.": "tot<",
        "Unit on the RCC": "kAh",
        "Unit": "kAh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7012: {
        "Nr": 7012,
        "information description": "Total Ah discharged",
        "Short desc.": "tot>",
        "Unit on the RCC": "kAh",
        "Unit": "kAh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7013: {
        "Nr": 7013,
        "information description": "Total time",
        "Short desc.": "Ttot",
        "Unit on the RCC": "days",
        "Unit": "days",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7017: {
        "Nr": 7017,
        "information description": "Custom charge Ah counter",
        "Short desc.": "cus<",
        "Unit on the RCC": "Ah",
        "Unit": "Ah",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7018: {
        "Nr": 7018,
        "information description": "Custom discharge Ah counter",
        "Short desc.": "cus>",
        "Unit on the RCC": "Ah",
        "Unit": "Ah",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7019: {
        "Nr": 7019,
        "information description": "Custom counter duration",
        "Short desc.": "Tcus",
        "Unit on the RCC": "h",
        "Unit": "h",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7029: {
        "Nr": 7029,
        "information description": "Battery temperature",
        "Short desc.": "Tbat",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7030: {
        "Nr": 7030,
        "information description": "Battery voltage (minute avg)",
        "Short desc.": "Ubat",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7031: {
        "Nr": 7031,
        "information description": "Battery current (minute avg)",
        "Short desc.": "Ibat",
        "Unit on the RCC": "Adc",
        "Unit": "Adc",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7032: {
        "Nr": 7032,
        "information description": "State of Charge (minute avg)",
        "Short desc.": "SOC",
        "Unit on the RCC": "%",
        "Unit": "%",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7033: {
        "Nr": 7033,
        "information description": "Battery temperature (minute avg)",
        "Short desc.": "Tbat",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7034: {
        "Nr": 7034,
        "information description": "ID type",
        "Short desc.": "Idt",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "BSP500 and BSP1200 = 10241d (0x2801)"
    },
    7035: {
        "Nr": 7035,
        "information description": "ID batt voltage",
        "Short desc.": "Idv",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7036: {
        "Nr": 7036,
        "information description": "ID HW",
        "Short desc.": "HW",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7037: {
        "Nr": 7037,
        "information description": "ID SOFT msb",
        "Short desc.": "Smsb",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'Software version encoding'"
    },
    7038: {
        "Nr": 7038,
        "information description": "ID SOFT lsb",
        "Short desc.": "Slsb",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'Software version encoding'"
    },
    7039: {
        "Nr": 7039,
        "information description": "Parameter number (in code)",
        "Short desc.": "pCod",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7040: {
        "Nr": 7040,
        "information description": "Info user number",
        "Short desc.": "iCod",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7041: {
        "Nr": 7041,
        "information description": "ID SID",
        "Short desc.": "SID",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7047: {
        "Nr": 7047,
        "information description": "Manufacturer State of Charge",
        "Short desc.": "mSOC",
        "Unit on the RCC": "%",
        "Unit": "%",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7048: {
        "Nr": 7048,
        "information description": "ID FID msb",
        "Short desc.": "",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'FID encoding'"
    },
    7049: {
        "Nr": 7049,
        "information description": "ID FID lsb",
        "Short desc.": "",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'FID encoding'"
    },
    7059: {
        "Nr": 7059,
        "information description": "Local daily communication error counter (CAN)",
        "Short desc.": "locE",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7060: {
        "Nr": 7060,
        "information description": "Number of parameters (in flash)",
        "Short desc.": "pFsh",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
}

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------- 1.7 Xcom-CAN BMS parameters ------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Contains 16 Parameters
XCOM_CAN_PARAMETERS = {
    6060: {
        "Level": "Basic",
        "Nr": 6060,
        "parameter description": "BASIC SETTINGS (Xcom-CAN BMS)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    6004: {
        "Level": "Basic",
        "Nr": 6004,
        "parameter description": "Restore default settings",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32,
        "Increment": "Signal"
    },
    6005: {
        "Level": "Inst.",
        "Nr": 6005,
        "parameter description": "Restore factory settings",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32,
        "Increment": "Signal"
    },
    6061: {
        "Level": "Expert",
        "Nr": 6061,
        "parameter description": "ADVANCED SETTINGS (Xcom-CAN BMS)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    6070: {
        "Level": "Expert",
        "Nr": 6070,
        "parameter description": "SOC level under which battery discharge is stopped",
        "Unit": "%",
        "Default": 5,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    6062: {
        "Level": "Expert",
        "Nr": 6062,
        "parameter description": "SOC level for backup",
        "Unit": "%",
        "Default": 100,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    6063: {
        "Level": "Expert",
        "Nr": 6063,
        "parameter description": "SOC level for grid feeding",
        "Unit": "%",
        "Default": 100,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    6071: {
        "Level": "Expert",
        "Nr": 6071,
        "parameter description": "Use battery priority as energy source when SOC >= SOC for backup "
                                 "(not recommended in parallel)",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    6068: {
        "Level": "Expert",
        "Nr": 6068,
        "parameter description": "Allow user to define the maximum charge current of the battery",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    6069: {
        "Level": "Expert",
        "Nr": 6069,
        "parameter description": "Maximum charge current defined by user",
        "Unit": "A",
        "Default": 10,
        "Min": 0,
        "Max": 10000,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    6066: {
        "Level": "Expert",
        "Nr": 6066,
        "parameter description": "Manufacturer SOC for 0% displayed",
        "Unit": "%",
        "Default": 0,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    6067: {
        "Level": "Expert",
        "Nr": 6067,
        "parameter description": "Manufacturer SOC for 100% displayed",
        "Unit": "%",
        "Default": 100,
        "Min": 80,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    6064: {
        "Level": "Expert",
        "Nr": 6064,
        "parameter description": "Use battery current limits instead of recommended values",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    6072: {
        "Level": "Expert",
        "Nr": 6072,
        "parameter description": "Solar Inverter connected on AC-Out",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    6073: {
        "Level": "Expert",
        "Nr": 6073,
        "parameter description": "Delta from user frequency to start derating of solar inverter",
        "Unit": "Hz",
        "Default": 1,
        "Min": 0,
        "Max": 5,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    6074: {
        "Level": "Expert",
        "Nr": 6074,
        "parameter description": "Delta from user frequency to reach 100% derating of solar inverter",
        "Unit": "Hz",
        "Default": 2.7,
        "Min": 0,
        "Max": 5,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
}

# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------- 1.8 Xcom-CAN BMS infos ---------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Contains 24 Infos
XCOM_CAN_INFOS = {
    7000: {
        "Nr": 7000,
        "information description": "Battery voltage",
        "Short desc.": "Ubat",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7001: {
        "Nr": 7001,
        "information description": "Battery current",
        "Short desc.": "Ibat",
        "Unit on the RCC": "Adc",
        "Unit": "Adc",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7002: {
        "Nr": 7002,
        "information description": "State of Charge",
        "Short desc.": "SOC",
        "Unit on the RCC": "%",
        "Unit": "%",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7003: {
        "Nr": 7003,
        "information description": "Power",
        "Short desc.": "Pbat",
        "Unit on the RCC": "W",
        "Unit": "W",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7007: {
        "Nr": 7007,
        "information description": "Ah charged today",
        "Short desc.": "0d<",
        "Unit on the RCC": "Ah",
        "Unit": "Ah",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7008: {
        "Nr": 7008,
        "information description": "Ah discharged today",
        "Short desc.": "0d>",
        "Unit on the RCC": "Ah",
        "Unit": "Ah",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7009: {
        "Nr": 7009,
        "information description": "Ah charged yesterday",
        "Short desc.": "-1d<",
        "Unit on the RCC": "Ah",
        "Unit": "Ah",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7010: {
        "Nr": 7010,
        "information description": "Ah discharged yesterday",
        "Short desc.": "-1d>",
        "Unit on the RCC": "Ah",
        "Unit": "Ah",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7029: {
        "Nr": 7029,
        "information description": "Battery temperature",
        "Short desc.": "Tbat",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7030: {
        "Nr": 7030,
        "information description": "Battery voltage (minute avg)",
        "Short desc.": "Ubat",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7031: {
        "Nr": 7031,
        "information description": "Battery current (minute avg)",
        "Short desc.": "Ibat",
        "Unit on the RCC": "Adc",
        "Unit": "Adc",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7032: {
        "Nr": 7032,
        "information description": "State of Charge (minute avg)",
        "Short desc.": "SOC",
        "Unit on the RCC": "%",
        "Unit": "%",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7033: {
        "Nr": 7033,
        "information description": "Battery temperature (minute avg)",
        "Short desc.": "Tbat",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7047: {
        "Nr": 7047,
        "information description": "Manufacturer State of Charge",
        "Short desc.": "mSOC",
        "Unit on the RCC": "%",
        "Unit": "%",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7055: {
        "Nr": 7055,
        "information description": "Battery Capacity",
        "Short desc.": "bCap",
        "Unit on the RCC": "Ah",
        "Unit": "Ah",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7057: {
        "Nr": 7057,
        "information description": "State Of Health",
        "Short desc.": "SOH",
        "Unit on the RCC": "%",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7058: {
        "Nr": 7058,
        "information description": "High resolution manufacturer State of Charge",
        "Short desc.": "hSOC",
        "Unit on the RCC": "%",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7061: {
        "Nr": 7061,
        "information description": "Charge voltage limit",
        "Short desc.": "UChL",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7062: {
        "Nr": 7062,
        "information description": "Discharge voltage limit",
        "Short desc.": "UDiL",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7063: {
        "Nr": 7063,
        "information description": "Charge current limit",
        "Short desc.": "IChL",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7064: {
        "Nr": 7064,
        "information description": "Discharge current limit",
        "Short desc.": "IDiL",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7065: {
        "Nr": 7065,
        "information description": "Recommended charge current",
        "Short desc.": "IChR",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7066: {
        "Nr": 7066,
        "information description": "Recommended discharge current",
        "Short desc.": "IDiR",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    7067: {
        "Nr": 7067,
        "information description": "Manufacturer name",
        "Short desc.": "name",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:OTHERS 1:BYD 2:PYLON 3:WECO"
    },
}

# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------- 1.9 VarioTrack parameters -------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Contains 297 Parameters
VARIO_TRACK_PARAMETERS = {
    10000: {
        "Level": "Basic",
        "Nr": 10000,
        "parameter description": "BASIC SETTINGS",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10054: {
        "Level": "Expert",
        "Nr": 10054,
        "parameter description": "Block manual programming (dip-switch)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10001: {
        "Level": "Basic",
        "Nr": 10001,
        "parameter description": "Voltage of the system",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Automatic 2:12V 4:24V 8:48V"
    },
    10037: {
        "Level": "Basic",
        "Nr": 10037,
        "parameter description": "Synchronisation battery cycle with Xtender",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10005: {
        "Level": "Basic",
        "Nr": 10005,
        "parameter description": "Floating voltage",
        "Unit": "Vdc",
        "Default": 54.4,
        "Min": 37.9,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10009: {
        "Level": "Basic",
        "Nr": 10009,
        "parameter description": "Absorption voltage",
        "Unit": "Vdc",
        "Default": 57.6,
        "Min": 37.9,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10017: {
        "Level": "Basic",
        "Nr": 10017,
        "parameter description": "Equalization allowed",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10021: {
        "Level": "Basic",
        "Nr": 10021,
        "parameter description": "Equalization voltage",
        "Unit": "Vdc",
        "Default": 62.4,
        "Min": 52.1,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10056: {
        "Level": "Basic",
        "Nr": 10056,
        "parameter description": "Restore default settings",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10057: {
        "Level": "Inst.",
        "Nr": 10057,
        "parameter description": "Restore factory settings",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10003: {
        "Level": "Expert",
        "Nr": 10003,
        "parameter description": "BATTERY MANAGEMENT AND CYCLE",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10002: {
        "Level": "Expert",
        "Nr": 10002,
        "parameter description": "Battery charge current",
        "Unit": "Adc",
        "Default": 80,
        "Min": 0,
        "Max": 80,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "2"
    },
    10334: {
        "Level": "Expert",
        "Nr": 10334,
        "parameter description": "Battery undervoltage",
        "Unit": "Vdc",
        "Default": 40,
        "Min": 34,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10036: {
        "Level": "Expert",
        "Nr": 10036,
        "parameter description": "Temperature compensation",
        "Unit": "mV/°C/cell",
        "Default": -3,
        "Min": -8,
        "Max": 0,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10004: {
        "Level": "Expert",
        "Nr": 10004,
        "parameter description": "Floating phase",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10006: {
        "Level": "Expert",
        "Nr": 10006,
        "parameter description": "Force phase of floating",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10007: {
        "Level": "Expert",
        "Nr": 10007,
        "parameter description": "Absorption phase",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10008: {
        "Level": "Expert",
        "Nr": 10008,
        "parameter description": "Absorption phase allowed",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10010: {
        "Level": "Expert",
        "Nr": 10010,
        "parameter description": "Force absorption phase",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10011: {
        "Level": "Expert",
        "Nr": 10011,
        "parameter description": "Absorption duration",
        "Unit": "min",
        "Default": 120,
        "Min": 5,
        "Max": 510,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10012: {
        "Level": "Expert",
        "Nr": 10012,
        "parameter description": "End of absorption triggered by the current",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10013: {
        "Level": "Expert",
        "Nr": 10013,
        "parameter description": "Current threshold to end absorption phase",
        "Unit": "Adc",
        "Default": 10,
        "Min": 2,
        "Max": 80,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "2"
    },
    10016: {
        "Level": "Expert",
        "Nr": 10016,
        "parameter description": "Equalization phase",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10018: {
        "Level": "Expert",
        "Nr": 10018,
        "parameter description": "Force equalization",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10020: {
        "Level": "Expert",
        "Nr": 10020,
        "parameter description": "Equalization current",
        "Unit": "Adc",
        "Default": 80,
        "Min": 2,
        "Max": 80,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "2"
    },
    10022: {
        "Level": "Expert",
        "Nr": 10022,
        "parameter description": "Equalization duration",
        "Unit": "min",
        "Default": 30,
        "Min": 5,
        "Max": 510,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10052: {
        "Level": "Expert",
        "Nr": 10052,
        "parameter description": "Equalization with fixed interval",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10025: {
        "Level": "Expert",
        "Nr": 10025,
        "parameter description": "Days between equalizations",
        "Unit": "days",
        "Default": 26,
        "Min": 1,
        "Max": 365,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10026: {
        "Level": "Expert",
        "Nr": 10026,
        "parameter description": "End of equalization triggered by the current",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10027: {
        "Level": "Expert",
        "Nr": 10027,
        "parameter description": "Current threshold to end equalization phase",
        "Unit": "Adc",
        "Default": 10,
        "Min": 4,
        "Max": 30,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10019: {
        "Level": "Expert",
        "Nr": 10019,
        "parameter description": "Equalization before absorption phase",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10028: {
        "Level": "Expert",
        "Nr": 10028,
        "parameter description": "New cycle",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10029: {
        "Level": "Expert",
        "Nr": 10029,
        "parameter description": "Force a new cycle",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10030: {
        "Level": "Expert",
        "Nr": 10030,
        "parameter description": "Voltage level 1 to start a new cycle",
        "Unit": "Vdc",
        "Default": 48.8,
        "Min": 37.9,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10031: {
        "Level": "Expert",
        "Nr": 10031,
        "parameter description": "Time period under voltage level 1 to start a new cycle",
        "Unit": "min",
        "Default": 30,
        "Min": 0,
        "Max": 240,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10032: {
        "Level": "Expert",
        "Nr": 10032,
        "parameter description": "Voltage level 2 to start a new cycle",
        "Unit": "Vdc",
        "Default": 47.2,
        "Min": 37.9,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10033: {
        "Level": "Expert",
        "Nr": 10033,
        "parameter description": "Time period under voltage level 2 to start a new cycle",
        "Unit": "min",
        "Default": 2,
        "Min": 0,
        "Max": 240,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10034: {
        "Level": "Expert",
        "Nr": 10034,
        "parameter description": "Cycling restricted",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10035: {
        "Level": "Expert",
        "Nr": 10035,
        "parameter description": "Minimal delay between cycles",
        "Unit": "hours",
        "Default": 1,
        "Min": 0,
        "Max": 540,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10085: {
        "Level": "Expert",
        "Nr": 10085,
        "parameter description": "Battery overvoltage level",
        "Unit": "Vdc",
        "Default": 68.2,
        "Min": 37.9,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10086: {
        "Level": "Expert",
        "Nr": 10086,
        "parameter description": "Restart voltage level after a battery overvoltage",
        "Unit": "Vdc",
        "Default": 64.8,
        "Min": 37.9,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10038: {
        "Level": "Expert",
        "Nr": 10038,
        "parameter description": "SYSTEM",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10060: {
        "Level": "Expert",
        "Nr": 10060,
        "parameter description": "Check Earthing",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:No control 2:Neg bat pole earth 4:Pos bat pole earth 8:Floating battery"
    },
    10087: {
        "Level": "Inst.",
        "Nr": 10087,
        "parameter description": "Disabling of the display button",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10312: {
        "Level": "Expert",
        "Nr": 10312,
        "parameter description": "Remote entry (Remote ON/OFF)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10313: {
        "Level": "Expert",
        "Nr": 10313,
        "parameter description": "Remote entry active",
        "Unit": "",
        "Default": 2,
        "Min": 1,
        "Max": 4,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Closed 2:Open 4:Edge"
    },
    10314: {
        "Level": "Expert",
        "Nr": 10314,
        "parameter description": "ON/OFF command",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10315: {
        "Level": "Expert",
        "Nr": 10315,
        "parameter description": "Activated by AUX1 state",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10316: {
        "Level": "Expert",
        "Nr": 10316,
        "parameter description": "Start equalization",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10317: {
        "Level": "Expert",
        "Nr": 10317,
        "parameter description": "Send a message when remote entry changes state",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10075: {
        "Level": "Expert",
        "Nr": 10075,
        "parameter description": "Type of MPP tracking",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 4,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:P&O 2:OC ratio 4:Upv fixed"
    },
    10053: {
        "Level": "Expert",
        "Nr": 10053,
        "parameter description": "Open circuit ratio -> MPP",
        "Unit": "%",
        "Default": 80,
        "Min": 1,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10103: {
        "Level": "Expert",
        "Nr": 10103,
        "parameter description": "PV voltage fixed -> MPP",
        "Unit": "Vdc",
        "Default": 70,
        "Min": 0,
        "Max": 145,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10335: {
        "Level": "QSP",
        "Nr": 10335,
        "parameter description": "Partial shading check",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10336: {
        "Level": "QSP",
        "Nr": 10336,
        "parameter description": "Time between checks",
        "Unit": "min",
        "Default": 5,
        "Min": 1,
        "Max": 30,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10342: {
        "Level": "Inst.",
        "Nr": 10342,
        "parameter description": "VarioTrack watchdog enabled (SCOM)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10343: {
        "Level": "Inst.",
        "Nr": 10343,
        "parameter description": "VarioTrack watchdog delay (SCOM)",
        "Unit": "sec",
        "Default": 60,
        "Min": 10,
        "Max": 300,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    10200: {
        "Level": "Expert",
        "Nr": 10200,
        "parameter description": "Reset PV energy meter",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10201: {
        "Level": "QSP",
        "Nr": 10201,
        "parameter description": "Reset total produced PV energy meter",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10043: {
        "Level": "Expert",
        "Nr": 10043,
        "parameter description": "Reset daily solar production meters",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10044: {
        "Level": "Expert",
        "Nr": 10044,
        "parameter description": "Reset daily min-max",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10058: {
        "Level": "Inst.",
        "Nr": 10058,
        "parameter description": "Parameters saved in flash memory",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10039: {
        "Level": "Expert",
        "Nr": 10039,
        "parameter description": "ON of the VarioTrack",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10040: {
        "Level": "Expert",
        "Nr": 10040,
        "parameter description": "OFF of the VarioTrack",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10051: {
        "Level": "Expert",
        "Nr": 10051,
        "parameter description": "Reset of all VarioTrack",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10088: {
        "Level": "Expert",
        "Nr": 10088,
        "parameter description": "AUXILIARY CONTACT 1",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10089: {
        "Level": "Expert",
        "Nr": 10089,
        "parameter description": "Operating mode (AUX 1)",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Automatic 2:Reversed automatic 4:Manual ON 8:Manual OFF"
    },
    10090: {
        "Level": "Expert",
        "Nr": 10090,
        "parameter description": "Combination of the events for the auxiliary contact (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 0:Any (Function OR) 1:All (Function AND)"
    },
    10092: {
        "Level": "Expert",
        "Nr": 10092,
        "parameter description": "Contact activated in night mode (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10093: {
        "Level": "Expert",
        "Nr": 10093,
        "parameter description": "Activated in night mode (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10094: {
        "Level": "Expert",
        "Nr": 10094,
        "parameter description": "Delay of activation after entering night mode (AUX 1)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10095: {
        "Level": "Expert",
        "Nr": 10095,
        "parameter description": "Activation time for the auxiliary relay in night mode (AUX 1)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10318: {
        "Level": "Expert",
        "Nr": 10318,
        "parameter description": "Contact active with a fixed time schedule (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10319: {
        "Level": "Expert",
        "Nr": 10319,
        "parameter description": "Contact activated with fixed time schedule (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10320: {
        "Level": "Expert",
        "Nr": 10320,
        "parameter description": "Start hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    10321: {
        "Level": "Expert",
        "Nr": 10321,
        "parameter description": "End hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    10096: {
        "Level": "Expert",
        "Nr": 10096,
        "parameter description": "Contact active on event (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10198: {
        "Level": "Expert",
        "Nr": 10198,
        "parameter description": "VarioTrack is ON (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10091: {
        "Level": "Expert",
        "Nr": 10091,
        "parameter description": "VarioTrack is OFF (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10308: {
        "Level": "Expert",
        "Nr": 10308,
        "parameter description": "Remote entry (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10097: {
        "Level": "Expert",
        "Nr": 10097,
        "parameter description": "Battery undervoltage (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10098: {
        "Level": "Expert",
        "Nr": 10098,
        "parameter description": "Battery overvoltage (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10099: {
        "Level": "Expert",
        "Nr": 10099,
        "parameter description": "Earth fault (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10100: {
        "Level": "Expert",
        "Nr": 10100,
        "parameter description": "PV error (48h without charge) (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10102: {
        "Level": "Expert",
        "Nr": 10102,
        "parameter description": "Overtemperature (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10104: {
        "Level": "Expert",
        "Nr": 10104,
        "parameter description": "Bulk charge phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10105: {
        "Level": "Expert",
        "Nr": 10105,
        "parameter description": "Absorption phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10106: {
        "Level": "Expert",
        "Nr": 10106,
        "parameter description": "Equalization phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10107: {
        "Level": "Expert",
        "Nr": 10107,
        "parameter description": "Floating (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10108: {
        "Level": "Expert",
        "Nr": 10108,
        "parameter description": "Reduced floating (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10109: {
        "Level": "Expert",
        "Nr": 10109,
        "parameter description": "Periodic absorption (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10110: {
        "Level": "Expert",
        "Nr": 10110,
        "parameter description": "Contact active according to battery voltage (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10111: {
        "Level": "Expert",
        "Nr": 10111,
        "parameter description": "Battery voltage 1 activate (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10112: {
        "Level": "Expert",
        "Nr": 10112,
        "parameter description": "Battery voltage 1 (AUX 1)",
        "Unit": "Vdc",
        "Default": 46.8,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10113: {
        "Level": "Expert",
        "Nr": 10113,
        "parameter description": "Delay 1 (AUX 1)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10114: {
        "Level": "Expert",
        "Nr": 10114,
        "parameter description": "Battery voltage 2 activate (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10115: {
        "Level": "Expert",
        "Nr": 10115,
        "parameter description": "Battery voltage 2 (AUX 1)",
        "Unit": "Vdc",
        "Default": 47.8,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10116: {
        "Level": "Expert",
        "Nr": 10116,
        "parameter description": "Delay 2 (AUX 1)",
        "Unit": "min",
        "Default": 10,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10117: {
        "Level": "Expert",
        "Nr": 10117,
        "parameter description": "Battery voltage 3 activate (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10118: {
        "Level": "Expert",
        "Nr": 10118,
        "parameter description": "Battery voltage 3 (AUX 1)",
        "Unit": "Vdc",
        "Default": 48.5,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10119: {
        "Level": "Expert",
        "Nr": 10119,
        "parameter description": "Delay 3 (AUX 1)",
        "Unit": "min",
        "Default": 60,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10120: {
        "Level": "Expert",
        "Nr": 10120,
        "parameter description": "Battery voltage to deactivate (AUX 1)",
        "Unit": "Vdc",
        "Default": 54,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10121: {
        "Level": "Expert",
        "Nr": 10121,
        "parameter description": "Delay to deactivate (AUX 1)",
        "Unit": "min",
        "Default": 60,
        "Min": 0,
        "Max": 480,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10122: {
        "Level": "Expert",
        "Nr": 10122,
        "parameter description": "Deactivate if battery in floating phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10123: {
        "Level": "Expert",
        "Nr": 10123,
        "parameter description": "Contact active according to battery temperature (AUX 1) With BSP or BTS",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10124: {
        "Level": "Expert",
        "Nr": 10124,
        "parameter description": "Contact activated with the temperature of battery (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10125: {
        "Level": "Expert",
        "Nr": 10125,
        "parameter description": "Contact activated over (AUX 1)",
        "Unit": "°C",
        "Default": 3,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10126: {
        "Level": "Expert",
        "Nr": 10126,
        "parameter description": "Contact deactivated below (AUX 1)",
        "Unit": "°C",
        "Default": 5,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10127: {
        "Level": "Expert",
        "Nr": 10127,
        "parameter description": "Only activated if the battery is not in bulk phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10128: {
        "Level": "Expert",
        "Nr": 10128,
        "parameter description": "Contact active according to SOC (AUX 1) Only with BSP",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10129: {
        "Level": "Expert",
        "Nr": 10129,
        "parameter description": "Contact activated with the SOC 1 of battery (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10130: {
        "Level": "Expert",
        "Nr": 10130,
        "parameter description": "Contact activated below SOC 1 (AUX 1)",
        "Unit": "% SOC",
        "Default": 50,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10131: {
        "Level": "Expert",
        "Nr": 10131,
        "parameter description": "Delay 1 (AUX 1)",
        "Unit": "hours",
        "Default": 12,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10132: {
        "Level": "Expert",
        "Nr": 10132,
        "parameter description": "Contact activated with the SOC 2 of battery (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10133: {
        "Level": "Expert",
        "Nr": 10133,
        "parameter description": "Contact activated below SOC 2 (AUX 1)",
        "Unit": "%",
        "Default": 30,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10134: {
        "Level": "Expert",
        "Nr": 10134,
        "parameter description": "Delay 2 (AUX 1)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10135: {
        "Level": "Expert",
        "Nr": 10135,
        "parameter description": "Contact activated with the SOC 3 of battery (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10136: {
        "Level": "Expert",
        "Nr": 10136,
        "parameter description": "Contact activated below SOC 3 (AUX 1)",
        "Unit": "%",
        "Default": 20,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10137: {
        "Level": "Expert",
        "Nr": 10137,
        "parameter description": "Delay 3 (AUX 1)",
        "Unit": "hours",
        "Default": 0,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10138: {
        "Level": "Expert",
        "Nr": 10138,
        "parameter description": "Contact deactivated over SOC (AUX 1)",
        "Unit": "% SOC",
        "Default": 90,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10139: {
        "Level": "Expert",
        "Nr": 10139,
        "parameter description": "Delay to deactivate (AUX 1)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 10,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10140: {
        "Level": "Expert",
        "Nr": 10140,
        "parameter description": "Deactivate if battery in floating phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10141: {
        "Level": "Expert",
        "Nr": 10141,
        "parameter description": "Reset all settings (AUX 1)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10142: {
        "Level": "Expert",
        "Nr": 10142,
        "parameter description": "AUXILIARY CONTACT 2",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10143: {
        "Level": "Expert",
        "Nr": 10143,
        "parameter description": "Operating mode (AUX 2)",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Automatic 2:Reversed automatic 4:Manual ON 8:Manual OFF"
    },
    10144: {
        "Level": "Expert",
        "Nr": 10144,
        "parameter description": "Combination of the events for the auxiliary contact (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 0:Any (Function OR) 1:All (Function AND)"
    },
    10146: {
        "Level": "Expert",
        "Nr": 10146,
        "parameter description": "Contact activated in night mode (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10147: {
        "Level": "Expert",
        "Nr": 10147,
        "parameter description": "Activated in night mode (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10148: {
        "Level": "Expert",
        "Nr": 10148,
        "parameter description": "Delay of activation after entering night mode (AUX 2)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10149: {
        "Level": "Expert",
        "Nr": 10149,
        "parameter description": "Activation time for the auxiliary relay in night mode (AUX 2)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10322: {
        "Level": "Expert",
        "Nr": 10322,
        "parameter description": "Contact active with a fixed time schedule (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10323: {
        "Level": "Expert",
        "Nr": 10323,
        "parameter description": "Contact activated with fixed time schedule (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10324: {
        "Level": "Expert",
        "Nr": 10324,
        "parameter description": "Start hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    10325: {
        "Level": "Expert",
        "Nr": 10325,
        "parameter description": "End hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    10150: {
        "Level": "Expert",
        "Nr": 10150,
        "parameter description": "Contact active on event (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10199: {
        "Level": "Expert",
        "Nr": 10199,
        "parameter description": "VarioTrack is ON (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10145: {
        "Level": "Expert",
        "Nr": 10145,
        "parameter description": "VarioTrack is OFF (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10309: {
        "Level": "Expert",
        "Nr": 10309,
        "parameter description": "Remote entry (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10151: {
        "Level": "Expert",
        "Nr": 10151,
        "parameter description": "Battery undervoltage (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10152: {
        "Level": "Expert",
        "Nr": 10152,
        "parameter description": "Battery overvoltage (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10153: {
        "Level": "Expert",
        "Nr": 10153,
        "parameter description": "Earth fault (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10154: {
        "Level": "Expert",
        "Nr": 10154,
        "parameter description": "PV error (48h without charge) (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10156: {
        "Level": "Expert",
        "Nr": 10156,
        "parameter description": "Overtemperature (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10158: {
        "Level": "Expert",
        "Nr": 10158,
        "parameter description": "Bulk charge phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10159: {
        "Level": "Expert",
        "Nr": 10159,
        "parameter description": "Absorption phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10160: {
        "Level": "Expert",
        "Nr": 10160,
        "parameter description": "Equalization phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10161: {
        "Level": "Expert",
        "Nr": 10161,
        "parameter description": "Floating (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10162: {
        "Level": "Expert",
        "Nr": 10162,
        "parameter description": "Reduced floating (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10163: {
        "Level": "Expert",
        "Nr": 10163,
        "parameter description": "Periodic absorption (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10164: {
        "Level": "Expert",
        "Nr": 10164,
        "parameter description": "Contact active according to battery voltage (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10165: {
        "Level": "Expert",
        "Nr": 10165,
        "parameter description": "Battery voltage 1 activate (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10166: {
        "Level": "Expert",
        "Nr": 10166,
        "parameter description": "Battery voltage 1 (AUX 2)",
        "Unit": "Vdc",
        "Default": 46.8,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10167: {
        "Level": "Expert",
        "Nr": 10167,
        "parameter description": "Delay 1 (AUX 2)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10168: {
        "Level": "Expert",
        "Nr": 10168,
        "parameter description": "Battery voltage 2 activate (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10169: {
        "Level": "Expert",
        "Nr": 10169,
        "parameter description": "Battery voltage 2 (AUX 2)",
        "Unit": "Vdc",
        "Default": 47.8,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10170: {
        "Level": "Expert",
        "Nr": 10170,
        "parameter description": "Delay 2 (AUX 2)",
        "Unit": "min",
        "Default": 10,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10171: {
        "Level": "Expert",
        "Nr": 10171,
        "parameter description": "Battery voltage 3 activate (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10172: {
        "Level": "Expert",
        "Nr": 10172,
        "parameter description": "Battery voltage 3 (AUX 2)",
        "Unit": "Vdc",
        "Default": 48.5,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10173: {
        "Level": "Expert",
        "Nr": 10173,
        "parameter description": "Delay 3 (AUX 2)",
        "Unit": "min",
        "Default": 60,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10174: {
        "Level": "Expert",
        "Nr": 10174,
        "parameter description": "Battery voltage to deactivate (AUX 2)",
        "Unit": "Vdc",
        "Default": 54,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10175: {
        "Level": "Expert",
        "Nr": 10175,
        "parameter description": "Delay to deactivate (AUX 2)",
        "Unit": "min",
        "Default": 60,
        "Min": 0,
        "Max": 480,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10176: {
        "Level": "Expert",
        "Nr": 10176,
        "parameter description": "Deactivate if battery in floating phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10177: {
        "Level": "Expert",
        "Nr": 10177,
        "parameter description": "Contact active according to battery temperature (AUX 2) With BSP or BTS",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10178: {
        "Level": "Expert",
        "Nr": 10178,
        "parameter description": "Contact activated with the temperature of battery (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10179: {
        "Level": "Expert",
        "Nr": 10179,
        "parameter description": "Contact activated over (AUX 2)",
        "Unit": "°C",
        "Default": 3,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10180: {
        "Level": "Expert",
        "Nr": 10180,
        "parameter description": "Contact deactivated below (AUX 2)",
        "Unit": "°C",
        "Default": 5,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10181: {
        "Level": "Expert",
        "Nr": 10181,
        "parameter description": "Only activated if the battery is not in bulk phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10182: {
        "Level": "Expert",
        "Nr": 10182,
        "parameter description": "Contact active according to SOC (AUX 2) Only with BSP",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10183: {
        "Level": "Expert",
        "Nr": 10183,
        "parameter description": "Contact activated with the SOC 1 of battery (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10184: {
        "Level": "Expert",
        "Nr": 10184,
        "parameter description": "Contact activated below SOC 1 (AUX 2)",
        "Unit": "% SOC",
        "Default": 50,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10185: {
        "Level": "Expert",
        "Nr": 10185,
        "parameter description": "Delay 1 (AUX 2)",
        "Unit": "hours",
        "Default": 12,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10186: {
        "Level": "Expert",
        "Nr": 10186,
        "parameter description": "Contact activated with the SOC 2 of battery (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10187: {
        "Level": "Expert",
        "Nr": 10187,
        "parameter description": "Contact activated below SOC 2 (AUX 2)",
        "Unit": "%",
        "Default": 30,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10188: {
        "Level": "Expert",
        "Nr": 10188,
        "parameter description": "Delay 2 (AUX 2)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10189: {
        "Level": "Expert",
        "Nr": 10189,
        "parameter description": "Contact activated with the SOC 3 of battery (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10190: {
        "Level": "Expert",
        "Nr": 10190,
        "parameter description": "Contact activated below SOC 3 (AUX 2)",
        "Unit": "%",
        "Default": 20,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10191: {
        "Level": "Expert",
        "Nr": 10191,
        "parameter description": "Delay 3 (AUX 2)",
        "Unit": "hours",
        "Default": 0,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10192: {
        "Level": "Expert",
        "Nr": 10192,
        "parameter description": "Contact deactivated over SOC (AUX 2)",
        "Unit": "% SOC",
        "Default": 90,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10193: {
        "Level": "Expert",
        "Nr": 10193,
        "parameter description": "Delay to deactivate (AUX 2)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 10,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10194: {
        "Level": "Expert",
        "Nr": 10194,
        "parameter description": "Deactivate if battery in floating phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10195: {
        "Level": "Expert",
        "Nr": 10195,
        "parameter description": "Reset all settings (AUX 2)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10202: {
        "Level": "Expert",
        "Nr": 10202,
        "parameter description": "AUXILIARY CONTACT 3",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10203: {
        "Level": "Expert",
        "Nr": 10203,
        "parameter description": "Operating mode (AUX 3)",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Automatic 2:Reversed automatic 4:Manual ON 8:Manual OFF"
    },
    10204: {
        "Level": "Expert",
        "Nr": 10204,
        "parameter description": "Combination of the events for the auxiliary contact (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 0:Any (Function OR) 1:All (Function AND)"
    },
    10205: {
        "Level": "Expert",
        "Nr": 10205,
        "parameter description": "Contact activated in night mode (AUX 3)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10206: {
        "Level": "Expert",
        "Nr": 10206,
        "parameter description": "Activated in night mode (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10207: {
        "Level": "Expert",
        "Nr": 10207,
        "parameter description": "Delay of activation after entering night mode (AUX 3)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10208: {
        "Level": "Expert",
        "Nr": 10208,
        "parameter description": "Activation time for the auxiliary relay in night mode (AUX 3)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10326: {
        "Level": "Expert",
        "Nr": 10326,
        "parameter description": "Contact active with a fixed time schedule (AUX 3)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10327: {
        "Level": "Expert",
        "Nr": 10327,
        "parameter description": "Contact activated with fixed time schedule (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10328: {
        "Level": "Expert",
        "Nr": 10328,
        "parameter description": "Start hour (AUX 3)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    10329: {
        "Level": "Expert",
        "Nr": 10329,
        "parameter description": "End hour (AUX 3)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    10209: {
        "Level": "Expert",
        "Nr": 10209,
        "parameter description": "Contact active on event (AUX 3)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10210: {
        "Level": "Expert",
        "Nr": 10210,
        "parameter description": "VarioTrack is ON (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10211: {
        "Level": "Expert",
        "Nr": 10211,
        "parameter description": "VarioTrack is OFF (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10310: {
        "Level": "Expert",
        "Nr": 10310,
        "parameter description": "Remote entry (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10212: {
        "Level": "Expert",
        "Nr": 10212,
        "parameter description": "Battery undervoltage (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10213: {
        "Level": "Expert",
        "Nr": 10213,
        "parameter description": "Battery overvoltage (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10214: {
        "Level": "Expert",
        "Nr": 10214,
        "parameter description": "Earth fault (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10215: {
        "Level": "Expert",
        "Nr": 10215,
        "parameter description": "PV error (48h without charge) (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10216: {
        "Level": "Expert",
        "Nr": 10216,
        "parameter description": "Overtemperature (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10217: {
        "Level": "Expert",
        "Nr": 10217,
        "parameter description": "Bulk charge phase (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10218: {
        "Level": "Expert",
        "Nr": 10218,
        "parameter description": "Absorption phase (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10219: {
        "Level": "Expert",
        "Nr": 10219,
        "parameter description": "Equalization phase (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10220: {
        "Level": "Expert",
        "Nr": 10220,
        "parameter description": "Floating (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10221: {
        "Level": "Expert",
        "Nr": 10221,
        "parameter description": "Reduced floating (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10222: {
        "Level": "Expert",
        "Nr": 10222,
        "parameter description": "Periodic absorption (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10223: {
        "Level": "Expert",
        "Nr": 10223,
        "parameter description": "Contact active according to battery voltage (AUX 3)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10224: {
        "Level": "Expert",
        "Nr": 10224,
        "parameter description": "Battery voltage 1 activate (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10225: {
        "Level": "Expert",
        "Nr": 10225,
        "parameter description": "Battery voltage 1 (AUX 3)",
        "Unit": "Vdc",
        "Default": 46.8,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10226: {
        "Level": "Expert",
        "Nr": 10226,
        "parameter description": "Delay 1 (AUX 3)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10227: {
        "Level": "Expert",
        "Nr": 10227,
        "parameter description": "Battery voltage 2 activate (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10228: {
        "Level": "Expert",
        "Nr": 10228,
        "parameter description": "Battery voltage 2 (AUX 3)",
        "Unit": "Vdc",
        "Default": 47.8,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10229: {
        "Level": "Expert",
        "Nr": 10229,
        "parameter description": "Delay 2 (AUX 3)",
        "Unit": "min",
        "Default": 10,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10230: {
        "Level": "Expert",
        "Nr": 10230,
        "parameter description": "Battery voltage 3 activate (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10231: {
        "Level": "Expert",
        "Nr": 10231,
        "parameter description": "Battery voltage 3 (AUX 3)",
        "Unit": "Vdc",
        "Default": 48.5,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10232: {
        "Level": "Expert",
        "Nr": 10232,
        "parameter description": "Delay 3 (AUX 3)",
        "Unit": "min",
        "Default": 60,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10233: {
        "Level": "Expert",
        "Nr": 10233,
        "parameter description": "Battery voltage to deactivate (AUX 3)",
        "Unit": "Vdc",
        "Default": 54,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10234: {
        "Level": "Expert",
        "Nr": 10234,
        "parameter description": "Delay to deactivate (AUX 3)",
        "Unit": "min",
        "Default": 60,
        "Min": 0,
        "Max": 480,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10235: {
        "Level": "Expert",
        "Nr": 10235,
        "parameter description": "Deactivate if battery in floating phase (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10236: {
        "Level": "Expert",
        "Nr": 10236,
        "parameter description": "Contact active according to battery temperature (AUX 3) With BSP or BTS",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10237: {
        "Level": "Expert",
        "Nr": 10237,
        "parameter description": "Contact activated with the temperature of battery (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10238: {
        "Level": "Expert",
        "Nr": 10238,
        "parameter description": "Contact activated over (AUX 3)",
        "Unit": "°C",
        "Default": 3,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10239: {
        "Level": "Expert",
        "Nr": 10239,
        "parameter description": "Contact deactivated below (AUX 3)",
        "Unit": "°C",
        "Default": 5,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10240: {
        "Level": "Expert",
        "Nr": 10240,
        "parameter description": "Only activated if the battery is not in bulk phase (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10241: {
        "Level": "Expert",
        "Nr": 10241,
        "parameter description": "Contact active according to SOC (AUX 3) Only with BSP",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10242: {
        "Level": "Expert",
        "Nr": 10242,
        "parameter description": "Contact activated with the SOC 1 of battery (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10243: {
        "Level": "Expert",
        "Nr": 10243,
        "parameter description": "Contact activated below SOC 1 (AUX 3)",
        "Unit": "% SOC",
        "Default": 50,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10244: {
        "Level": "Expert",
        "Nr": 10244,
        "parameter description": "Delay 1 (AUX 3)",
        "Unit": "hours",
        "Default": 12,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10245: {
        "Level": "Expert",
        "Nr": 10245,
        "parameter description": "Contact activated with the SOC 2 of battery (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10246: {
        "Level": "Expert",
        "Nr": 10246,
        "parameter description": "Contact activated below SOC 2 (AUX 3)",
        "Unit": "%",
        "Default": 30,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10247: {
        "Level": "Expert",
        "Nr": 10247,
        "parameter description": "Delay 2 (AUX 3)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10248: {
        "Level": "Expert",
        "Nr": 10248,
        "parameter description": "Contact activated with the SOC 3 of battery (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10249: {
        "Level": "Expert",
        "Nr": 10249,
        "parameter description": "Contact activated below SOC 3 (AUX 3)",
        "Unit": "%",
        "Default": 20,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10250: {
        "Level": "Expert",
        "Nr": 10250,
        "parameter description": "Delay 3 (AUX 3)",
        "Unit": "hours",
        "Default": 0,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10251: {
        "Level": "Expert",
        "Nr": 10251,
        "parameter description": "Contact deactivated over SOC (AUX 3)",
        "Unit": "% SOC",
        "Default": 90,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10252: {
        "Level": "Expert",
        "Nr": 10252,
        "parameter description": "Delay to deactivate (AUX 3)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 10,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10253: {
        "Level": "Expert",
        "Nr": 10253,
        "parameter description": "Deactivate if battery in floating phase (AUX 3)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10254: {
        "Level": "Expert",
        "Nr": 10254,
        "parameter description": "Reset all settings (AUX 3)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    10255: {
        "Level": "Expert",
        "Nr": 10255,
        "parameter description": "AUXILIARY CONTACT 4",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10256: {
        "Level": "Expert",
        "Nr": 10256,
        "parameter description": "Operating mode (AUX 4)",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Automatic 2:Reversed automatic 4:Manual ON 8:Manual OFF"
    },
    10257: {
        "Level": "Expert",
        "Nr": 10257,
        "parameter description": "Combination of the events for the auxiliary contact (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 0:Any (Function OR) 1:All (Function AND)"
    },
    10258: {
        "Level": "Expert",
        "Nr": 10258,
        "parameter description": "Contact activated in night mode (AUX 4)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10259: {
        "Level": "Expert",
        "Nr": 10259,
        "parameter description": "Activated in night mode (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10260: {
        "Level": "Expert",
        "Nr": 10260,
        "parameter description": "Delay of activation after entering night mode (AUX 4)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10261: {
        "Level": "Expert",
        "Nr": 10261,
        "parameter description": "Activation time for the auxiliary relay in night mode (AUX 4)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10330: {
        "Level": "Expert",
        "Nr": 10330,
        "parameter description": "Contact active with a fixed time schedule (AUX 4)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10331: {
        "Level": "Expert",
        "Nr": 10331,
        "parameter description": "Contact activated with fixed time schedule (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10332: {
        "Level": "Expert",
        "Nr": 10332,
        "parameter description": "Start hour (AUX 4)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    10333: {
        "Level": "Expert",
        "Nr": 10333,
        "parameter description": "End hour (AUX 4)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    10262: {
        "Level": "Expert",
        "Nr": 10262,
        "parameter description": "Contact active on event (AUX 4)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10263: {
        "Level": "Expert",
        "Nr": 10263,
        "parameter description": "VarioTrack is ON (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10264: {
        "Level": "Expert",
        "Nr": 10264,
        "parameter description": "VarioTrack is OFF (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10311: {
        "Level": "Expert",
        "Nr": 10311,
        "parameter description": "Remote entry (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10265: {
        "Level": "Expert",
        "Nr": 10265,
        "parameter description": "Battery undervoltage (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10266: {
        "Level": "Expert",
        "Nr": 10266,
        "parameter description": "Battery overvoltage (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10267: {
        "Level": "Expert",
        "Nr": 10267,
        "parameter description": "Earth fault (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10268: {
        "Level": "Expert",
        "Nr": 10268,
        "parameter description": "PV error (48h without charge) (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10269: {
        "Level": "Expert",
        "Nr": 10269,
        "parameter description": "Overtemperature (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10270: {
        "Level": "Expert",
        "Nr": 10270,
        "parameter description": "Bulk charge phase (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10271: {
        "Level": "Expert",
        "Nr": 10271,
        "parameter description": "Absorption phase (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10272: {
        "Level": "Expert",
        "Nr": 10272,
        "parameter description": "Equalization phase (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10273: {
        "Level": "Expert",
        "Nr": 10273,
        "parameter description": "Floating (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10274: {
        "Level": "Expert",
        "Nr": 10274,
        "parameter description": "Reduced floating (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10275: {
        "Level": "Expert",
        "Nr": 10275,
        "parameter description": "Periodic absorption (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10276: {
        "Level": "Expert",
        "Nr": 10276,
        "parameter description": "Contact active according to battery voltage (AUX 4)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10277: {
        "Level": "Expert",
        "Nr": 10277,
        "parameter description": "Battery voltage 1 activate (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10278: {
        "Level": "Expert",
        "Nr": 10278,
        "parameter description": "Battery voltage 1 (AUX 4)",
        "Unit": "Vdc",
        "Default": 46.8,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10279: {
        "Level": "Expert",
        "Nr": 10279,
        "parameter description": "Delay 1 (AUX 4)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10280: {
        "Level": "Expert",
        "Nr": 10280,
        "parameter description": "Battery voltage 2 activate (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10281: {
        "Level": "Expert",
        "Nr": 10281,
        "parameter description": "Battery voltage 2 (AUX 4)",
        "Unit": "Vdc",
        "Default": 47.8,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10282: {
        "Level": "Expert",
        "Nr": 10282,
        "parameter description": "Delay 2 (AUX 4)",
        "Unit": "min",
        "Default": 10,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10283: {
        "Level": "Expert",
        "Nr": 10283,
        "parameter description": "Battery voltage 3 activate (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10284: {
        "Level": "Expert",
        "Nr": 10284,
        "parameter description": "Battery voltage 3 (AUX 4)",
        "Unit": "Vdc",
        "Default": 48.5,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10285: {
        "Level": "Expert",
        "Nr": 10285,
        "parameter description": "Delay 3 (AUX 4)",
        "Unit": "min",
        "Default": 60,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10286: {
        "Level": "Expert",
        "Nr": 10286,
        "parameter description": "Battery voltage to deactivate (AUX 4)",
        "Unit": "Vdc",
        "Default": 54,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    10287: {
        "Level": "Expert",
        "Nr": 10287,
        "parameter description": "Delay to deactivate (AUX 4)",
        "Unit": "min",
        "Default": 60,
        "Min": 0,
        "Max": 480,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10288: {
        "Level": "Expert",
        "Nr": 10288,
        "parameter description": "Deactivate if battery in floating phase (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10289: {
        "Level": "Expert",
        "Nr": 10289,
        "parameter description": "Contact active according to battery temperature (AUX 4) With BSP or BTS",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10290: {
        "Level": "Expert",
        "Nr": 10290,
        "parameter description": "Contact activated with the temperature of battery (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10291: {
        "Level": "Expert",
        "Nr": 10291,
        "parameter description": "Contact activated over (AUX 4)",
        "Unit": "°C",
        "Default": 3,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10292: {
        "Level": "Expert",
        "Nr": 10292,
        "parameter description": "Contact deactivated below (AUX 4)",
        "Unit": "°C",
        "Default": 5,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    10293: {
        "Level": "Expert",
        "Nr": 10293,
        "parameter description": "Only activated if the battery is not in bulk phase (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10294: {
        "Level": "Expert",
        "Nr": 10294,
        "parameter description": "Contact active according to SOC (AUX 4) Only with BSP",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    10295: {
        "Level": "Expert",
        "Nr": 10295,
        "parameter description": "Contact activated with the SOC 1 of battery (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10296: {
        "Level": "Expert",
        "Nr": 10296,
        "parameter description": "Contact activated below SOC 1 (AUX 4)",
        "Unit": "% SOC",
        "Default": 50,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10297: {
        "Level": "Expert",
        "Nr": 10297,
        "parameter description": "Delay 1 (AUX 4)",
        "Unit": "hours",
        "Default": 12,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10298: {
        "Level": "Expert",
        "Nr": 10298,
        "parameter description": "Contact activated with the SOC 2 of battery (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10299: {
        "Level": "Expert",
        "Nr": 10299,
        "parameter description": "Contact activated below SOC 2 (AUX 4)",
        "Unit": "%",
        "Default": 30,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10300: {
        "Level": "Expert",
        "Nr": 10300,
        "parameter description": "Delay 2 (AUX 4)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10301: {
        "Level": "Expert",
        "Nr": 10301,
        "parameter description": "Contact activated with the SOC 3 of battery (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10302: {
        "Level": "Expert",
        "Nr": 10302,
        "parameter description": "Contact activated below SOC 3 (AUX 4)",
        "Unit": "%",
        "Default": 20,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10303: {
        "Level": "Expert",
        "Nr": 10303,
        "parameter description": "Delay 3 (AUX 4)",
        "Unit": "hours",
        "Default": 0,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10304: {
        "Level": "Expert",
        "Nr": 10304,
        "parameter description": "Contact deactivated over SOC (AUX 4)",
        "Unit": "% SOC",
        "Default": 90,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    10305: {
        "Level": "Expert",
        "Nr": 10305,
        "parameter description": "Delay to deactivate (AUX 4)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 10,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    10306: {
        "Level": "Expert",
        "Nr": 10306,
        "parameter description": "Deactivate if battery in floating phase (AUX 4)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    10307: {
        "Level": "Expert",
        "Nr": 10307,
        "parameter description": "Reset all settings (AUX 4)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
}

# -------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------- 1.10 VarioTrack infos ---------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Contains 54 Infos
VARIO_TRACK_INFOS = {
    11000: {
        "Nr": 11000,
        "information description": "Battery voltage",
        "Short desc.": "Ubat",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11001: {
        "Nr": 11001,
        "information description": "Battery current",
        "Short desc.": "Ibat",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11002: {
        "Nr": 11002,
        "information description": "Voltage of the PV generator",
        "Short desc.": "Upv",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11003: {
        "Nr": 11003,
        "information description": "Current of the PV generator",
        "Short desc.": "Ipv",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11004: {
        "Nr": 11004,
        "information description": "Power of the PV generator",
        "Short desc.": "Psol",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11005: {
        "Nr": 11005,
        "information description": "Battery temperature",
        "Short desc.": "Tbat",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11006: {
        "Nr": 11006,
        "information description": "Production in (Ah) for the current day",
        "Short desc.": "Cd",
        "Unit on the RCC": "Ah",
        "Unit": "Ah",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11007: {
        "Nr": 11007,
        "information description": "Production in (kWh) for the current day",
        "Short desc.": "Ed",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11008: {
        "Nr": 11008,
        "information description": "Produced energy resettable counter",
        "Short desc.": "kWhR",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11009: {
        "Nr": 11009,
        "information description": "Total produced energy",
        "Short desc.": "MWhT",
        "Unit on the RCC": "MWh",
        "Unit": "MWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11010: {
        "Nr": 11010,
        "information description": "Production in (Ah) for the previous day",
        "Short desc.": "Cd-1",
        "Unit on the RCC": "Ah",
        "Unit": "Ah",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11011: {
        "Nr": 11011,
        "information description": "Production in (Wh) for the previous day",
        "Short desc.": "Ed-1",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11012: {
        "Nr": 11012,
        "information description": "Number of parameters (in code)",
        "Short desc.": "pCod",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11013: {
        "Nr": 11013,
        "information description": "Number of parameters (in flash)",
        "Short desc.": "pFla",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11014: {
        "Nr": 11014,
        "information description": "Number of infos users",
        "Short desc.": "iCod",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11015: {
        "Nr": 11015,
        "information description": "Model of VarioTrack",
        "Short desc.": "Type",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:VT-80 1:VT-65 2:VT-40 3:VT-HV"
    },
    11016: {
        "Nr": 11016,
        "information description": "Operating mode",
        "Short desc.": "Mode",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Night "
                                            "1:StartUp "
                                            "2:--- "
                                            "3:Charger "
                                            "4:--- "
                                            "5:Security "
                                            "6:OFF "
                                            "7:--- "
                                            "8:Charge "
                                            "9:Charge V "
                                            "10:Charge I "
                                            "11:Charge T "
                                            "12:Ch. Ibsp "
                                            "See the VarioTrack user manual for a description of the modes. "
                                            "Mode 3: is available up to VT code version 1.5.8. "
                                            "Modes 8: to 11: are available from VT code version 1.5.10."
    },
    11017: {
        "Nr": 11017,
        "information description": "Max PV voltage for the current day",
        "Short desc.": "PVmx",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11018: {
        "Nr": 11018,
        "information description": "Max battery current of the current day",
        "Short desc.": "Ibmx",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11019: {
        "Nr": 11019,
        "information description": "Max power production for the current day",
        "Short desc.": "PVxP",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11020: {
        "Nr": 11020,
        "information description": "Max battery voltage for the current day",
        "Short desc.": "Bmax",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11021: {
        "Nr": 11021,
        "information description": "Min battery voltage for the current day",
        "Short desc.": "Bmin",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11025: {
        "Nr": 11025,
        "information description": "Number of irradiation hours for the current day",
        "Short desc.": "Sd",
        "Unit on the RCC": "h",
        "Unit": "h",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11026: {
        "Nr": 11026,
        "information description": "Number of irradiation hours for the previous day",
        "Short desc.": "Sd-1",
        "Unit on the RCC": "h",
        "Unit": "h",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11034: {
        "Nr": 11034,
        "information description": "Type of error",
        "Short desc.": "Err",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:No Error "
                                            "1:BatOverV "
                                            "2:Earth "
                                            "3:No Batt "
                                            "4:OverTemp "
                                            "5:BatOverV "
                                            "6:PvOverV "
                                            "7:Others "
                                            "8:--- "
                                            "9:--- "
                                            "10:--- "
                                            "11:--- "
                                            "12:HardErr "
                                            "See the VarioTrack user manual for a description of these errors"
    },
    11037: {
        "Nr": 11037,
        "information description": "Number of days before next equalization",
        "Short desc.": "EqIn",
        "Unit on the RCC": "days",
        "Unit": "days",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11038: {
        "Nr": 11038,
        "information description": "Battery cycle phase",
        "Short desc.": "Phas",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Bulk "
                                            "1:Absorpt. "
                                            "2:Equalize "
                                            "3:Floating "
                                            "4:--- "
                                            "5:--- "
                                            "6:R.float. "
                                            "7:Per.abs. "
                                            "8:--- "
                                            "9:--- "
                                            "10:--- "
                                            "11:---"
    },
    11039: {
        "Nr": 11039,
        "information description": "Battery voltage (minute avg)",
        "Short desc.": "UbaM",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11040: {
        "Nr": 11040,
        "information description": "Battery current (minute avg)",
        "Short desc.": "IbaM",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11041: {
        "Nr": 11041,
        "information description": "PV voltage (minute avg)",
        "Short desc.": "UpvM",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11043: {
        "Nr": 11043,
        "information description": "PV power (minute avg)",
        "Short desc.": "PsoM",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11044: {
        "Nr": 11044,
        "information description": "Battery temperature (minute avg)",
        "Short desc.": "TbaM",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11045: {
        "Nr": 11045,
        "information description": "Electronic temperature 1 (minute avg)",
        "Short desc.": "Dev1",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11046: {
        "Nr": 11046,
        "information description": "Electronic temperature 2 (minute avg)",
        "Short desc.": "Dev2",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11047: {
        "Nr": 11047,
        "information description": "ID type",
        "Short desc.": "Idt",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "VT65 and VT80 = 9079d (0x2601)"
    },
    11048: {
        "Nr": 11048,
        "information description": "ID batt voltage",
        "Short desc.": "Idv",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11049: {
        "Nr": 11049,
        "information description": "ID HW",
        "Short desc.": "HW",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11050: {
        "Nr": 11050,
        "information description": "ID SOFT msb",
        "Short desc.": "Smsb",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'Software version encoding'"
    },
    11051: {
        "Nr": 11051,
        "information description": "ID SOFT lsb",
        "Short desc.": "Slsb",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'Software version encoding'"
    },
    11052: {
        "Nr": 11052,
        "information description": "ID SID",
        "Short desc.": "SID",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11061: {
        "Nr": 11061,
        "information description": "State of auxiliary relay 1",
        "Short desc.": "Aux 1",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Opened 1:Closed"
    },
    11062: {
        "Nr": 11062,
        "information description": "State of auxiliary relay 2",
        "Short desc.": "Aux 2",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Opened 1:Closed"
    },
    11063: {
        "Nr": 11063,
        "information description": "Relay aux 1 mode",
        "Short desc.": "Aux 1",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:--- 1:A 2:I 3:M 4:M 5:G"
    },
    11064: {
        "Nr": 11064,
        "information description": "Relay aux 2 mode",
        "Short desc.": "Aux 2",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:--- 1:A 2:I 3:M 4:M 5:G"
    },
    11066: {
        "Nr": 11066,
        "information description": "Synchronisation state",
        "Short desc.": "Sync",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:--- "
                                            "1:---  "
                                            "2:--- "
                                            "3:--- "
                                            "4:XTslave "
                                            "5:VTslave "
                                            "6:--- "
                                            "7:--- "
                                            "8:VTmaster "
                                            "9:Autonom. "
                                            "10:VSslave "
                                            "11:VSmaster"
    },
    11067: {
        "Nr": 11067,
        "information description": "ID FID msb",
        "Short desc.": "",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'FID encoding'"
    },
    11068: {
        "Nr": 11068,
        "information description": "ID FID lsb",
        "Short desc.": "",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'FID encoding'"
    },
    11069: {
        "Nr": 11069,
        "information description": "State of the VarioTrack",
        "Short desc.": "VT state",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Off 1:On"
    },
    11076: {
        "Nr": 11076,
        "information description": "Local daily communication error counter (CAN)",
        "Short desc.": "locEr",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    11077: {
        "Nr": 11077,
        "information description": "State of auxiliary relay 3",
        "Short desc.": "Aux 3",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Opened 1:Closed"
    },
    11078: {
        "Nr": 11078,
        "information description": "State of auxiliary relay 4",
        "Short desc.": "Aux 4",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Opened 1:Closed"
    },
    11079: {
        "Nr": 11079,
        "information description": "Relay aux 3 mode",
        "Short desc.": "Aux 3",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:--- 1:A 2:I 3:M 4:M 5:G"
    },
    11080: {
        "Nr": 11080,
        "information description": "Relay aux 4 mode",
        "Short desc.": "Aux 4",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:--- 1:A 2:I 3:M 4:M 5:G"
    },
    11082: {
        "Nr": 11082,
        "information description": "Remote entry state",
        "Short desc.": "RME",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:RM EN 0 1:RM EN 1"
    },
}

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------- 1.11 VarioString parameters ------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Contains 199 Parameters
VARIO_STRING_PARAMETERS = {
    14000: {
        "Level": "Basic",
        "Nr": 14000,
        "parameter description": "BASIC SETTINGS",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14174: {
        "Level": "Expert",
        "Nr": 14174,
        "parameter description": "Block manual programming (dip-switch)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14001: {
        "Level": "Expert",
        "Nr": 14001,
        "parameter description": "Battery charge current (VS-120)",
        "Unit": "Adc",
        "Default": 120,
        "Min": 0,
        "Max": 120,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "2"
    },
    14217: {
        "Level": "Expert",
        "Nr": 14217,
        "parameter description": "Battery charge current (VS-70)",
        "Unit": "Adc",
        "Default": 70,
        "Min": 0,
        "Max": 70,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14002: {
        "Level": "Basic",
        "Nr": 14002,
        "parameter description": "Configuration of PV modules (VS-120)",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Automatic 2:Independent 4:Serial 8:Parallel"
    },
    14067: {
        "Level": "Basic",
        "Nr": 14067,
        "parameter description": "Restore default settings",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    14068: {
        "Level": "Inst.",
        "Nr": 14068,
        "parameter description": "Restore factory settings",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    14003: {
        "Level": "Expert",
        "Nr": 14003,
        "parameter description": "BATTERY MANAGEMENT AND CYCLE",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14036: {
        "Level": "Basic",
        "Nr": 14036,
        "parameter description": "Synchronisation battery cycle with Xtender",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14216: {
        "Level": "Expert",
        "Nr": 14216,
        "parameter description": "Battery undervoltage",
        "Unit": "Vdc",
        "Default": 40,
        "Min": 34,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14035: {
        "Level": "Expert",
        "Nr": 14035,
        "parameter description": "Temperature compensation",
        "Unit": "mV/°C/cell",
        "Default": -3,
        "Min": -8,
        "Max": 0,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14004: {
        "Level": "Expert",
        "Nr": 14004,
        "parameter description": "Floating phase",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14005: {
        "Level": "Expert",
        "Nr": 14005,
        "parameter description": "Floating voltage",
        "Unit": "Vdc",
        "Default": 54.4,
        "Min": 37.9,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14006: {
        "Level": "Expert",
        "Nr": 14006,
        "parameter description": "Force phase of floating",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    14007: {
        "Level": "Expert",
        "Nr": 14007,
        "parameter description": "Absorption phase",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14008: {
        "Level": "Expert",
        "Nr": 14008,
        "parameter description": "Absorption phase allowed",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14009: {
        "Level": "Expert",
        "Nr": 14009,
        "parameter description": "Absorption voltage",
        "Unit": "Vdc",
        "Default": 57.6,
        "Min": 37.9,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14010: {
        "Level": "Expert",
        "Nr": 14010,
        "parameter description": "Force absorption phase",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    14011: {
        "Level": "Expert",
        "Nr": 14011,
        "parameter description": "Absorption duration",
        "Unit": "min",
        "Default": 120,
        "Min": 5,
        "Max": 510,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    14012: {
        "Level": "Expert",
        "Nr": 14012,
        "parameter description": "End of absorption triggered by the current",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14013: {
        "Level": "Expert",
        "Nr": 14013,
        "parameter description": "Current threshold to end absorption phase",
        "Unit": "Adc",
        "Default": 10,
        "Min": 2,
        "Max": 120,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "2"
    },
    14016: {
        "Level": "Expert",
        "Nr": 14016,
        "parameter description": "Equalization phase",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14017: {
        "Level": "Expert",
        "Nr": 14017,
        "parameter description": "Equalization allowed",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14018: {
        "Level": "Expert",
        "Nr": 14018,
        "parameter description": "Force equalization",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    14021: {
        "Level": "Expert",
        "Nr": 14021,
        "parameter description": "Equalization voltage",
        "Unit": "Vdc",
        "Default": 62.4,
        "Min": 52.1,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14020: {
        "Level": "Expert",
        "Nr": 14020,
        "parameter description": "Equalization current",
        "Unit": "Adc",
        "Default": 80,
        "Min": 2,
        "Max": 120,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "2"
    },
    14022: {
        "Level": "Expert",
        "Nr": 14022,
        "parameter description": "Equalization duration",
        "Unit": "min",
        "Default": 30,
        "Min": 5,
        "Max": 510,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    14023: {
        "Level": "Expert",
        "Nr": 14023,
        "parameter description": "Equalization with fixed interval",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14024: {
        "Level": "Expert",
        "Nr": 14024,
        "parameter description": "Days between equalizations",
        "Unit": "days",
        "Default": 26,
        "Min": 1,
        "Max": 365,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14025: {
        "Level": "Expert",
        "Nr": 14025,
        "parameter description": "End of equalization triggered by the current",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14026: {
        "Level": "Expert",
        "Nr": 14026,
        "parameter description": "Current threshold to end equalization phase",
        "Unit": "Adc",
        "Default": 10,
        "Min": 4,
        "Max": 30,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14019: {
        "Level": "Expert",
        "Nr": 14019,
        "parameter description": "Equalization before absorption phase",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14027: {
        "Level": "Expert",
        "Nr": 14027,
        "parameter description": "New cycle",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14028: {
        "Level": "Expert",
        "Nr": 14028,
        "parameter description": "Force a new cycle",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    14029: {
        "Level": "Expert",
        "Nr": 14029,
        "parameter description": "Voltage level 1 to start a new cycle",
        "Unit": "Vdc",
        "Default": 48.8,
        "Min": 37.9,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14030: {
        "Level": "Expert",
        "Nr": 14030,
        "parameter description": "Time period under voltage level 1 to start a new cycle",
        "Unit": "min",
        "Default": 30,
        "Min": 0,
        "Max": 240,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14031: {
        "Level": "Expert",
        "Nr": 14031,
        "parameter description": "Voltage level 2 to start a new cycle",
        "Unit": "Vdc",
        "Default": 47.2,
        "Min": 37.9,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14032: {
        "Level": "Expert",
        "Nr": 14032,
        "parameter description": "Time period under voltage level 2 to start a new cycle",
        "Unit": "min",
        "Default": 2,
        "Min": 0,
        "Max": 240,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14033: {
        "Level": "Expert",
        "Nr": 14033,
        "parameter description": "Cycling restricted",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14034: {
        "Level": "Expert",
        "Nr": 14034,
        "parameter description": "Minimal delay between cycles",
        "Unit": "hours",
        "Default": 1,
        "Min": 0,
        "Max": 540,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14065: {
        "Level": "Expert",
        "Nr": 14065,
        "parameter description": "Battery overvoltage level",
        "Unit": "Vdc",
        "Default": 68.2,
        "Min": 37.9,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14066: {
        "Level": "Expert",
        "Nr": 14066,
        "parameter description": "Restart voltage level after a battery overvoltage",
        "Unit": "Vdc",
        "Default": 64.8,
        "Min": 37.9,
        "Max": 68.2,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14037: {
        "Level": "Expert",
        "Nr": 14037,
        "parameter description": "SYSTEM",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14040: {
        "Level": "Expert",
        "Nr": 14040,
        "parameter description": "Type of battery grounding",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:No control 2:Bat+ grounded 4:Bat- grounded 8:Bat floating"
    },
    14194: {
        "Level": "Expert",
        "Nr": 14194,
        "parameter description": "Configuration for VS-120",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14041: {
        "Level": "Expert",
        "Nr": 14041,
        "parameter description": "Type of PV grounding",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:No control 2:PV+ grounded 4:PV- grounded 8:PV floating"
    },
    14175: {
        "Level": "Expert",
        "Nr": 14175,
        "parameter description": "Type of PV1 grounding",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:No control 2:PV+ grounded 4:PV- grounded 8:PV floating"
    },
    14042: {
        "Level": "Expert",
        "Nr": 14042,
        "parameter description": "Type of PV2 grounding",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:No control 2:PV+ grounded 4:PV- grounded 8:PV floating"
    },
    14180: {
        "Level": "Expert",
        "Nr": 14180,
        "parameter description": "Type of MPPT algorithm",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14043: {
        "Level": "Expert",
        "Nr": 14043,
        "parameter description": "Type of MPP tracking algorithm PV",
        "Unit": "",
        "Default": 8,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:P&O 2:OC ratio 4:Upv fixed 8:LSF"
    },
    14044: {
        "Level": "Expert",
        "Nr": 14044,
        "parameter description": "PV voltage fixed (for PV in series)",
        "Unit": "Vdc",
        "Default": 700,
        "Min": 200,
        "Max": 900,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    14179: {
        "Level": "Expert",
        "Nr": 14179,
        "parameter description": "PV voltage fixed (for PV in //)",
        "Unit": "Vdc",
        "Default": 500,
        "Min": 100,
        "Max": 600,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    14045: {
        "Level": "Expert",
        "Nr": 14045,
        "parameter description": "Ratio of PV open circuit voltage",
        "Unit": "",
        "Default": 0.7,
        "Min": 0.5,
        "Max": 1,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.010009766"
    },
    14176: {
        "Level": "Expert",
        "Nr": 14176,
        "parameter description": "Type of MPP tracking algorithm PV1",
        "Unit": "",
        "Default": 8,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:P&O 2:OC ratio 4:Upv fixed 8:LSF"
    },
    14177: {
        "Level": "Expert",
        "Nr": 14177,
        "parameter description": "PV1 voltage fixed",
        "Unit": "Vdc",
        "Default": 500,
        "Min": 100,
        "Max": 600,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    14178: {
        "Level": "Expert",
        "Nr": 14178,
        "parameter description": "Ratio of PV1 open circuit voltage",
        "Unit": "",
        "Default": 0.7,
        "Min": 0.5,
        "Max": 1,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.010009766"
    },
    14046: {
        "Level": "Expert",
        "Nr": 14046,
        "parameter description": "Type of MPP tracking algorithm PV2",
        "Unit": "",
        "Default": 8,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:P&O 2:OC ratio 4:Upv fixed 8:LSF"
    },
    14047: {
        "Level": "Expert",
        "Nr": 14047,
        "parameter description": "PV2 voltage fixed",
        "Unit": "Vdc",
        "Default": 500,
        "Min": 100,
        "Max": 600,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    14048: {
        "Level": "Expert",
        "Nr": 14048,
        "parameter description": "Ratio of PV2 open circuit voltage",
        "Unit": "",
        "Default": 0.7,
        "Min": 0.5,
        "Max": 1,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.010009766"
    },
    14192: {
        "Level": "Inst.",
        "Nr": 14192,
        "parameter description": "Establishment time (Algo MPPT)",
        "Unit": "sec",
        "Default": 0,
        "Min": 0,
        "Max": 300,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14193: {
        "Level": "Inst.",
        "Nr": 14193,
        "parameter description": "Averaging time (Algo MPPT)",
        "Unit": "sec",
        "Default": 0,
        "Min": 0,
        "Max": 300,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14190: {
        "Level": "Inst.",
        "Nr": 14190,
        "parameter description": "PV wiring type erased from memory",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    14195: {
        "Level": "Expert",
        "Nr": 14195,
        "parameter description": "Configuration for VS-70",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14196: {
        "Level": "Expert",
        "Nr": 14196,
        "parameter description": "Type of PV grounding",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:No control 2:PV+ grounded 4:PV- grounded 8:PV floating"
    },
    14197: {
        "Level": "Expert",
        "Nr": 14197,
        "parameter description": "Type of MPP tracking algorithm PV",
        "Unit": "",
        "Default": 8,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:P&O 2:OC ratio 4:Upv fixed 8:LSF"
    },
    14198: {
        "Level": "Expert",
        "Nr": 14198,
        "parameter description": "PV voltage fixed",
        "Unit": "Vdc",
        "Default": 500,
        "Min": 100,
        "Max": 600,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    14199: {
        "Level": "Expert",
        "Nr": 14199,
        "parameter description": "Ratio of PV open circuit voltage",
        "Unit": "",
        "Default": 0.7,
        "Min": 0.5,
        "Max": 1,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.010009766"
    },
    14200: {
        "Level": "Expert",
        "Nr": 14200,
        "parameter description": "Remote entry (Remote ON/OFF)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14201: {
        "Level": "Expert",
        "Nr": 14201,
        "parameter description": "Remote entry active",
        "Unit": "",
        "Default": 2,
        "Min": 1,
        "Max": 4,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Closed 2:Open 4:Edge"
    },
    14202: {
        "Level": "Expert",
        "Nr": 14202,
        "parameter description": "ON/OFF command",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14203: {
        "Level": "Expert",
        "Nr": 14203,
        "parameter description": "Activated by AUX1 state",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14204: {
        "Level": "Expert",
        "Nr": 14204,
        "parameter description": "Start equalization",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14205: {
        "Level": "Expert",
        "Nr": 14205,
        "parameter description": "Send a message when remote entry changes state",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14218: {
        "Level": "Inst.",
        "Nr": 14218,
        "parameter description": "VarioString watchdog enabled (SCOM)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14219: {
        "Level": "Inst.",
        "Nr": 14219,
        "parameter description": "VarioString watchdog delay (SCOM)",
        "Unit": "sec",
        "Default": 60,
        "Min": 10,
        "Max": 300,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "10"
    },
    14182: {
        "Level": "Expert",
        "Nr": 14182,
        "parameter description": "Reset PV energy meter",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    14183: {
        "Level": "QSP",
        "Nr": 14183,
        "parameter description": "Reset total produced PV energy meter",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    14051: {
        "Level": "Expert",
        "Nr": 14051,
        "parameter description": "Reset daily solar production meters",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    14052: {
        "Level": "Expert",
        "Nr": 14052,
        "parameter description": "Reset daily min-max",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    14069: {
        "Level": "Inst.",
        "Nr": 14069,
        "parameter description": "Parameters saved in flash memory",
        "Unit": "",
        "Default": 1,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14038: {
        "Level": "Expert",
        "Nr": 14038,
        "parameter description": "ON of the VarioString",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    14039: {
        "Level": "Expert",
        "Nr": 14039,
        "parameter description": "OFF of the VarioString",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    14059: {
        "Level": "Expert",
        "Nr": 14059,
        "parameter description": "Reset of all VarioString",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    14070: {
        "Level": "Expert",
        "Nr": 14070,
        "parameter description": "AUXILIARY CONTACT 1",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14071: {
        "Level": "Expert",
        "Nr": 14071,
        "parameter description": "Operating mode (AUX 1)",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Automatic 2:Reversed automatic 4:Manual ON 8:Manual OFF"
    },
    14072: {
        "Level": "Expert",
        "Nr": 14072,
        "parameter description": "Combination of the events for the auxiliary contact (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 0:Any (Function OR) 1:All (Function AND)"
    },
    14073: {
        "Level": "Expert",
        "Nr": 14073,
        "parameter description": "Contact activated in night mode (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14074: {
        "Level": "Expert",
        "Nr": 14074,
        "parameter description": "Activated in night mode (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14075: {
        "Level": "Expert",
        "Nr": 14075,
        "parameter description": "Delay of activation after entering night mode (AUX 1)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14076: {
        "Level": "Expert",
        "Nr": 14076,
        "parameter description": "Activation time for the auxiliary relay in night mode (AUX 1)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14206: {
        "Level": "Expert",
        "Nr": 14206,
        "parameter description": "Contact active with a fixed time schedule (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14207: {
        "Level": "Expert",
        "Nr": 14207,
        "parameter description": "Contact activated with fixed time schedule (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14208: {
        "Level": "Expert",
        "Nr": 14208,
        "parameter description": "Start hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    14209: {
        "Level": "Expert",
        "Nr": 14209,
        "parameter description": "End hour (AUX 1)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    14077: {
        "Level": "Expert",
        "Nr": 14077,
        "parameter description": "Contact active on event (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14188: {
        "Level": "Expert",
        "Nr": 14188,
        "parameter description": "VarioString is ON (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14078: {
        "Level": "Expert",
        "Nr": 14078,
        "parameter description": "VarioString is OFF (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14214: {
        "Level": "Expert",
        "Nr": 14214,
        "parameter description": "Remote entry (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14079: {
        "Level": "Expert",
        "Nr": 14079,
        "parameter description": "Battery undervoltage (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14080: {
        "Level": "Expert",
        "Nr": 14080,
        "parameter description": "Battery overvoltage (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14081: {
        "Level": "Expert",
        "Nr": 14081,
        "parameter description": "Earth fault (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14082: {
        "Level": "Expert",
        "Nr": 14082,
        "parameter description": "PV error (48h without charge) (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14083: {
        "Level": "Expert",
        "Nr": 14083,
        "parameter description": "Overtemperature (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14084: {
        "Level": "Expert",
        "Nr": 14084,
        "parameter description": "Bulk charge phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14085: {
        "Level": "Expert",
        "Nr": 14085,
        "parameter description": "Absorption phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14086: {
        "Level": "Expert",
        "Nr": 14086,
        "parameter description": "Equalization phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14087: {
        "Level": "Expert",
        "Nr": 14087,
        "parameter description": "Floating (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14088: {
        "Level": "Expert",
        "Nr": 14088,
        "parameter description": "Reduced floating (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14089: {
        "Level": "Expert",
        "Nr": 14089,
        "parameter description": "Periodic absorption (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14090: {
        "Level": "Expert",
        "Nr": 14090,
        "parameter description": "Contact active according to battery voltage (AUX 1)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14091: {
        "Level": "Expert",
        "Nr": 14091,
        "parameter description": "Battery voltage 1 activate (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14092: {
        "Level": "Expert",
        "Nr": 14092,
        "parameter description": "Battery voltage 1 (AUX 1)",
        "Unit": "Vdc",
        "Default": 46.8,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14093: {
        "Level": "Expert",
        "Nr": 14093,
        "parameter description": "Delay 1 (AUX 1)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14094: {
        "Level": "Expert",
        "Nr": 14094,
        "parameter description": "Battery voltage 2 activate (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14095: {
        "Level": "Expert",
        "Nr": 14095,
        "parameter description": "Battery voltage 2 (AUX 1)",
        "Unit": "Vdc",
        "Default": 47.8,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14096: {
        "Level": "Expert",
        "Nr": 14096,
        "parameter description": "Delay 2 (AUX 1)",
        "Unit": "min",
        "Default": 10,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14097: {
        "Level": "Expert",
        "Nr": 14097,
        "parameter description": "Battery voltage 3 activate (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14098: {
        "Level": "Expert",
        "Nr": 14098,
        "parameter description": "Battery voltage 3 (AUX 1)",
        "Unit": "Vdc",
        "Default": 48.5,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14099: {
        "Level": "Expert",
        "Nr": 14099,
        "parameter description": "Delay 3 (AUX 1)",
        "Unit": "min",
        "Default": 60,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14100: {
        "Level": "Expert",
        "Nr": 14100,
        "parameter description": "Battery voltage to deactivate (AUX 1)",
        "Unit": "Vdc",
        "Default": 54,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14101: {
        "Level": "Expert",
        "Nr": 14101,
        "parameter description": "Delay to deactivate (AUX 1)",
        "Unit": "min",
        "Default": 60,
        "Min": 0,
        "Max": 480,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    14102: {
        "Level": "Expert",
        "Nr": 14102,
        "parameter description": "Deactivate if battery in floating phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14103: {
        "Level": "Expert",
        "Nr": 14103,
        "parameter description": "Contact active according to battery temperature (AUX 1) With BSP or BTS",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14104: {
        "Level": "Expert",
        "Nr": 14104,
        "parameter description": "Contact activated with the temperature of battery (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14105: {
        "Level": "Expert",
        "Nr": 14105,
        "parameter description": "Contact activated over (AUX 1)",
        "Unit": "°C",
        "Default": 3,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14106: {
        "Level": "Expert",
        "Nr": 14106,
        "parameter description": "Contact deactivated below (AUX 1)",
        "Unit": "°C",
        "Default": 5,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14107: {
        "Level": "Expert",
        "Nr": 14107,
        "parameter description": "Only activated if the battery is not in bulk phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14108: {
        "Level": "Expert",
        "Nr": 14108,
        "parameter description": "Contact active according to SOC (AUX 1) Only with BSP",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14109: {
        "Level": "Expert",
        "Nr": 14109,
        "parameter description": "Contact activated with the SOC 1 of battery (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14110: {
        "Level": "Expert",
        "Nr": 14110,
        "parameter description": "Contact activated below SOC 1 (AUX 1)",
        "Unit": "% SOC",
        "Default": 50,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    14111: {
        "Level": "Expert",
        "Nr": 14111,
        "parameter description": "Delay 1 (AUX 1)",
        "Unit": "hours",
        "Default": 12,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    14112: {
        "Level": "Expert",
        "Nr": 14112,
        "parameter description": "Contact activated with the SOC 2 of battery (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14113: {
        "Level": "Expert",
        "Nr": 14113,
        "parameter description": "Contact activated below SOC 2 (AUX 1)",
        "Unit": "%",
        "Default": 30,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    14114: {
        "Level": "Expert",
        "Nr": 14114,
        "parameter description": "Delay 2 (AUX 1)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    14115: {
        "Level": "Expert",
        "Nr": 14115,
        "parameter description": "Contact activated with the SOC 3 of battery (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14116: {
        "Level": "Expert",
        "Nr": 14116,
        "parameter description": "Contact activated below SOC 3 (AUX 1)",
        "Unit": "%",
        "Default": 20,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    14117: {
        "Level": "Expert",
        "Nr": 14117,
        "parameter description": "Delay 3 (AUX 1)",
        "Unit": "hours",
        "Default": 0,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    14118: {
        "Level": "Expert",
        "Nr": 14118,
        "parameter description": "Contact deactivated over SOC (AUX 1)",
        "Unit": "% SOC",
        "Default": 90,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    14119: {
        "Level": "Expert",
        "Nr": 14119,
        "parameter description": "Delay to deactivate (AUX 1)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 10,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    14120: {
        "Level": "Expert",
        "Nr": 14120,
        "parameter description": "Deactivate if battery in floating phase (AUX 1)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14121: {
        "Level": "Expert",
        "Nr": 14121,
        "parameter description": "Reset all settings (AUX 1)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
    14122: {
        "Level": "Expert",
        "Nr": 14122,
        "parameter description": "AUXILIARY CONTACT 2",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14123: {
        "Level": "Expert",
        "Nr": 14123,
        "parameter description": "Operating mode (AUX 2)",
        "Unit": "",
        "Default": 1,
        "Min": 1,
        "Max": 8,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 1:Automatic 2:Reversed automatic 4:Manual ON 8:Manual OFF"
    },
    14124: {
        "Level": "Expert",
        "Nr": 14124,
        "parameter description": "Combination of the events for the auxiliary contact (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.LONG_ENUM,
        "Increment": "Only 1 bit 0:Any (Function OR) 1:All (Function AND)"
    },
    14125: {
        "Level": "Expert",
        "Nr": 14125,
        "parameter description": "Contact activated in night mode (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14126: {
        "Level": "Expert",
        "Nr": 14126,
        "parameter description": "Activated in night mode (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14127: {
        "Level": "Expert",
        "Nr": 14127,
        "parameter description": "Delay of activation after entering night mode (AUX 2)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14128: {
        "Level": "Expert",
        "Nr": 14128,
        "parameter description": "Activation time for the auxiliary relay in night mode (AUX 2)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14210: {
        "Level": "Expert",
        "Nr": 14210,
        "parameter description": "Contact active with a fixed time schedule (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14211: {
        "Level": "Expert",
        "Nr": 14211,
        "parameter description": "Contact activated with fixed time schedule (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14212: {
        "Level": "Expert",
        "Nr": 14212,
        "parameter description": "Start hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 420,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    14213: {
        "Level": "Expert",
        "Nr": 14213,
        "parameter description": "End hour (AUX 2)",
        "Unit": "Minutes",
        "Default": 1200,
        "Min": 0,
        "Max": 1440,
        "Scom format": PropertyFormat.INT32,
        "Increment": "1"
    },
    14129: {
        "Level": "Expert",
        "Nr": 14129,
        "parameter description": "Contact active on event (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14189: {
        "Level": "Expert",
        "Nr": 14189,
        "parameter description": "VarioString is ON (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14130: {
        "Level": "Expert",
        "Nr": 14130,
        "parameter description": "VarioString is OFF (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14215: {
        "Level": "Expert",
        "Nr": 14215,
        "parameter description": "Remote entry (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14131: {
        "Level": "Expert",
        "Nr": 14131,
        "parameter description": "Battery undervoltage (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14132: {
        "Level": "Expert",
        "Nr": 14132,
        "parameter description": "Battery overvoltage (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14133: {
        "Level": "Expert",
        "Nr": 14133,
        "parameter description": "Earth fault (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14134: {
        "Level": "Expert",
        "Nr": 14134,
        "parameter description": "PV error (48h without charge) (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14135: {
        "Level": "Expert",
        "Nr": 14135,
        "parameter description": "Overtemperature (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14136: {
        "Level": "Expert",
        "Nr": 14136,
        "parameter description": "Bulk charge phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14137: {
        "Level": "Expert",
        "Nr": 14137,
        "parameter description": "Absorption phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14138: {
        "Level": "Expert",
        "Nr": 14138,
        "parameter description": "Equalization phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14139: {
        "Level": "Expert",
        "Nr": 14139,
        "parameter description": "Floating (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14140: {
        "Level": "Expert",
        "Nr": 14140,
        "parameter description": "Reduced floating (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14141: {
        "Level": "Expert",
        "Nr": 14141,
        "parameter description": "Periodic absorption (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14142: {
        "Level": "Expert",
        "Nr": 14142,
        "parameter description": "Contact active according to battery voltage (AUX 2)",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14143: {
        "Level": "Expert",
        "Nr": 14143,
        "parameter description": "Battery voltage 1 activate (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14144: {
        "Level": "Expert",
        "Nr": 14144,
        "parameter description": "Battery voltage 1 (AUX 2)",
        "Unit": "Vdc",
        "Default": 46.8,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14145: {
        "Level": "Expert",
        "Nr": 14145,
        "parameter description": "Delay 1 (AUX 2)",
        "Unit": "min",
        "Default": 1,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14146: {
        "Level": "Expert",
        "Nr": 14146,
        "parameter description": "Battery voltage 2 activate (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14147: {
        "Level": "Expert",
        "Nr": 14147,
        "parameter description": "Battery voltage 2 (AUX 2)",
        "Unit": "Vdc",
        "Default": 47.8,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14148: {
        "Level": "Expert",
        "Nr": 14148,
        "parameter description": "Delay 2 (AUX 2)",
        "Unit": "min",
        "Default": 10,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14149: {
        "Level": "Expert",
        "Nr": 14149,
        "parameter description": "Battery voltage 3 activate (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14150: {
        "Level": "Expert",
        "Nr": 14150,
        "parameter description": "Battery voltage 3 (AUX 2)",
        "Unit": "Vdc",
        "Default": 48.5,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14151: {
        "Level": "Expert",
        "Nr": 14151,
        "parameter description": "Delay 3 (AUX 2)",
        "Unit": "min",
        "Default": 60,
        "Min": 0,
        "Max": 60,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14152: {
        "Level": "Expert",
        "Nr": 14152,
        "parameter description": "Battery voltage to deactivate (AUX 2)",
        "Unit": "Vdc",
        "Default": 54,
        "Min": 36,
        "Max": 72,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.1"
    },
    14153: {
        "Level": "Expert",
        "Nr": 14153,
        "parameter description": "Delay to deactivate (AUX 2)",
        "Unit": "min",
        "Default": 60,
        "Min": 0,
        "Max": 480,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    14154: {
        "Level": "Expert",
        "Nr": 14154,
        "parameter description": "Deactivate if battery in floating phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14155: {
        "Level": "Expert",
        "Nr": 14155,
        "parameter description": "Contact active according to battery temperature (AUX 2) With BSP or BTS",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14156: {
        "Level": "Expert",
        "Nr": 14156,
        "parameter description": "Contact activated with the temperature of battery (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14157: {
        "Level": "Expert",
        "Nr": 14157,
        "parameter description": "Contact activated over (AUX 2)",
        "Unit": "°C",
        "Default": 3,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14158: {
        "Level": "Expert",
        "Nr": 14158,
        "parameter description": "Contact deactivated below (AUX 2)",
        "Unit": "°C",
        "Default": 5,
        "Min": -10,
        "Max": 50,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "1"
    },
    14159: {
        "Level": "Expert",
        "Nr": 14159,
        "parameter description": "Only activated if the battery is not in bulk phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14160: {
        "Level": "Expert",
        "Nr": 14160,
        "parameter description": "Contact active according to SOC (AUX 2) Only with BSP",
        "Unit": "",
        "Default": None,
        "Min": None,
        "Max": None,
        "Scom format": PropertyFormat.ONLY_LEVEL,
        "Increment": "Menu"
    },
    14161: {
        "Level": "Expert",
        "Nr": 14161,
        "parameter description": "Contact activated with the SOC 1 of battery (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14162: {
        "Level": "Expert",
        "Nr": 14162,
        "parameter description": "Contact activated below SOC 1 (AUX 2)",
        "Unit": "% SOC",
        "Default": 50,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    14163: {
        "Level": "Expert",
        "Nr": 14163,
        "parameter description": "Delay 1 (AUX 2)",
        "Unit": "hours",
        "Default": 12,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    14164: {
        "Level": "Expert",
        "Nr": 14164,
        "parameter description": "Contact activated with the SOC 2 of battery (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14165: {
        "Level": "Expert",
        "Nr": 14165,
        "parameter description": "Contact activated below SOC 2 (AUX 2)",
        "Unit": "%",
        "Default": 30,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    14166: {
        "Level": "Expert",
        "Nr": 14166,
        "parameter description": "Delay 2 (AUX 2)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    14167: {
        "Level": "Expert",
        "Nr": 14167,
        "parameter description": "Contact activated with the SOC 3 of battery (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14168: {
        "Level": "Expert",
        "Nr": 14168,
        "parameter description": "Contact activated below SOC 3 (AUX 2)",
        "Unit": "%",
        "Default": 20,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    14169: {
        "Level": "Expert",
        "Nr": 14169,
        "parameter description": "Delay 3 (AUX 2)",
        "Unit": "hours",
        "Default": 0,
        "Min": 0,
        "Max": 99,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    14170: {
        "Level": "Expert",
        "Nr": 14170,
        "parameter description": "Contact deactivated over SOC (AUX 2)",
        "Unit": "% SOC",
        "Default": 90,
        "Min": 0,
        "Max": 100,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "5"
    },
    14171: {
        "Level": "Expert",
        "Nr": 14171,
        "parameter description": "Delay to deactivate (AUX 2)",
        "Unit": "hours",
        "Default": 0.2,
        "Min": 0,
        "Max": 10,
        "Scom format": PropertyFormat.FLOAT,
        "Increment": "0.25"
    },
    14172: {
        "Level": "Expert",
        "Nr": 14172,
        "parameter description": "Deactivate if battery in floating phase (AUX 2)",
        "Unit": "",
        "Default": 0,
        "Min": 0,
        "Max": 1,
        "Scom format": PropertyFormat.BOOL,
        "Increment": "1"
    },
    14173: {
        "Level": "Expert",
        "Nr": 14173,
        "parameter description": "Reset all settings (AUX 2)",
        "Unit": "",
        "Default": S,
        "Min": S,
        "Max": S,
        "Scom format": PropertyFormat.INT32_SIGNAL,
        "Increment": "Signal"
    },
}

# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------- 1.12 VarioString infos ---------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Contains 87 Infos
VARIO_STRING_INFOS = {
    15000: {
        "Nr": 15000,
        "information description": "Battery voltage",
        "Short desc.": "Ubat",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15001: {
        "Nr": 15001,
        "information description": "Battery current",
        "Short desc.": "Ibat",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15002: {
        "Nr": 15002,
        "information description": "Battery cycle phase",
        "Short desc.": "Phas",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Bulk "
                                            "1:Absorpt. "
                                            "2:Equalize "
                                            "3:Floating "
                                            "4:--- "
                                            "5:--- "
                                            "6:R.float. "
                                            "7:Per.abs. "
                                            "8:--- "
                                            "9:--- "
                                            "10:--- "
                                            "11:---"
    },
    15003: {
        "Nr": 15003,
        "information description": "PV type of wiring",
        "Short desc.": "conf",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Unknown 1:Independ. 2:Series 3:Parallel 4:Error"
    },
    15004: {
        "Nr": 15004,
        "information description": "PV voltage",
        "Short desc.": "Upv",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15005: {
        "Nr": 15005,
        "information description": "PV1 voltage",
        "Short desc.": "Upv1",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15006: {
        "Nr": 15006,
        "information description": "PV2 voltage",
        "Short desc.": "Upv2",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15007: {
        "Nr": 15007,
        "information description": "PV current",
        "Short desc.": "Ipv",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15008: {
        "Nr": 15008,
        "information description": "PV1 current",
        "Short desc.": "Ipv1",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15009: {
        "Nr": 15009,
        "information description": "PV2 current",
        "Short desc.": "Ipv2",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15010: {
        "Nr": 15010,
        "information description": "PV power",
        "Short desc.": "Ppv",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15011: {
        "Nr": 15011,
        "information description": "PV1 power",
        "Short desc.": "Ppv1",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15012: {
        "Nr": 15012,
        "information description": "PV2 power",
        "Short desc.": "Ppv2",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15013: {
        "Nr": 15013,
        "information description": "PV operating mode",
        "Short desc.": "Mode",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Night "
                                            "1:Security "
                                            "2:OFF "
                                            "3:Charge "
                                            "4:ChargeV "
                                            "5:Charge I "
                                            "6:ChargeP "
                                            "7:ChargeIpv "
                                            "8:ChargeT "
                                            "9:--- "
                                            "10:Ch.Ibsp"
    },
    15014: {
        "Nr": 15014,
        "information description": "PV1 operating mode",
        "Short desc.": "Mod1",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Night "
                                            "1:Security "
                                            "2:OFF "
                                            "3:Charge "
                                            "4:ChargeV "
                                            "5:Charge I "
                                            "6:ChargeP "
                                            "7:ChargeIpv "
                                            "8:ChargeT "
                                            "9:--- "
                                            "10:Ch.Ibsp"
    },
    15015: {
        "Nr": 15015,
        "information description": "PV2 operating mode",
        "Short desc.": "Mod2",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Night "
                                            "1:Security "
                                            "2:OFF "
                                            "3:Charge "
                                            "4:ChargeV "
                                            "5:Charge I "
                                            "6:ChargeP "
                                            "7:ChargeIpv "
                                            "8:ChargeT "
                                            "9:--- "
                                            "10:Ch.Ibsp"
    },
    15016: {
        "Nr": 15016,
        "information description": "Production PV in (Ah) for the current day",
        "Short desc.": "Cd",
        "Unit on the RCC": "Ah",
        "Unit": "Ah",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15017: {
        "Nr": 15017,
        "information description": "Production PV in (kWh) for the current day",
        "Short desc.": "Ed",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15018: {
        "Nr": 15018,
        "information description": "Production PV1 in (kWh) for the current day",
        "Short desc.": "Ed1",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15019: {
        "Nr": 15019,
        "information description": "Production PV2 in (kWh) for the current day",
        "Short desc.": "Ed2",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15020: {
        "Nr": 15020,
        "information description": "Produced PV energy resettable counter",
        "Short desc.": "kWhR",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15021: {
        "Nr": 15021,
        "information description": "Produced PV1 energy resettable counter",
        "Short desc.": "kWh1",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15022: {
        "Nr": 15022,
        "information description": "Produced PV2 energy resettable counter",
        "Short desc.": "kWh2",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15023: {
        "Nr": 15023,
        "information description": "Total PV produced energy",
        "Short desc.": "MWhT",
        "Unit on the RCC": "MWh",
        "Unit": "MWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15024: {
        "Nr": 15024,
        "information description": "Total PV1 produced energy",
        "Short desc.": "MWh1",
        "Unit on the RCC": "MWh",
        "Unit": "MWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15025: {
        "Nr": 15025,
        "information description": "Total PV2 produced energy",
        "Short desc.": "MWh2",
        "Unit on the RCC": "MWh",
        "Unit": "MWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15026: {
        "Nr": 15026,
        "information description": "Production PV in (Ah) for the previous day",
        "Short desc.": "Cd-1",
        "Unit on the RCC": "Ah",
        "Unit": "Ah",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15027: {
        "Nr": 15027,
        "information description": "Production PV in (Wh) for the previous day",
        "Short desc.": "Ed-",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15028: {
        "Nr": 15028,
        "information description": "Production PV1 in (Wh) for the previous day",
        "Short desc.": "Ed1-",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15029: {
        "Nr": 15029,
        "information description": "Production PV2 in (Wh) for the previous day",
        "Short desc.": "Ed2-",
        "Unit on the RCC": "kWh",
        "Unit": "kWh",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15030: {
        "Nr": 15030,
        "information description": "Number of irradiation hours for the current day",
        "Short desc.": "Sd",
        "Unit on the RCC": "h",
        "Unit": "h",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15031: {
        "Nr": 15031,
        "information description": "Number of irradiation hours for the previous day",
        "Short desc.": "Sd-1",
        "Unit on the RCC": "h",
        "Unit": "h",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15032: {
        "Nr": 15032,
        "information description": "Battery temperature",
        "Short desc.": "Tbat",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15033: {
        "Nr": 15033,
        "information description": "Max PV voltage for the current day",
        "Short desc.": "Upmx",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15034: {
        "Nr": 15034,
        "information description": "Max PV1 voltage for the current day",
        "Short desc.": "Upm1",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15035: {
        "Nr": 15035,
        "information description": "Max PV2 voltage for the current day",
        "Short desc.": "Upm2",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15036: {
        "Nr": 15036,
        "information description": "Max battery current of the current day",
        "Short desc.": "Ibmx",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15037: {
        "Nr": 15037,
        "information description": "Max PV power for the current day",
        "Short desc.": "Ppmx",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15038: {
        "Nr": 15038,
        "information description": "Max PV1 power for the current day",
        "Short desc.": "Ppm1",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15039: {
        "Nr": 15039,
        "information description": "Max PV2 power for the current day",
        "Short desc.": "Ppm2",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15040: {
        "Nr": 15040,
        "information description": "Max battery voltage for the current day",
        "Short desc.": "Ubmx",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15041: {
        "Nr": 15041,
        "information description": "Min battery voltage for the current day",
        "Short desc.": "Ubmn",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15042: {
        "Nr": 15042,
        "information description": "Time in absorption of the current day",
        "Short desc.": "Tabs",
        "Unit on the RCC": "h",
        "Unit": "h",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15043: {
        "Nr": 15043,
        "information description": "BAT- and Earth voltage",
        "Short desc.": "BatE",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15044: {
        "Nr": 15044,
        "information description": "PV- and Earth voltage",
        "Short desc.": "pv-E",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15045: {
        "Nr": 15045,
        "information description": "PV1- and Earth voltage",
        "Short desc.": "pv1E",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15046: {
        "Nr": 15046,
        "information description": "PV2- and Earth voltage",
        "Short desc.": "pv2E",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15049: {
        "Nr": 15049,
        "information description": "Type of error",
        "Short desc.": "Err",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:None "
                                            "1:OverV_B "
                                            "2:OverV_PV "
                                            "3:OverV_PV1 "
                                            "4:OverV_PV2 "
                                            "5:OverI_PV "
                                            "6:OverI_PV1 "
                                            "7:OverI_PV2 "
                                            "8:GroundBat "
                                            "9:GroundPV "
                                            "10:GroundPV1 "
                                            "11:GroundPV2 "
                                            "12:OverTemp "
                                            "13:UnderV_B "
                                            "14:Cabling "
                                            "15:Other"
    },
    15050: {
        "Nr": 15050,
        "information description": "Synchronized with Xtender battery cycle",
        "Short desc.": "Sync",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:No 1:Yes"
    },
    15051: {
        "Nr": 15051,
        "information description": "Synchronisation state",
        "Short desc.": "Sync",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:--- "
                                            "1:--- "
                                            "2:--- "
                                            "3:--- "
                                            "4:XTslave "
                                            "5:VTslave "
                                            "6:--- "
                                            "7:--- "
                                            "8:VTmaster "
                                            "9:Autonom "
                                            "10:VSslave "
                                            "11:VSmaster"
    },
    15052: {
        "Nr": 15052,
        "information description": "Number of days before next equalization",
        "Short desc.": "EqIn",
        "Unit on the RCC": "days",
        "Unit": "days",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15053: {
        "Nr": 15053,
        "information description": "Battery set point",
        "Short desc.": "Bset",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15054: {
        "Nr": 15054,
        "information description": "Battery voltage (minute avg)",
        "Short desc.": "Ubat",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15055: {
        "Nr": 15055,
        "information description": "Battery voltage (minute max)",
        "Short desc.": "Ubat+",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15056: {
        "Nr": 15056,
        "information description": "Battery voltage (minute min)",
        "Short desc.": "Ubat-",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15057: {
        "Nr": 15057,
        "information description": "Battery current (minute avg)",
        "Short desc.": "Ibat",
        "Unit on the RCC": "Adc",
        "Unit": "A",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15058: {
        "Nr": 15058,
        "information description": "PV voltage (minute avg)",
        "Short desc.": "Upv",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15059: {
        "Nr": 15059,
        "information description": "PV1 voltage (minute avg)",
        "Short desc.": "Upv1",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15060: {
        "Nr": 15060,
        "information description": "PV2 voltage (minute avg)",
        "Short desc.": "Upv2",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15061: {
        "Nr": 15061,
        "information description": "PV power (minute avg)",
        "Short desc.": "Ppv",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15062: {
        "Nr": 15062,
        "information description": "PV1 power (minute avg)",
        "Short desc.": "Ppv1",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15063: {
        "Nr": 15063,
        "information description": "PV2 power (minute avg)",
        "Short desc.": "Ppv2",
        "Unit on the RCC": "kW",
        "Unit": "kW",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15064: {
        "Nr": 15064,
        "information description": "Battery temperature (minute avg)",
        "Short desc.": "Tbat",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15065: {
        "Nr": 15065,
        "information description": "Electronic temperature 1 (minute avg)",
        "Short desc.": "Dev1",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15066: {
        "Nr": 15066,
        "information description": "Electronic temperature 1 (minute max)",
        "Short desc.": "Dev1+",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15067: {
        "Nr": 15067,
        "information description": "Electronic temperature 1 (minute min)",
        "Short desc.": "Dev1-",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15068: {
        "Nr": 15068,
        "information description": "Electronic temperature 2 (minute avg)",
        "Short desc.": "Dev2",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15069: {
        "Nr": 15069,
        "information description": "Electronic temperature 2 (minute max)",
        "Short desc.": "Dev2+",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15070: {
        "Nr": 15070,
        "information description": "Electronic temperature 2 (minute min)",
        "Short desc.": "Dev2-",
        "Unit on the RCC": "°C",
        "Unit": "°C",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15071: {
        "Nr": 15071,
        "information description": "Number of parameters (in code)",
        "Short desc.": "pCod",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15072: {
        "Nr": 15072,
        "information description": "Number of parameters (in flash)",
        "Short desc.": "pFla",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15073: {
        "Nr": 15073,
        "information description": "Number of infos users",
        "Short desc.": "iCod",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15074: {
        "Nr": 15074,
        "information description": "ID type",
        "Short desc.": "Idt",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "VS120 = 12801d (0x3201), VS70 = 13057d (0x3301)"
    },
    15075: {
        "Nr": 15075,
        "information description": "ID bat voltage",
        "Short desc.": "Idv",
        "Unit on the RCC": "Vdc",
        "Unit": "V",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15076: {
        "Nr": 15076,
        "information description": "ID HW",
        "Short desc.": "HW",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15077: {
        "Nr": 15077,
        "information description": "ID SOFT msb",
        "Short desc.": "Smsb",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'Software version encoding'"
    },
    15078: {
        "Nr": 15078,
        "information description": "ID SOFT lsb",
        "Short desc.": "Slsb",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'Software version encoding'"
    },
    15079: {
        "Nr": 15079,
        "information description": "ID SID",
        "Short desc.": "SID",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15088: {
        "Nr": 15088,
        "information description": "State of auxiliary Aux 1",
        "Short desc.": "Aux 1",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Opened 1:Closed"
    },
    15089: {
        "Nr": 15089,
        "information description": "State of auxiliary Aux 2",
        "Short desc.": "Aux 2",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Opened 1:Closed"
    },
    15090: {
        "Nr": 15090,
        "information description": "Relay Aux 1 mode",
        "Short desc.": "Aux 1",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:--- 1:A 2:I 3:M 4:M"
    },
    15091: {
        "Nr": 15091,
        "information description": "Relay Aux 2 mode",
        "Short desc.": "Aux 2",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:--- 1:A 2:I 3:M 4:M"
    },
    15102: {
        "Nr": 15102,
        "information description": "ID FID msb",
        "Short desc.": "",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'FID encoding'"
    },
    15103: {
        "Nr": 15103,
        "information description": "ID FID lsb",
        "Short desc.": "",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": "See section 'FID encoding'"
    },
    15108: {
        "Nr": 15108,
        "information description": "State of the VarioString",
        "Short desc.": "VS state",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:Off 1:On"
    },
    15109: {
        "Nr": 15109,
        "information description": "Local daily communication error counter (CAN)",
        "Short desc.": "locEr",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.FLOAT,
        "Related parameter or description": ""
    },
    15111: {
        "Nr": 15111,
        "information description": "Remote entry state",
        "Short desc.": "RME",
        "Unit on the RCC": "",
        "Unit": "",
        "Format": PropertyFormat.SHORT_ENUM,
        "Related parameter or description": "0:RM EN 0 1:RM EN 1"
    },
}

# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------- 1.13 RCC messages ------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
# Contains 183 Messages
RCC_MESSAGES = {
    0: {
        "Level": "V.O.",
        "Nr": 0,
        "Messages": "Warning (000): Battery low"
    },
    1: {
        "Level": "V.O.",
        "Nr": 1,
        "Messages": "Warning (001): Battery too high"
    },
    2: {
        "Level": "V.O.",
        "Nr": 2,
        "Messages": "Warning (002): Bulk charge too long"
    },
    3: {
        "Level": "V.O.",
        "Nr": 3,
        "Messages": "(003): AC-In synchronization in progress"
    },
    4: {
        "Level": "V.O.",
        "Nr": 4,
        "Messages": "Warning (004): Input frequency AC-In wrong"
    },
    5: {
        "Level": "V.O.",
        "Nr": 5,
        "Messages": "Warning (005): Input frequency AC-In wrong"
    },
    6: {
        "Level": "V.O.",
        "Nr": 6,
        "Messages": "Warning (006): Input voltage AC-In too high"
    },
    7: {
        "Level": "V.O.",
        "Nr": 7,
        "Messages": "Warning (007): Input voltage AC-In too low"
    },
    8: {
        "Level": "V.O.",
        "Nr": 8,
        "Messages": "Halted (008): Inverter overload SC"
    },
    9: {
        "Level": "V.O.",
        "Nr": 9,
        "Messages": "Halted (009): Charger short circuit"
    },
    10: {
        "Level": "V.O.",
        "Nr": 10,
        "Messages": "(010): System start-up in progress"
    },
    11: {
        "Level": "V.O.",
        "Nr": 11,
        "Messages": "Warning (011): AC-In Energy quota"
    },
    12: {
        "Level": "V.O.",
        "Nr": 12,
        "Messages": "(012): Use of battery temperature sensor"
    },
    13: {
        "Level": "V.O.",
        "Nr": 13,
        "Messages": "(013): Use of additional remote control"
    },
    14: {
        "Level": "V.O.",
        "Nr": 14,
        "Messages": "Halted (014): Over temperature EL"
    },
    15: {
        "Level": "V.O.",
        "Nr": 15,
        "Messages": "Halted (015): Inverter overload BL"
    },
    16: {
        "Level": "V.O.",
        "Nr": 16,
        "Messages": "Warning (016): Fan error detected"
    },
    17: {
        "Level": "V.O.",
        "Nr": 17,
        "Messages": "(017): Programing mode"
    },
    18: {
        "Level": "V.O.",
        "Nr": 18,
        "Messages": "Warning (018): Excessive battery voltage ripple"
    },
    19: {
        "Level": "V.O.",
        "Nr": 19,
        "Messages": "Halted (019): Battery undervoltage"
    },
    20: {
        "Level": "V.O.",
        "Nr": 20,
        "Messages": "Halted (020): Battery overvoltage"
    },
    21: {
        "Level": "V.O.",
        "Nr": 21,
        "Messages": "(021): Transfer not authorized, AC-Out current is higher than {1107}"
    },
    22: {
        "Level": "V.O.",
        "Nr": 22,
        "Messages": "Halted (022): Voltage presence on AC-Out"
    },
    23: {
        "Level": "V.O.",
        "Nr": 23,
        "Messages": "Halted (023): Phase not defined"
    },
    24: {
        "Level": "V.O.",
        "Nr": 24,
        "Messages": "Warning (024): Change the clock battery"
    },
    25: {
        "Level": "V.O.",
        "Nr": 25,
        "Messages": "Halted (025): Unknown Command board. Software upgrade needed"
    },
    26: {
        "Level": "V.O.",
        "Nr": 26,
        "Messages": "Halted (026): Unknown Power board. Software upgrade needed"
    },
    27: {
        "Level": "V.O.",
        "Nr": 27,
        "Messages": "Halted (027): Unknown extension board. Software upgrade needed"
    },
    28: {
        "Level": "V.O.",
        "Nr": 28,
        "Messages": "Halted (028): Voltage incompatibility Power - Command"
    },
    29: {
        "Level": "V.O.",
        "Nr": 29,
        "Messages": "Halted (029): Voltage incompatibility Ext. - Command"
    },
    30: {
        "Level": "V.O.",
        "Nr": 30,
        "Messages": "Halted (030): Power incompatibility Power - Command"
    },
    31: {
        "Level": "V.O.",
        "Nr": 31,
        "Messages": "Halted (031): Command board software incompatibility"
    },
    32: {
        "Level": "V.O.",
        "Nr": 32,
        "Messages": "Halted (032): Power board software incompatibility"
    },
    33: {
        "Level": "V.O.",
        "Nr": 33,
        "Messages": "Halted (033): Extension board software incompatibility"
    },
    34: {
        "Level": "V.O.",
        "Nr": 34,
        "Messages": "Halted (034): FID corruption, call factory"
    },
    35: {
        "Level": "V.O.",
        "Nr": 35,
        "Messages": "(035): Memory structure modified"
    },
    36: {
        "Level": "V.O.",
        "Nr": 36,
        "Messages": "Halted (036): Parameter file lacking"
    },
    37: {
        "Level": "V.O.",
        "Nr": 37,
        "Messages": "Warning (037): Message file lack. SW upgrade advised"
    },
    38: {
        "Level": "V.O.",
        "Nr": 38,
        "Messages": "Warning (038): Upgrade of the device software advised"
    },
    39: {
        "Level": "V.O.",
        "Nr": 39,
        "Messages": "Warning (039): Upgrade of the device software advised"
    },
    40: {
        "Level": "V.O.",
        "Nr": 40,
        "Messages": "Warning (040): Upgrade of the device software advised"
    },
    41: {
        "Level": "V.O.",
        "Nr": 41,
        "Messages": "Warning (041): Over temperature TR"
    },
    42: {
        "Level": "V.O.",
        "Nr": 42,
        "Messages": "Halted (042): Unauthorized energy source at the output"
    },
    43: {
        "Level": "V.O.",
        "Nr": 43,
        "Messages": "(043): Start of monthly test"
    },
    44: {
        "Level": "V.O.",
        "Nr": 44,
        "Messages": "(044): End of successfully monthly test"
    },
    45: {
        "Level": "V.O.",
        "Nr": 45,
        "Messages": "Warning (045): Monthly autonomy test failed"
    },
    46: {
        "Level": "V.O.",
        "Nr": 46,
        "Messages": "(046): Start of weekly test"
    },
    47: {
        "Level": "V.O.",
        "Nr": 47,
        "Messages": "(047): End of successfully weekly test"
    },
    48: {
        "Level": "V.O.",
        "Nr": 48,
        "Messages": "Warning (048): Weekly autonomy test failed"
    },
    49: {
        "Level": "V.O.",
        "Nr": 49,
        "Messages": "(049): Transfer opened because AC-In max current exceeded {1107}"
    },
    50: {
        "Level": "V.O.",
        "Nr": 50,
        "Messages": "Error (050): Incomplete data transfer"
    },
    51: {
        "Level": "V.O.",
        "Nr": 51,
        "Messages": "(051): The update is finished"
    },
    52: {
        "Level": "V.O.",
        "Nr": 52,
        "Messages": "(052): Your installation is already updated"
    },
    53: {
        "Level": "V.O.",
        "Nr": 53,
        "Messages": "Halted (053): Devices not compatible, software update required"
    },
    54: {
        "Level": "V.O.",
        "Nr": 54,
        "Messages": "(054): Please wait. Data transfer in progress"
    },
    55: {
        "Level": "V.O.",
        "Nr": 55,
        "Messages": "Error (055): No SD card inserted"
    },
    56: {
        "Level": "V.O.",
        "Nr": 56,
        "Messages": "Warning (056): Upgrade of the RCC software advised"
    },
    57: {
        "Level": "V.O.",
        "Nr": 57,
        "Messages": "(057): Operation finished successfully"
    },
    58: {
        "Level": "V.O.",
        "Nr": 58,
        "Messages": "Halted (058): Master synchronization missing"
    },
    59: {
        "Level": "V.O.",
        "Nr": 59,
        "Messages": "Halted (059): Inverter overload HW"
    },
    60: {
        "Level": "V.O.",
        "Nr": 60,
        "Messages": "Warning (060): Time security 1512 AUX1"
    },
    61: {
        "Level": "V.O.",
        "Nr": 61,
        "Messages": "Warning (061): Time security 1513 AUX2"
    },
    62: {
        "Level": "V.O.",
        "Nr": 62,
        "Messages": "Warning (062): Genset, no AC-In coming after AUX command"
    },
    63: {
        "Level": "V.O.",
        "Nr": 63,
        "Messages": "(063): Save parameter XT"
    },
    64: {
        "Level": "V.O.",
        "Nr": 64,
        "Messages": "(064): Save parameter BSP"
    },
    65: {
        "Level": "V.O.",
        "Nr": 65,
        "Messages": "(065): Save parameter VarioTrack"
    },
    71: {
        "Level": "V.O.",
        "Nr": 71,
        "Messages": "Error (071): Insufficient disk space on SD card"
    },
    72: {
        "Level": "V.O.",
        "Nr": 72,
        "Messages": "Halted (072): COM identification incorrect"
    },
    73: {
        "Level": "V.O.",
        "Nr": 73,
        "Messages": "(073): Datalogger is enabled on this RCC"
    },
    74: {
        "Level": "V.O.",
        "Nr": 74,
        "Messages": "(074): Save parameter Xcom-MS"
    },
    75: {
        "Level": "V.O.",
        "Nr": 75,
        "Messages": "(075): MPPT MS address changed successfully"
    },
    76: {
        "Level": "V.O.",
        "Nr": 76,
        "Messages": "Error (076): Error during change of MPPT MS address"
    },
    77: {
        "Level": "V.O.",
        "Nr": 77,
        "Messages": "Error (077): Wrong MPPT MS DIP Switch position"
    },
    78: {
        "Level": "V.O.",
        "Nr": 78,
        "Messages": "(078): SMS or email sent"
    },
    79: {
        "Level": "V.O.",
        "Nr": 79,
        "Messages": "Halted (079): More than 9 XTs in the system"
    },
    80: {
        "Level": "V.O.",
        "Nr": 80,
        "Messages": "Halted (080): No battery (or reverse polarity)"
    },
    81: {
        "Level": "V.O.",
        "Nr": 81,
        "Messages": "Warning (081): Earthing fault"
    },
    82: {
        "Level": "V.O.",
        "Nr": 82,
        "Messages": "Halted (082): PV overvoltage"
    },
    83: {
        "Level": "V.O.",
        "Nr": 83,
        "Messages": "Warning (083): No solar production in the last 48h"
    },
    84: {
        "Level": "V.O.",
        "Nr": 84,
        "Messages": "(084): Equalization performed"
    },
    85: {
        "Level": "V.O.",
        "Nr": 85,
        "Messages": "Error (085): Modem not available"
    },
    86: {
        "Level": "V.O.",
        "Nr": 86,
        "Messages": "Error (086): Incorrect PIN code, unable to initiate the modem"
    },
    87: {
        "Level": "V.O.",
        "Nr": 87,
        "Messages": "Error (087): Insufficient Signal from GSM modem"
    },
    88: {
        "Level": "V.O.",
        "Nr": 88,
        "Messages": "Error (088): No connection to GSM network"
    },
    89: {
        "Level": "V.O.",
        "Nr": 89,
        "Messages": "Error (089): No Xcom server access"
    },
    90: {
        "Level": "V.O.",
        "Nr": 90,
        "Messages": "(090): Xcom server connected"
    },
    91: {
        "Level": "V.O.",
        "Nr": 91,
        "Messages": "Warning (091): Update finished. Update software of other RCC/Xcom-232i"
    },
    92: {
        "Level": "V.O.",
        "Nr": 92,
        "Messages": "Error (092): More than 4 RCC or Xcom in the system"
    },
    93: {
        "Level": "V.O.",
        "Nr": 93,
        "Messages": "Error (093): More than 1 BSP in the system"
    },
    94: {
        "Level": "V.O.",
        "Nr": 94,
        "Messages": "Error (094): More than 1 Xcom-MS in the system"
    },
    95: {
        "Level": "V.O.",
        "Nr": 95,
        "Messages": "Error (095): More than 15 VarioTrack in the system"
    },
    121: {
        "Level": "V.O.",
        "Nr": 121,
        "Messages": "Error (121): Impossible communication with target device"
    },
    122: {
        "Level": "V.O.",
        "Nr": 122,
        "Messages": "Error (122): SD card corrupted"
    },
    123: {
        "Level": "V.O.",
        "Nr": 123,
        "Messages": "Error (123): SD card not formatted"
    },
    124: {
        "Level": "V.O.",
        "Nr": 124,
        "Messages": "Error (124): SD card not compatible"
    },
    125: {
        "Level": "V.O.",
        "Nr": 125,
        "Messages": "Error (125): SD card format not recognized. Should be FAT"
    },
    126: {
        "Level": "V.O.",
        "Nr": 126,
        "Messages": "Error (126): SD card write protected"
    },
    127: {
        "Level": "V.O.",
        "Nr": 127,
        "Messages": "Error (127): SD card, file(s) corrupted"
    },
    128: {
        "Level": "V.O.",
        "Nr": 128,
        "Messages": "Error (128): SD card file or directory could not be found"
    },
    129: {
        "Level": "V.O.",
        "Nr": 129,
        "Messages": "Error (129): SD card has been prematurely removed"
    },
    130: {
        "Level": "V.O.",
        "Nr": 130,
        "Messages": "Error (130): Update directory is empty"
    },
    131: {
        "Level": "V.O.",
        "Nr": 131,
        "Messages": "(131): The VarioTrack is configured for 12V batteries"
    },
    132: {
        "Level": "V.O.",
        "Nr": 132,
        "Messages": "(132): The VarioTrack is configured for 24V batteries"
    },
    133: {
        "Level": "V.O.",
        "Nr": 133,
        "Messages": "(133): The VarioTrack is configured for 48V batteries"
    },
    134: {
        "Level": "V.O.",
        "Nr": 134,
        "Messages": "(134): Reception level of the GSM signal"
    },
    137: {
        "Level": "V.O.",
        "Nr": 137,
        "Messages": "(137): VarioTrack master synchronization lost"
    },
    138: {
        "Level": "V.O.",
        "Nr": 138,
        "Messages": "Error (138): XT master synchronization lost"
    },
    139: {
        "Level": "V.O.",
        "Nr": 139,
        "Messages": "(139): Synchronized on VarioTrack master"
    },
    140: {
        "Level": "V.O.",
        "Nr": 140,
        "Messages": "(140): Synchronized on XT master"
    },
    141: {
        "Level": "V.O.",
        "Nr": 141,
        "Messages": "Error (141): More than 1 Xcom-SMS in the system"
    },
    142: {
        "Level": "V.O.",
        "Nr": 142,
        "Messages": "Error (142): More than 15 VarioString in the system"
    },
    143: {
        "Level": "V.O.",
        "Nr": 143,
        "Messages": "(143): Save parameter Xcom-SMS"
    },
    144: {
        "Level": "V.O.",
        "Nr": 144,
        "Messages": "(144): Save parameter VarioString"
    },
    145: {
        "Level": "V.O.",
        "Nr": 145,
        "Messages": "Error (145): SIM card blocked, PUK code required"
    },
    146: {
        "Level": "V.O.",
        "Nr": 146,
        "Messages": "Error (146): SIM card missing"
    },
    147: {
        "Level": "V.O.",
        "Nr": 147,
        "Messages": "Error (147): Install R532 firmware release prior to install an older release"
    },
    148: {
        "Level": "V.O.",
        "Nr": 148,
        "Messages": "(148): Datalogger function interrupted (SD card removed)"
    },
    149: {
        "Level": "V.O.",
        "Nr": 149,
        "Messages": "Error (149): Parameter setting incomplete"
    },
    150: {
        "Level": "V.O.",
        "Nr": 150,
        "Messages": "Error (150): Cabling error between PV and VarioString"
    },
    162: {
        "Level": "V.O.",
        "Nr": 162,
        "Messages": "Error (162): Communication loss with RCC or Xcom-232i"
    },
    163: {
        "Level": "V.O.",
        "Nr": 163,
        "Messages": "Error (163): Communication loss with Xtender"
    },
    164: {
        "Level": "V.O.",
        "Nr": 164,
        "Messages": "Error (164): Communication loss with BSP"
    },
    165: {
        "Level": "V.O.",
        "Nr": 165,
        "Messages": "Error (165): Communication loss with Xcom-MS"
    },
    166: {
        "Level": "V.O.",
        "Nr": 166,
        "Messages": "Error (166): Communication loss with VarioTrack"
    },
    167: {
        "Level": "V.O.",
        "Nr": 167,
        "Messages": "Error (167): Communication loss with VarioString"
    },
    168: {
        "Level": "V.O.",
        "Nr": 168,
        "Messages": "(168): Synchronized with VarioString master"
    },
    169: {
        "Level": "V.O.",
        "Nr": 169,
        "Messages": "(169): Synchronization with VarioString master lost"
    },
    170: {
        "Level": "V.O.",
        "Nr": 170,
        "Messages": "Warning (170): No solar production in the last 48h on PV1"
    },
    171: {
        "Level": "V.O.",
        "Nr": 171,
        "Messages": "Warning (171): No solar production in the last 48h on PV2"
    },
    172: {
        "Level": "V.O.",
        "Nr": 172,
        "Messages": "Error (172): FID change impossible. More than one unit."
    },
    173: {
        "Level": "V.O.",
        "Nr": 173,
        "Messages": "Error (173): Incompatible Xtender. Please contact Studer Innotec SA"
    },
    174: {
        "Level": "V.O.",
        "Nr": 174,
        "Messages": "(174): Inaccessible parameter, managed by the Xcom-CAN"
    },
    175: {
        "Level": "V.O.",
        "Nr": 175,
        "Messages": "Halted (175): Critical undervoltage"
    },
    176: {
        "Level": "V.O.",
        "Nr": 176,
        "Messages": "(176): Calibration setting lost"
    },
    177: {
        "Level": "V.O.",
        "Nr": 177,
        "Messages": "(177): An Xtender has started up"
    },
    178: {
        "Level": "V.O.",
        "Nr": 178,
        "Messages": "(178): No BSP. Necessary for programming with SOC"
    },
    179: {
        "Level": "V.O.",
        "Nr": 179,
        "Messages": "(179): No BTS or BSP. Necessary for programming with temperature"
    },
    180: {
        "Level": "V.O.",
        "Nr": 180,
        "Messages": "(180): Command entry activated"
    },
    181: {
        "Level": "V.O.",
        "Nr": 181,
        "Messages": "Error (181): Disconnection of BTS"
    },
    182: {
        "Level": "V.O.",
        "Nr": 182,
        "Messages": "(182): BTS/BSP battery temperature measurement used by a device"
    },
    183: {
        "Level": "V.O.",
        "Nr": 183,
        "Messages": "Halted (183): An Xtender has lost communication with the system"
    },
    184: {
        "Level": "V.O.",
        "Nr": 184,
        "Messages": "Error (184): Check phase orientation or circuit breakers state on AC-In"
    },
    185: {
        "Level": "V.O.",
        "Nr": 185,
        "Messages": "Warning (185): AC-In voltage level with delay too low"
    },
    186: {
        "Level": "V.O.",
        "Nr": 186,
        "Messages": "Halted (186): Critical undervoltage (fast)"
    },
    187: {
        "Level": "V.O.",
        "Nr": 187,
        "Messages": "Halted (187): Critical overvoltage (fast)"
    },
    188: {
        "Level": "V.O.",
        "Nr": 188,
        "Messages": "(188): CAN stage startup"
    },
    189: {
        "Level": "V.O.",
        "Nr": 189,
        "Messages": "Error (189): Incompatible configuration file"
    },
    190: {
        "Level": "V.O.",
        "Nr": 190,
        "Messages": "(190): The Xcom-SMS is busy"
    },
    191: {
        "Level": "V.O.",
        "Nr": 191,
        "Messages": "(191): Parameter not supported"
    },
    192: {
        "Level": "V.O.",
        "Nr": 192,
        "Messages": "(192): Unknown reference"
    },
    193: {
        "Level": "V.O.",
        "Nr": 193,
        "Messages": "(193): Invalid value"
    },
    194: {
        "Level": "V.O.",
        "Nr": 194,
        "Messages": "(194): Value too low"
    },
    195: {
        "Level": "V.O.",
        "Nr": 195,
        "Messages": "(195): Value too high"
    },
    196: {
        "Level": "V.O.",
        "Nr": 196,
        "Messages": "(196): Writing error"
    },
    197: {
        "Level": "V.O.",
        "Nr": 197,
        "Messages": "(197): Reading error"
    },
    198: {
        "Level": "V.O.",
        "Nr": 198,
        "Messages": "(198): User level insufficient"
    },
    199: {
        "Level": "V.O.",
        "Nr": 199,
        "Messages": "(199): No data for the report"
    },
    200: {
        "Level": "V.O.",
        "Nr": 200,
        "Messages": "Error (200): Memory full"
    },
    202: {
        "Level": "V.O.",
        "Nr": 202,
        "Messages": "Warning (202): Battery alarm arrives"
    },
    203: {
        "Level": "V.O.",
        "Nr": 203,
        "Messages": "(203): Battery alarm leaves"
    },
    204: {
        "Level": "V.O.",
        "Nr": 204,
        "Messages": "Error (204): Battery stop arrives"
    },
    205: {
        "Level": "V.O.",
        "Nr": 205,
        "Messages": "(205): Battery stop leaves"
    },
    206: {
        "Level": "V.O.",
        "Nr": 206,
        "Messages": "Halted (206): Board hardware incompatibility"
    },
    207: {
        "Level": "V.O.",
        "Nr": 207,
        "Messages": "(207): AUX1 relay activation"
    },
    208: {
        "Level": "V.O.",
        "Nr": 208,
        "Messages": "(208): AUX1 relay deactivation"
    },
    209: {
        "Level": "V.O.",
        "Nr": 209,
        "Messages": "(209): AUX2 relay activation"
    },
    210: {
        "Level": "V.O.",
        "Nr": 210,
        "Messages": "(210): AUX2 relay deactivation"
    },
    211: {
        "Level": "V.O.",
        "Nr": 211,
        "Messages": "(211): Command entry deactivated"
    },
    212: {
        "Level": "V.O.",
        "Nr": 212,
        "Messages": "Error (212): VarioTrack software incompatibility. Upgrade needed"
    },
    213: {
        "Level": "V.O.",
        "Nr": 213,
        "Messages": "(213): Battery current limitation by the BSP stopped"
    },
    214: {
        "Level": "V.O.",
        "Nr": 214,
        "Messages": "Warning (214): Half period RMS voltage limit exceeded, transfer opened"
    },
    215: {
        "Level": "V.O.",
        "Nr": 215,
        "Messages": "Warning (215): UPS limit reached, transfer opened"
    },
    216: {
        "Level": "V.O.",
        "Nr": 216,
        "Messages": "Warning (216): Scom watchdog caused the reset of Xcom-232i"
    },
    217: {
        "Level": "V.O.",
        "Nr": 217,
        "Messages": "Warning (217): CAN problem at Xtender declaration"
    },
    218: {
        "Level": "V.O.",
        "Nr": 218,
        "Messages": "Warning (218): CAN problem while writing parameters"
    },
    222: {
        "Level": "V.O.",
        "Nr": 222,
        "Messages": "(222): Front ON/OFF button pressed"
    },
    223: {
        "Level": "V.O.",
        "Nr": 223,
        "Messages": "(223): Main OFF detected"
    },
    224: {
        "Level": "V.O.",
        "Nr": 224,
        "Messages": "(224): Delay before closing transfer relay in progress {1580}"
    },
    225: {
        "Level": "V.O.",
        "Nr": 225,
        "Messages": "Error (225): Communication with lithium battery lost"
    },
    226: {
        "Level": "V.O.",
        "Nr": 226,
        "Messages": "(226): Communication with lithium battery restored"
    },
    227: {
        "Level": "V.O.",
        "Nr": 227,
        "Messages": "Error (227): Overload on high voltage DC side"
    },
    228: {
        "Level": "V.O.",
        "Nr": 228,
        "Messages": "Error (228): Startup error"
    },
    229: {
        "Level": "V.O.",
        "Nr": 229,
        "Messages": "Error (229): Short-circuit on high voltage DC side"
    },
}

# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------- End of 1. Appendix ----------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
