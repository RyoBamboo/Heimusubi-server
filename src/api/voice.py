import sys
from flask import Blueprint, request
from pprint import pprint

from src import db
from src.service.response import Response

from src.models.user import User

bp_voice = Blueprint('voice', __name__)


@bp_voice.route('/api/heimu/register', methods=['POST'])
def upload():
    json_string = request.form
    print(json_string, file=sys.stderr)
