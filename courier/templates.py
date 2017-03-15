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