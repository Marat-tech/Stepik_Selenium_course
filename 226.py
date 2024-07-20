from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    f = browser.find_element(By.CSS_SELECTOR, "#answer")
    f.send_keys(y)
    button1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    button1.click()
    button2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("window.scrollBy(0, 400);", button2)
    button2.click()
    button.click()
finally:
    time.sleep(25)
    browser.quit()
