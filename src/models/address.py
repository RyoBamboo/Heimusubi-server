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
class Address(db.Model):

	__tablename__ = 'addresses'
	id = db.Column(db.Integer, primary_key = True)
	open_weather_id = db.Column(db.Integer)
	address_name = db.Column(db.String(32))
	weather_status = db.Column(db.Integer)
	created = db.Column(db.Integer)
	modified = db.Column(db.Integer)

	def __init__(self):
		return ''

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
	def update_by(cls, key, value, update_value):
		address = db.session.query(cls).filter(getattr(cls, key) == value).first()
		print(update_value)
		address.weather_status = update_value
		address.modified = int(datetime.now().strftime('%s'))

		db.session.commit()