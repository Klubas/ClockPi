import sys
import time
import schedule
import subprocess
import threading
import RPi.GPIO as GPIO

gpio_pin = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class ClockSchedule:
    
    def __init__(self, player='aplay'):
        self.player = player
        self.sound = None

    def play_sound(self, cmd):
        if type(cmd) == str:
            cmd=cmd.split(' ')

        with subprocess.Popen(cmd) as process:
            GPIO.wait_for_edge(gpio_pin, GPIO.FALLING)
            print("Stopping alarm")
            process.kill()

    def job(self, sound, repeat=True):

        cmd = str(self.player) + str(sound)

        if self.player and sound:
            s = threading.Thread(target=self.play_sound, args=(cmd, ), daemon=True)
            s.start()

            if not repeat:
                return schedule.CancelJob

        else:
            log_file = open("log.log", "a")

            log = "[{2}] Job execution failed:\n Player: {0} sound: {1}\n CMD: {3}".format(
                    self.player, sound, str(time.strftime("%H:%M:%S")), cmd)

            log_file.write(str(log))
            log_file.close()

    def create_schedule(self, hour=None, **kwargs):

        sound   = self.sound     if kwargs.get('sound')  is None else str(kwargs.get('sound'))
        repeat  = True           if kwargs.get('repeat') is None else bool(kwargs.get('repeat'))
        tag     = 'alarm'        if kwargs.get('tag')    is None else str(kwargs.get('tag'))

        if hour and sound:
            schedule.every().day.at(hour).do(self.job, sound, repeat).tag(hour, tag)
            return True, 'Alarm job scheduled at ' + hour
        else:
            return False, 'Job scheduling failed '
             
    def delete_schedule(self, tag):
        schedule.clear(tag)

    def set_default_sound(self, file_path):
        self.sound = file_path

    def set_default_player(self, player, args=''):
        self.player = player + args + ' '

    def start(self):
        schedule.run_continuously()
        print("Scheduler started")
        #while True:
        #    schedule.run_pending()
        #    time.sleep(1)

