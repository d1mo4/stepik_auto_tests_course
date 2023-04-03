import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
res = calc(x)

browser.execute_script("window.scrollBy(0, 100);")

answer = browser.find_element(By.CSS_SELECTOR, '#answer')
answer.send_keys(res)

check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
check.click()

rr = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
rr.click()

button = browser.find_element(By.TAG_NAME, "button")
button.click()
time.sleep(10)
browser.quit()