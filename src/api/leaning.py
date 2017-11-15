import sys
from flask import Blueprint, request
from pprint import pprint

from src import db
from src.service.response import Response


bp_learning = Blueprint('learning', __name__)


@bp_learning.route('/api/learning/start')
def start():
	return 'ok'
