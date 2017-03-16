"""
Generic templates to send 
"""

class GenericTemplate:
	"""
	Generic template card widget

	Arguments: (title, item_url, image_url, subtitle, buttons<array>)

	"""

	def __init__(self, title, item_url, image_url, subtitle, buttons):
		self.title = title
		self.item_url = item_url
		self.image_url = image_url
		self.subtitle = subtitle
		self.buttons = buttons

	def to_json(self):
		return {
			'attachment': {
				'type': 'template',
				'elements': [{
					'title': self.title,
					'item_url': self.item_url,
					'image_url': self.image_url,
					'subtitle': self.subtitle,
					'buttons': self.buttons
				}]
			}
		}

class ButtonTemplate:
	"""
	Button template
	"""

	def __init__(self, text, buttons):
		self.text = text
		self.buttons = buttons

	def to_json(self):
		return {
			'attachment': {
				'type': 'template',
				'payload': {
					'template_type': 'button',
					'text': self.text,
					'buttons': self.buttons
				}
			}
		}


class ListTemplate:
	"""
	List template
	"""

	def __init__(self, text, list_items, button = None, top_element_style = None):
		self.text = text
		self.list_items = list_items
		self.button = button
		self.top_element_style = top_element_style

	def to_json(self):
		json = {
			'attachment': {
				'type': 'template',
				'payload': {
					'template_type': 'list',
					'elements': self.list_items,
					'buttons': [self.button]
				}
			}
		}
		if self.button is not None: json["buttons"] = [self.button]
		if self.top_element_style is not None: json["top_element_style"] = self.top_element_style
		return json


class ReceiptTemplate:
	def __init__(self, recipient_name, order_number, currency, payment_method, summary,
				 merchant_name = None, timestamp = None, order_url = None, elements = None,
				 address = None, adjustments = None):
		self.recipient_name = recipient_name
		self.merchant_name = merchant_name
		self.order_number = order_number
		self.currency = currency
		self.payment_method = payment_method
		self.timestamp = timestamp
		self.order_url = order_url
		self.elements = elements
		self.address = address
		self.summary = summary
		self.adjustments = adjustments


	def to_json(self):
		json = {
			"attachment": {
				"type": "template",
				"payload":{
					"template_type": "receipt",
					"recipient_name": self.recipient_name,
					"order_number": self.order_number,
					"currency": self.currency,
					"payment_method": self.payment_method,
					"summary": self.summary
				}
			}
		}
		if self.merchant_name is not None: json["merchant_name"] = self.merchant_name
		if self.timestamp is not None: json["timestamp"] = self.timestamp
		if self.order_url is not None: json["order_url"] = self.order_url
		if self.elements is not None: json["elements"] = self.elements
		if self.address is not None: json["address"] = self.address
		if self.adjustments is not None: json["adjustments"] = self.adjustments
		return json
