import sys
from flask import Blueprint, request
from pprint import pprint

from src import db

from src.models.user import User

bp = Blueprint('auth', __name__)

@bp.route('/api/auth/signin')
def signIn():
	return request.args.post('id', '')


@bp.route('/api/auth/signup', methods=['GET, POST'])
def signUp():

	user_name = request.form['user_name']
	email = request.form['email']
	plaintext_passward = request['plaintext_passward']
	unregisted_user = User(user_name, email, plaintext_passward)

	return True


@bp.route('/api/auth/signout')
def signOut():
	is_valid_email = User().is_email_available('a')

	if is_valid_email:
		return 'OK'
	else:
		return 'NO'
	# return is_valid_email