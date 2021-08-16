from page_objects.locators import OpencartAdminLoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_for_element(browser, element):
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(element))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")


def test_admin_page_correct_title(browser, url):
    browser.get(url + OpencartAdminLoginLocators.ADMINPAGE_RELATIVE_URL)
    assert browser.title == "Administration", "Wrong title of the Admin login page"


def test_presence_of_login_button(browser, url):
    browser.get(url + OpencartAdminLoginLocators.ADMINPAGE_RELATIVE_URL)
    wait_for_element(browser, OpencartAdminLoginLocators.ADMINPAGE_LOGIN_BUTTON)


def test_presence_of_forgotten_password_link(browser, url):
    browser.get(url + OpencartAdminLoginLocators.ADMINPAGE_RELATIVE_URL)
    wait_for_element(browser, OpencartAdminLoginLocators.FORGOTTEN_PASSWORD_LINK)


def test_presence_of_username_input_field(browser, url):
    browser.get(url + OpencartAdminLoginLocators.ADMINPAGE_RELATIVE_URL)
    wait_for_element(browser, OpencartAdminLoginLocators.INPUT_USERNAME)


def test_presence_of_password_input_field(browser, url):
    browser.get(url + OpencartAdminLoginLocators.ADMINPAGE_RELATIVE_URL)
    wait_for_element(browser, OpencartAdminLoginLocators.INPUT_PASSWORD)


def test_presence_of_header_logo(browser, url):
    browser.get(url + OpencartAdminLoginLocators.ADMINPAGE_RELATIVE_URL)
    wait_for_element(browser, OpencartAdminLoginLocators.HEADER_LOGO)
