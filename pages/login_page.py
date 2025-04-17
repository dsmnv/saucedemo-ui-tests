from playwright.sync_api import Page, Locator


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input: Locator = page.locator('#user-name')
        self.password_input: Locator = page.locator('#password')
        self.login_button: Locator = page.locator('#login-button')
        self.error_message: Locator = page.locator('[data-test="error"]')

    def open(self):
        self.page.goto('/')

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_error_visible(self):
        assert self.error_message.is_visible(), 'ошибка не появилась'

    def assert_error_message_text(self, expected):
        actual = self.error_message.inner_text()
        assert actual == expected, f'Ожидаем: {expected}, получаем: {actual}'

