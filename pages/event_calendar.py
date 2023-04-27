from pages.basepage import BasePage
from utils.config import *


class EventCalendar(BasePage, Helper):
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
    event_info_text = "07:00 AM Event Title March"

    event_title = (By.XPATH, f'//*[@id="eaelecModal"]/div[2]/div[1]/h2')
    event_title_text = "Event Title March"
    calendar_icon = (By.XPATH, f'//*[@id="eaelecModal"]/div[2]/div[1]/span[1]/i')
    event_start = (By.XPATH, f'//*[@id="eaelecModal"]/div[2]/div[1]/span[1]')
    event_start_text = "Mar 4th 7:00 AM"
    event_end = (By.XPATH, f'//*[@id="eaelecModal"]/div[2]/div[1]/span[2]')
    event_end_text = "- 7:00 AM"

    event_des = (By.XPATH, f'//*[@id="eaelecModal"]/div[2]/div[2]')
    event_des_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod " \
                     "tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse " \
                     "ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. " \
                     "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor " \
                     "incididunt ut labore et dolore magna aliqua."
    modal_close = (By.XPATH, f'//*[@id="eaelecModal"]/div[2]/div[1]/div/span/i')

    scroll = (By.CSS_SELECTOR, '.elementor-element-9daeb76')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.event_calendar)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to_element(self.scroll)
                for i in range(12):
                    month_name = self.get_element_text(self.month)
                    """click previous button util get the expected month"""
                    if month_name == self.month_text:
                        self.check_text_matches_with(self.event_info, self.event_info_text)
                        self.do_click(self.event_info)
                        self.check_text_matches_with(self.event_title, self.event_title_text)
                        self.check_text_matches_with(self.event_start, self.event_start_text)
                        self.check_text_matches_with(self.event_end, self.event_end_text)
                        self.check_text_matches_with(self.event_des, self.event_des_text)
                        self.is_visible(self.calendar_icon, "Calendar icon is not visible.")
                        self.do_click(self.modal_close)
                        break
                    self.do_click(self.prev_button)
