import time
import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

button = browser.find_element(By.ID, "book")
button.click()

x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
res = calc(x)

answer = browser.find_element(By.CSS_SELECTOR, '#answer')
answer.send_keys(res)

button = browser.find_element(By.ID, "solve")
button.click()

time.sleep(10)
browser.quit()