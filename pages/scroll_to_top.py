from selenium.webdriver import Keys

from utils.config import *


class ScrollToTop(Helper):
    widget = '//*[@id="post-271396"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Scroll to Top'
    doc_link = '//*[@id="post-271396"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA SCROLL TO TOP"

    scroll_to_top_btn = (By.XPATH, f"//span[@class='eael-ext-scroll-to-top-button']")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.scroll_to_top)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(1)

                element = self.browser.find_element(*self.scroll_to_top_btn)
                self.browser.execute_script("arguments[0].click();", element)
                self.check_visibility(self.widget, "Scroll to top not working.")