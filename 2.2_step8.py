import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    # Ваш код
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]').send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]').send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]').send_keys("iiiiii@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, '2.2_step8.txt')           # добавляем к этому пути имя файла 
    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()