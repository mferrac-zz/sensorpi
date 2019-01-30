#!/usr/bin/python3
import Adafruit_DHT as dht
import numpy as np
import pandas as pd
import smbus
from datetime import datetime as dt
from time import sleep
import os
#import SDL_Pi_HDC1000
import time
import Adafruit_ADS1x15
from urllib.request import urlopen

def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number. Optional parameter 'decimals'
  # will round to specified number of decimal places.
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

os.chdir('/home/pi/data/')

#BH1750 config
ONE_TIME_HIGH_RES_MODE = 0x21
bus = smbus.SMBus(1)
DEVICE     = 0x23 # Default device I2C address
DEVICE2    = 0X5c
POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value

def readLight(addr=DEVICE):
  # Read data from I2C interface
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE)
  return convertToNumber(data)

lightLevel=readLight()
#lightLevel2=lightLevel#readLight(addr=DEVICE2)

#HDC1080
#hdc1000 = SDL_Pi_HDC1000.SDL_Pi_HDC1000()
#ti2c = hdc1000.readTemperature()
#hi2c = hdc1000.readHumidity()

#ADS1115
adc = Adafruit_ADS1x15.ADS1115()
moist = adc.read_adc(0,gain=1)

#gpios = []
#reads = [dht.read_retry(dht.DHT22,x) for x in gpios]
read3 = dht.read_retry(dht.DHT22,17)
sleep(0.5)
read4 = dht.read_retry(dht.DHT22,18)

df = pd.DataFrame(columns=['h26','t26',
                           'h19','t19',
                           'moist',
                           'lux'])
df.loc[0] = np.hstack([read3,read4,moist,lightLevel])
df['date'] = '{:%Y-%m-%d %H:%M:%S}'.format(dt.now())


if os.path.isfile('./sensor_log.csv'):
    df.round(2).to_csv('sensor_log.csv',index=False,header=False,mode='a')
else:
    df.round(2).to_csv('sensor_log.csv',index=False)
print(df.round(2))

#send data to thingspeak
#base_url = 'https://api.thingspeak.com/update?api_key=DVMKA0FSWXTDG0DG&'
#try:
#    f1 = urlopen(base_url+'field1='+str(df['date'][0])+
#                 '&field2='+str(df['h26'][0])+
#                 '&field3='+str(df['t26'][0])+
#                 '&field4='+str(df['h19'][0])+
#                 '&field5='+str(df['t19'][0])+
#                 '&field6='+str(df['hi2c'][0])+
#                 '&field7='+str(df['ti2c'][0])+
#                 '&field8='+str(df['moist'][0]))
#except:
#    print('failed to send data to thingspeak')
