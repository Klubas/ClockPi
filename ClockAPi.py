import json
from flask import request
from flask_restful import Resource

from AlarmController import AlarmController

alarm = AlarmController()
alarm.clock.start()

class Index(Resource):
    def get(self):
        return {'Status', 'OK'}, 200

class AlarmList(Resource):
    def get(self):
        return {'Status', 'OK'}, 200

class ConfigAlarm(Resource):
    def get(self):
        return {'Status', 'OK'}, 200

class Alarm(Resource):
    def put(self):
        
        json = request.get_json(force=True)
        json_dict=json.loads()
        
        print(json_dict)

        hour=json_dict['hour']
        sound=json_dict['sound']
        repeat=json_dict['repeat']
        tag=json_dict['tag']

        alarm.create_alarm(
            hour=hour
            , sound=sound
            , repeat=repeat
            , tag=tag 
        )

        return {'Hour': hour}, 200

        
