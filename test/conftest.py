import platform
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pathlib import Path
from selenium.webdriver.chrome.service import Service as ChromeService

"""Driver initialization method"""

# @pytest.fixture(params=["chrome"], scope='module')
# def init_driver(request):
#     if request.param.__eq__("chrome"):
#         browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     elif request.param.__eq__("firefox"):
#         browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     else:
#         print("Please pass a correct browser name")
#         raise Exception("Driver is no found")
#
#     browser.maximize_window()
#     browser.implicitly_wait('10')
#
#     yield browser
#
#     browser.quit()


"""For development"""


@pytest.fixture(scope='module')
def init_driver():
    options = Options()
    # # opts.add_experimental_option("detach", True)
    options.add_experimental_option('debuggerAddress', 'localhost:9250')

    if platform.system().__eq__("Windows"):
        # For Windows
        path = str(Path(__file__).parent.parent) + "/venv/Lib/site-packages/seleniumbase/drivers/chromedriver.exe"
    else:
        # For Mac
        path = str(
            Path(__file__).parent.parent) + "/venv/lib/python3.10/site-packages/seleniumbase/drivers/chromedriver"

    browser = webdriver.Chrome(executable_path=path, chrome_options=options)
    browser.maximize_window()
    browser.implicitly_wait('10')

    yield browser

    # browser.quit()
