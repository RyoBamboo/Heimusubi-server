import os
from flask import Flask, request
from controllers import auth

app = Flask(__name__)

modules_define = [auth.app]
for module in modules_define:
	app.register_blueprint(module)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(port=port)

@app.route('/')
def index():
  return 'HelloWorld!!!!!!'

