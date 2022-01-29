Package **XcomLAN**
===================

Python library to access Studer-Innotec Xcom-LAN/Xcom-232i node through (SCOM) Xtender Serial Protocol over a TCP/IP
Network connection.

Prerequisites
-------------

Please read the complete documentation available on : Studer Innotec SA -> Support -> Download Center ->
Software and Updates -> Communication protocols Xcom-232i

Installation
------------
The Package can be installed from the Python package manager. Simply execute in a console the following command:

```bash
  $ pip install XcomLAN
```

or , if you will use the attached ThingsBoardClient

```bash
  $ pip install XcomLAN[ThingsBoard]
```

Getting Started
----------------

- copy the example code [example.py](https://github.com/Mustafa-Abu-Ghazy/XcomLAN/blob/master/example.py)
- setup the Xcom-232i device in Xcom-LAN mode.
- configure the MOXA-NPort Operation Mode

```
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
```

- define your own NODES_LIST

```python
NODES_LIST = {
    "N01": {"interface": "<SERIAL_VIRTUAL_PORT>",
            # ...
            },
    "N02": {"interface": "rfc2217://<host>:<port>",
            # ...
            },
    "N03": {"interface": "socket://<host>:<port>",
            # ...
            },
    # ...
}
```

- create .env file like

```
THINGSBOARD_SERVER=<your tb host>>
GATEWAY_Access_TOKEN=<your tb gatway-device access-token>

READINGS_DELAY_IN_SECONDS=60
```
- run the script, and start to design your own TB dashboards based on the received telemetry
- the examble code by default have some infos of interst per device type, and address ranges for devices to be discovered.
it will auto discover all possible XT, VT, VS, BSP device in the node.

Warnings
--------
- make sure scom package has been installed successfully, you might be required to move the two files
  from the site-packages directory to site-packages\sino\scom directory
  - baseframe.*.pyd|so
  - property.*.pyd|so

TODO
----
- enhance documentations
- add full features list

Authors
-------

- **Mustafa M. A. U. AbuGhazy**

License
-------

This project is licensed under the MIT License - see the `LICENSE` file for details


Credits
-------

Thanks for [HES-SO Valais-Wallis](https://github.com/hesso-valais)
for their great package [scom](https://pypi.org/project/scom/). As I've developed this package by inspiration of **
scom** and depend on it.

External References:
--------------------

- [Studer-Innotec](https://www.studer-innotec.com)
- [Studer-Innotec -> xcom485i Package](https://github.com/studer-innotec/xcom485i.git)
- [Studer-Innotec -> xcomcan Package](https://github.com/studer-innotec/xcomcan.git)
- [HES-SO Valais-Wallis -> scom Package](https://github.com/hesso-valais/scom.git)