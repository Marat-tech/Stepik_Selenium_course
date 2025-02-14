import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)
    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button.click()
    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    f = browser.find_element(By.CSS_SELECTOR, "#answer")
    f.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, '#solve')
    button2.click()
finally:
    time.sleep(20)
    browser.quit()


