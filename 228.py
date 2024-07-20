from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    firstname = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    firstname.send_keys('Marat')
    lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    lastname.send_keys('Nugumanov')
    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys('nugmarat@yandex.ru')
    import os
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'тест.txt'
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, '#file')
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button.click()
finally:
    time.sleep(10)
    browser.quit()