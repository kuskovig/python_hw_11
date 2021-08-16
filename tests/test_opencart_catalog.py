from page_objects.locators import OpencartCatalogLocators
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
    browser.get(url + OpencartCatalogLocators.LAPTOPS_CATALOG_RELATIVE_URL)
    assert browser.title == "Laptops & Notebooks", "Wrong title of the Laptops & Notebooks catalog page"


def test_presence_of_pagination_info(browser, url):
    browser.get(url + OpencartCatalogLocators.LAPTOPS_CATALOG_RELATIVE_URL)
    wait_for_element(browser, OpencartCatalogLocators.PAGINATION_TEXT)


def test_presence_of_compare_link(browser, url):
    browser.get(url + OpencartCatalogLocators.LAPTOPS_CATALOG_RELATIVE_URL)
    wait_for_element(browser, OpencartCatalogLocators.COMPARE_HYPERLINK)


def test_presence_of_text_description_block(browser, url):
    browser.get(url + OpencartCatalogLocators.LAPTOPS_CATALOG_RELATIVE_URL)
    wait_for_element(browser, OpencartCatalogLocators.DESCRIPTION_TEXT_BLOCK)


def test_presence_of_sorting_selector(browser, url):
    browser.get(url + OpencartCatalogLocators.LAPTOPS_CATALOG_RELATIVE_URL)
    wait_for_element(browser, OpencartCatalogLocators.SORTING_SELECTOR)


def test_presence_of_input_limit(browser, url):
    browser.get(url + OpencartCatalogLocators.LAPTOPS_CATALOG_RELATIVE_URL)
    wait_for_element(browser, OpencartCatalogLocators.INPUT_LIMIT)
