from flask import Blueprint, request

app = Blueprint('auth', __name__)

@app.route('/api/signin')
def signIn():
	return request.args.post('id', '')