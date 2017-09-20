# -*- coding: utf-8 -*-
import json

class Response():

	response = {
		"status" : 200,
		"data" : "",
		"error_message": ''
	}

	def __init__(self, status = '', data = '', error_message = ''):
		self.status = status
		self.data = data
		self.error_message = error_message

	def set_status(self, status):
		self.status = status

	def set_data(self, data):
		self.data = data

	def set_error_message(self, error_message):
		self.error_message = error_message

	def send(self):
		return json.dumps(self.response)