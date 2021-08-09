import pytest
from page_objects.locators import OpencartUrls
from selenium import webdriver

YANDEX_DRIVER_PATH = "C:\webdrivers\yandexdriver.exe"


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     choices=["chrome", "firefox", "opera", "edge", "yandex"],
                     default="chrome")
    parser.addoption("--url",
                     action="store",
                     default=OpencartUrls.OPENCART_MAIN_URL)


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
    elif choice == "yandex":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(YANDEX_DRIVER_PATH, options=options)

    request.addfinalizer(teardown)
    return driver

