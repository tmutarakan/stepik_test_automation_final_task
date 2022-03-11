from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def get_element_text(self, how, what: str):
        if self.is_element_present(how, what):
            return self.browser.find_element(how, what).text
        return None

    def match_product_name(self):
        # проверка, совпадения имён
        mes_name = self.get_element_text(*ProductPageLocators.MESSAGE_PRODUCT_NAME)
        name = self.get_element_text(*ProductPageLocators.PRODUCT_NAME)
        assert mes_name == name, "The names don't match"

    def match_product_price(self):
        # проверка, совпадения цен
        mes_price = self.get_element_text(*ProductPageLocators.MESSAGE_PRODUCT_PRICE)
        price = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)
        assert mes_price == price, "The prices don't match"
