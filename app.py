from flask import Flask, request
from src import app
from src.api.auth import bp_auth
from src.admin.admin import bp_admin

app.register_blueprint(bp_auth)
app.register_blueprint(bp_admin)

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=5000, debug=True)

