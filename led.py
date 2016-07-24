#!/usr/bin/python
import os
import time
import CHIP_IO.GPIO as GPIO


for n in range(0,7):
    GPIO.setup("CSID" + str(n), GPIO.OUT)

while True:
    for n in range(0,7):
        print n
        input()
        GPIO.output("CSID" + str(n), not GPIO.input("CSID" + str(n)))
        time.sleep(0.1)



