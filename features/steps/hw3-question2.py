from selenium.webdriver.common.by import By
from behave import given, when, then

@when ('click on orders')
def click_on_orders(context):
    context.driver.find_element(By.XPATH, '//a[@id="nav-orders"]').click()

@then('verify the sign in page is open')
def verify_sign_in_page_is_open(context):
    actual_result = context.driver.find_element(By.XPATH, '//h1').text
    expected_result = 'Sign in'
    assert expected_result == actual_result, f'Expected {expected_result} and got {actual_result}'

