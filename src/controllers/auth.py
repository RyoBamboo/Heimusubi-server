from flask import Blueprint, request

from src import db

from src.models.user import User

bp = Blueprint('auth', __name__)

@bp.route('/api/signin')
def signIn():
	return request.args.post('id', '')


@bp.route('/api/signout')
def signOut():
	User.create_user('a', 'a', 1, 1, 1)
	return 'signOut'