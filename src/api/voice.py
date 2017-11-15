import sys
import os
import base64
import pysftp
from src import app

from flask import Blueprint, request, jsonify


bp_voice = Blueprint('voice', __name__)


@bp_voice.route('/api/voice/upload', methods=['POST'])
def upload():
    if request.headers['Content-Type'] != 'application/json':
        print("aaa", file=sys.stderr)
        print(request.headers['Content-Type'], file=sys.stderr)
        return jsonify(res='error'), 400


    # sound = data['sound']['file_data']
    # # fp = open('./test.m4a', 'w')
    # # fp.write(str(base64.b64decode(sound)))
    # BASE_DIR = os.path.dirname(__file__)
    # myfile = open(os.path.join(BASE_DIR, 'static/sample.m4a'), "wb")
    # myfile.write(base64.b64decode(sound))

    return jsonify(res='ok')

