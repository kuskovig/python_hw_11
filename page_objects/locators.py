from selenium.webdriver.common.by import By


class OpencartUrls:

    OPENCART_DESKTOP_CATALOG_URL = "https://demo.opencart.com/index.php?route=product/category&path=20"
    OPENCART_PRODUCT_CARD_URL = "https://demo.opencart.com/index.php?route=product/product&path=20&product_id=44"



class OpencartMainPageLocators:
    OPENCART_BASE_URL = "https://demo.opencart.com"
    MAIN_PAGE_CART_BUTTON = (By.CSS_SELECTOR, "#cart button")
    MAIN_PAGE_HEADER_CART_LINK = (By.CSS_SELECTOR, "#top-links li:nth-child(4)")
    MAIN_PAGE_LANGUAGE_SELECTOR = (By.CSS_SELECTOR, "#form-language")
    MAIN_PAGE_SLIDESHOW = (By.CSS_SELECTOR, "#slideshow0.swiper-container")
    RECOMMENDED_ITEMS_WISHLIST_BUTTONS = (By.CSS_SELECTOR, ".product-layout button:nth-child(2)")  # all the buttons
    WISHLIST_ATTEMPT_ALERT = (By.CSS_SELECTOR, ".alert")
    WISHLIST_ATTEMPT_ALERT_CLOSE = (By.CSS_SELECTOR, ".alert button")
    SEARCH_BAR_SEARCH_BUTTON = (By.CSS_SELECTOR, "span.input-group-btn button")


class OpencartCatalogLocators:
    a = 1


class OpencartProductPageLocators:
    a = 1


class OpencartAdminLoginLocators:
    ADMINPAGE_RELATIVE_URL = "/admin/"
    ADMINPAGE_LOGIN_BUTTON = (By.CSS_SELECTOR, "button")
    FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, ".help-block a")
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    HEADER_LOGO = (By.CSS_SELECTOR, "#header-logo")


