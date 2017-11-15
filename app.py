from flask import Flask, request
from src import app
from src.api.auth import bp_auth
from src.api.heimu import bp_heimu
from src.api.voice import bp_voice
from src.api.weather import bp_weather
from src.admin.admin import bp_admin

app.register_blueprint(bp_auth)
app.register_blueprint(bp_heimu)
app.register_blueprint(bp_voice)
app.register_blueprint(bp_weather)
app.register_blueprint(bp_admin)

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=5000, debug=False)
