# -*- coding: utf-8 -*-


class Button:
	"""
	Creates a button element can be of any type with any arguments
		
	"""
	def __init__(self, btn_type, btn_title, **kwargs):
		self.btn_type  = btn_type
		self.btn_title = btn_title
		self._args     = kwargs

	def to_json(self):
		payload = {'type': self.btn_type, 'title': self.btn_title}
		payload.update(self._args)
		return payload

class ButtonShare:
	"""
	Creates a share button
	"""
	def __init__(self):
		pass

	def to_json(self):
	    return {'type': 'element_share'}


class QuickReply:
	"""
	Creates a quick reply element 
	"""
	def __init__(self, reply_title, reply_payload):
		self.reply_title = reply_title
		self.reply_payload = reply_payload

	def to_json(self):
		return {'content_type': 'text', 'title': self.reply_title, 'payload': self.reply_payload}

class QuickReplyImage:
	"""
	Creates a quick reply element  with an image
	"""
	def __init__(self, reply_title, reply_payload, reply_image):
		self.reply_title = reply_title
		self.reply_payload = reply_payload

	def to_json(self):
		return {'content_type': 'text', 'title': self.reply_title, 'payload': self.reply_payload, 'image_url': self.reply_image}


class QuickLocation:
	"""
	Creates a quick reply location getter element 
	"""
	def __init__(self):

	def to_json(self):
		return {'content_type': 'location'}



class SenderAction:
	""""
		Return a sender action:
			mark_seen, typing_on , typing_off
	"""
	def __init__(self, action):
		self.action = action

	def to_json(self):
		return {'sender_action': self.action}


