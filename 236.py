from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    f = browser.find_element(By.CSS_SELECTOR, "#answer")
    f.send_keys(y)
    button1 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button1.click()
finally:
    time.sleep(25)
    browser.quit()