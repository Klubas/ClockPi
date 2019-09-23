from ClockSchedule import ClockSchedule as Clock

class AlarmController:
    def __init__(self):
        self.clock = Clock()

    def config_alarm(self, sound, player):
        self.clock.set_default_sound(sound)
        self.clock.set_default_player(player)

    def create_alarm(self, hour="07:00", sound=None, repeat=True, tag=None):
        self.clock.create_schedule(hour=hour)