from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    number1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    number2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    x = number1.text
    y = number2.text
    i = int(x) + int(y)
    q = str(i)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(q)
    button2 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button2.click()
    print(i)
finally:
    time.sleep(25)
    browser.quit()