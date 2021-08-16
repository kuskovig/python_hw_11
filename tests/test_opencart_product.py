from page_objects.locators import OpencartProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_for_element(browser, element):
    try:
        element = WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(element))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")
    return element



def test_admin_page_correct_title(browser, url):
    browser.get(url + OpencartProductPageLocators.PRODUCT_RELATIVE_URL)
    assert browser.title == "Sony VAIO", "Wrong title of the Sony VAIO page"


def test_presence_of_reviews_tab_link(browser, url):
    browser.get(url + OpencartProductPageLocators.PRODUCT_RELATIVE_URL)
    wait_for_element(browser, OpencartProductPageLocators.REVIEWS_TAB_LINK)


def test_presence_of_add_review_button(browser, url):
    browser.get(url + OpencartProductPageLocators.PRODUCT_RELATIVE_URL)
    # open review tab
    review_tab = wait_for_element(browser, OpencartProductPageLocators.REVIEWS_TAB_LINK)
    review_tab.click()
    # search for Continue button (which adds review)
    wait_for_element(browser, OpencartProductPageLocators.ADD_REVIEW_BUTTON)



def test_presence_of_alert_for_norating_review(browser, url):
    browser.get(url + OpencartProductPageLocators.PRODUCT_RELATIVE_URL)
    # open review tab
    review_tab = wait_for_element(browser, OpencartProductPageLocators.REVIEWS_TAB_LINK)
    review_tab.click()
    continue_button = wait_for_element(browser, OpencartProductPageLocators.ADD_REVIEW_BUTTON)
    continue_button.click()
    # search for warning alert
    wait_for_element(browser, OpencartProductPageLocators.ADD_REVIEW_NO_RATING_ALERT)


def test_presence_of_add_to_cart_button(browser, url):
    browser.get(url + OpencartProductPageLocators.PRODUCT_RELATIVE_URL)
    wait_for_element(browser, OpencartProductPageLocators.ADD_TO_CART_BUTTON)


def test_presence_of_added_to_cart_product_alert(browser, url):
    browser.get(url + OpencartProductPageLocators.PRODUCT_RELATIVE_URL)
    # clicking add to cart button
    cart_button = wait_for_element(browser, OpencartProductPageLocators.ADD_TO_CART_BUTTON)
    cart_button.click()
    # searching for the alert
    wait_for_element(browser, OpencartProductPageLocators.ADDED_TO_CART_ALERT)
