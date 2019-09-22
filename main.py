#!/usr/bin/env python3
import sys
import argparse
from Screen import Screen
from ClockSchedule import ClockSchedule as Clock
import threading

clock = Clock()

def config_alarm(**kwargs):
    """
    sound
    player
    """
    pass

def create_alarm(hour="07:00"):
    clock.create_schedule(hour=hour)

if __name__ == '__main__':

    screen = Screen()

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

        clock.set_tone(sound)
        clock.set_player(player)

        c = threading.Thread(target=create_alarm, args=(hour,))
        c.start()

        clock.start()

    except (KeyboardInterrupt, SystemExit):
        screen.lcd.clear()
        screen.lcd.enable_display(False)
        screen.lcd.set_backlight(0)
        print("\nAlarm canceled")
