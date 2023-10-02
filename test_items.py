from selenium.webdriver.common.by import By
import time


def test_check_button_add_to_basket_on_page(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    button_add_to_basket = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form button")
    assert button_add_to_basket, "button_add_to_basket is not present at page"