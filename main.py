#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:32:40 2019

@author: Stan
"""

import RPi.GPIO as GPIO                    
import time
import sys

sys.path.insert(0, '/home/pi/Cocktail_Machine/mylibs')                                
#from relay import PumpRelay
from pumps import Pumps
#from HC_SR04 import Stock_Sensor
#from cocktail_gen import Cocktail_Generator

#cocktail = Cocktail_Generator( cocktail_name = 'mix1', volume = 0.1 )
pump_ch = [21, 20, 16, 26]                              #Relay channels

HC_SR04_ch = [[23, 24], [17, 18], [27,22], [13,19]]     #[TRIG, ECHO] sensor pair
#pumps = PumpRelay( pump_ch )
#stock_amount = Stock_Sensor( HC_SR04_ch )

pump1 = Pumps( pump_ch[1] )
 

pumps = []
for i in pump_ch:
    pump = Pumps( i )
    pumps.append( pump )
    

## Test pumps
pumps[0].on()
time.sleep(4)
pumps[0].off()    
    
pump1.on()
time.sleep(4)
pump1.off()

#pumps.motor_on( pump_ch[2] )
#time.sleep(4)
#pumps.motor_off( pump_ch[2] )
#
#pumps.motor_on( pump_ch[3] )
#time.sleep(4)
#pumps.motor_off( pump_ch[3] )
#
#pumps.motor_on( pump_ch[4] )
#time.sleep(4)
#pumps.motor_off( pump_ch[4] )

GPIO.cleanup() 