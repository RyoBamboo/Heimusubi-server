import os
from flask import Flask
from models import auth

app = Flask(__name__)

modules_define = [auth.app]
for module in modules_define:
	app.register_blueprint(module)

@app.route('/')
def index():
  return 'HelloWorld!!!!!!'
