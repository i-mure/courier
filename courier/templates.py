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
					'buttons': buttons
				}]
			}
		}

class ButtonTemplate:
	"""
	Button template
	"""

	def __init__(self, text, buttons):
		self.title = title
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