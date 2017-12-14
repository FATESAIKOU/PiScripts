#!/usr/bin/env python3
import RPi.GPIO as GPIO
import sys
import random
import time


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

    while False:
        now_pins = random.sample(PINS, random.randint(1, 3))
        print("Use Pin:", now_pins)
    
        print("Setup Pins")
        setupPin(now_pins)
        time.sleep(random.uniform(0.1, 0.7))
    
        print("setoff Pins")
        setoffPin(now_pins)
    
    GPIO.cleanup()


if __name__ == '__main__':
    main()
