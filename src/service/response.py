# -*- coding: utf-8 -*-
import json

class Response():

	response = {
		"status" : 200,
		"data" : "",
		"error_message": ''
	}

	def __init__(self, status = '', data = '', error_message = ''):
		self.set_status(status)
		self.set_data(data)
		self.set_error_message(error_message)

	def set_status(self, status):
		self.response['status'] = status

	def set_data(self, data):
		self.response['data'] = data

	def set_error_message(self, error_message):
		self.response['error_message'] = error_message

	def send(self):
		return json.dumps(self.response)