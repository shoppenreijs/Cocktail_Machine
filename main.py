#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:32:40 2019

@author: Stan
"""

import RPi.GPIO as GPIO                    
import time                                
from mylibs.relay.py import PumpRelay
from mylibs.HC_SR04 import Stock_Sensor
from mylibs.cocktail_gen import Cocktail_Generator

cocktail = Cocktail_Generator( cocktail_name = 'mix1', volume = 0.1 )
pump_ch = [21, 20, 16, 26]                              #Relay channels
HC_SR04_ch = [[23, 24], [17, 18], [27,22], [13,19]]     #[TRIG, ECHO] sensor pair
pump_control = PumpRelay(pump_ch)
stock_amount = HC_SR04( HC_SR04_ch )


    
    
    try:
        motor_on(motor1)
        print('motor1 on')
        time.sleep(2)
        motor_off(motor1)
        print('motor1 off')
        time.sleep(2)
        motor_on(motor2)
        print('motor2 on')
        time.sleep(1)
        motor_off(motor2)
        print('motor2 off')
        time.sleep(1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()