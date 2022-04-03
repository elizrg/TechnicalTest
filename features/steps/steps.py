import time

from behave import *
import unittest
from function.functions import Functions


class PruebaTest(unittest.TestCase):

    @given(u'the user open the browser')
    def test_openBrowserChrome(self):
        # parameters
        link_browser = "https://www.google.com.co"
        expected_value = "https://www.google.com.co"
        message = "links browser do not match"
        title = Functions.openBrowserChrome(self, link_browser, "Google")
        self.assertEqual("Google", title, "Different")

    @then(u'the user type and search the word on the google search engine')
    def test_searchWord(self):
    # parameters
        search_word = "Simetrik"
        expected_value = "Simetrik"
        message = "Words do not match"
        results = Functions.searchWord(self, search_word)
        self.assertIsNot(0, results, "Equals")


