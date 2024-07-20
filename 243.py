from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/wait1.html"
    browser.implicitly_wait(5)
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "#verify") #тест падает, потому что кнопка появляется с задержкой
    button.click()
    message = browser.find_element(By.CSS_SELECTOR, "#verify_message")
    assert "successful!" in message.text
finally:
    time.sleep(10)
    browser.quit()

