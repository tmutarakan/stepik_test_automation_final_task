from pages.base_page import BasePage
from pages.locators import BasketPageLocator


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocator.PRODUCT_IN_BASKET)

    def should_be_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocator.BASKET_IS_EMPTY)
        # print(self.browser.find_element(*BasketPageLocator.BASKET_IS_EMPTY).text)
