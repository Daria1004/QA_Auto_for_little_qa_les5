from playwright.sync_api import expect


class BasePage:
    __BASE_URL = 'https://www.saucedemo.com'    # приватный атрибут, хранящий базовый урл сайта, с которым мы работаем
                                                # 1й принцип ООП - инкапсуляция
    def __init__(self, page):
        self.page = page
        self._endpoint = ''    # защищённый атрибут, представляющий конкретный эндпоинт на нашей странице
                               # предназначен для внутреннего использования классом и его наследниками

    def _get_full_url(self):    # защищённый метод для получения полного урл
        return f'{self.__BASE_URL}/{self._endpoint}'

    def navigate_to(self):    # для навигации к нашей странице
        full_url = self._get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(full_url)

    def wait_for_selector_and_click(self, selector): # метод для взаимодействия с элементами
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def wait_for_selector_and_fill(self, selector, value): # метод для взаимодействия с элементами
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)

    def wait_for_selector_and_type(self, selector, value, delay): # метод для взаимодействия с элементами
        self.page.wait_for_selector(selector)
        self.page.type(selector, value, delay=delay)

    def assert_element_is_visible(self, selector): # проверки состояния элементов и их содержимого
        expect(self.page.locator(selector)).to_be_visible()

    def assert_text_present_on_page(self, text):
        expect(self.page.locator("body")).to_contain_text(text)

    def assert_text_in_element(self, selector, text):
        expect(self.page.locator(selector)).to_have_text(text)

    def assert_input_value(self, selector, expected_value):
        expect(self.page.locator(selector)).to_have_value(expected_value)
