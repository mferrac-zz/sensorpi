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

while True:
    read3 = dht.read_retry(dht.DHT22,19)
    sleep(0.5)
    read4 = dht.read_retry(dht.DHT22,26)
    print(str(read3[0]) + ',' + str(read4[0]))
    sleep(3)
