from utils.config import *
from selenium.webdriver.support.color import Color


class Divider(BasePage, Helper):
    widget = '//*[@id="post-2950"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Divider'
    doc_link = '//*[@id="post-2950"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "DIVIDER"

    left_divider = (By.XPATH, f'//*[@id="post-2950"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                              f'/div/div/div[1]/div/div/div[2]/div/div/div/div/span[1]/span')
    right_divider = (By.XPATH, f'//*[@id="post-2950"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                               f'/div/div/div[1]/div/div/div[2]/div/div/div/div/span[3]/span')
    img_divider = (By.XPATH, f'//*[@id="post-2950"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                             f'/div[1]/div/div/div[2]/div/div/div/div/span[2]/span/img')
    border_color = "#1aed9d"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.divider)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(971)

                left = self.get_element(self.left_divider).value_of_css_property('border-color')
                left_border = Color.from_string(left).hex
                assert_that(left_border).is_equal_to(self.border_color)
                right = self.get_element(self.right_divider).value_of_css_property('border-color')
                right_border = Color.from_string(right).hex
                assert_that(right_border).is_equal_to(self.border_color)

                self.is_visible(self.img_divider, "Image not visible.")
