# -*- coding: utf-8 -*-

import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from src import config

app = Flask(__name__, template_folder='admin/templates', static_url_path='')
app.config.from_object(config.BaseConfig)	# 設定の読み込み

db = SQLAlchemy(app)
