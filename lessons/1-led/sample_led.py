#!/usr/bin/env python3
"""
This is a program for simple led control on RasberryPi(R)

@author: FATESAIKOU
@argv[1:]: ALL Pins for using
"""

import RPi.GPIO as GPIO
import sys
import random
import time
import signal

shining = True

def end_handler(signal, frame):
    global shining
    print("end of shining")
    shining = False

def initEnv():
    GPIO.setmode(GPIO.BOARD)

def initPin(pins):
    for ledPin in pins:
        GPIO.setup(ledPin, GPIO.OUT)

def setupPin(pins):
    for ledPin in pins:
        GPIO.output(ledPin, True)

def setoffPin(pins):
    for ledPin in pins:
        GPIO.output(ledPin, False)

def main():
    PINS = [int(s) for s in sys.argv[1:]]

    print("Init Env")
    initEnv()
    initPin(PINS)

    signal.signal(signal.SIGINT, end_handler)

    while shining:
        now_pins = random.sample(PINS, random.randint(1, len(PINS)))
        print("Use Pin:", now_pins)
    
        print("Setup Pins")
        setupPin(now_pins)
        time.sleep(random.uniform(0.1, 0.7))
    
        print("setoff Pins")
        setoffPin(now_pins)
    
    GPIO.cleanup()


if __name__ == '__main__':
    main()
