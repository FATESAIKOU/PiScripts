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
    pwms = []
    for ledPin in pins:
        GPIO.setup(ledPin, GPIO.OUT)
        t_pwm = GPIO.PWM(ledPin, 500)
        t_pwm.start(100)
        
        pwms.append(t_pwm)

    return pwms
        

def setPin(pwms, duties):
    for i in range(len(pwms)):
        pwms[i].ChangeDutyCycle(duties[i])


def main():
    PINS = [int(s) for s in sys.argv[1:]]

    print("Init Env")
    initEnv()
    pwms = initPin(PINS)

    signal.signal(signal.SIGINT, end_handler)

    while shining:
        duties = [random.randint(0, 100) for _ in range(len(pwms))]
        print("Use Duties:", duties)
    
        print("Setup Pins")
        setPin(pwms, duties)
        time.sleep(random.uniform(0.1, 0.7))

    
    print("Setoff Pins")
    setPin(pwms, [0] * len(pwms))
    GPIO.cleanup()


if __name__ == '__main__':
    main()
