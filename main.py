#!/usr/bin/env python3
import sys
import argparse
import threading

from Screen import Screen
from ClockSchedule import ClockSchedule as Clock

class AlarmController:

    def __init__(self):
        self.clock = Clock()

    def config_alarm(self, sound, player):
        self.clock.set_default_sound(sound)
        self.clock.set_default_player(player)

    def create_alarm(self, hour="07:00", sound=None, tag=None):
        self.clock.create_schedule(hour=hour)


if __name__ == '__main__':

    screen = Screen()
    alarm = AlarmController()

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

        args = parser.parse_args()

        if args.Hour:
            hour = args.Hour

        if args.Sound:
            sound = args.Sound

        if args.Player:
            player = args.Player
        
        alarm.config_alarm(sound, player)
        alarm.create_alarm(hour=hour)
        alarm.clock.start()

    except (KeyboardInterrupt, SystemExit):
        screen.lcd.clear()
        screen.lcd.enable_display(False)
        screen.lcd.set_backlight(0)
        print("\nAlarm canceled")
