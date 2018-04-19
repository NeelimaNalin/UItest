from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# create chrome session
cap = DesiredCapabilities().CHROME
cap['marionette'] = False
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# homepage navigation
driver.get("http://google.ca")

# identify text box
search_box = driver.find_element_by_id("lst-ib")
search_box.clear()

# search for keyword
search_box.send_keys("Web automation using Python")
search_box.submit()

# screenshot
driver.save_screenshot("C:/Users/neelima.nalin/PycharmProjects/UItest/screenshots/page1.png")

# close browser
driver.quit()