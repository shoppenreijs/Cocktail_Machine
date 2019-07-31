#!/usr/bin/env python

# Control HC-SR04 ultrasone sensor from Raspberry Pi
# https://raspberrytips.nl/hc-sr04-ultrasone-sensor/

import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
import math


class Stock_sensor:
    
    ## Initialize GPIO for stock sensor
    #
    #  @param  HC_SR04_ch   Sensor channels [TRIG, ECHO]
    def __init__ ( self, HC_SR04_ch ):
        
        GPIO.setmode( GPIO.BCM )                          #Set GPIO pin numbering 
        
        self.TRIG = HC_SR04_ch[0]
        self.ECHO = HC_SR04_ch[1]
        self.init_distance_list = []

        GPIO.setup( self.TRIG, GPIO.OUT, initial=False )  #Set pin TRIG as GPIO out and value LOW
        GPIO.setup( self.ECHO, GPIO.IN )                  #Set pin ECHO as GPIO in
    
    ## Initialize stock height 
    #
    def initialize_height ( self ):
        
        self.init_height = self.read_distance()  #Read out initial distance
        print(self.init_height)
    
    ## Readout stock height
    #
    #  @return       stock height
    def read_distance ( self ):
        
      GPIO.output( self.TRIG, True )             #Set TRIG as HIGH
      time.sleep( 0.00001 )                      #Delay of 0.00001 seconds
      GPIO.output( self.TRIG, False )            #Set TRIG as LOW
    
      while GPIO.input( self.ECHO )==0:          #Check whether the ECHO is LOW
        pulse_start = time.time()                #Saves the last known time of LOW pulse
    
      while GPIO.input( self.ECHO )==1:          #Check whether the ECHO is HIGH
        pulse_end = time.time()                  #Saves the last known time of HIGH pulse 
    
      pulse_duration = pulse_end - pulse_start   #Get pulse duration to a variable
    
      distance = pulse_duration * 17150          #Multiply pulse duration by 17150 to get distance
      distance = round(distance, 3)              #Round to two decimal points
    
      if distance > 2 and distance < 400:        #Check whether the distance is within range
        return distance 
      else:
        print("Sensor out Of Range")             #display out of range
      

    ## Calc stock volume
    #
    #  @return  Stock volume
    def calc_volume ( self ):
        diameter = 0.075    # [m]
        area = math.pi * diameter
        height = self.read_distance()
        volume = area * abs( height - self.init_height )
        
        #hier oplette dat initial distance list bijgewerkt wordt als de juiste hoeveelheid volume is verpompt. 
        self.init_height = height
        
        return volume
        