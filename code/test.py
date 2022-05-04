#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
#此程序可以点亮LED灯
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
try:
    while True:
        GPIO.output(18,GPIO.HIGH)
except:
    GPIO.cleanup()
