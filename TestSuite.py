import unittest

import os
from HtmlTestRunner import HTMLTestRunner
from UnitTest import SearchText
from GoogleImage import HomePageTest

# get the directory path to output report file
dir = os.getcwd()


# get all tests from SearchText and HomePageTest class
search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text])

# run the suite
runner = HTMLTestRunner(output='example_test_suite')


# run the suite using HTMLTestRunner
runner.run(test_suite)