#!/usr/bin/env python3
import time
import sys
import os
import Adafruit_DHT as DHT


def main():
    BCM_PIN    = int(sys.argv[1])
    TOTAL_TIME = float(sys.argv[2])
    DELAY      = float(sys.argv[3])


    iter_num = int(TOTAL_TIME / DELAY)
    for i in range(iter_num):
        h, t = DHT.read_retry(11, BCM_PIN)
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t, h))

        time.sleep(DELAY)

if __name__ == "__main__":
    main()
