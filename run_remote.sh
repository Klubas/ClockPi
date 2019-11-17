#!/bin/bash
ssh pi@192.168.0.103 'killall python3; cd /home/pi/git/ClockPi; source env/bin/activate && python3 /home/pi/git/ClockPi/clockpi.py --hostname 0.0.0.0:8080 '
