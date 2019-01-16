#!/usr/bin/python3
import Adafruit_DHT as dht
import numpy as np
import pandas as pd
from time import sleep
import SDL_Pi_HDC1000
import time
import sys

if len(sys.argv) == 1:
    gpio1 = 19
    gpio2 = 26
else:
    gpio1 = sys.argv[1]
    gpio2 = sys.argv[2]

#HDC1080
hdc1000 = SDL_Pi_HDC1000.SDL_Pi_HDC1000()
ti2c = hdc1000.readTemperature()
hi2c = hdc1000.readHumidity()

while True:
    read3 = dht.read_retry(dht.DHT22,19)
    sleep(0.5)
    read4 = dht.read_retry(dht.DHT22,26)

    df = pd.DataFrame(columns=['h'+str(gpio1),'t'+str(gpio1),
                               'h'+str(gpio2),'t'+str(gpio2),
                               'hi2c','ti2c'])
    df.loc[0] = np.hstack([read3,read4,hi2c,ti2c])
    print(round(df,2))
    sleep(3)
