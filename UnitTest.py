import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

# UnitTest:
# The standard workflow is:
# 1. You define your own class derived from unittest.TestCase.
# 2. Then you fill it with functions that start with ‘test_’.
# 3. You run the tests by placing unittest.main() in your file, usually at the bottom
# 4. Methods setUp() and teatDown() are called prior and after each test case

class SearchText(unittest.TestCase):
    def setUp(self):
        # create session
        cap = DesiredCapabilities.FIREFOX
        cap['marionette'] = False
        self.driver = webdriver.Firefox(capabilities=cap)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # go to homepage
        self.driver.get("http://www.google.com")

    def test_search_by_text(self):
        #search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys("selenium automation")
        self.search_field.submit()
        lists = self.driver.find_elements_by_class_name("r")
        no=len(lists)
        self.assertEquals(11,len(lists))
        # no = len(lists)
        # self.assertEquals(10,no)
    def test_search_by_name(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("python class")
        self.search_field.submit()
        list_new = self.driver.find_elements_by_class_name("r")
        self.assertEqual(14, len(list_new))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()