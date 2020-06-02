#!/usr/bin/env python
# -*- coding: utf-8 -*-


import errno
import sys
import os
import struct
from ctypes import (CDLL, get_errno)
from ctypes.util import find_library
import socket

#     AF_BLUETOOTH,
#     SOCK_RAW,
#     BTPROTO_HCI,
#     SOL_HCI,
#     HCI_FILTER,
# )

print(os.getuid())
if not os.geteuid() == 501:
    sys.exit("script only works as root")

btlib = find_library("bluetooth")
print(btlib)
if not btlib:
    raise Exception(
        "Can't find required bluetooth libraries"
        " (need to install bluez)"
    )
bluez = CDLL(btlib, use_errno=True)

dev_id = bluez.hci_get_route(None)

sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_RAW, socket.BTPROTO_HCI)
sock.bind((dev_id,))

err = bluez.hci_le_set_scan_parameters(sock.fileno(), 0, 0x10, 0x10, 0, 0, 1000)
if err < 0:
    raise Exception("Set scan parameters failed")
    # occurs when scanning is still enabled from previous call

# allows LE advertising events
hci_filter = struct.pack(
    "<IQH",
    0x00000010,
    0x4000000000000000,
    0
)
sock.setsockopt(socket.SOL_HCI, socket.HCI_FILTER, hci_filter)

err = bluez.hci_le_set_scan_enable(
    sock.fileno(),
    1,  # 1 - turn on;  0 - turn off
    0,  # 0-filtering disabled, 1-filter out duplicates
    1000  # timeout
)
if err < 0:
    errnum = get_errno()
    raise Exception("{} {}".format(
        errno.errorcode[errnum],
        os.strerror(errnum)
    ))

while True:
    data = sock.recv(1024)
    # print bluetooth address from LE Advert. packet
    print(':'.join("{0:02x}".format(x) for x in data[12:6:-1]))
