import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    valuex = browser.find_element(By.ID, "input_value")
    x = valuex.text
    y = calc(x)

    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # browser.switch_to.window(window_name)
# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок. 
# Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

# new_window = browser.window_handles[1]
# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

# first_window = browser.window_handles[0]