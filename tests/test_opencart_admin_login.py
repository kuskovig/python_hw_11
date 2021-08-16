from page_objects.locators import OpencartAdminLoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_admin_page_correct_title(browser, url):
    browser.get(url + OpencartAdminLoginLocators.ADMINPAGE_RELATIVE_URL)
    assert browser.title == "Administration", "Wrong title of the Admin login page"


def test_presence_of_login_button(browser, url):
    browser.get(url + OpencartAdminLoginLocators.ADMINPAGE_RELATIVE_URL)
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartAdminLoginLocators.ADMINPAGE_LOGIN_BUTTON))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")


def test_presence_of_forgotten_password_link(browser, url):
    browser.get(url + OpencartAdminLoginLocators.ADMINPAGE_RELATIVE_URL)
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartAdminLoginLocators.FORGOTTEN_PASSWORD_LINK))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")


def test_presence_of_username_input_field(browser, url):
    browser.get(url + OpencartAdminLoginLocators.ADMINPAGE_RELATIVE_URL)
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartAdminLoginLocators.INPUT_USERNAME))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")


def test_presence_of_password_input_field(browser, url):
    browser.get(url + OpencartAdminLoginLocators.ADMINPAGE_RELATIVE_URL)
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartAdminLoginLocators.INPUT_PASSWORD))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")


def test_presence_of_header_logo(browser, url):
    browser.get(url + OpencartAdminLoginLocators.ADMINPAGE_RELATIVE_URL)
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartAdminLoginLocators.HEADER_LOGO))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")
