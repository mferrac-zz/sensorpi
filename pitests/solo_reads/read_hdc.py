#!/usr/bin/python3
import Adafruit_DHT as dht
import numpy as np
import pandas as pd
from time import sleep
import SDL_Pi_HDC1000
import time
import sys

#HDC1080

hdc1000 = SDL_Pi_HDC1000.SDL_Pi_HDC1000()

while True:
    ti2c = hdc1000.readTemperature()
    hi2c = hdc1000.readHumidity()
    print(str(ti2c) + ' ' + str(hi2c))
