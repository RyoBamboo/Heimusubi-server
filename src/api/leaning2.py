import sys
from flask import Blueprint, request
from pprint import pprint
import subprocess

from src import db
from src.service.response import Response

bp_learning = Blueprint('learning', __name__)



@bp_learning.route('/api/learning/start')
def start():
	is_happy = subprocess.run("python ../bin/voice_svm_test.py ../bin/file.wav")
	print(is_happy)
	return 'ok'
