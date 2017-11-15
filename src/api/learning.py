# coding:utf-8

import sys
import os
from flask import Blueprint, request
from pprint import pprint
import subprocess

from src import db
from src.service.response import Response


bp_learning = Blueprint('learning', __name__)


@bp_learning.route('/api/learning/start')
def start():
	print(os.path.dirname(os.path.abspath(__file__)))
	cmd = "python ../bin/test.py"
	result = subprocess.Popen(['python', '/Users/takenoshita/local_project/02 個人開発・コンペ/heimusubi-server/src/api/bin/voice_svm_test.py', '/Users/takenoshita/local_project/02 個人開発・コンペ/heimusubi-server/src/api/bin/file.wav'], stdout=subprocess.PIPE)
	# print(result.communicate()[0].decode('utf-8'))
	data = result.communicate()[0]
	decoded_result = data.decode('utf-8').strip()
	print(decoded_result)


	
	if result.returncode != 0:
		print("失敗")
	# cmd = "python ../bin/test.py"
	# is_happy = subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT, shell=True)
	# print("今から学習を始めるよ")
	# cmd = "python ../bin/voice_svm_test.py ../bin/file.wav"
	# is_happy = subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT, shell=True)
	# # is_happy = subprocess.run("python ../bin/voice_svm_test.py ../bin/file.wav", shell=True, check=True)
	# print(is_happy)
	# print(is_happy)
	return 'ok'
