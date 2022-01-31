from selenium.webdriver import ActionChains

from utils.config import *


class Countdown(Helper):
    widget = '//*[@id="post-23"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Countdown'
    doc_link = '//*[@id="post-23"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "COUNTDOWN"
    days = f'//*[@id="eael-countdown-56d8c80a"]/li[1]/div/span[1]'
    days_text = (By.XPATH, f'//*[@id="eael-countdown-56d8c80a"]/li[1]/div/span[2]')
    days_text_text = "DAYS"
    hours = f'//*[@id="eael-countdown-56d8c80a"]/li[2]/div/span[1]'
    hours_text = (By.XPATH, f'//*[@id="eael-countdown-56d8c80a"]/li[2]/div/span[2]')
    hours_text_text = "HOURS"
    minutes = f'//*[@id="eael-countdown-56d8c80a"]/li[3]/div/span[1]'
    minutes_text = (By.XPATH, f'//*[@id="eael-countdown-56d8c80a"]/li[3]/div/span[2]')
    minutes_text_text = "MINUTES"
    seconds = f'//*[@id="eael-countdown-56d8c80a"]/li[4]/div/span[1]'
    seconds_text = (By.XPATH, f'//*[@id="eael-countdown-56d8c80a"]/li[4]/div/span[2]')
    seconds_text_text = "SECONDS"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.countdown)

    def testcase(self):
        c = Helper(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                c.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 914)")
            assert_that(self.browser.find_element(*self.days_text).text).is_equal_to(self.days_text_text)
            assert_that(self.browser.find_element(*self.hours_text).text).is_equal_to(self.hours_text_text)
            assert_that(self.browser.find_element(*self.minutes_text).text).is_equal_to(self.minutes_text_text)
            assert_that(self.browser.find_element(*self.seconds_text).text).is_equal_to(self.seconds_text_text)

            self.check_visibility(self.days, "Days not visible.")
            self.check_visibility(self.hours, "Hours not visible.")
            self.check_visibility(self.minutes, "Minutes not visible.")
            self.check_visibility(self.seconds, "Seconds not visible.")

            sec = self.browser.find_element(By.XPATH, self.seconds).text
            time.sleep(1.5)
            sec_1 = self.browser.find_element(By.XPATH, self.seconds).text
            if sec == sec_1:
                assert_that("").is_equal_to("Countdown not working")



