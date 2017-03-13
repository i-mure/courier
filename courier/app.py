import logging
import requests


from .constants import FB_URL, HEADERS_JSON


class Messenger:
	"""
		Class that represents a singleton used to send messages to the Facebook API

	"""

	def __init__(self, token=None)
		self.token = token
		self.post_url = FB_URL.format(self.token)

	@property
	def token(self):
		return self.token

	@token.setter(self, value):
		self.token = value

	def send(self, payload):
		"""
			send() : takes a payload and sends it to the API
					 returns tuple of (HTTP_STATUS_CODE, HTTP_STATUS_TEXT)

			payload: message should be propery formatted JSON dict/string

		"""
		status = requests.post(self.post_url,data=payload, headers=HEADERS_JSON)
		return (status.status_code, status.text)


		