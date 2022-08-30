from pages.basepage import BasePage
from utils.config import *
from selenium.webdriver.support.color import Color


class DualColorHeading(BasePage, Helper):
    widget = '//*[@id="post-1511"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = "Dual Color Heading"
    PAGE_TITLE_TEXT = "Dual Color Heading"
    doc_link = '//*[@id="post-1511"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "DUAL COLOR HEADING"

    icon = (By.XPATH, f'//*[@id="post-1511"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/span[1]/i')
    first_color = (By.XPATH, f'//*[@id="post-1511"]/div/div/div/div/section[2]'
                             f'/div/div/div/div/div/div/div/div/h2/span[1]')
    first_color_code = "#4f6592"
    first_color_text = "Dual Headers"
    second_color = (By.XPATH, f'//*[@id="post-1511"]/div/div/div/div/section[2]'
                              f'/div/div/div/div/div/div/div/div/h2/span[2]')
    second_color_code = "#207eff"
    second_color_text = "With Icon"
    des = (By.XPATH, f'//*[@id="post-1511"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/span[2]/p')
    des_text = "Add Icon with dual headings"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.dual_color_heading)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(908)
                """Icon visible"""
                self.is_visible(self.icon, "Icon is not visible.")
                """First string color"""
                first_rgb = self.get_element(self.first_color).value_of_css_property('color')
                hex_code = Color.from_string(first_rgb).hex
                """Color code check"""
                self.string_match(hex_code, self.first_color_code)
                """First string text"""
                assert_that(self.browser.find_element(*self.first_color).text).is_equal_to(self.first_color_text)
                """Second string color"""
                second_rgb = self.get_element(self.second_color).value_of_css_property('color')
                hex_code = Color.from_string(second_rgb).hex
                """Color code check"""
                self.string_match(hex_code, self.second_color_code)
                """Second string color"""
                self.check_text_matches_with(self.second_color, self.second_color_text)
                """Description"""
                self.check_text_matches_with(self.des, self.des_text)

