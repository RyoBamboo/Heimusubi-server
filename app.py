import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello World!!'

@app.route('/user/<username>')
def get_user_profile(username):
	return 'User is %s' % username
