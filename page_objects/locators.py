from selenium import webdriver
from selenium.webdriver.common.by import By


class OpencartUrls:
    OPENCART_MAIN_URL = "http://demo-opencart.ru/"
    OPENCART_DESKTOP_CATALOG_URL = "http://demo-opencart.ru/index.php?route=product/category&path=20"
    OPENCART_PRODUCT_CARD_URL = "http://demo-opencart.ru/index.php?route=product/product&path=20&product_id=44"
    OPENCART_ADMINPAGE_LOGIN_URL = "http://demo-opencart.ru/admin/"

class OpencartMainPageLocators:
    MAIN_PAGE_CART_BUTTON = (By.CSS_SELECTOR, "#cart button")
    MAIN_PAGE_HEADER_CART_LINK = (By.CSS_SELECTOR, "#top-links li:nth-child(4)")
    MAIN_PAGE_LANGUAGE_SELECTOR = (By.CSS_SELECTOR, "#form-language")
    MAIN_PAGE_SLIDESHOW = By.CSS_SELECTOR, "#slideshow0.swiper-container"
class OpencartCatalogLocators:
    a=1
class OpencartProductPageLocators:
    a=1
class OpencartAdminLoginLocators:
    a=1