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
from pumps import Pump_relay
from HC_SR04 import Stock_sensor
#from cocktail_gen import Cocktail_Generator

#cocktail = Cocktail_Generator( cocktail_name = 'mix1', volume = 0.1 )

## define input/output channels
pump_ch = [21, 20, 16, 26]                              #Relay channels
stock_ch = [[23, 24], [17, 18], [27,22], [13,19]]     #[TRIG, ECHO] sensor pair

## initialize pumps
pumps = []
for idx in pump_ch:
    pump = Pump_relay( idx )
    pumps.append( pump )
 
## initialize HC_SR04 sensors
stock = []
for idx in stock_ch:
    single_stock = Stock_sensor( idx )
    stock.append( single_stock )

### initialize stock height
#for idx in range( len(stock) ):
#    stock[idx].initialize_height()    

#stock[0].initialize_height()

## Test stock sensors
print( stock[0].read_distance() ) 
#print( stock[1].read_distance() ) 
#print( stock[2].read_distance() ) 
#print( stock[3].read_distance() ) 

## Test pumps
for i in pumps:
    pumps[i].on()
    time.sleep(4)
    pumps[i].off()    
    

## Ending GPIO
GPIO.cleanup() 