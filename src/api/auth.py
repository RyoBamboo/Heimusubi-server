import sys
from flask import Blueprint, request
from pprint import pprint

from src import db
from src.service.response import Response

from src.models.user import User

bp_auth = Blueprint('auth', __name__)


@bp_auth.route('/api/auth/signin', methods=['POST'])
def signIn():
	email = request.form['email']
	password = User.hash_password(request.form['plain_text_password'])

	user = User.get_by('email', email)
	if  user is not None and user.password == password:
		return Response(200, user.get_attrs(), '').send()
	else:
		return Response(400, '', 'Your Email or Password is invalid').send()


@bp_auth.route('/api/auth/signup', methods=['POST'])
def signUp():

	user_name = request.form['user_name']
	email = request.form['email']
	plain_text_password = request.form['plain_text_password']
	password = User.hash_password(plain_text_password)

	if User.is_email_available(email):
		unregisted_user = User(user_name, email, password)
		unregisted_user.create()
		return Response(200, '', '').send()

	else:
		return  Response(400, '', 'Your email has been registered already.').send()
