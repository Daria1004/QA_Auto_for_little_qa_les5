from pages.base_page import BasePage


class CartPage(BasePage):
    SELECTOR_CART_ITEM = '.cart_item'
    SELECTOR_REMOVE = ".cart_button >> text='Remove'"

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/cart.html'

    def expect_items_in_cart(self):
        self.assert_element_is_visible(self.SELECTOR_CART_ITEM)

    def remove_items_from_cart(self):
        self.wait_for_selector_and_click(self.SELECTOR_REMOVE)

    def expect_empty_cart(self):
        self.assert_element_not_exist(self.SELECTOR_CART_ITEM)
