from pages.base_page import BasePage
from playwright.sync_api import expect


class InventoryPage(BasePage):
    SELECTOR_ADD_TO_CART = ".inventory_item >> text='Add to cart'"
    SELECTOR_SHOPPING_CART_LINK = '[data-test="shopping-cart-link"]'
    SELECTOR_REMOVE = ".inventory_item >> text='Remove'"

    SELECTOR_BACKPACK = "#add-to-cart-sauce-labs-backpack"
    SELECTOR_BIKE_LIGHT = "#add-to-cart-sauce-labs-bike-light"
    SELECTOR_BOLT_T_SHIRTS = "#add-to-cart-sauce-labs-bolt-t-shirt"
    SELECTOR_FLEECE_JACKET = "#add-to-cart-sauce-labs-fleece-jacket"
    SELECTOR_ONESIE = "#add-to-cart-sauce-labs-onesie"
    SELECTOR_T_SHIRT_RED = '#add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)'
    SELECTOR_CART_BADGE = f"{SELECTOR_SHOPPING_CART_LINK} .shopping_cart_badge"


    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/inventory.html'

    def add_first_item_to_cart(self):
        self.wait_for_selector_and_click(self.SELECTOR_ADD_TO_CART)
        self.assert_element_is_visible(self.SELECTOR_SHOPPING_CART_LINK)
        self.wait_for_selector_and_click(self.SELECTOR_SHOPPING_CART_LINK)

    def add_items_to_cart(self):
        self.wait_for_selector_and_click(self.SELECTOR_BACKPACK)
        self.wait_for_selector_and_click(self.SELECTOR_BIKE_LIGHT)
        self.wait_for_selector_and_click(self.SELECTOR_BOLT_T_SHIRTS)
        self.wait_for_selector_and_click(self.SELECTOR_FLEECE_JACKET)
        self.wait_for_selector_and_click(self.SELECTOR_ONESIE)
        self.wait_for_selector_and_click(self.SELECTOR_T_SHIRT_RED)
        self.assert_element_is_visible(self.SELECTOR_SHOPPING_CART_LINK)
        self.assert_text_in_element(self.SELECTOR_CART_BADGE, "6")

    def remove_item_on_products_page(self):
        self.wait_for_selector_and_click(self.SELECTOR_ADD_TO_CART)
        self.assert_text_in_element(self.SELECTOR_CART_BADGE, '1')
        self.wait_for_selector_and_click(self.SELECTOR_REMOVE)
        self.assert_element_text_empty(self.SELECTOR_SHOPPING_CART_LINK)
