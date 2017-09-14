# -*- coding: utf-8 -*-

#	モジュールの読み込み
import os, sys
sys.path.append(os.getcwd())

from src import db

#	クラス定義
class User(db.Model):

	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	user_name = db.Column(db.String(32))
	email = db.Column(db.String(32))
	status = db.Column(db.Integer)
	heimu_id = db.Column(db.Integer)
	address_id = db.Column(db.Integer)
	created = db.Column(db.DateTime)
	modified = db.Column(db.DateTime)

	def create_user(user_name, email, status, heimu_id, address_id):
		user = User()
		user.user_name = user_name
		user.email = email
		user.status = 127
		user.heimu_id = 127
		user.address_id = 127

		db.session.add(user)
		db.session.commit()

	def get_user_by_email(email):
		return  True
