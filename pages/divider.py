from selenium.webdriver import Keys

from utils.config import *
from selenium.webdriver.support.color import Color


class Divider(Helper):
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
    img_divider = f'//*[@id="post-2950"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                             f'/div[1]/div/div/div[2]/div/div/div/div/span[2]/span/img'
    border_color = "#1aed9d"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.divider)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 971)")

                left = self.browser.find_element(*self.left_divider).value_of_css_property('border-color')
                left_border = Color.from_string(left).hex
                assert_that(left_border).is_equal_to(self.border_color)
                right = self.browser.find_element(*self.right_divider).value_of_css_property('border-color')
                right_border = Color.from_string(right).hex
                assert_that(right_border).is_equal_to(self.border_color)

                self.check_visibility(self.img_divider, "Image not visible.")
