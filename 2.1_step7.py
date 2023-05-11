import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    # Ваш код
    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    y = calc(x)
    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
