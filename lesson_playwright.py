from playwright.sync_api import sync_playwright
import time

# создаём экземпляр Playwright и запускаем его
playwright = sync_playwright().start()

#  далее, используя объект Playwright, можно запустить браузер и работать с ним
browser = playwright.chromium.launch(headless=False, slow_mo=500)
page = browser.new_page()
page.goto('https://www.saucedemo.com/')
page.wait_for_load_state('load')
page.wait_for_selector('#user-name')
page.type(selector='[id="user-name"]', text='standard_user', delay=100)
page.fill(selector='#password', value='secret_sauce')
page.click(selector='.submit-button')    # [class = 'submit-button']
page.wait_for_url('https://www.saucedemo.com/inventory.html', timeout=10000)
page.wait_for_selector(".btn.btn_primary.btn_small.btn_inventory")
page.is_enabled(".inventory_item .pricebar:has-text('Add to cart')")
page.is_visible(".inventory_item .pricebar:has-text('Add to cart')")


page.click(".inventory_item >> text='Add to cart'")
page.click(".inventory_item .pricebar:has-text('Add to cart')")

page.click('[data-test="shopping-cart-link"]')
page.click('[id="checkout"]')
page.type(selector='#first-name', text='first-name', delay=100)
page.type(selector='#last-name', text='last-name', delay=100)
page.type(selector='input[name="postalCode"]', text='123321', delay=100)

time.sleep(5)
# После выполлнения необходимых действий, следует явно закрыть браузер
browser.close()

# И остановить Playwright, чтоб освободить ресурсы
playwright.stop()
