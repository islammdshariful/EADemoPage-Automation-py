from selenium.webdriver import Keys

from utils.config import *
from selenium.webdriver.support.color import Color


class ProgressBar(Helper):
    widget = '//*[@id="post-3802"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Progress Bar'
    doc_link = '//*[@id="post-3802"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "PROGRESS BAR"
    name = (By.XPATH, f'//*[@id="post-3802"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                      f'/div/div/div[1]/div/div/div[1]/div/div/div[1]')
    name_text = "Photoshop"
    count = (By.XPATH, f'//*[@id="post-3802"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                       f'/div/div/div[1]/div/div/div[1]/div/div/div[2]/span[1]')
    count_text = "62%"

    progress_bar_full = (By.XPATH, f'//*[@id="post-3802"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                   f'/div/div/div[1]/div/div/div[1]/div/div/div[2]')
    progress_bar_full_color = "#f6f6f6"
    progress_bar_fill = (By.XPATH, f'//*[@id="post-3802"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                   f'/div/div/div[1]/div/div/div[1]/div/div/div[2]/span[2]')
    progress_bar_fill_color = "#6a61fb"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.progress_bar)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1037)")
                assert_that(self.browser.find_element(*self.name).text).is_equal_to(self.name_text)
                time.sleep(1)

                full_rgb = self.browser.find_element(*self.progress_bar_full).value_of_css_property('background-color')
                hex_1 = Color.from_string(full_rgb).hex
                assert_that(hex_1).is_equal_to(self.progress_bar_full_color)

                fill_rgb = self.browser.find_element(*self.progress_bar_fill).value_of_css_property('background-color')
                hex_2 = Color.from_string(fill_rgb).hex
                assert_that(hex_2).is_equal_to(self.progress_bar_fill_color)
                time.sleep(1)
                assert_that(self.browser.find_element(*self.count).text).is_equal_to(self.count_text)
