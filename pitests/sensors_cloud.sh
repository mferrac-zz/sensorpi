#!/bin/bash

#sync from pi
/usr/bin/rsync -e 'ssh -i/home/mferrac/.ssh/id_rsa' -avzp sensorpi01:data/ /home/mferrac/pidata/sensorpi01/

#connect FEAGRI wifi
nmcli c up FEAGRI

#sync data to google drive
rclone sync -v /home/mferrac/pidata/ gdrive:masters/pidata/

#connect to SISDA
nmcli c up SISDA
