import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(y)
    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()
    rr = browser.find_element(By.ID, "robotsRule")
    rr.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()