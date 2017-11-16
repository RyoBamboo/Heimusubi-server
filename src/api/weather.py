import sys
import json
from flask import Blueprint, request
from pprint import pprint
import urllib.request
import time

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

			index = str(weather_id)[0:1]

			weather_status = 0

			if index == '2':
				weather_status = 1
			elif index == '3':
				weather_status = 2
			elif index == '5':
				weather_status = 2
			elif index == '6':
				weather_status = 2
			elif index == '7':
				weather_status = 1
			elif index == '8':
				weather_status = 1
			
			if weather_id == 800:
				weather_status = 0

			print('天気の状態は' + str(weather_status))
			print('天気の元のIDは'+str(weather_id))

			Address.update_by('id', address.id, weather_status)
			print('更新したアドレスIDは'+str(address.id))
			time.sleep(2.0)

	return 'ok'



@bp_weather.route('/api/weather/get', methods=['POST'])
def get():
	address_id = request.form['address_id']
	address = Address.get_by('id', address_id)
	weather_status = address.weather_status
	return str(weather_status)
