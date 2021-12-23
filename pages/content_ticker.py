from selenium.webdriver import ActionChains

from utils.config import *


class ContentTicker:
    widget = '//*[@id="post-2323"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Content Ticker'
    doc_link = '//*[@id="post-2323"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "CONTENT TICKER"

    label = (By.XPATH, f'//*[@id="eael-ticker-wrap-5107a1de"]/div[1]/span')
    label_text = "Trending Today"
    content_1 = (By.XPATH, f'//*[@id="eael-ticker-wrap-5107a1de"]/div[2]/div[1]/div/div[2]/div/a')
    content_1_text = "How to Include Elementor Template using a Shortcode"
    content_2 = (By.XPATH, f'//*[@id="eael-ticker-wrap-5107a1de"]/div[2]/div[1]/div/div[3]/div/a')
    content_2_text = "How to Include Elementor Template"
    prev_btn = (By.XPATH, f'//*[@id="eael-ticker-wrap-5107a1de"]/div[2]/div[2]/div[2]/i')
    next_btn = (By.XPATH, f'//*[@id="eael-ticker-wrap-5107a1de"]/div[2]/div[2]/div[1]/i')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(content_ticker)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 982)")

            assert_that(self.browser.find_element(*self.label).text).is_equal_to(self.label_text)
            if self.browser.find_element(*self.content_1).is_displayed():
                assert_that(self.browser.find_element(*self.content_1).text).is_equal_to(self.content_1_text)
                self.browser.find_element(*self.next_btn).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.content_2).text).is_equal_to(self.content_2_text)
                self.browser.find_element(*self.prev_btn).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.content_1).text).is_equal_to(self.content_1_text)
            else:
                assert_that(self.browser.find_element(*self.content_2).text).is_equal_to(self.content_2_text)
                self.browser.find_element(*self.next_btn).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.content_1).text).is_equal_to(self.content_1_text)
                self.browser.find_element(*self.prev_btn).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.content_2).text).is_equal_to(self.content_2_text)