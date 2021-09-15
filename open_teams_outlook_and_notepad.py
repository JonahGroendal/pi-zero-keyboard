#!/usr/bin/env python3

import time

NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def wait_then_release_keys():
	time.sleep(0.1)
	write_report(NULL_CHAR*8)

def type_out(str_to_type):
	for char in str_to_type:
		time.sleep(0.1)
		# press letter's key
		write_report(NULL_CHAR*2+chr(ord(char)-93)+NULL_CHAR*5)
		wait_then_release_keys()

def open_from_windows_menu(search_str):
	# press esc key in case windows menu is already open
	write_report(NULL_CHAR*2+chr(41)+NULL_CHAR*5)
	wait_then_release_keys()
	# press windows key
	write_report(chr(8)+NULL_CHAR*7)
	wait_then_release_keys()
	time.sleep(1)
	# type out name of program
	type_out(search_str)
	# press enter
	write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)
	wait_then_release_keys()

open_from_windows_menu("teams")
time.sleep(5)
open_from_windows_menu("outlook")
time.sleep(5)
open_from_windows_menu("notepad")

