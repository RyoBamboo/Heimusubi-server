# -*- coding: utf-8 -*-

#	基本モジュールの読み込み
import os, sys, hashlib
import time
from datetime import *

#	プロジェクトモジュールの読み込み
sys.path.append(os.getcwd())
from src import db
from src import config

#	クラス定義
class User(db.Model):

	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	user_name = db.Column(db.String(32))
	email = db.Column(db.String(32))
	password = db.Column(db.String(32))
	status = db.Column(db.Integer)
	heimu_id = db.Column(db.Integer)
	created = db.Column(db.DateTime)
	modified = db.Column(db.DateTime)

	def __init__(self, user_name, email, password):
		self.user_name = user_name
		self.email = email
		self.password = password


	def create(self):
		self.status 	= 1
		self.created = datetime.now()
		self.modified = datetime.now()

		db.session.add(self)
		db.session.commit()


	@classmethod
	def hash_password(cls, plaintext_password):
		password_str = (config.BaseConfig.PASSWORD_SALT + plaintext_password).encode('utf-8')
		return hashlib.md5(password_str).hexdigest()


	@classmethod
	def is_email_available(cls, email):
		if db.session.query(User).filter(User.email == email).first() is None:
			return True
		else:
			return False
