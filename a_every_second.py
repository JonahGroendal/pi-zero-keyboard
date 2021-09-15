#!/usr/bin/env python3

import time

NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

while True:
	# press a
	write_report(NULL_CHAR*2+chr(4)+NULL_CHAR*5)
	# release all keys
	write_report(NULL_CHAR*8)
	# wait one second
	time.sleep(1)
