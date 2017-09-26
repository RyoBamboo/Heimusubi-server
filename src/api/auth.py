import sys
from flask import Blueprint, request
from pprint import pprint

from src import db
from src.service.response import Response

from src.models.user import User

bp = Blueprint('auth', __name__)


# @bp.route('/api/auth/signin', methods=['POST'])
@bp.route('/api/auth/signin')
def signIn():
	# email = request.form['email']
	# password = User.hash_password(request.form['plaintext_password'])
	email = 'itakedaka@gmail.com'
	password = User.hash_password('bimboo09')

	user = User.get_by('email', email)
	user_attrs = user.get_attrs()
	if  user is not None and user.password == password:
		# Success Signin
		return Response(200, user_attrs, '').send()
	else:
		return Response(400, '', 'Your Email or Password is invalid').send()


#@bp.route('/api/auth/signup', methods=['POST'])
@bp.route('/api/auth/signup')
def signUp():

	user_name = request.form['user_name']
	email = request.form['email']
	plaintext_passward = request['plaintext_passward']
	password = User.hash_password(plaintext_password)

	if User.is_email_available(email):
		# if user's email is available, register user information to database
		unregisted_user = User(user_name, email, password)
		unregisted_user.create()
		return Response(200, '', '').send()

	else:
		return  Response(400, '', 'Your email has been registered already.').send()



@bp.route('/api/auth/signout')
def signOut():

	return response.send()
	# is_valid_email = User().is_email_available('a')

	# if is_valid_email:
	# 	return 'OK'
	# else:
	# 	return 'NO'
	# return is_valid_email