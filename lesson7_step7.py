from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element(By.CSS_SELECTOR, 'img').get_attribute('valuex')
    res = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(res)

    check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    check.click()

    rr = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    rr.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()