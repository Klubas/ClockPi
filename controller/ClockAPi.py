import json
from flask import request
from flask_restful import Resource

from AlarmController import AlarmController

alarm = AlarmController()
alarm.config_alarm(sound='sound/sound.mp3', player='mpv --no-terminal')
alarm.clock.start()

class Index(Resource):
    def get(self):
        return {'Status': 'OK'}, 200


class AlarmList(Resource):
    def get(self):
        return {'Status': 'OK'}, 200


class ConfigAlarm(Resource):
    def get(self):
        return {'Status': 'OK'}, 200


class Alarm(Resource):
    def post(self):
        
        json = request.get_json(force=True)
        #json_dict=json.loads()
        
        print(json)

        hour=json['hour']
        #sound=json['sound']
        #repeat=json['repeat']
        #tag=json['tag']

        status = alarm.create_alarm(
            hour=hour
            #, sound=sound
            #, repeat=repeat
            #, tag=tag 
        )

        return {'Response': status[1]}, 200

        
