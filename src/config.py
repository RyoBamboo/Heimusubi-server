# -*- coding: utf-8 -*-
"""
設定ファイル
"""

import os

class BaseConfig():
	PASSWORD_SALT = 'taiyakis_stnm'
	SQLALCHEMY_DATABASE_URI = "postgresql://takenoshita@localhost:5432/heimusubi-server"
	# SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

	SQLALCHEMY_TRACK_MODIFICATIONS = True
	UPLOAD_FOLDER = '/tmp'
