import time
import schedule
import subprocess

class ClockSchedule:
    
    def __init__(self, screen=None):
        self.player = None
        self.tone = None
        self.lcd = screen

    def job(self):
        cmd = str(self.player) + str(self.tone)
        if self.player and self.tone:
            s = subprocess.call(cmd, shell=True)
            print(s)
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

