import unittest
import os
import sys

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))

from courier import widgets

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


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
    """Need to implement this test
    """



if __name__ == '__main__':
    test_cases_to_run = [ButtonWidgetTests, ShareButtonWidgetTests, UnlinkAccountWidgetTests,
                         LoginButtonWidgetTests, CallButtonWidgetTests, PostbackButtonWidgetTests,
                         URLButtonWidgetTests]

    for test_case in test_cases_to_run:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
        unittest.TextTestRunner(verbosity=2).run(suite)