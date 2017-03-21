import unittest
import os
import sys

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))

from courier import widgets, templates
from courier.app import serialize_

class ButtonWidgetTests(unittest.TestCase):

    def test_isdict(self):
        btn = widgets.Button (None, None)
        self.assertTrue(type(btn.to_json()) is dict)

    def test_format(self):
        btn = widgets.Button("test_type", "test_title")
        self.assertEquals(btn.to_json(),     {
        "type":"test_type",
        "title":"test_title"
      })

    def test_optional_format(self):
        btn = widgets.Button("test_type")
        self.assertEquals(btn.to_json(),     {
        "type":"test_type"
      })

    def test_wrong_format(self):
        btn = widgets.Button("test_type", "test_title")
        self.assertNotEqual(btn.to_json(), {
            "type": "test",
            "title": "test"
        })

class ShareButtonWidgetTests(unittest.TestCase):

    def test_isdict(self):
        btn = widgets.ShareButton()
        self.assertTrue(type(btn.to_json()) is dict)

    def test_format(self):
        btn = widgets.ShareButton()
        self.assertEquals(btn.to_json(),     {
        "type":"element_share"
      })

    def test_wrong_format(self):
        btn = widgets.ShareButton()
        self.assertNotEqual(btn.to_json(), {
            "type": "element_share",
            "title": "test"
        })

class UnlinkAccountWidgetTests(unittest.TestCase):

    def test_isdict(self):
        btn = widgets.UnlinkAccount()
        self.assertTrue(type(btn.to_json()) is dict)

    def test_format(self):
        btn = widgets.UnlinkAccount()
        self.assertEquals(btn.to_json(),     {
        "type":"account_unlink"
      })

    def test_wrong_format(self):
        btn = widgets.UnlinkAccount()
        self.assertNotEqual(btn.to_json(), {
            "type": "account_unlink",
            "title": "test"
        })


class LoginButtonWidgetTests(unittest.TestCase):

    def test_isdict(self):
        btn = widgets.LoginButton(None)
        self.assertTrue(type(btn.to_json()) is dict)

    def test_format(self):
        btn = widgets.LoginButton("url")
        self.assertEquals(btn.to_json(),     {
            "type":"account_link",
            "url": "url"
      })

    def test_wrong_format(self):
        btn = widgets.LoginButton("url")
        self.assertNotEqual(btn.to_json(), {
            "type": "account_link",
            "url": "tst"
        })


class CallButtonWidgetTests(unittest.TestCase):

    def test_isdict(self):
        btn = widgets.CallButton(None, None)
        self.assertTrue(type(btn.to_json()) is dict)

    def test_format(self):
        btn = widgets.CallButton("title", "32480923")
        self.assertEquals(btn.to_json(),     {
            "type": "phone_number",
            "title":"title",
            "payload": "32480923"
      })

    def test_wrong_format(self):
        btn = widgets.CallButton("title", "32480923")
        self.assertNotEqual(btn.to_json(), {
            "type": "phone_number",
            "title": "account_link",
            "payload": "tst"
        })


class PostbackButtonWidgetTests(unittest.TestCase):

    def test_isdict(self):
        btn = widgets.PostbackButton(None, None)
        self.assertTrue(type(btn.to_json()) is dict)

    def test_format(self):
        btn = widgets.PostbackButton("Bookmark Item", "DEVELOPER_DEFINED_PAYLOAD")
        self.assertEquals(btn.to_json(),     {
            "type": "postback",
            "title": "Bookmark Item",
            "payload": "DEVELOPER_DEFINED_PAYLOAD"
      })

    def test_wrong_format(self):
        btn = widgets.PostbackButton("title", "32480923")
        self.assertNotEqual(btn.to_json(), {
            "type": "postback",
            "title": "Bookmark Item",
            "payload": "PAYLOAD"
        })


class URLButtonWidgetTests(unittest.TestCase):

    def test_isdict(self):
        btn = widgets.URLButton(None, None)
        self.assertTrue(type(btn.to_json()) is dict)

    def test_format(self):

        btn = widgets.URLButton("View Item", "https://petersfancyapparel.com/classic_white_tshirt",
                                     webview_height_ratio=widgets.URLButton.WebviewHeightRatio.compact)
        self.assertEquals(btn.to_json(),     {
            "type": "web_url",
            "url": "https://petersfancyapparel.com/classic_white_tshirt",
            "title": "View Item",
            "webview_height_ratio": "compact"
      })

    def test_wrong_format(self):
        btn = widgets.URLButton("View Item", "https://petersfancyapparel.com/classic_white_tshirt",
                                     widgets.URLButton.WebviewHeightRatio.compact)
        self.assertNotEqual(btn.to_json(), {
            "type": "web_url",
            "url": "http",
            "title": "View Item",
            "webview_height_ratio": "compact"
        })


class BuyButtonWidgetTests(unittest.TestCase):
    """
    Need to implement this test
    """
    pass

class GenericTemplateTests(unittest.TestCase):
    def setUp(self):
        self._template = templates.GenericTemplate('Test template', 'https://item-url.com', 'https://item-url.com/img.jpg', 'Test Subtitle', 
                                                    [widgets.PostbackButton('Hello', 'Hello')])
        self._template_string = {
                                    'attachment': {
                                        'type': 'template',
                                        'elements': [{
                                            'title': 'Test template',
                                            'item_url': 'https://item-url.com',
                                            'image_url': 'https://item-url.com/img.jpg',
                                            'subtitle': 'Test Subtitle',
                                            'buttons': [
                                                {
                                                    'title': 'Hello',
                                                    'type': 'postback',
                                                    'payload': 'Hello'
                                                }
                                            ]
                                        }]
                                    }
                                }

    def test_generic_template(self):
        self.assertEqual(serialize_(self._template.to_json()), self._template_string)

class ButtonTemplateTests(unittest.TestCase):
    def setUp(self):
        self._template = templates.ButtonTemplate('Test Buttons', [widgets.PostbackButton('Hello', 'Hello')])

        self._template_string = {
            'attachment': {
                'type': 'template',
                'payload': {
                    'template_type': 'button',
                    'text': 'Test Buttons',
                    'buttons':  [
                        {
                            'title': 'Hello',
                            'type': 'postback',
                            'payload': 'Hello'
                        }
                    ]
                }
            }
        }


    def test_button_template(self):
        self.assertEqual(serialize_(self._template.to_json()), self._template_string)



if __name__ == '__main__':
    test_cases_to_run = [ButtonWidgetTests, ShareButtonWidgetTests, UnlinkAccountWidgetTests,
                         LoginButtonWidgetTests, CallButtonWidgetTests, PostbackButtonWidgetTests,
                         URLButtonWidgetTests, 

                         # Template Tests
                         GenericTemplateTests, ButtonTemplateTests]

    for test_case in test_cases_to_run:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
        unittest.TextTestRunner(verbosity=2).run(suite) 
