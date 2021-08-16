from page_objects.locators import OpencartMainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random


def wait_for_element(browser, element):
    try:
        element = WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(element))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")
    return element


def test_opens_mainpage_with_default_url(browser, url):
    browser.get(url)
    assert browser.title == "Your Store", "Wrong title of the  main page"


def test_there_is_slideshow(browser, url):
    browser.get(url)
    wait_for_element(browser, OpencartMainPageLocators.MAIN_PAGE_SLIDESHOW)



def test_alert_correctly_closes(browser, url):
    browser.get(url)
    random_wishlist = random.randint(0, 3)
    # clicking wishlist button of random item
    wishlist_button = browser.find_elements(*OpencartMainPageLocators.
                                            RECOMMENDED_ITEMS_WISHLIST_BUTTONS)[random_wishlist]
    wishlist_button.click()
    # waiting for alert to appear and closing it
    alert_close_button = wait_for_element(browser, OpencartMainPageLocators.WISHLIST_ATTEMPT_ALERT_CLOSE)
    alert_close_button.click()
    # asserting that alert correctly closed
    try:
        WebDriverWait(browser, 2). \
            until_not(EC.presence_of_element_located(OpencartMainPageLocators.WISHLIST_ATTEMPT_ALERT))
    except TimeoutException:
        raise AssertionError("Element didn't disappear after 2 seconds")


def test_presence_of_cart_button(browser, url):
    browser.get(url)
    wait_for_element(browser, OpencartMainPageLocators.MAIN_PAGE_CART_BUTTON)


def test_presence_of_currency_selector(browser, url):
    browser.get(url)
    wait_for_element(browser, OpencartMainPageLocators.MAIN_PAGE_CURRENCY_SELECTOR)


def test_presence_of_search_button(browser, url):
    browser.get(url)
    wait_for_element(browser, OpencartMainPageLocators.SEARCH_BAR_SEARCH_BUTTON)
