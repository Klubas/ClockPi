import sys
import time
import schedule
import subprocess
import threading
import RPi.GPIO as GPIO

gpio_pin = 26

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
            while True:
                if GPIO.input(gpio_pin) == GPIO.LOW:
                    process.kill()
                    return True, 'Alarm stopped'
                elif process.poll() is not None:
                    self.play_sound(cmd)

    def job(self, sound, repeat=True, actions=None):
        threads = list()
        cmd = str(self.player) + str(sound)

        if self.player and sound:
            try:

                threads.append(
                    threading.Thread(target=self.play_sound, args=(cmd, ), daemon=True)
                )

                if actions:
                    for action in actions:
                        threads.append(
                            threading.Thread(
                                target=action['function'], args=(action['args'])
                            )  # args must be a tuple
                        )

                for t in threads:
                    t.start()

                if not repeat:
                    return schedule.CancelJob

            except Exception as e:
                print(e)

        else:
            log_file = open("log.log", "a")

            log = "[{2}] Job execution failed:\n Player: {0} sound: {1}\n CMD: {3}".format(
                    self.player, sound, str(time.strftime("%H:%M:%S")), cmd)

            log_file.write(str(log))
            log_file.close()

    def create_schedule(self, hour=None, actions=None, **kwargs):

        sound = self.sound if kwargs.get('sound') is None else str(kwargs.get('sound'))
        repeat = True if kwargs.get('repeat') is None else bool(kwargs.get('repeat'))
        tag = 'alarm' if kwargs.get('tag') is None else str(kwargs.get('tag'))

        if hour and sound:
            schedule.every().day.at(hour).do(self.job, sound, repeat, actions).tag(hour, tag)
            return True, 'Alarm job scheduled at ' + hour
        else:
            return False, 'Job scheduling failed '
             
    def delete_schedule(self, tag):
        schedule.clear(tag)

    def set_default_sound(self, file_path):
        self.sound = file_path

    def set_default_player(self, player, args=''):
        self.player = player + args + ' '

    def _run_job_thread_(self, interval):
        while True:
            schedule.run_pending()
            time.sleep(interval)

    def start(self):
        print("Scheduler started")
        t = threading.Thread(target=self._run_job_thread_, args=(1,), daemon=True)
        t.start()

