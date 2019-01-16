#!/usr/bin/env python3
#
# Test SDL_Pi_HDC1000
#
# June 2017
#

#imports

import sys          
import time
import datetime
import SDL_Pi_HDC1000


print ("Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S"))


hdc1000 = SDL_Pi_HDC1000.SDL_Pi_HDC1000()

while True:
        
        print ("-----------------")
        print ("Temperature = %3.1f C" % hdc1000.readTemperature())
        print ("Humidity = %3.1f %%" % hdc1000.readHumidity())
        print ("-----------------")

        time.sleep(3.0)
