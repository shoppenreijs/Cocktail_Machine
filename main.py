#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:32:40 2019

@author: Stan
"""

import RPi.GPIO as GPIO                    
import time
import sys
import paho.mqtt.client as mqttClient

sys.path.insert(0, '/home/pi/Cocktail_Machine/mylibs')                                
#from relay import PumpRelay
from pumps import Pump_relay
from HC_SR04 import Stock_sensor
from programs import clean_motors
from cocktail_gen import Cocktail_Generator
#from SubscribeCloudMQTT import *

## define input/output channels
pump_ch = [21, 20, 16, 26]                              #Relay channels
stock_ch = [[27,22], [23, 24]]#, [17, 18], [13,19]]     #[TRIG, ECHO] sensor pair

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
    time.sleep(0.01)
    
## initialize stock height
for idx in range( len(stock) ):
    stock[idx].initialize_height()
    time.sleep(0.01)
    

stock[0].initialize_height()
print('check0')
stock[1].initialize_height()
print('check1')

#for i in range(len(pump_ch)):
#    pumps[i].on()
#    time.sleep(5)   #self.pumptimes[i])
#    pumps[i].off()
#
#pumps[0].on()
#pumps[1].on()
#time.sleep(120)
#pumps[0].off()
#pumps[1].off()
#
#pumps[2].on()
#pumps[3].on()
#time.sleep(180)
#pumps[2].off()
#pumps[3].off()

def brew_cocktail ( cocktail_name, volume=100 ):
    print(cocktail_name)
    cocktail = Cocktail_Generator( cocktail_name, volume, pumps )
    pump_times = cocktail.make_cocktail()
    
    #for i in range(len(pump_times)):
            if pump_times[0] != 0 and  pump_times[1] != 0:
                pumps[0].on()
                pumps[1].on()
                time.sleep( pump_times[1] )
                pumps[1].off()
                time.sleep( (pump_times[0]-pump_times[1] )   #self.pumptimes[i])
                pumps[0].off()
                
            if pump_times[0] != 0 and  pump_times[2] != 0:
                pumps[0].on()
                pumps[2].on()
                time.sleep( pump_times[2] )
                pumps[2].off()
                time.sleep( pump_times[0] - pump_times[2] )   #self.pumptimes[i])
                pumps[0].off()
            if pump_times[4] != 0 and  pump_times[2] != 0:
                pumps[4].on()
                pumps[2].on()
                time.sleep( pump_times[2] )
                pumps[2].off()
                time.sleep( pump_times[4] - pump_times[2] )   #self.pumptimes[i])
                pumps[4].off()
             if pump_times[2] != 0 and  pump_times[3] == 0 and pump_times[1] == 0 and pump_times[0] == 0:
                
                pumps[2].on()
                time.sleep( pump_times[2] )
                pumps[2].off()
                  
                
              
                
    print('Enjoy your cocktail!')
    
    
 
def on_connect(client, userdata, flags, rc):
    client.subscribe("cocktailsknallen")
    
def on_message(client, userdata, message):
    print("Message received: "  + str(message.payload.decode("utf-8")))
    brew_cocktail(str(message.payload.decode("utf-8")), 100)    


Connected = False   #global variable for the state of the connection
 
broker_address= "m24.cloudmqtt.com"  #Broker address
port = 10552                         #Broker port
user = "xvgfmnhm"                    #Connection username
password = "YD2yAN5wS9_U"            #Connection password
 
client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
 
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_forever()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)





#try:
#    print("Enter your cocktail (woap/baap/wowa/ba):")
#    cocktail_name = str(input())
#    print("Enter cocktail volume [ml]")
#    volume = input()
#    cocktail = Cocktail_Generator( cocktail_name, volume, pumps )
#    pump_times = cocktail.make_cocktail()
#    
#    for i in range(len(pump_times)):
#            if pump_times[i] != 0:
#                pumps[i].on()
#                time.sleep( pump_times[i] )   #self.pumptimes[i])
#                pumps[i].off()
#    
#    GPIO.cleanup()

## Test pumps
#pumps[0].on()
#time.sleep(240)
#pumps[0].off()   

#pumps[2].off()
#pumps[3].off() 
    
#pumps[1].on()
#time.sleep(4)
#pumps[1].off() 
#
#pumps[2].on()
#time.sleep(4)
#pumps[2].off()
# 
#pumps[3].on()
#time.sleep(4)
#pumps[3].off()

## Ending GPIO

#Reset GPIO settings
#GPIO.cleanup()

# end program cleanly
#except KeyboardInterrupt:
#    GPIO.cleanup()
#    print("done")