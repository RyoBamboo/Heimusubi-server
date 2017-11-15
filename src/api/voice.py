import sys
import os
import base64
from src import app

from flask import Blueprint, request, jsonify


bp_voice = Blueprint('voice', __name__)


@bp_voice.route('/api/voice/upload', methods=['POST'])
def upload():
    if request.headers['Content-Type'] != 'application/json':
        print("aaa", file=sys.stderr)
        print(request.headers['Content-Type'], file=sys.stderr)
        return jsonify(res='error'), 400

    data = request.json
    bin_data = base64.b64decode(data['sound']['file_data'])

	filename = 'aaaaa.txt'
	path_2_tmp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
	filepath = os.path.join(path_2_tmp, filename)	

	if not os.path.exists(path_2_tmp):
		os.mkdir(path_2_tmp)
	f = open(filepath, 'wb')
	f.write(bin_data)
	f.close()
    # sound = data['sound']['file_data']
    # # fp = open('./test.m4a', 'w')
    # # fp.write(str(base64.b64decode(sound)))
    # BASE_DIR = os.path.dirname(__file__)
    # myfile = open(os.path.join(BASE_DIR, 'static/sample.m4a'), "wb")
    # myfile.write(base64.b64decode(sound))

    return jsonify(res='ok')


@bp_voice.route('/api/voice/test')
def test():
	filename = 'aaaaa.txt'
	path_2_tmp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
	filepath = os.path.join(path_2_tmp, filename)	
	print(filepath)

	if not os.path.exists(path_2_tmp):
		os.mkdir(path_2_tmp)
	f = open(filepath, 'w')
	f.write('tet')
	f.close()
	return 'ok'
    