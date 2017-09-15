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
	# passward = db.Column(db.String(32))
	status = db.Column(db.Integer)
	heimu_id = db.Column(db.Integer)
	created = db.Column(db.DateTime)
	modified = db.Column(db.DateTime)

	@classmethod
	def is_email_available(cls, email):
		if db.session.query(User).filter(User.email == email).first() is None:
			return True
		else:
			return False
