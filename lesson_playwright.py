from playwright.sync_api import sync_playwright
import time

from cart_page import CartPage
from checkout_page import CheckoutPage
from inventory_page import InventoryPage
from login_page import LoginPage
from conftest import browser

# # создаём экземпляр Playwright и запускаем его
# playwright = sync_playwright().start()
#
# #  далее, используя объект Playwright, можно запустить браузер и работать с ним
# browser = playwright.chromium.launch(headless=False, slow_mo=500)
# page = browser.new_page()
# page.goto('https://www.saucedemo.com/')
# page.wait_for_load_state('load')
# page.wait_for_selector('#user-name')
# page.type(selector='#user-name', text='standard_user')
# page.fill(selector='#password', value='secret_sauce')
# page.click(selector='#login-button')
# page.wait_for_url('https://www.saucedemo.com/inventory.html')
# page.wait_for_selector(".btn.btn_primary.btn_small.btn_inventory")
# page.is_enabled(".inventory_item .pricebar:has-text('Add to cart')")
# page.is_visible(".inventory_item .pricebar:has-text('Add to cart')")
#
#
# page.click(".inventory_item >> text='Add to cart'")    #- один из
# page.click(".inventory_item .pricebar:has-text('Add to cart')")
#
# page.click('[data-test="shopping-cart-link"]')
# page.click('[id="checkout"]')
# page.type(selector='#first-name', text='first-name', delay=100)
# page.type(selector='#last-name', text='last-name', delay=100)
# page.type(selector='input[name="postalCode"]', text='123321', delay=100)
#
# time.sleep(5)
# # После выполлнения необходимых действий, следует явно закрыть браузер
# browser.close()
#
# # И остановить Playwright, чтоб освободить ресурсы
# playwright.stop()


def test_add_items_and_checkout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.login('standard_user', 'secret_sauce')
    login_page.expect_login_success()

    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form("John", "Doe", '123321')

def test_add_all_items(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login('standard_user', 'secret_sauce')
    login_page.expect_login_success()

    inventory_page.add_items_to_cart()

def test_add_items_and_remove(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login('standard_user', 'secret_sauce')
    login_page.expect_login_success()

    inventory_page.remove_item_on_products_page()


def test_check_items_in_cart(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.login('standard_user', 'secret_sauce')
    login_page.expect_login_success()

    inventory_page.add_first_item_to_cart()
    cart_page.expect_items_in_cart()


def test_clear_cart(browser):
    page = browser.new_page()
    login_page = LoginPage(page)

    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.login('standard_user', 'secret_sauce')
    login_page.expect_login_success()

    inventory_page.add_first_item_to_cart()
    cart_page.remove_items_from_cart()
    cart_page.expect_empty_cart()


def test_incorrect_password(browser):
    page = browser.new_page()
    login_page = LoginPage(page)

    login_page.login('standard_user', 'incorrect_password')
    login_page.expect_login_failed()
