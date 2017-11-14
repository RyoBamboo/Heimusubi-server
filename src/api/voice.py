import sys
import base64
from flask import Blueprint, request, jsonify
from pprint import pprint

from src import db
from src.service.response import Response

from src.models.user import User

bp_voice = Blueprint('voice', __name__)


@bp_voice.route('/api/voice/upload', methods=['POST'])
def upload():
    if request.headers['Content-Type'] != 'application/json':
        print("aaa", file=sys.stderr)
        print(request.headers['Content-Type'], file=sys.stderr)
        return flask.jsonify(res='error'), 400

    data = request.json
    sound = data['sound']['file_data']
    fp = open('./test.m4a', 'w')
    fp.write(str(base64.b64decode(sound)))

	return jsonify(res='ok')