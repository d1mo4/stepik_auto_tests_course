import time
import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)

button = browser.find_element(By.ID, "button")
button.click()

time.sleep(5)
browser.quit()