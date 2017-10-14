import sys
from flask import Blueprint, request, render_template, send_from_directory, redirect
from flask_httpauth import HTTPBasicAuth
from src import db
from src import app
from src.models.user import User
from datetime import datetime


bp_admin = Blueprint('admin', __name__)


#-----------------------------------------------
# Setting Basic Authentification
#-----------------------------------------------
auth = HTTPBasicAuth()

users = {
	"taiyakis": "taiyakis"
}

@auth.get_password
def get_pw(username):
	if username in users:
		return users.get(username)
	return none


#-----------------------------------------------
# Setting Static Files
#-----------------------------------------------
@bp_admin.route('/admin/static/<path:filename>')
def base_static(filename):
	print(filename, file=sys.stderr)
	return send_from_directory(app.root_path + '/admin/static/', filename)


#-----------------------------------------------
# User
#-----------------------------------------------
@bp_admin.route('/admin/')
@bp_admin.route('/admin/user')
@auth.login_required
def index():
	users = User.get_all()
	for user in users:
		user.created = datetime.fromtimestamp(user.created)
		user.modified = datetime.fromtimestamp(user.modified)
	return render_template('index.html', title="ユーザ管理画面", users=users)


@bp_admin.route('/admin/user/add')
def add():
	user = User('テスト', 'test@gmail.com', 'test')
	User.create(user)
	return redirect("/admin/user")


@bp_admin.route('/admin/user/delete/<user_id>')
def delete(user_id):
	User.delete_by('id', user_id)
	return redirect("/admin/user")


