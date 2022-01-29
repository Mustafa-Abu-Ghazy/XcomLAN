# -*- coding: utf-8 -*-
"""
This file contains definition/implementation of the Connection-Class that Handles the SCOM serial connection.
Inspired from and Based on hesso-valais/scom : scom.py
<https://github.com/hesso-valais/scom/blob/0.7.3/src/sino/scom/scom.py>
"""

import logging

import serial
from sino import scom


# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------  Scom Class  --------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class Scom(scom.Scom):
    """
    Handles the SCOM serial connection.
    """

    def __init__(self, node_name):
        super(Scom, self).__init__()
        self._node_name = node_name
        self.log = logging.getLogger(__name__ + ":" + self._node_name)

    @property
    def node_name(self):
        """
        Returns the Node Name.

        :return:
        """
        return self._node_name

    def initialize(self, com_port: str, baudrate: str or int = 115200, parity=serial.PARITY_NONE):
        """
        Initializes the instance and connects to the given COM port.
        Note Default Setting if Xcom-232i is configured as Xcom-LAN {baudrate= 115200, parity=serial.PARITY_NONE}

        :param parity:
        :param com_port Name of the COM port. Ex. '/dev/ttyUSB0', 'COM1', etc.
        :param baudrate Baud rate of the COM port. Default value is '38400'
        """
        try:
            # change: serial.Serial(port=) to serial.serial_for_url(url=) if the provided value fit to be a url
            # So you should set the 'com_port' in the config for initialize the DeviceManager to be like
            # 'scom': { 'interface': 'COM1', .....}
            # 'scom': { 'interface': 'socket://<host>:<port>', .....}
            # 'scom': { 'interface': 'rfc2217://<host>:<port>',  .....}

            if "://" in com_port:
                self._ser = serial.serial_for_url(url=com_port, baudrate=baudrate, parity=parity)
            else:
                self._ser = serial.Serial(port=com_port, baudrate=baudrate, parity=parity)

            # Set RX timeout
            self._ser.timeout = 1  # second
        except Exception as msg:
            self.log.info(msg)
            exit()

# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------  End of Scom Class  ----------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
