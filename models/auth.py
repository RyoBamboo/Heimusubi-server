import os
from flask import Blueprint

app = Blueprint("auth", __name__, url_prefix="/auth")

@app.route('/auth')
def test():
	print('tset')