from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    picture = browser.find_element(By.CSS_SELECTOR, "#treasure")
    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = picture.get_attribute('valuex')
    x = x_element
    print(x)
    y = calc(x)
    f = browser.find_element(By.CSS_SELECTOR, "#answer")
    f.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    button.click()
    time.sleep(1)
    button1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    button1.click()
    button2 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button2.click()
finally:
    time.sleep(25)
    browser.quit()
