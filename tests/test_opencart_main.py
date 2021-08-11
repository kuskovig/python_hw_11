from page_objects.locators import OpencartMainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random


def test_opens_mainpage_with_default_url(browser, url):
    browser.get(url)
    assert browser.title == "Your Store", "Wrong title of the  main page"


def test_there_is_slideshow(browser, url):
    browser.get(url)
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartMainPageLocators.MAIN_PAGE_SLIDESHOW))
    except TimeoutException:
        return False
    return True


def test_alert_correctly_closes(browser, url):
    browser.get(url)
    random_wishlist = random.randint(0, 3)
    # clicking wishlist button of random item
    wishlist_button = browser.find_elements(*OpencartMainPageLocators.
                                            RECOMMENDED_ITEMS_WISHLIST_BUTTONS)[random_wishlist]
    wishlist_button.click()
    # waiting for alert to appear and closing it
    try:
        alert_close_button = WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartMainPageLocators.WISHLIST_ATTEMPT_ALERT_CLOSE))
    except TimeoutException:
        return False
    alert_close_button.click()
    # asserting that alert correctly closed
    try:
        WebDriverWait(browser, 2). \
            until_not(EC.presence_of_element_located(OpencartMainPageLocators.WISHLIST_ATTEMPT_ALERT))
    except TimeoutException:
        return False
    return True


def test_presence_of_cart_button(browser, url):
    browser.get(url)
    try:
        WebDriverWait(browser, 2). \
            until_not(EC.presence_of_element_located(OpencartMainPageLocators.MAIN_PAGE_CART_BUTTON))
    except TimeoutException:
        return False
    return True


def test_presence_of_language_selector(browser, url):
    browser.get(url)
    try:
        WebDriverWait(browser, 2). \
            until_not(EC.presence_of_element_located(OpencartMainPageLocators.MAIN_PAGE_LANGUAGE_SELECTOR))
    except TimeoutException:
        return False
    return True


def test_presence_of_search_button(browser, url):
    browser.get(url)
    try:
        WebDriverWait(browser, 2). \
            until_not(EC.presence_of_element_located(OpencartMainPageLocators.SEARCH_BAR_SEARCH_BUTTON))
    except TimeoutException:
        return False
    return True
