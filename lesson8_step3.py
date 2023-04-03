from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    n1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
    n2 = browser.find_element(By.CSS_SELECTOR, '#num2').text
    res = int(n1) + int(n2)

    lst = browser.find_element(By.CSS_SELECTOR, '#dropdown')
    lst.click()

    answer = browser.find_element(By.CSS_SELECTOR, f'[value=\'{res}\']')
    answer.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()