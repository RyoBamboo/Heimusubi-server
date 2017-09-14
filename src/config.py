# -*- coding: utf-8 -*-
import os

"""
設定ファイル
"""

class BaseConfig():
	DEBUG = True
	TESTING = True


class ProductionConfig(BaseConfig):

	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):

	SQLALCHEMY_DATABASE_URI = ''