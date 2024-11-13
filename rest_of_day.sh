#!/bin/bash

NOON=$(($(date +%s -d "12:00")/60))
ONE=$(($(date +%s -d "12:57")/60))
FIVE=$(($(date +%s -d "17:00")/60))

NOW=$(($( date +%s )/60))
if [ $NOW -lt $NOON ]
then
	MINS=$(($NOON-$NOW))
	echo "keeping active until lunch: ${MINS} mins"
	python3 /home/pi/usbDevice/wait_random.py
	python3 /home/pi/usbDevice/log_in.py
	python3 /home/pi/usbDevice/keep_active_for.py $MINS
	python3 /home/pi/usbDevice/wait_random.py
	python3 /home/pi/usbDevice/keep_active_for.py 1
fi

NOW=$(($( date +%s )/60))
if [ $NOW -lt $ONE ]
then
	MINS=$(($ONE-$NOW))
	echo "on lunch for ${MINS} mins"
	sleep $(($MINS*60))
fi

NOW=$(($( date +%s )/60))
if [ $NOW -lt $FIVE ]
then
	MINS=$(($FIVE-$NOW))
	echo "keeping active until end of day: ${MINS} mins"
	python3 /home/pi/usbDevice/wait_random.py
	python3 /home/pi/usbDevice/log_in.py
	python3 /home/pi/usbDevice/keep_active_for.py $MINS
fi
