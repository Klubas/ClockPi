from flask import request
from flask_restful import Resource

from AlarmController import AlarmController

class Index(Resource):
    def get(self):
        return {'Status', 'OK'}, 200
