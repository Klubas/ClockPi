#!/usr/bin/env python3
import sys
import argparse
import threading
import time

from Screen import Screen
from ClockSchedule import ClockSchedule as Clock
from Api import Index

from flask import Flask
from flask_restful import Api

class AlarmController:

    def __init__(self):
        self.clock = Clock()

    def config_alarm(self, sound, player):
        self.clock.set_default_sound(sound)
        self.clock.set_default_player(player)

    def create_alarm(self, hour="07:00", sound=None, tag=None):
        self.clock.create_schedule(hour=hour)


if __name__ == '__main__':

    app = Flask(__name__)
    api = Api(app)

    screen = Screen()
    alarm = AlarmController()

    #add resources
    api.add_resource(Index, '/')

    try:

        parser = argparse.ArgumentParser(
            description="Alarm Clock for raspberryPi"
        )

        parser.add_argument(
            'Hour'
            , metavar='hour'
            , type=str
            , help="set the alarm time"
        )

        parser.add_argument(
            'Sound'
            , metavar='sound'
            , type=str
            , help="what sound should ClockPi play for the alarm"
        )

        parser.add_argument(
            'Player'
            , metavar='player'
            , type=str
            , help="what audio player should ClockPi use"
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

        if args.Hour:
            hour = args.Hour

        if args.Sound:
            sound = args.Sound

        if args.Player:
            player = args.Player

        if args.Host:
            hostname = args.Host.split(":")
            host=hostname[0]
            port=int(hostname[1])

        if args.Debug:
            debug = args.Debug
        else:
            debug = False
        
        alarm.config_alarm(sound, player)
        alarm.clock.start()
        
        app.run(host=host, port=port, debug=debug)

        #while True:
        #    hour = input("Alarm at: ")
        #    tag = input("Tag: ")
        #    alarm.create_alarm(hour=hour, tag=tag)
        #    time.sleep(1)

    except (KeyboardInterrupt, SystemExit):
        screen.lcd.clear()
        screen.lcd.enable_display(False)
        screen.lcd.set_backlight(0)
        print("\nAlarm canceled")
