from importlib import import_module
import logging
from flask import request
from flask_restful import Resource

from modules.yeelight.LightController import LightController
from controller.AlarmController import AlarmController

alarm = AlarmController()
alarm.config_alarm(sound='sound/sound.mp3', player='mpv --no-terminal')
alarm.clock.start()

lights = LightController()
bulb_names = lights.get_bulb_names()


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

        logging.debug(json)

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


class Bulb(Resource):
    def post(self):
        json = request.get_json(force=True)

        logging.debug(json)

        bulb_ip = json['ip'] if 'ip' in json else None
        bulb_name = json['name'] if 'name' in json else None
        action = json['action'] if 'action' in json else None
        params = json['params'] if 'params' in json else None

        status = lights.run_action(
            ip=bulb_ip
            , name=bulb_name
            , action=action
            , params=params
        )

        return {'Response': status}, 200
