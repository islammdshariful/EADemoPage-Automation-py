from selenium.webdriver import ActionChains

from utils.config import *
from selenium.webdriver.support.color import Color


class DualColorHeading:
    widget = '//*[@id="post-1511"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = "Dual Color Heading"
    PAGE_TITLE_TEXT = "Dual Color Heading"
    DOC_LINK = '//*[@id="post-1511"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "DUAL COLOR HEADING"

    icon = (By.XPATH, f'//*[@id="post-1511"]/div/div/div/div/section[2]/'
                      f'div/div/div/div/div/div/div/div/span[1]/i')
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
        self.browser = browser

    def load(self):
        self.browser.get(dual_color_heading)

    def testcase(self):
        c = CheckText(self.browser)

        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.DOC_LINK, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 908)")
            time.sleep(1)

            if self.browser.find_element(*self.icon).is_displayed():
                print("ICON IS VISIBLE")
            else:
                print("ICON IS NOT VISIBLE")

            first_rgb = self.browser.find_element(*self.first_color).value_of_css_property('color')
            hex_1 = Color.from_string(first_rgb).hex
            assert_that(hex_1).is_equal_to(self.first_color_code)
            assert_that(self.browser.find_element(*self.first_color).text).is_equal_to(self.first_color_text)

            second_rgb = self.browser.find_element(*self.second_color).value_of_css_property('color')
            hex_2 = Color.from_string(second_rgb).hex
            assert_that(hex_2).is_equal_to(self.second_color_code)
            assert_that(self.browser.find_element(*self.second_color).text).is_equal_to(self.second_color_text)
            assert_that(self.browser.find_element(*self.des).text).is_equal_to(self.des_text)

