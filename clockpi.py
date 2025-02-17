#!/usr/bin/env python3
import sys
import argparse
import threading
import time

from flask import Flask
from flask_restful import Api

from controller.AlarmController import AlarmController
from controller.Screen import Screen
from controller.ClockAPi import Index, AlarmList, Alarm, ConfigAlarm, Bulb

if __name__ == '__main__':

    app = Flask(__name__)
    api = Api(app)

    #add resources
    api.add_resource(Index, '/')
    api.add_resource(AlarmList, '/alarm/alarms')
    api.add_resource(Alarm, '/alarm/new_alarm')
    api.add_resource(ConfigAlarm, '/alarm/preferences')
    api.add_resource(Bulb, '/light/bulb')

    try:

        parser = argparse.ArgumentParser(
            description="Alarm Clock for raspberryPi"
        )

        parser.add_argument(
            '--hostname'
            , metavar='hostname:port'
            , type=str
            , help="hostname and port number for the server in the format: <hostname>:<port>"
        )

        parser.add_argument(
            '--debug'
            , help="Run in debug mode"
            , action='store_true'
        )

        args = parser.parse_args()
        
        print(args)
        
        if args.hostname:
            hostname = args.hostname.split(":")
            host = hostname[0]
            port = int(hostname[1])
        else:
            sys.exit(-1)
        
        app.run(host=host, port=port, debug=args.debug)

    except (KeyboardInterrupt, SystemExit):
        screen = Screen()
        screen.lcd.clear()
        screen.lcd.enable_display(False)
        screen.lcd.set_backlight(0)
        print("\nAlarm canceled")

else:
    sys.exit()
