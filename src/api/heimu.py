import sys
from flask import Blueprint, request
from pprint import pprint

from src import db
from src.service.response import Response

from src.models.user import User

bp_heimu = Blueprint('heimu', __name__)


@bp_heimu.route('/api/heimu/register', methods=['POST'])
def register():
	heimu_name = request.form['heimu_name']

	user = User.get_by('email', email)
	if  user is not None and user.password == password:
		return Response(200, user.get_attrs(), '').send()
	else:
		return Response(400, '', 'Your Email or Password is invalid').send()


@bp_heimu.route('/api/auth/signup', methods=['POST'])
def signUp():

	user_name = request.form['user_name']
	email = request.form['email']
	plain_text_passward = request['plain_text_passward']
	password = User.hash_password(plain_text_password)

	if User.is_email_available(email):
		unregisted_user = User(user_name, email, password)
		unregisted_user.create()
		return Response(200, '', '').send()

	else:
		return  Response(400, '', 'Your email has been registered already.').send()
