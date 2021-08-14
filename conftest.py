import pytest
from page_objects.locators import OpencartMainPageLocators
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     choices=["chrome", "firefox", "opera", "edge"],
                     default="chrome")
    parser.addoption("--url",
                     action="store",
                     default=OpencartMainPageLocators.OPENCART_BASE_URL)


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def browser(request):

    def teardown():
        driver.quit()

    choice = request.config.getoption("--browser")
    driver = None
    if choice == "chrome":
        driver = webdriver.Chrome()
    elif choice == "firefox":
        driver = webdriver.Firefox()
    elif choice == "opera":
        driver = webdriver.Opera()
    elif choice == "edge":
        driver = webdriver.Edge()

    request.addfinalizer(teardown)
    return driver
