from selenium.webdriver import ActionChains

from utils.config import *


class EventCalendar:
    PAGE_TITLE_TEXT = "Event Calendar | Essential Addons for Elementor"
    DOC_LINK = '//*[@id="post-257828"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/' \
               'section/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA EVENT CALENDAR"
    prev_button = (By.XPATH, f'//*[@id="eael-event-calendar-22bed70e"]/div[1]/div[1]/div/button[1]')
    next_button = (By.XPATH, f'//*[@id="eael-event-calendar-22bed70e"]/div[1]/div[1]/div/button[2]')
    month = (By.XPATH, f'//*[@id="eael-event-calendar-22bed70e"]/div[1]/div[2]/h2')
    month_text = "November 2021"

    event_info = (By.XPATH, f'//*[@id="eael-event-calendar-22bed70e"]/div[2]/div/table/'
                            f'tbody/tr/td/div/div/div[1]/div[2]/table/tbody/tr/td[4]/a')
    event_info_text = "07:00 AM Event Title Nov"

    event_title = (By.XPATH, f'//*[@id="eaelecModal"]/div[2]/div[1]/h2')
    event_title_text = "Event Title Nov"
    calendar_icon = (By.XPATH, f'//*[@id="eaelecModal"]/div[2]/div[1]/span[1]/i')
    event_start = (By.XPATH, f'//*[@id="eaelecModal"]/div[2]/div[1]/span[1]')
    event_start_text = "Nov 4th 7:00 AM"
    event_end = (By.XPATH, f'//*[@id="eaelecModal"]/div[2]/div[1]/span[2]')
    event_end_text = "- 7:00 AM"

    event_des = (By.XPATH, f'//*[@id="eaelecModal"]/div[2]/div[2]/p')
    event_des_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod " \
                     "tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse " \
                     "ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. " \
                     "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor " \
                     "incididunt ut labore et dolore magna aliqua."
    modal_close = (By.XPATH, f'//*[@id="eaelecModal"]/div[2]/div[1]/div/span/i')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(event_calendar)

    def testcase(self):

        with soft_assertions():
            assert_that(self.browser.title).is_equal_to(self.PAGE_TITLE_TEXT)

            doc = Documentation(self.browser)
            if check_doc:
                doc.check_doc(self.DOC_LINK, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1628)")
            # while assert_that(self.browser.find_element(*self.month).text).is_not_equal_to(self.month_text):
            ele = self.browser.find_element(*self.month).text
            for i in range(0, 12):
                if assert_that(self.browser.find_element(*self.month).text).is_equal_to(self.month_text):
                    assert_that(self.browser.find_element(*self.event_info).text).is_equal_to(self.event_info_text)
                    self.browser.find_element(*self.event_info).click()

                    assert_that(self.browser.find_element(*self.event_title).text).is_equal_to(self.event_title_text)
                    assert_that(self.browser.find_element(*self.event_start).text).is_equal_to(self.event_start_text)
                    assert_that(self.browser.find_element(*self.event_end).text).is_equal_to(self.event_end_text)
                    assert_that(self.browser.find_element(*self.event_des).text).is_equal_to(self.event_des_text)
                    if self.browser.find_element(*self.calendar_icon).is_displayed():
                        print("ICON IS VISIBLE")
                    else:
                        print("ICON IS NOT VISIBLE")

                    self.browser.find_element(*self.modal_close).click()
                    break
                self.browser.find_element(*self.prev_button).click()