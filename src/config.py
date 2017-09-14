# -*- coding: utf-8 -*-
"""
設定ファイル
"""

import os

class BaseConfig():
	SQLALCHEMY_DATABASE_URI = "postgresql://takenoshita@localhost:5432/heimusubi-server"
	SQLALCHEMY_TRACK_MODIFICATIONS = True
