from selenium.webdriver import ActionChains

from utils.config import *


class ContentProtection:
    widget = '//*[@id="post-255091"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Content Protection'
    doc_link = '//*[@id="post-255091"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA CONTENT PROTECTION"

    input = (By.XPATH, f'//*[@id="post-255091"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div'
                       f'/div/div/div/div/div/div/div[2]/form/input[1]')
    submit_btn = (By.XPATH, f'//*[@id="post-255091"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div'
                            f'/div/div/div/div/div/div/div/div[2]/form/input[3]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(content_protection)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 947)")
            self.browser.find_element(*self.input).send_keys("HOLIDAY")
            if self.browser.find_element(*self.submit_btn).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to(0)
