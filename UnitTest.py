import unittest
from selenium import webdriver

class SearchText(unittest.TestCase):
    def setUp(self):
        # create session
        self.driver = webdriver.Chrome()
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
        lists = self.driver.find_element_by_xpath()
        print(lists)
        # no = len(lists)
        # self.assertEquals(10,no)


if __name__ == '__main__':
    unittest.main()