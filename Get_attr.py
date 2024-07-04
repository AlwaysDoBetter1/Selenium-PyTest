import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/get_attribute.html'
browser.get(link)

row = browser.find_element(By.ID, 'treasure')
x_element = row.get_attribute('valuex')
y = calc(x_element)

#filling page
browser.find_element(By.ID, 'answer').send_keys(y)
browser.find_element(By.ID, 'robotCheckbox').click()
browser.find_element(By.ID, 'robotsRule').click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(20)