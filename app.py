import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from controllers import auth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

modules_define = [auth.app]
for module in modules_define:
	app.register_blueprint(module)

@app.route('/')
def index():
	return os.environ['DATABASE_URL']

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(port=port)


