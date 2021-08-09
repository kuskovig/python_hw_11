from page_objects.locators import OpencartMainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_opens_mainpage_with_default_url(browser, url):
    browser.get(url)
    assert browser.title == "Your Store"

def test_there_is_slideshow(browser, url):
    browser.get(url)
    try:
        WebDriverWait(browser, 2).\
            until(EC.presence_of_element_located(OpencartMainPageLocators.MAIN_PAGE_SLIDESHOW))
    except TimeoutException:
        return False
    return True

def test_random_test(browser, url):
    browser.get(url)
    assert browser.find_element(*OpencartMainPageLocators.MAIN_PAGE_CART_BUTTON)