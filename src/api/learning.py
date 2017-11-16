# coding:utf-8

import sys
import os
from flask import Blueprint, request
from pprint import pprint
import subprocess

from src import db
from src.service.response import Response

from time import sleep
import paho.mqtt.client as mqtt


bp_learning = Blueprint('learning', __name__)


@bp_learning.route('/api/learning/start')
def start():
	result = subprocess.Popen(['python', '/Users/takenoshita/local_project/02 個人開発・コンペ/heimusubi-server/src/api/bin/voice_svm_test.py', '/Users/takenoshita/local_project/02 個人開発・コンペ/heimusubi-server/src/api/bin/file.wav'], stdout=subprocess.PIPE)
	data = result.communicate()[0]
	decoded_result = data.decode('utf-8').strip()
	print(decoded_result)

	host = 'm14.cloudmqtt.com'
	port = 17419
	topic = 'test'
	username = 'hufvczek'
	password = 'Jxv8I_AvjN7S'

	mqttc = mqtt.Client()
	mqttc.on_publish = on_publish
	mqttc.username_pw_set(username, password)
	mqttc.connect(host, port)


	mqttc.publish(topic, decoded_result)
	mqttc.disconnect()

	
	return 'ok'


def on_publish(client, obj, mid):
	print("send")