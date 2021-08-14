from selenium.webdriver.common.by import By


class OpencartMainPageLocators:
    OPENCART_BASE_URL = "https://demo.opencart.com"
    MAIN_PAGE_CART_BUTTON = (By.CSS_SELECTOR, "#cart button")
    MAIN_PAGE_HEADER_CART_LINK = (By.CSS_SELECTOR, "#top-links li:nth-child(4)")
    MAIN_PAGE_CURRENCY_SELECTOR = (By.CSS_SELECTOR, "#form-currency")
    MAIN_PAGE_SLIDESHOW = (By.CSS_SELECTOR, "#slideshow0.swiper-container")
    RECOMMENDED_ITEMS_WISHLIST_BUTTONS = (By.CSS_SELECTOR, ".product-layout button:nth-child(2)")
    WISHLIST_ATTEMPT_ALERT = (By.CSS_SELECTOR, ".alert")
    WISHLIST_ATTEMPT_ALERT_CLOSE = (By.CSS_SELECTOR, ".alert button")
    SEARCH_BAR_SEARCH_BUTTON = (By.CSS_SELECTOR, "span.input-group-btn button")


class OpencartCatalogLocators:
    LAPTOPS_CATALOG_RELATIVE_URL = "/index.php?route=product/category&path=18"
    COMPARE_HYPERLINK = (By.CSS_SELECTOR, "#compare-total")
    SORTING_SELECTOR = (By.CSS_SELECTOR, "#input-sort")
    INPUT_LIMIT = (By.CSS_SELECTOR, "#input-limit")
    DESCRIPTION_TEXT_BLOCK = (By.CSS_SELECTOR, "#content p:nth-child(1)")
    PAGINATION_TEXT = (By.CSS_SELECTOR, ".text-right")


class OpencartProductPageLocators:
    PRODUCT_RELATIVE_URL = "/index.php?route=product/product&path=18&product_id=46"
    REVIEWS_TAB_LINK = (By.CSS_SELECTOR, ".nav-tabs li:nth-child(2) a")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    ADDED_TO_CART_ALERT = (By.CSS_SELECTOR, ".alert")
    ADD_REVIEW_BUTTON = (By.CSS_SELECTOR, "#button-review")
    ADD_REVIEW_NO_RATING_ALERT = (By.CSS_SELECTOR, ".alert-danger")


class OpencartAdminLoginLocators:
    ADMINPAGE_RELATIVE_URL = "/admin/"
    ADMINPAGE_LOGIN_BUTTON = (By.CSS_SELECTOR, "button")
    FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, ".help-block a")
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    HEADER_LOGO = (By.CSS_SELECTOR, "#header-logo")
