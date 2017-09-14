# -*- coding: utf-8 -*-
"""
設定ファイル
"""

import os

class BaseConfig():
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = True
