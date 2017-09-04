import os
from flask import Blueprint

app = Blueprint("auth", __name__, url_prefix="/auth")

@app.route('/')
def test():
	print('tset')