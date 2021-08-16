from page_objects.locators import OpencartProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_admin_page_correct_title(browser, url):
    browser.get(url + OpencartProductPageLocators.PRODUCT_RELATIVE_URL)
    assert browser.title == "Sony VAIO", "Wrong title of the Sony VAIO page"


def test_presence_of_reviews_tab_link(browser, url):
    browser.get(url + OpencartProductPageLocators.PRODUCT_RELATIVE_URL)
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartProductPageLocators.REVIEWS_TAB_LINK))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")


def test_presence_of_add_review_button(browser, url):
    browser.get(url + OpencartProductPageLocators.PRODUCT_RELATIVE_URL)
    # open review tab
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartProductPageLocators.REVIEWS_TAB_LINK)).click()
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")

    # search for Continue button (which adds review)
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartProductPageLocators.ADD_REVIEW_BUTTON))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")


def test_presence_of_alert_for_norating_review(browser, url):
    browser.get(url + OpencartProductPageLocators.PRODUCT_RELATIVE_URL)
    # open review tab
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartProductPageLocators.REVIEWS_TAB_LINK)).click()
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")

    # click  Continue button without setting the rating
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartProductPageLocators.ADD_REVIEW_BUTTON)).click()
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")

    # search for warning alert
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartProductPageLocators.ADD_REVIEW_NO_RATING_ALERT)).click()
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")


def test_presence_of_add_to_cart_button(browser, url):
    browser.get(url + OpencartProductPageLocators.PRODUCT_RELATIVE_URL)
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartProductPageLocators.ADD_TO_CART_BUTTON))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")


def test_presence_of_added_to_cart_product_alert(browser, url):
    browser.get(url + OpencartProductPageLocators.PRODUCT_RELATIVE_URL)
    # clicking add to cart button
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartProductPageLocators.ADD_TO_CART_BUTTON)).click()
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")
    # searching for the alert
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartProductPageLocators.ADDED_TO_CART_ALERT))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")
