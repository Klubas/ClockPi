#!/usr/bin/env python3
from Screen import Screen
from ClockSchedule import ClockSchedule as Clock
import threading

screen = Screen()
lcd = screen.lcd

clock = Clock(lcd)

def create_alarm(nome=None):
    clock.set_tone('sound/tone.mp3')
    clock.set_player('mpv')
    hour = str(input("Hour: "))
    clock.create_schedule(hour=hour)

if __name__ == '__main__':
    print("Configure your alarm...")
    c = threading.Thread(target=create_alarm, args=(1,))
    c.start()
    clock.start()


