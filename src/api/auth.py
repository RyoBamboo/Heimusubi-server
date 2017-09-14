from flask import Blueprint, request

from src import db

from src.models.user import User

bp = Blueprint('auth', __name__)

@bp.route('/api/auth/signin')
def signIn():
	return request.args.post('id', '')


@bp.route('api/auth/signup')
def signUp():



@bp.route('/api/auth/signout')
def signOut():
	User.create_user('a', 'a', 1, 1, 1)
	return 'signOut'