#!/bin/python3
import Adafruit_DHT as dht
import numpy as np
import pandas as pd
from datetime import datetime as dt
from time import sleep
import os

os.chdir('/home/pi/repos/masters/data/')

gpios = [17,3,4]
#reads = [dht.read_retry(dht.DHT22,x) for x in gpios]
read17 = dht.read_retry(dht.DHT22,17)
sleep(0.5)
read3 = dht.read_retry(dht.DHT22,19)
sleep(0.5)
read4 = dht.read_retry(dht.DHT22,26)
reads = [read17,read3,read4]
df = pd.DataFrame(reads)
df.columns = ['h','t']
df['date'] = '{:%Y-%m-%d %H:%M:%S}'.format(dt.now())
df['gpios'] = gpios
#df.round(2).to_csv('room_log.csv', mode='a', header=False, index=False)
print('done')
print(df)
