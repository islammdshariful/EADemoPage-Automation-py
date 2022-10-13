from utils.config import *


class Countdown(BasePage, Helper):
    widget = '//*[@id="post-23"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Countdown'
    doc_link = '//*[@id="post-23"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "COUNTDOWN"
    days = (By.XPATH, f'//*[@id="eael-countdown-56d8c80a"]/li[1]/div/span[1]')
    days_text = (By.XPATH, f'//*[@id="eael-countdown-56d8c80a"]/li[1]/div/span[2]')
    days_text_text = "DAYS"
    hours = (By.XPATH, f'//*[@id="eael-countdown-56d8c80a"]/li[2]/div/span[1]')
    hours_text = (By.XPATH, f'//*[@id="eael-countdown-56d8c80a"]/li[2]/div/span[2]')
    hours_text_text = "HOURS"
    minutes = (By.XPATH, f'//*[@id="eael-countdown-56d8c80a"]/li[3]/div/span[1]')
    minutes_text = (By.XPATH, f'//*[@id="eael-countdown-56d8c80a"]/li[3]/div/span[2]')
    minutes_text_text = "MINUTES"
    seconds = (By.XPATH, f'//*[@id="eael-countdown-56d8c80a"]/li[4]/div/span[1]')
    seconds_text = (By.XPATH, f'//*[@id="eael-countdown-56d8c80a"]/li[4]/div/span[2]')
    seconds_text_text = "SECONDS"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.countdown)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1037)

                self.check_text_matches_with(self.days_text, self.days_text_text)
                self.check_text_matches_with(self.hours_text, self.hours_text_text)
                self.check_text_matches_with(self.minutes_text, self.minutes_text_text)
                self.check_text_matches_with(self.seconds_text, self.seconds_text_text)

                self.is_visible(self.days, "Days not visible.")
                self.is_visible(self.hours, "Hours not visible.")
                self.is_visible(self.minutes, "Minutes not visible.")
                self.is_visible(self.seconds, "Seconds not visible.")

                sec = self.get_element_text(self.seconds)
                time.sleep(1.5)
                sec_1 = self.get_element_text(self.seconds)
                if sec.__eq__(sec_1):
                    assert_that("Countdown working").is_equal_to("Countdown not working")



