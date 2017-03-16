from .widgets import *

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
					'elements': self.list_items
				}
			}
		}
		if self.button is not None: json["payload"]["buttons"] = [self.button]
		if self.top_element_style is not None: json["payload"]["top_element_style"] = self.top_element_style
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
		if self.merchant_name is not None: json["payload"]["merchant_name"] = self.merchant_name
		if self.timestamp is not None: json["payload"]["timestamp"] = self.timestamp
		if self.order_url is not None: json["payload"]["order_url"] = self.order_url
		if self.elements is not None: json["payload"]["elements"] = self.elements
		if self.address is not None: json["payload"]["address"] = self.address
		if self.adjustments is not None: json["payload"]["adjustments"] = self.adjustments
		return json


class AirlineBoardingPassTemplate:
	"""Send a message that contains boarding passes for one or more flights or one more passengers
    """

	def __init__(self, intro_message, locale, boarding_pass: list[BoardingPass], theme_color):
		self.intro_message = intro_message
		self.locale = locale
		self.boarding_pass = boarding_pass
		self.theme_color = theme_color


	def to_json(self):
		json = {
			"attachement":{
				"type": "template",
				"payload": {
					"template_type": "template_type",
					"intro_message": self.intro_message,
					"locale": self.locale,
					"boarding_pass": self.boarding_pass
				}
			}
		}
		if self.theme_color is not None: json["payload"]["theme_color"] = self.theme_color
		return json


class AirlineCheckinReminderTemplate:
	"""Send a check-in reminder message
    """

	def __init__(self, intro_message, locale, pnr_number, flight_info: list[FlightInfo],
				 checkin_url, theme_color = None):
		self.intro_message = intro_message
		self.locale = locale
		self.pnr_number = pnr_number
		self.checkin_url = checkin_url
		self.flight_info = flight_info
		self.theme_color = theme_color

	def to_json(self):
		json = {
			"attachement": {
				"type": "template",
				"payload": {
					"template_type": "airline_checkin",
					"intro_message": self.intro_message,
					"locale": self.locale,
					"checkin_url": self.checkin_url,
					"pnr_number": self.pnr_number,
					"boarding_pass": self.flight_info
				}
			}
		}
		if self.theme_color is not None: json["payload"]["theme_color"] = self.theme_color
		return json


class AirlineItineraryTemplate:
	"""Send a confirmation message that contains the itinerary and receipt.
    """

	def __init__(self, intro_message, locale, pnr_number, passenger_info: list[PassengerInfo],
				 flight_info: list[IteneraryFlightInfo], passenger_segment_info: list[PassengerSegmentInfo],
				 total_price, currency, price_info: list[PriceInfo] = None, base_price = None, tax = None,
				 theme_color = None):
		self.intro_message = intro_message
		self.locale = locale
		self.pnr_number = pnr_number
		self.passenger_info = passenger_info
		self.passenger_segment_info = passenger_segment_info
		self.total_price = total_price
		self.currency = currency
		self.price_info = price_info
		self.base_price = base_price
		self.tax = tax
		self.flight_info = flight_info
		self.theme_color = theme_color

	def to_json(self):
		json = {
			"attachement": {
				"type": "template",
				"payload": {
					"template_type": "airline_itinerary",
					"intro_message": self.intro_message,
					"locale": self.locale,
					"pnr_number": self.pnr_number,
					"passenger_info": self.passenger_info,
					"flight_info": self.flight_info,
					"passenger_segment_info": self.passenger_segment_info,
					"total_price": self.total_price,
					"currency": self.currency,
					"boarding_pass": self.flight_info
				}
			}
		}
		if self.price_info is not None: json["payload"]["price_info"] = self.price_info
		if self.base_price is not None: json["payload"]["base_price"] = self.base_price
		if self.tax is not None: json["payload"]["tax"] = self.tax
		if self.theme_color is not None: json["payload"]["theme_color"] = self.theme_color
		return json