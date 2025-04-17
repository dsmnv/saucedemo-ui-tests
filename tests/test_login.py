import allure
import pytest
import time


username = 'standard_user'
password = 'secret_sauce'


def test_login_with_valid_credentials(page):
    page.goto('/')
    with allure.step('Открыта главная страница'):
        assert page.title() == 'Swag Labs'

    with allure.step('Ввод логина и пароля'):
        page.fill('#user-name', username)
        page.fill('#password', password)

    with allure.step('Нажатие на кнопку логина'):
        page.click('#login-button')

    with allure.step('Проверка редиректа в катало'):
        assert page.url == 'https://www.saucedemo.com/inventory.html'
        allure.attach(page.screenshot(), name='Catalog page', attachment_type=allure.attachment_type.PNG)


def test_login_with_invalid_password(page):
    page.goto('/')
    with allure.step('Открыта главная страница'):
        assert page.title() == 'Swag Labs'

    with allure.step('Ввод логина'):
        page.fill('#user-name', username)

    with allure.step('Ввод неверного пароля'):
        page.fill('#password', '123456')

    with allure.step('Нажатие на кнопку логина'):
        page.click('#login-button')

    with allure.step('Появилось сообщение об ошибке'):
        error = page.locator('[data-test="error"]')
        assert error.is_visible()
        assert error.inner_text() == 'Epic sadface: Username and password do not match any user in this service'
        allure.attach(page.screenshot(), name='Error message', attachment_type=allure.attachment_type.PNG)




