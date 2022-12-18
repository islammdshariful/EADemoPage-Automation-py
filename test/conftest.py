import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='module')
def init_driver():
    options = Options()
    # # opts.add_experimental_option("detach", True)
    # options.add_experimental_option('debuggerAddress', 'localhost:9250')
    browser = webdriver.Chrome(chrome_options=options)
    browser.maximize_window()
    browser.implicitly_wait(10)

    yield browser

    browser.quit()
