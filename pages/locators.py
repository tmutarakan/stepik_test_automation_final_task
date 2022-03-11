from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")


class BasketPageLocator:
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-title")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages strong')
    MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, '#messages p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')
