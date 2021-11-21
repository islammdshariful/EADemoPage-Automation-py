import os
import sys
import json
import pytest
from selenium import webdriver
# from src.testproject.sdk.drivers import webdriver
from selenium.webdriver.chrome.options import Options

# To open a file
@pytest.fixture
def config(scope='session'):
    with open(str(sys.path[1]) + '/utils/config.json') as config_file:
        config = json.load(config_file)

    assert isinstance(config['implicitly_wait'], int)

    return config


# This will run before all test case
@pytest.fixture
def browser(config):
    opts = Options()
    # opts.add_experimental_option("detach", True)
    opts.add_experimental_option('debuggerAddress', 'localhost:9250')
    b = webdriver.Chrome(str(os.getenv('chromedriver')), chrome_options=opts)
    # b = webdriver.Chrome(chrome_options=opts)
    b.maximize_window()

    b.implicitly_wait(config['implicitly_wait'])

    yield b

    # b.quit()
