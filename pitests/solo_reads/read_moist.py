#!/usr/bin/python3
from time import sleep
import os
import Adafruit_ADS1x15
import sys

def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number. Optional parameter 'decimals'
  # will round to specified number of decimal places.
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

gain = sys.argv[1]
os.chdir('/home/pi/data/')

#ADS1115
adc = Adafruit_ADS1x15.ADS1115()

while True:
    moist = adc.read_adc(0,gain=1)
    print('Moist:' + str(moist) + '\n')
    sleep(2)
