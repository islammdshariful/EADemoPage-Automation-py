from selenium.webdriver import Keys

from utils.config import *


class ContentProtection(Helper):
    widget = '//*[@id="post-255091"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Content Protection'
    doc_link = '//*[@id="post-255091"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA CONTENT PROTECTION"

    input = (By.XPATH, f'//*[@id="post-255091"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div'
                       f'/div/div/div/div/div/div/div[2]/form/input[1]')
    submit_btn = f'//*[@id="post-255091"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                            f'/div/div/div/div/div/div/div/div[2]/form/input[3]'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.content_protection)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 947)")
                time.sleep(1)
                self.browser.find_element(*self.input).send_keys("HOLIDAY")
                self.check_visibility(self.submit_btn, "Submit button is not visible.")
