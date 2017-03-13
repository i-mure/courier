# -*- coding: utf-8 -*-


class Button:
	"""
		Creates a button element can be of any type with any arguments
		
	"""
	def __init__(self, btn_type='', btn_title='', **kwargs):
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
	def __init__(self, reply_title='', reply_payload=''):
		self.reply_title = reply_title
		self.reply_payload = reply_payload

	def to_json(self):
		return {'content_type': 'text', 'title': self.reply_title, 'payload': self.reply_payload}



