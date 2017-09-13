# -*- coding: utf-8 -*-
import sys
import os
from unittest import TestCase

from nose.tools import ok_, eq_


from models.user import User


class TestUser():

	def test_get_user_by_email(self):
		email = 'valid@gmail.com'
		ok_(User.get_user_by_email(email))