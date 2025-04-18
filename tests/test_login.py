import allure
import pytest
import time


username = 'standard_user'
password = 'secret_sauce'


def test_login_with_valid_credentials(login_page, page):
    with allure.step('Открыта главная страница'):
        login_page.open()
        assert page.title() == 'Swag Labs'

    with allure.step('Ввод логина и пароля'):
        login_page.login(username, password)

    with allure.step('Открыта страница каталога'):
        assert page.url == 'https://www.saucedemo.com/inventory.html'
        allure.attach(page.screenshot(), name='Catalog page', attachment_type=allure.attachment_type.JPG)


def test_login_with_invalid_password(login_page, page):
    with allure.step('Открыта главная страница'):
        login_page.open()
        assert page.title() == 'Swag Labs'

    with allure.step('Ввод логина и неверного пароля'):
        login_page.login(username, '123456')

    with allure.step('Появилось сообщение об ошибке'):
        login_page.assert_error_visible()
        login_page.assert_error_message_text('Epic sadface: Username and password do not match any user in this service')
        allure.attach(page.screenshot(), name='Error message', attachment_type=allure.attachment_type.JPG)


def test_login_without_data(login_page, page):
    login_page.open()

    with allure.step('Нажатие на кнопку логина'):
        login_page.login_button.click()

    with allure.step('Появилось сообщение об ошибке'):
        login_page.assert_error_visible()
        login_page.assert_error_message_text('Epic sadface: Username is required')
        allure.attach(page.screenshot(), name='Error message', attachment_type=allure.attachment_type.JPG)



