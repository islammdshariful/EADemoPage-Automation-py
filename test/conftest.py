import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session', autouse=True)
def init_driver():
    options = Options()
    # uncomment this ↓ if you want to run the test in chrome port 9250
    # options.add_experimental_option('debuggerAddress', 'localhost:9250')
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(10)
    close_all_notice(browser)

    yield browser

    browser.quit()


def close_all_notice(browser):
    browser.get('https://essential-addons.com/elementor/demos/')
    close_crips(browser)
    close_nx_bar(browser)


def close_crips(browser):
    close_button = browser.find_elements('xpath', "//span[@data-id='new_messages']/span[1]/span[1]/span")
    if len(close_button) > 0:
        ele = browser.find_element('xpath', "//span[@data-id='new_messages']/span[1]/span[1]/span")
        browser.execute_script("arguments[0].click();", ele)


def close_nx_bar(browser):
    close_button = browser.find_elements('xpath', "//div[@class='nx-bar-inner']/div[2]")
    if len(close_button) > 0:
        ele = browser.find_element('xpath', "//div[@class='nx-bar-inner']/div[2]")
        browser.execute_script("arguments[0].click();", ele)

