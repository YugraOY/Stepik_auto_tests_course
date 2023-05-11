import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код
    valuex = browser.find_element(By.ID, "input_value")
    x = valuex.text
    y = calc(x)
    ans = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", ans)
    ans.send_keys(y)
    check = browser.find_element(By.ID, "robotCheckbox").click()
    rr = browser.find_element(By.ID, "robotsRule").click()
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()