from page_objects.locators import OpencartCatalogLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_admin_page_correct_title(browser, url):
    browser.get(url + OpencartCatalogLocators.LAPTOPS_CATALOG_RELATIVE_URL)
    assert browser.title == "Laptops & Notebooks", "Wrong title of the Laptops & Notebooks catalog page"


def test_presence_of_pagination_info(browser, url):
    browser.get(url + OpencartCatalogLocators.LAPTOPS_CATALOG_RELATIVE_URL)
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartCatalogLocators.PAGINATION_TEXT))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")


def test_presence_of_compare_link(browser, url):
    browser.get(url + OpencartCatalogLocators.LAPTOPS_CATALOG_RELATIVE_URL)
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartCatalogLocators.COMPARE_HYPERLINK))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")


def test_presence_of_text_description_block(browser, url):
    browser.get(url + OpencartCatalogLocators.LAPTOPS_CATALOG_RELATIVE_URL)
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartCatalogLocators.DESCRIPTION_TEXT_BLOCK))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")


def test_presence_of_sorting_selector(browser, url):
    browser.get(url + OpencartCatalogLocators.LAPTOPS_CATALOG_RELATIVE_URL)
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartCatalogLocators.SORTING_SELECTOR))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")


def test_presence_of_input_limit(browser, url):
    browser.get(url + OpencartCatalogLocators.LAPTOPS_CATALOG_RELATIVE_URL)
    try:
        WebDriverWait(browser, 2). \
            until(EC.presence_of_element_located(OpencartCatalogLocators.INPUT_LIMIT))
    except TimeoutException:
        raise AssertionError("Couldn't find element after 2 seconds")
