from Screen import Screen
from ClockSchedule import ClockSchedule as Clock

screen = Screen()
lcd = screen.lcd

clock = Clock(lcd)

def create_alarm():
    clock.set_tone('sound/tone.mp3')
    clock.set_player('mpv')
    hour = str(input("Hour: "))
    clock.create_schedule(hour=hour)
    lcd.clear()
    lcd.message("Alarm set to: " + hour + "\n")

if __name__ == '__main__':
    print("Configure your alarm...")
    create_alarm()
    clock.start()


