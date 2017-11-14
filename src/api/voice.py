import sys
import base64
from flask import Blueprint, request, jsonify
from pprint import pprint

from src.service.response import Response


bp_voice = Blueprint('voice', __name__)


@bp_voice.route('/api/voice/upload', methods=['POST'])
def upload():
    if request.headers['Content-Type'] != 'application/json':
        print("aaa", file=sys.stderr)
        print(request.headers['Content-Type'], file=sys.stderr)
        return jsonify(res='error'), 400

    data = request.json
    sound = data['sound']['file_data']
    filename = ".testaa.m4a"
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(sound))
    return jsonify(res='ok')


@bp_voice.route('/api/voice/test')
def test():

	return 'ok'