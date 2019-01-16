#!/usr/bin/python
import smbus
import time
# Define some constants from the datasheet
DEVICE     = 0x23 # Default device I2C address
DEVICE2    = 0X5c
POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value
ONE_TIME_HIGH_RES_MODE = 0x20
  
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1
   
def convertToNumber(data):
    # Simple function to convert 2 bytes of data
    return ((data[1] + (256 * data[0])) / 1.2)
          
def readLight(addr=DEVICE):
   # Read data from I2C interface
   data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE)
   return convertToNumber(data)
   
def main():

    while True:
        lightLevel=readLight()
        #lightLevel2=readLight(addr=DEVICE2)
        print("Light Level : " + format(lightLevel,'.2f') + " lx")
        #print("Light Level 2 : " + format(lightLevel2,'.2f') + " lx")
        time.sleep(4)

if __name__=="__main__":
    main()
