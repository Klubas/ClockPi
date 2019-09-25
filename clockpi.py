#!/usr/bin/env python3
import sys
import argparse
import threading
import time

from flask import Flask
from flask_restful import Api

from AlarmController import AlarmController
from Screen import Screen
from ClockAPi import Index, AlarmList, Alarm, ConfigAlarm

if __name__ == '__main__':

    app = Flask(__name__)
    api = Api(app)

    screen = Screen()
    

    #add resources
    api.add_resource(Index, '/')
    api.add_resource(AlarmList, '/alarms')
    api.add_resource(Alarm, '/new_alarm')
    api.add_resource(ConfigAlarm, '/preferences')

    try:

        parser = argparse.ArgumentParser(
            description="Alarm Clock for raspberryPi"
        )

        parser.add_argument(
            'Host'
            , metavar='hostname:port'
            , type=str
            , help="hostname and port number for the server in the format: <hostname>:<port>"
        )

        parser.add_argument(
            'Debug'
            , metavar='debug'
            , type=bool
            , help="Run in debug mode (True/False)"
        )

        args = parser.parse_args()

        if args.Host:
            hostname = args.Host.split(":")
            host=hostname[0]
            port=int(hostname[1])

        if args.Debug:
            debug = args.Debug
        else:
            debug = False
        
#        alarm.config_alarm(sound, player)
        
       	app.run(host=host, port=port, debug=debug)
        screen.lcd.enable_display(False)

    except (KeyboardInterrupt, SystemExit):
        screen.lcd.clear()
        screen.lcd.enable_display(False)
        screen.lcd.set_backlight(0)
        print("\nAlarm canceled")

else:
    sys.exit()
