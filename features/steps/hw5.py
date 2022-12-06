from selenium.webdriver.common.by import By
from behave import given, when, then

@given  ('Open product page')
def click_on_orders(context):
    context.driver.get("https://www.amazon.com/gp/product/B07BJKRR25/")

@then('Click on every color')
def verify_sign_in_page_is_open(context):
    expected_colors = ['Black', 'Blue, Over Dye','Bright White','Dark Blue Vintage','Dark Indigo/Rinsed', 'Dark Khaki Brown','Dark Wash', 'Indigo Wash','Light Blue Vintage','Light Khaki Brown','Light Wash','Medium Blue, Vintage','Medium Wash' ,'Olive', 'Rinsed', 'Sage Green', 'Vintage Wash', 'Washed Black','Washed Grey']
    colors = context.driver.find_elements(By.CSS_SELECTOR, "#variation_color_name ul li")

    for color in colors:
        color.click()
        current_color_name = context.driver.find_element(By.CSS_SELECTOR, "#variation_color_name span.selection").text
        assert current_color_name in expected_colors, f'{current_color_name} is not inside the list'
