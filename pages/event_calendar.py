from selenium.webdriver import ActionChains, Keys

from utils.config import *


class EventCalendar(Helper):
    widget = '//*[@id="post-257828"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = "Event Calendar"
    doc_link = '//*[@id="post-257828"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/' \
               'section/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA EVENT CALENDAR"
    prev_button = (By.XPATH, f'//*[@id="eael-event-calendar-22bed70e"]/div[1]/div[1]/div/button[1]')
    next_button = (By.XPATH, f'//*[@id="eael-event-calendar-22bed70e"]/div[1]/div[1]/div/button[2]')
    month = (By.XPATH, f'//*[@id="eael-event-calendar-22bed70e"]/div[1]/div[2]/h2')
    month_text = "March 2022"

    event_info = (By.XPATH, f'//*[@id="eael-event-calendar-22bed70e"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/'
                            f'div[2]/table/tbody/tr/td[5]')
    event_info_text = "07:00 AM Event Title Mar"

    event_title = (By.XPATH, f'//*[@id="eaelecModal"]/div[2]/div[1]/h2')
    event_title_text = "Event Title Mar"
    calendar_icon = f'//*[@id="eaelecModal"]/div[2]/div[1]/span[1]/i'
    event_start = (By.XPATH, f'//*[@id="eaelecModal"]/div[2]/div[1]/span[1]')
    event_start_text = "Mar 4th 7:00 AM"
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
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.event_calendar)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1641)")
                time.sleep(1)

                for i in range(0, 12):
                    mnt = self.browser.find_element(*self.month).text
                    if mnt == self.month_text:
                        assert_that(self.browser.find_element(*self.event_info).text).is_equal_to(self.event_info_text)
                        self.browser.find_element(*self.event_info).click()

                        time.sleep(1)
                        assert_that(self.browser.find_element(*self.event_title).text).is_equal_to(self.event_title_text)
                        assert_that(self.browser.find_element(*self.event_start).text).is_equal_to(self.event_start_text)
                        assert_that(self.browser.find_element(*self.event_end).text).is_equal_to(self.event_end_text)
                        assert_that(self.browser.find_element(*self.event_des).text).is_equal_to(self.event_des_text)
                        self.check_visibility(self.calendar_icon, "Calendar icon is not visible.")
                        self.browser.find_element(*self.modal_close).click()
                        break
                    self.browser.find_element(*self.prev_button).click()
