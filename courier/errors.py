# -*- coding: utf-8 -*-

""""
All the errors raised/used by Courier.

"""

class CourierError(Exception):
	"""
	Base exception for the courier library
	"""
	def __init__(self, message):
		self._message = message

	def __str__(self):
		return self._message


class CourierRequestError(CourierError):
	pass


class TemplateError(CourierError):
	pass