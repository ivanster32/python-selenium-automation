'//a[@id="nav-orders"]'
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path="/Users/ivansantana/Desktop/QA_Automation/python-selenium-automation/chromedriver 3")
driver.maximize_window()
driver.get("https://www.amazon.com/")
driver.find_element(By.XPATH, '//a[@id="nav-orders"]').click()
actual_result = driver.find_element(By.XPATH, '//h1').text
expected_result = 'Sign in'
assert expected_result == actual_result, f'Expected {expected_result} and got {actual_result}'
driver.quit() 