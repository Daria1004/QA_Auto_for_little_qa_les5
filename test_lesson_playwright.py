from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_add_items_and_checkout(browser_tab):
    page = browser_tab
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.login('standard_user', 'secret_sauce')
    login_page.expect_login_success()

    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form("John", "Doe", '123321')


def test_add_all_items(browser_tab):
    page = browser_tab
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login('standard_user', 'secret_sauce')
    login_page.expect_login_success()

    inventory_page.add_items_to_cart()


def test_add_items_and_remove(browser_tab):
    page = browser_tab
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login('standard_user', 'secret_sauce')
    login_page.expect_login_success()

    inventory_page.remove_item_on_products_page()


def test_check_items_in_cart(browser_tab):
    page = browser_tab
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.login('standard_user', 'secret_sauce')
    login_page.expect_login_success()

    inventory_page.add_first_item_to_cart()
    cart_page.expect_items_in_cart()


def test_clear_cart(browser_tab):
    page = browser_tab
    login_page = LoginPage(page)

    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.login('standard_user', 'secret_sauce')
    login_page.expect_login_success()

    inventory_page.add_first_item_to_cart()
    cart_page.remove_items_from_cart()
    cart_page.expect_empty_cart()


def test_incorrect_password(browser_tab):
    page = browser_tab
    login_page = LoginPage(page)

    login_page.login('standard_user', 'incorrect_password')
    login_page.expect_login_failed()
