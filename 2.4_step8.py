import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try: 
    browser = webdriver.Chrome()
    browser.implicitly_wait(12) # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ваш код
    book = browser.find_element(By.ID, "book")
    #price = browser.find_element(By.ID, "price")
    check = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    book.click()

    button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    valuex = browser.find_element(By.ID, "input_value")
    x = valuex.text
    y = calc(x)

    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(y)

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()