from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    f = browser.find_element(By.CSS_SELECTOR, "#answer")
    f.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
