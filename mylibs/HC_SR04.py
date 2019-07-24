#!/usr/bin/env python

# Control HC-SR04 ultrasone sensor from Raspberry Pi
# https://raspberrytips.nl/hc-sr04-ultrasone-sensor/

import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
import math


class Stock_Sensor:
    
    def __init__ ( self, HC_SR04_ch ):
        
        GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
        self.HC_SR04_ch = HC_SR04_ch
        self.init_distance_list = []
        
        for i in HC_SR04_ch:                              #Associate pin 24 to ECHO
            GPIO.setup(i[0],GPIO.OUT, initial=False)      #Set pin TRIG as GPIO out and value LOW
            GPIO.setup(i[1],GPIO.IN)                      #Set pin ECHO as GPIO in
            init_height = self.read_distance(i)           #Read out initial distance
            self.init_distance_list.append(init_height)   #save intial distance 


    def read_distance ( self, idx ):
        
      TRIG = self.HC_SR04_ch[idx][0]
      ECHO = self.HC_SR04_ch[idx][1]
      GPIO.output(TRIG, True)                  #Set TRIG as HIGH
      time.sleep(0.00001)                      #Delay of 0.00001 seconds
      GPIO.output(TRIG, False)                 #Set TRIG as LOW
    
      while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse
    
      while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 
    
      pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
    
      distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
      distance = round(distance, 3)            #Round to two decimal points
    
      if distance > 2 and distance < 400:      #Check whether the distance is within range
        print("Distance:",distance - 0.5,"cm")  #Print distance with 0.5 cm calibration
      else:
        print("Out Of Range")                   #display out of range
        
      self.reset_sensor(TRIG)
      
      return distance
        
    def reset_sensor (self, TRIG):
        GPIO.output(TRIG, False)
        
    def calc_volume (self, idx ):
        diameter = 0.075    # [m]
        area = math.pi * diameter
        height = self.read_distance()
        volume = area * abs( height - self.init_distance_list[idx] )
        
        #hier oplette dat initial distance list bijgewerkt wordt als de juiste hoeveelheid volume is verpompt. 
        return volume
        