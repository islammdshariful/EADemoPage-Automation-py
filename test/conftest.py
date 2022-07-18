import os
import sys
import json
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path


# This will run before all test case
@pytest.fixture(scope='module')
def browser():
    opts = Options()
    opts.add_experimental_option("detach", True)
    # opts.add_experimental_option('debuggerAddress', 'localhost:9250')
    # For Windows
    # path = str(Path(__file__).parent.parent) + "\\venv\\Lib\\site-packages\\seleniumbase\\drivers\\chromedriver.exe"
    # For Mac
    path = str(Path(__file__).parent.parent) + "/venv/lib/python3.10/site-packages/seleniumbase/drivers/chromedriver"
    b = webdriver.Chrome(executable_path=path, chrome_options=opts)
    b.maximize_window()
    b.implicitly_wait('10')

    yield b

    # b.quit()
