#https://selenium-python.readthedocs.io/
#http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/
#https://demo.seleniumeasy.com/

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from msedge.selenium_tools import Edge, EdgeOptions
# options = webdriver.ChromeOptions()
# options.add_argument("--log-level=0")
# options.add_argument("--disable-extensions")
# service = ChromeService(executable_path='E:\Python\Automation_Testing\chromedriver.exe')
# driver = webdriver.Chrome(service=service)

#Chrome
chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

# This solves the issue with the Popup for those that encounter it:
chrome_browser.implicitly_wait(2)
popup =chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
popup.click()

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')
 
time.sleep(2)
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
show_message_button.click()
 
output_message = chrome_browser.find_element(By.ID, 'display')
assert 'I AM EXTRA COOOOL' in output_message.text

time.sleep(5)
chrome_browser.quit()

#end chrom

#edge
driver = webdriver.Edge()

driver.get('https://bing.com')

element = driver.find_element(By.ID, 'sb_form_q')
element.send_keys('WebDriver')
element.submit()

time.sleep(5)
driver.quit()
#end edge






