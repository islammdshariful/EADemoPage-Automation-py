import time

from assertpy import assert_that
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def do_click(self, by_locator):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).send_keys()

    def get_element(self, by_locator):
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    def check_element_text(self, by_locator):
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def check_text_matches_with(self, by_locator, text):
        assert_that(self.check_element_text(by_locator)).is_equal_to(text)

    def check_existence(self, by_locator):
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_visible(self, by_locator, error_message):
        if WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed():
            assert_that(1).is_equal_to(1)
        else:
            assert_that(1).is_equal_to(error_message)

    def get_title(self, title):
        WebDriverWait(self.browser, 10).until(EC.title_is(title))
        return self.browser.title

    def move_to(self, by_locator):
        cursor = ActionChains(self.browser)
        element = self.get_element(by_locator)
        cursor.move_to_element(element).perform()
        time.sleep(1)

    def go_back(self):
        self.browser.back()
        time.sleep(1)


