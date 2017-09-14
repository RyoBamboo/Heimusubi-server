from flask import Flask, request
from src import app
from src.controllers.auth import bp

app.register_blueprint(bp)

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=5000, debug=True)



