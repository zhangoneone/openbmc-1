#!/bin/sh

echo "Initial CMC Config"
#Unblock command
/usr/local/bin/ipmb-util 8 0x68 0xd8 0xf2 0x00 0xff 0x00