import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from  selenium.webdriver.common.by import By

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        cap = DesiredCapabilities.FIREFOX
        cap['marionette'] = False
        inst.driver = webdriver.Firefox(capabilities=cap)
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get("http://www.google.com/")
    def test_search_text_box(self):
        self.assertTrue(self.is_element_present(By.NAME,"q"))

    def test_image_link(self):
        image_link = self.driver.find_element_by_link_text("Images")
        image_link.click()
        self.assertTrue(self.is_element_present(By.NAME,"q"))
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("Selenium Webdriver framework architecture diagram")
        self.search_field.submit()
    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how,value=what)
        except NoSuchElementException: return False
        return True
if __name__ == '__main__':
    unittest.main()