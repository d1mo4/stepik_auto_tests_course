import time

import body as body
from selenium.webdriver.common.by import By
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    link1 = ("http://suninjuly.github.io/registration1.html")
    link2 = ("http://suninjuly.github.io/registration2.html")
    browser.get(link1)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    time.sleep(1)
    input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    #Для успешного запуска теста по второй ссылке необходимо изменить локаторы
    #Получается что из за изменения локаторов тест по второй ссылке будет падать
    #input2 = browser.find_element(By.CLASS_NAME, "form-control.first")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "(//input[@placeholder='Input your email'])[1]")
    input3.send_keys("KalyuzhniyKO@gmail.com")
    input4 = browser.find_element(By.XPATH, "(//input[@placeholder='Input your phone:'])[1]")
    input4.send_keys("0981323798")
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text


finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()