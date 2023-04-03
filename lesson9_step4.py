import time
import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
res = calc(x)

answer = browser.find_element(By.CSS_SELECTOR, '#answer')
answer.send_keys(res)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(10)
browser.quit()