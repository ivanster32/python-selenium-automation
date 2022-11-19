from selenium.webdriver.common.by import By
from behave import given, when, then

@given('open amazon bestsellers page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@when('click on login')
def  search_signin (context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

@then ('verify the {expected_count} links')
def verify_link_count(context, expected_count):
    links = context.driver.find_elements(By.XPATH, "//div[@class='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq']/ul/li/div/a")
    actual_count = str(len(links))
    assert actual_count == expected_count, f"Expected {expected_count} links but got {actual_count}"

