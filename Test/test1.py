from selenium import webdriver
import time

import selenium

driver = webdriver.Chrome() # Create a session with Chromer using selenium webdriver
# driver = webdriver.Firefox()
# driver = webdriver.Edge()

driver.set_page_load_timeout(10) # set maximum time for load the page: 10s. If the page will not loaded in this time, it will occur a exception.
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("btnK").click()
time.sleep(4)
driver.quit()

# print("Hello QNT")

print("Phiên bản Selenium:", selenium.__version__)

# every time a new version of the driver is released, auto update webdriver version
# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Test 
driver.get("https://google.com")
time.sleep(2)
driver.close()
driver.quit()
print("Done")