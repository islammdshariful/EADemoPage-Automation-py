from pages.basepage import BasePage
from utils.config import *


class CreativeButton(BasePage, Helper):
    widget = '//*[@id="post-21"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = "Creative Buttons"
    doc_link = '//*[@id="post-21"]/div/div/div/div/section[1]/div[3]/div/div[2]' \
               '/div/div/section/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "CREATIVE BUTTONS"

    FIRST_BUTTON = (By.XPATH, f'//*[@id="post-21"]/div/div/div/div/section[2]/div/div/'
                              f'div/div/div/section[2]/div/div/div[1]/div/div/div/div/div/a/div/span[2]')
    FIRST_BUTTON_TEXT = "EXPLORE THE GLOBE"
    LAST_BUTTON = (By.XPATH, f'//*[@id="post-21"]/div/div/div/div/section[2]/div/div/div/'
                             f'div/div/section[6]/div/div/div[4]/div/div/div/div/div/a/div/span[2]')
    LAST_BUTTON_TEXT = "EXPLORE MORE"
    LAST_BUTTON_ATTRIBUTE = (By.XPATH, f'//*[@id="post-21"]/div/div/div/div/section[2]/div/div/div/div'
                                       f'/div/section[6]/div/div/div[4]/div/div/div/div/div/a')
    LAST_BUTTON_ATTRIBUTE_TEXT = "Go!"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.create_button)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1023)
                """move cursor to a button"""
                self.move_cursor_to(self.FIRST_BUTTON)
                """check button text"""
                self.check_text_matches_with(self.FIRST_BUTTON, self.FIRST_BUTTON_TEXT)
                """move another button"""
                self.move_cursor_to(self.LAST_BUTTON)
                """check button text"""
                self.check_text_matches_with(self.LAST_BUTTON, self.LAST_BUTTON_TEXT)
                """check button attribute"""
                assert_that(self.get_element(self.LAST_BUTTON_ATTRIBUTE).get_attribute("data-text")).\
                    is_equal_to(self.LAST_BUTTON_ATTRIBUTE_TEXT)


