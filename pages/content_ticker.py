from selenium.webdriver import Keys

from utils.config import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContentTicker(Helper):
    widget = '//*[@id="post-2323"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Content Ticker'
    doc_link = '//*[@id="post-2323"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "CONTENT TICKER"

    label = (By.XPATH, f'//*[@id="eael-ticker-wrap-5107a1de"]/div[1]/span')
    label_text = "Trending Today"
    content_1 = f'//*[@id="eael-ticker-wrap-5107a1de"]/div[2]/div[1]/div/div[4]/div/a'
    content_1_text = "How to Include Elementor Template using a Shortcode"
    content_2 = f'//*[@id="eael-ticker-wrap-5107a1de"]/div[2]/div[1]/div/div[3]/div/a'
    content_2_text = "How to Include Elementor Template"
    prev_btn = (By.XPATH, f'//*[@id="eael-ticker-wrap-5107a1de"]/div[2]/div[2]/div[2]/i')
    next_btn = (By.XPATH, f'//*[@id="eael-ticker-wrap-5107a1de"]/div[2]/div[2]/div[1]/i')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.content_ticker)

    def testcase(self):
        # with soft_assertions():
        self.check_widget_name(self.widget, self.widget_name)
        if self.check_doc:
            self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
            self.check_documents(self.doc_link, self.doc_name)
        else:
            self.browser.execute_script("window.scrollTo(0, 982)")
            time.sleep(1)

            assert_that(self.browser.find_element(*self.label).text).is_equal_to(self.label_text)
            if self.browser.find_element(By.XPATH, self.content_1).is_displayed():
                WebDriverWait(self.browser, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.content_1), self.content_1_text))

                assert_that(self.browser.find_element(By.XPATH, self.content_1).text).is_equal_to(self.content_1_text)
                self.browser.find_element(*self.next_btn).click()

                WebDriverWait(self.browser, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.content_2), self.content_2_text))

                assert_that(self.browser.find_element(By.XPATH, self.content_2).text).is_equal_to(self.content_2_text)
                self.browser.find_element(*self.prev_btn).click()

                WebDriverWait(self.browser, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.content_1), self.content_1_text))

                assert_that(self.browser.find_element(By.XPATH, self.content_1).text).is_equal_to(self.content_1_text)
            else:

                WebDriverWait(self.browser, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.content_2), self.content_2_text))

                assert_that(self.browser.find_element(By.XPATH, self.content_2).text).is_equal_to(self.content_2_text)
                self.browser.find_element(*self.next_btn).click()

                WebDriverWait(self.browser, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.content_1), self.content_1_text))

                assert_that(self.browser.find_element(By.XPATH, self.content_1).text).is_equal_to(self.content_1_text)
                self.browser.find_element(*self.prev_btn).click()

                WebDriverWait(self.browser, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.content_2), self.content_2_text))

                assert_that(self.browser.find_element(By.XPATH, self.content_2).text).is_equal_to(self.content_2_text)
