#!/bin/bash

/usr/bin/rsync -e 'ssh -i/home/mferrac/.ssh/id_rsa' -avzp sensorpi01:data/ /home/mferrac/pidata/sensorpi01

/usr/bin/nmcli c up FEAGRI
#sleep 5
#/usr/bin/nmcli c up SISDA
