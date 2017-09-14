# import os
# import importlib
from flask import Flask, request
from src import app
from src.controllers.auth import bp

# app = importlib.import_module("heimusubi-server.app")

# from flask_sqlalchemy import SQLAlchemy
# from controllers import auth

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# db = SQLAlchemy(app)

# modules_define = [auth.app]
# for module in modules_define:
# 	app.register_blueprint(module)
app.register_blueprint(bp)

@app.route('/')
def index():
	return 'hellow'
if __name__ == "__main__":
	app.run(host='127.0.0.1', port=5000, debug=True)

# 	port = int(os.environ.get('PORT', 5000))
# 	app.run(port=port)


