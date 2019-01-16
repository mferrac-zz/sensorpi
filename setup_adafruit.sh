#!/bin/bash

git clone https://github.com/adafruit/Adafruit_Python_DHT.git

sudo apt-get update

#sudo apt install build-essential python-dev

cd Adafruit_Python_DHT

sudo python setup.py install
