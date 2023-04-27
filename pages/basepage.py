import time

from assertpy import assert_that
from selenium.common import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.cursor = ActionChains(self.browser)

    def close_nx_popup(self):
        close_button = self.browser.find_elements('xpath', "//div[@class='notificationx-inner']//div[3]")
        if len(close_button) > 0:
            ele = self.browser.find_element('xpath', "//div[@class='notificationx-inner']//div[3]")
            self.browser.execute_script("arguments[0].click();", ele)
        time.sleep(1)

    def go_to(self, url):
        self.browser.get(url)

    def get_element(self, by_locator):
        try:
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
            return element
        except TimeoutException:
            try:
                element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(by_locator))
                return element
            except TimeoutException:
                print("Loading took too much time!")

    def does_element_has_text(self, by_locator, text):
        try:
            WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element(by_locator, text))
        except TimeoutException:
            assert_that(self.get_element_text(by_locator)).is_equal_to(text)

    def do_click(self, by_locator, click_after_wait=None):
        try:
            try:
                WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(by_locator))
            except TimeoutException:
                self.get_element(by_locator).click()
            self.get_element(by_locator).click()
        except ElementClickInterceptedException:
            self.close_nx_popup()
            self.cursor.move_to_element(self.get_element(by_locator)).click().perform()

        if click_after_wait is not None:
            time.sleep(1)

    def do_clear_field(self, by_locator):
        self.get_element(by_locator).clear()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        return self.get_element(by_locator).text

    def check_text_matches_with(self, by_locator, text):
        assert_that(self.get_element_text(by_locator)).is_equal_to(text)

    def check_element_present(self, by_locator):
        return bool(self.get_element(by_locator))

    def run_script(self, script, args):
        self.browser.execute_script(script, self.get_element(args))

    def set_screen_size(self, width, height):
        self.browser.set_window_size(width, height)
        time.sleep(1)

    def set_screen_full_size(self):
        self.browser.maximize_window()
        time.sleep(1)

    def is_visible(self, by_locator, error_message):
        if not WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed():
            assert_that(1).is_equal_to(error_message)

    def is_displaying(self, *by_locator):
        try:
            return self.browser.find_element(*by_locator).is_displayed()
        except NoSuchElementException:
            time.sleep(2)
            return self.browser.find_element(*by_locator).is_displayed()

    def get_page_title(self, title):
        WebDriverWait(self.browser, 10).until(EC.title_is(title))
        return self.browser.title

    def move_cursor_to(self, by_locator):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        self.cursor.move_to_element(self.get_element(by_locator)).perform()
        time.sleep(1)

    def move_cursor_and_click(self, by_locator):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(by_locator))
        self.cursor.move_to_element(self.get_element(by_locator)).click().perform()
        time.sleep(1)

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

    def scroll_to(self, y):
        self.browser.execute_script("window.scrollTo(0, " + str(y) + ")")
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
