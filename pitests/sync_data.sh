#!/bin/bash

#connect FEAGRI wifi
nmcli c up FEAGRI

#sync data to google drive
/snap/bin/rclone sync -v /home/mferrac/pidata/ gdrive:masters/pidata/

#connect to SISDA
nmcli c up SISDA
