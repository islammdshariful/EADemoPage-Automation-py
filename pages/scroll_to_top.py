from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import *


class ScrollToTop:
    widget = '//*[@id="post-271396"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Scroll to Top'
    doc_link = '//*[@id="post-271396"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA SCROLL TO TOP"

    scroll_to_top_btn = (By.XPATH, f'/html/body/div[5]/span')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(scroll_to_top)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)

            element = self.browser.find_element(*self.scroll_to_top_btn)
            self.browser.execute_script("arguments[0].click();", element)
            if self.browser.find_element(By.XPATH, self.widget).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to("Scroll to top not working.")