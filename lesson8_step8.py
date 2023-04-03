import time
import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.CSS_SELECTOR, 'input[name=\'firstname\']')
input1.send_keys("Ivan")
input2 = browser.find_element(By.CSS_SELECTOR, 'input[name=\'lastname\']')
input2.send_keys("Ivan")
input3 = browser.find_element(By.CSS_SELECTOR, 'input[name=\'email\']')
input3.send_keys("Ivan")

download = browser.find_element(By.CSS_SELECTOR, '#file')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')

download.send_keys(file_path)


button = browser.find_element(By.TAG_NAME, "button")
button.click()
time.sleep(10)
browser.quit()