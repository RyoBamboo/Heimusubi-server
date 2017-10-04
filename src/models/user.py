# -*- coding: utf-8 -*-

#	基本モジュールの読み込み
import os, sys, hashlib
import time
from datetime import datetime

#	プロジェクトモジュールの読み込み
sys.path.append(os.getcwd())
from src import db
from src import config

from datetime import datetime

#	クラス定義
class User(db.Model):

	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	user_name = db.Column(db.String(32))
	email = db.Column(db.String(32))
	password = db.Column(db.String(32))
	status = db.Column(db.Integer)
	heimu_id = db.Column(db.Integer)
	created = db.Column(db.Integer)
	modified = db.Column(db.Integer)

	def __init__(self, user_name, email, password):
		self.user_name = user_name
		self.email = email
		self.password = password


	def create(self):
		self.status 	= 1
		self.created =  int(datetime.now().strftime('%s'))
		self.modified =  int(datetime.now().strftime('%s'))

		db.session.add(self)
		db.session.commit()
		return self


	def get_attrs(self):
		attrs_list = {}
		for key, value in vars(self).items():
			if key != '_sa_instance_state': attrs_list[key] = value

		return attrs_list


	@classmethod
	def get_all(cls):
		return db.session.query(cls).all()


	@classmethod
	def get_by(cls, key, value):
		return db.session.query(cls).filter(getattr(cls, key) == value).first()


	@classmethod
	def get_all_by(cls, key, value):
		return db.session.query(cls).filter(getattr(cls, key) == value).all()


	@classmethod
	def delete_by(cls, key, value):
		user = db.session.query(cls).filter(getattr(cls, key) == value).first()
		db.session.delete(user)
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
