#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 18:45:37 2019

@author: Stan
"""

#!/usr/bin/env python
import time

def clean_motors ( pumps ):
    pumps[0].on()
    pumps[1].on()
    time.sleep(40)
    pumps[0].off()
    pumps[1].off()
    
    pumps[2].on()
    pumps[3].on()
    time.sleep(40)
    pumps[2].off()
    pumps[3].off()

    

    