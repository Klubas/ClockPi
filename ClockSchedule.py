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
    
    def __init__(self):
        self.player = None
        self.tone = None

    def play_sound(self, cmd):
        if type(cmd) == str:
            cmd=cmd.split(' ')

        with subprocess.Popen(cmd) as process:
            GPIO.wait_for_edge(gpio_pin, GPIO.FALLING)
            print("Stopping alarm")
            process.kill()

    def job(self):
        cmd = str(self.player) + str(self.tone)
        if self.player and self.tone:
            s = threading.Thread(target=self.play_sound, args=(cmd, ), daemon=True)
            s.start()

        else:
            log_file = open("log.log", "a")

            log = "[{2}] Job execution failed:\n Player: {0} Tone: {1}\n CMD: {3}".format(
                    self.player, self.tone, str(time.strftime("%H:%M:%S")), cmd
            )

            log_file.write(str(log))
            log_file.close()

    def create_schedule(self, hour=None):   
        if hour:
            schedule.every().day.at(hour).do(self.job)

    def delete_schedule(self):
        pass

    def set_tone(self, file_path):
        self.tone = file_path

    def set_player(self, player, args=''):
        self.player = player + args + ' '

    def start(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

