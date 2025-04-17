import playwright
import pytest
import os
import shutil
from pages.login_page import LoginPage


@pytest.fixture(scope='session', autouse=True)
def clean_reports():
    reports_dir = 'reports'
    if os.path.exists(reports_dir):
        shutil.rmtree(reports_dir)
    os.makedirs(reports_dir)


@pytest.fixture()
def login_page(page):
    return LoginPage(page)

