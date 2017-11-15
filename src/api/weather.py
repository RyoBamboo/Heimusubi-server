import sys
import json
from flask import Blueprint, request
from pprint import pprint
import urllib.request

from src import db

from src.models.address import Address

bp_weather = Blueprint('weather', __name__)


@bp_weather.route('/api/weather/update')
def udpate():

	addresses = Address.get_all()
	for address in addresses:
		city_id = address.open_weather_id
		app_id = '1faf5a4f569c8d1ad490cdf120193875'
		url = 'http://api.openweathermap.org/data/2.5/weather?id=' + str(city_id) + '&APPID=' + str(app_id)
		with urllib.request.urlopen(url) as response:
			result = response.read()
			data = json.loads(result)
			weather_data = data['weather']
			weather_id = weather_data[0]['id']
			Address.update_by('id', address.id, weather_id)
			print(address.id)

	return 'ok'



@bp_weather.route('/api/weather/get', methods=['POST'])
def get():

	for address in addresses:
		city_id = address.open_weather_id
		app_id = '1faf5a4f569c8d1ad490cdf120193875'
		url = 'http://api.openweathermap.org/data/2.5/weather?id=' + str(city_id) + '&APPID=' + str(app_id)
		with urllib.request.urlopen(url) as response:
			result = response.read()
			data = json.loads(result)
			weather_data = data['weather']
			weather_id = weather_data[0]['id']
			Address.update_by('id', address.id, weather_id)
			print(address.id)

	return 'ok'
