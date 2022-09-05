import time

from assertpy import assert_that
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.cursor = ActionChains(self.browser)

    def go_to(self, url):
        self.browser.get(url)

    def do_click(self, by_locator):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def clear_field(self, by_locator):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

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

    def is_displaying(self, *by_locator):
        return self.browser.find_element(*by_locator).is_displayed()

    def get_title(self, title):
        WebDriverWait(self.browser, 10).until(EC.title_is(title))
        return self.browser.title

    def move_cursor_to(self, by_locator):
        self.cursor.move_to_element(self.get_element(by_locator)).perform()
        time.sleep(1)

    def move_cursor_to_and_click(self, by_locator):
        self.cursor.move_to_element(self.get_element(by_locator)).click().perform()
        time.sleep(.5)

    def go_back(self):
        self.browser.back()
        time.sleep(1)

    def reload_page(self):
        self.browser.refresh()

    def switch_to_frame(self, by_locator):
        self.browser.switch_to.frame(self.get_element(by_locator))
        time.sleep(1)

    def switch_frame_to_default(self):
        self.browser.switch_to.default_content()
        time.sleep(1)

    def scroll_to(self, Y):
        self.browser.execute_script("window.scrollTo(0, " + str(Y) + ")")
        time.sleep(1)

    def scroll_to_top(self):
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)

    def scroll_to_bottom(self):
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(1)

    def scroll_to_element(self, by_locator):
        self.browser.execute_script("arguments[0].scrollIntoView();", self.get_element(by_locator))
        time.sleep(1)
