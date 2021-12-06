import os
import sys
import json
import pytest
from selenium import webdriver
# from src.testproject.sdk.drivers import webdriver
from selenium.webdriver.chrome.options import Options

# This will run before all test case
@pytest.fixture
def browser():
    opts = Options()
    # opts.add_experimental_option("detach", True)
    opts.add_experimental_option('debuggerAddress', 'localhost:9250')
    b = webdriver.Chrome(str(os.getenv('chromedriver')), chrome_options=opts)
    # b = webdriver.Chrome(chrome_options=opts)
    b.maximize_window()
    b.implicitly_wait('10')

    yield b

    # b.quit()
