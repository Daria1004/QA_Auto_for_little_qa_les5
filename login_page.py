from pages.base_page import BasePage


class LoginPage(BasePage): # наследуется от BasePage и расширяет тем самым методы BasePage
    def __init__(self, page):
        super().__init__(page) # гарантирует, что иницивлизация, выполненная BasePage, также применяется к каждому экземпляру LoginPage. Обеспечивает доступ к атрибуту self.page
        self._endpoint = ''

    USERNAME_SELECTOR = '#user-name'
    PASSWORD_SELECTOR = '#password'
    LOGIN_BUTTON_SELECTOR = '#login-button'

    def login(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_fill(self.USERNAME_SELECTOR, username)
        self.wait_for_selector_and_fill(self.PASSWORD_SELECTOR, password)
        self.wait_for_selector_and_click(self.LOGIN_BUTTON_SELECTOR)

    def expect_login_success(self):
        self.assert_text_present_on_page('Products')

    def expect_login_failed(self):
        self.assert_text_present_on_page('Epic sadface: Username and password do not match any user in this service')
