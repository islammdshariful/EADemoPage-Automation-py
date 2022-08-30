from selenium.webdriver import ActionChains

from pages.basepage import BasePage
from utils.config import *


class InfoBox(BasePage, Helper):
    widget = '//*[@id="post-1509"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Info Box'
    doc_link = '//*[@id="post-1509"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "INFO BOX"

    info_box_icon_1 = (By.XPATH, f'//*[@id="post-1509"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                            f'/div/div/div[1]/div/div/div/div/div/div[1]/div')
    info_box_1 = (By.XPATH, f'//*[@id="post-1509"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                            f'/div/div/div[1]/div/div/div/div/div/div[2]/h4')
    info_box_1_text = "Development"
    info_box_icon_2 = (By.XPATH, f'//*[@id="post-1509"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                 f'/div/div/div[2]/div/div/div/div/div/div[1]/div')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.info_box)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1028)
                """Move cursor to icon 1"""
                self.move_cursor_to(self.info_box_icon_1)
                """Check infobox title"""
                self.check_text_matches_with(self.info_box_1, self.info_box_1_text)
                """Move cursor to icon 1"""
                self.move_cursor_to(self.info_box_icon_2)
