import sys
from flask import Blueprint, request
from pprint import pprint

from src import db
from src.service.response import Response

from src.models.user import User

bp = Blueprint('auth', __name__)

@bp.route('/api/auth/signin', methods=['POST'])
def signIn():
	email = request.form['email']


@bp.route('/api/auth/signup', methods=['POST'])
def signUp():

	user_name = request.form['user_name']
	email = request.form['email']
	plaintext_passward = request['plaintext_passward']

	passward = User.hash_password(plaintext_passward)

	unregisted_user = User(user_name, email, passward)
	unregisted_user.create()

	return 'ok'


@bp.route('/api/auth/signout')
def signOut():
	response = Response(200, 'test', '222')


	return response.send()
	# is_valid_email = User().is_email_available('a')

	# if is_valid_email:
	# 	return 'OK'
	# else:
	# 	return 'NO'
	# return is_valid_email