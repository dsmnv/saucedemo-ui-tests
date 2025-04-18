import allure
import pytest
import os
import shutil
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture(scope='session', autouse=True)
def clean_reports():
    reports_dir = 'reports'
    if os.path.exists(reports_dir):
        shutil.rmtree(reports_dir)
    os.makedirs(reports_dir)


@pytest.fixture()
def login_page(page):
    return LoginPage(page)


@pytest.fixture()
def inventory_page(page):
    return InventoryPage(page)


@pytest.fixture()
def login_as_standard_user(page, login_page):
    page.goto('/')
    login_page.login('standard_user', 'secret_sauce')


@pytest.fixture()
def add_product_to_cart(page, inventory_page, login_as_standard_user):
    inventory_page.add_to_cart_buttons.nth(0).click()



