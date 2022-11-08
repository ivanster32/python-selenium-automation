from selenium.webdriver.common.by import By
from behave import given, when, then

@given('open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('search for the coffee')
def  search_product(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()



