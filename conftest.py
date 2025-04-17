import playwright
import pytest
import os
import shutil


@pytest.fixture(scope='session', autouse=True)
def clean_reports():
    reports_dir = 'reports'
    if os.path.exists(reports_dir):
        shutil.rmtree(reports_dir)
    os.makedirs(reports_dir)
