#!/usr/bin/env python3

import time

# ctl_alt+del space ctl+alt+del space backspace backspace username enter space password enter
NULL_CHAR = chr(0)
SPACE = NULL_CHAR*2+chr(44)+NULL_CHAR*5
UNAME = "jgroenda"
PSSWD = "av5Workcc"

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def release_keys():
    time.sleep(0.3)
    write_report(NULL_CHAR*8)

def ctrl_alt_del():
    time.sleep(0.2)
    write_report(chr(5)+NULL_CHAR+chr(76)+NULL_CHAR*5)
    release_keys()

def space():
    time.sleep(0.1)
    write_report(NULL_CHAR*2+chr(44)+NULL_CHAR*5)
    release_keys()

def backspace():
    time.sleep(0.2)
    write_report(NULL_CHAR*2+chr(42)+NULL_CHAR*5)
    release_keys()

def enter():
    time.sleep(0.2)
    write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)
    release_keys()

def type_out(str_to_type):
    for char in str_to_type:
        time.sleep(0.1)
        modifiers = 0
        if char.isdigit():
            if char == '0':
                keycode = 0x27
            else:
                keycode = int(char) + 0x1D
        elif char.islower():
            keycode = ord(char) - ord('a') + 0x04
        elif char.isupper():
            keycode = ord(char) - ord('A') + 0x04
            modifiers = 0x20  # shift key pressed
        else:
            keycode = ord(char)

        write_report(chr(modifiers)+NULL_CHAR*2+chr(keycode)+NULL_CHAR*5)
        release_keys()

space()
backspace()
ctrl_alt_del()
time.sleep(3)
space()
time.sleep(3)
ctrl_alt_del()
time.sleep(3)
space()
time.sleep(3)
backspace()
backspace()
backspace()
type_out(UNAME)
enter()
time.sleep(3)
space()
time.sleep(3)
backspace()
type_out(PSSWD)
enter()
time.sleep(5)
