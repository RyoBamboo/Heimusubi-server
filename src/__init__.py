import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 本番用環境
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://takenoshita@localhost:5432/heimusubi-server"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from sqlalchemy import create_engine, Integer, String
from sqlalchemy.sql import select, text, bindparam, exists, func, and_, or_, not_

# modules_define = [controllers.auth.app]
# for module in modules_define:
# 	app.register_blueprint(module)


# @app.route('/')
# def index():
# 	return 'hellow'