# -*- coding: utf-8 -*-
#
"""
Example showing how to use the SCOM DeviceManager to find Studer devices
on the SCOM bus.

The following Example tries to detect some Xtender's. For each
Xtender device found the software version is then print out.

Then loop on them to read the required infos/telemetry from (XT, VT, BSP) devices and push it to ThingsBoard
"""
import copy
import logging
import os
import threading
import time

import serial
from dotenv import load_dotenv

from XcomLAN.device import BSP_DEVICE_ID_DEFAULT_SCAN_RANGE
from XcomLAN.device import DeviceType
from XcomLAN.device import RCC_DEVICE_ID_DEFAULT_SCAN_RANGE
from XcomLAN.device import VS_DEVICE_ID_DEFAULT_SCAN_RANGE
from XcomLAN.device import VT_DEVICE_ID_DEFAULT_SCAN_RANGE
from XcomLAN.device import XT_DEVICE_ID_DEFAULT_SCAN_RANGE
from XcomLAN.node_manager import NodeManager
from XcomLAN.node_manager import NodeObserver
from XcomLAN.thingsboard import ThingsBoardClient

# ----------------------------------------------------------------------------------------------------------------------
# Load & Set Environment Variables:
# ---------------------------------
load_dotenv()  # Load Environment Variables From The .env File

THINGSBOARD_SERVER = os.environ.get("THINGSBOARD_SERVER", "localhost")
GATEWAY_Access_TOKEN = os.environ.get("GATEWAY_Access_TOKEN")

NODES_LIST = {
    "N01": {"interface": "COM10",  # "rfc2217://10.210.3.11:4001",
            "longitude": 0,
            "latitude": 0
            },
    "N02": {"interface": "COM12", "longitude": 0, "latitude": 0},
    "N03": {"interface": None, "longitude": 0, "latitude": 0},
    "N04": {"interface": None, "longitude": 0, "latitude": 0},
    "N05": {"interface": None, "longitude": 0, "latitude": 0},
}

# SCOM Template Node Configuration
XCOM_LAN_CONFIG_TEMPLATE = {
    "scom": {
        "interface": None,
        """
            Test Succeed:
                # MOXA-NPort Operation Mode: RFC2217
                "interface": "rfc2217://<host>:<port>",
            Test Failed:
                # MOXA-NPort Operation Mode: TCP Server
                "interface": "socket://<host>:<port>",
            Test Succeed:
                # MOXA-NPort Operation Mode: TCP Server,
                # And Use Any COM Mapping Tool like "TCP-Com.exe" as TCP-Client connects on <host>:<port>
                #       -->{BaudRate: 115200, Parity: None, StopBits: 1, DataBits: 8}
                "interface": "<SERIAL_VIRTUAL_PORT>",
            Test Succeed:
                # MOXA-NPort Operation Mode: RealCOM,
                # And Use MOXA drivers/COM Mapping Tool
                #       -->{BaudRate: 115200, Parity: None, StopBits: 1, DataBits: 8}
                "interface": "<SERIAL_VIRTUAL_PORT>",
        """
        "baudrate": 115200,
        "parity": serial.PARITY_NONE
    },
    "scom-device-address-scan": {
        DeviceType.XTENDER: XT_DEVICE_ID_DEFAULT_SCAN_RANGE,
        DeviceType.VARIO_TRACK: VT_DEVICE_ID_DEFAULT_SCAN_RANGE,
        DeviceType.VARIO_STRING: VS_DEVICE_ID_DEFAULT_SCAN_RANGE,
        DeviceType.RCC: RCC_DEVICE_ID_DEFAULT_SCAN_RANGE,
        DeviceType.BSP: BSP_DEVICE_ID_DEFAULT_SCAN_RANGE
    }
}

READINGS_DELAY_IN_SECONDS = int(os.environ.get("READINGS_DELAY_IN_SECONDS", 60))
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Enable & Setup Logging:
# -----------------------
logging.basicConfig(
    format="%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO
)


# ----------------------------------------------------------------------------------------------------------------------


def get_list_of_user_infos_of_interest(device):
    # list_of_user_infos_of_interest_for_single_xt = list(XTENDER_INFOS.keys()) # Succeed without 3169
    list_of_user_infos_of_interest_for_single_xt = [3090, 3113, 3116, 3098, 3097, 3110, 3122,
                                                    3010, 3028, 3020, 3086, 3054, 3055, 3092,
                                                    3095, 3119, 3101, 3103]
    # list_of_user_infos_of_interest_for_multicast_xt = list(XTENDER_INFOS.keys()) # Succeed for group of one XT
    list_of_user_infos_of_interest_for_multicast_xt = []

    # list_of_user_infos_of_interest_for_single_vt = list(VARIO_TRACK_INFOS.keys())  # Succeed
    list_of_user_infos_of_interest_for_single_vt = [11000, 11043, 11043, 11016, 11045, 11041,
                                                    11040, 11039, 11038, 11082, 11061, 11062]
    # list_of_user_infos_of_interest_for_multicast_vt = list(VARIO_TRACK_INFOS.keys())  # Succeed
    list_of_user_infos_of_interest_for_multicast_vt = [11043, ]

    # list_of_user_infos_of_interest_for_single_vs = list(VARIO_STRING_INFOS.keys())  # Succeed
    list_of_user_infos_of_interest_for_single_vs = [15061, 15013, 15065, 15058, 15054, 15057, 15002, 15111,
                                                    15088, 15089]
    # list_of_user_infos_of_interest_for_multicast_vs = list(VARIO_STRING_INFOS.keys())  # Succeed
    list_of_user_infos_of_interest_for_multicast_vs = [15061, ]

    # list_of_user_infos_of_interest_for_single_bsp = list(BSP_INFOS.keys()) # Succeed
    list_of_user_infos_of_interest_for_single_bsp = [7030, 7031, 7032, 7033]

    list_of_user_infos_of_interest = []
    if device.device_type == DeviceType.XTENDER:
        if device.is_multicast_device:
            list_of_user_infos_of_interest = list_of_user_infos_of_interest_for_multicast_xt
        else:
            list_of_user_infos_of_interest = list_of_user_infos_of_interest_for_single_xt
    elif device.device_type == DeviceType.VARIO_TRACK:
        if device.is_multicast_device:
            list_of_user_infos_of_interest = list_of_user_infos_of_interest_for_multicast_vt
        else:
            list_of_user_infos_of_interest = list_of_user_infos_of_interest_for_single_vt
    elif device.device_type == DeviceType.VARIO_STRING:
        if device.is_multicast_device:
            list_of_user_infos_of_interest = list_of_user_infos_of_interest_for_multicast_vs
        else:
            list_of_user_infos_of_interest = list_of_user_infos_of_interest_for_single_vs
    elif device.device_type == DeviceType.BSP:
        list_of_user_infos_of_interest = list_of_user_infos_of_interest_for_single_bsp
    return list_of_user_infos_of_interest


def invoke_read_user_infos_as_telemetry(things_board_client, node_name, device, list_of_user_infos_of_interest):
    things_board_client.node_telemetry_enqueue(
        node_name=node_name,
        timestamp=int(round(time.time() * 1000)),
        telemetry_values=device.read_user_infos_as_telemetry(list_of_user_infos_of_interest)
    )


if __name__ == "__main__":
    things_board_client = ThingsBoardClient(THINGSBOARD_SERVER, GATEWAY_Access_TOKEN)

    nodes_observers = []
    for node_name, node_dict in NODES_LIST.items():
        try:
            # Try to create NodeManager & NodeObserver and connect to the interface
            if node_dict["interface"]:
                # Prepare SCOM Node Configuration
                config = XCOM_LAN_CONFIG_TEMPLATE
                config["scom"]["interface"] = node_dict.get("interface")
                # Create node manager detecting devices on the SCOM bus
                node_manager = NodeManager(node_name=node_name, config=config)
                # Create observer waiting for NodeManager notifications
                node_observer = NodeObserver(node_manager)
                nodes_observers.append(node_observer)
        except Exception as e:
            logging.error("Can't connect to the node: " + node_name)
            logging.exception(e)

    # This loop reads the required infos from (XT, VT, BSP) and push it to ThingsBoard
    while True:
        for node_observer in nodes_observers:
            # Use Copy to avoid "RuntimeError: dictionary changed size during iteration"
            connected_devices = copy.copy(node_observer.connected_devices)
            for device_address, device in connected_devices.items():
                thread = threading.Thread(target=invoke_read_user_infos_as_telemetry, args=(
                    things_board_client,
                    node_observer.node_name,
                    device,
                    get_list_of_user_infos_of_interest(device)
                ))
                thread.setDaemon(True)
                thread.start()

        time.sleep(READINGS_DELAY_IN_SECONDS)
