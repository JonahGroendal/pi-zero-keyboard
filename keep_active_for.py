#!/usr/bin/env python3

import time
import sys

NULL_CHAR = chr(0)

if len(sys.argv) != 2:
	print("Invalid number of arguments. You must supply the number of minutes.")
	sys.exit(1)


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

for x in range(int(sys.argv[1])):
	# press a
	write_report(NULL_CHAR*2+chr(4)+NULL_CHAR*5)
	# release all keys
	write_report(NULL_CHAR*8)
	# wait one minute
	time.sleep(60)
