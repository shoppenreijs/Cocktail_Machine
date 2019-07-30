#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:25:42 2019

@author: Stan
"""

import RPi.GPIO as GPIO

class Pump_relay:
    
    def __init__ ( self, pump_ch ):
    
        self.pin = pump_ch
        GPIO.setmode( GPIO.BCM )
        GPIO.setup( pump_ch, GPIO.OUT, initial=GPIO.HIGH )
    
    
    def on( self ):
        GPIO.output( self.pin, GPIO.LOW)  # Turn motor on
    
    
    def off( self ):
        GPIO.output( self.pin, GPIO.HIGH)  # Turn motor off
    
    

