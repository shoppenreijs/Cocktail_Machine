#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 22:00:19 2019

@author: Stan
"""

import paho.mqtt.client as mqttClient
import time
 
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