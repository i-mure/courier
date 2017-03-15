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
		pass

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


class ListItem:
	""""
		Standard widget for items in a list template
	"""
	def __init__(self, title, subtitle = None, default_action = None, button = None,
				 image_url = None):
		self.title = title
		self.subtitle = subtitle
		self.default_action = default_action
		self.button = button
		self.image_url = image_url


	def to_json(self):
		json = {
			"title": self.title
		}
		if self.subtitle is not None: json["subtitle"] = self.subtitle
		if self.default_action is not None: json["default_action"] = self.default_action
		if self.button is not None: json["button"] = [self.button]
		if self.image_url is not None: json["image_url"] = self.image_url
		return json


class DefaultAction:
	""""
		Adds clickable events to various widgets
    """
	TYPE_WEB_URL = "web_url"
	WEB_HEIGHT_TALL = "tall"

	def __init__(self, type, url = None, messenger_extensions = True,
				 web_view_ratio = TYPE_WEB_URL, fallback_url = None):
		self.type = type
		self.url = url
		self.messenger_extensions = messenger_extensions
		self.web_view_ratio = web_view_ratio
		self.fallback_url = fallback_url


	def to_json(self):
		json = {
			"type": self.type,
			"messenger_extensions": self.messenger_extensions,
			"webview_height_ratio": self.web_view_ratio
		}
		if self.type == self.TYPE_WEB_URL :
			json["url"] = self.url
			json["fallback_url"] = self.fallback_url if self.fallback_url is not None else self.url

		return json