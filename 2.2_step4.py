import math

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
    # browser.get(link)

    # # Ваш код
    # first = browser.find_element(By.ID, "num1")
    # x = first.text
    # second = browser.find_element(By.ID, "num2")
    # y = second.text
    # total = int(x)+int(y)
    # select = Select(browser.find_element(By.ID, "dropdown"))
    # select.select_by_value(str(total)).click() # ищем элемент с текстом ответа
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()