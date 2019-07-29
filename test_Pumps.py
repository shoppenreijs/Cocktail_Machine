#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 21:53:02 2019

@author: Stan
"""

import RPi.GPIO as GPIO
import time

pump_ch = [21, 20, 16, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pump_ch, GPIO.OUT, initial=GPIO.HIGH)

GPIO.output(pump_ch[1], GPIO.LOW)
time.sleep(10)
GPIO.output(pump_ch[1], GPIO.HIGH)

GPIO.output(pump_ch[2], GPIO.LOW)
time.sleep(10)
GPIO.output(pump_ch[2], GPIO.HIGH)

GPIO.output(pump_ch[3], GPIO.LOW)
time.sleep(10)
GPIO.output(pump_ch[3], GPIO.HIGH)

GPIO.cleanup()