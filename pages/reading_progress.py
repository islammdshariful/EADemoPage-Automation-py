from selenium.webdriver import ActionChains

from utils.config import *
from selenium.webdriver.support.color import Color

class ReadingProgress:
    widget = '//*[@id="post-255176"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'Reading Progress Bar'
    doc_link = '//*[@id="post-255176"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA READING PROGRESS BAR"

    progress_bar = (By.XPATH, f'/html/body/div[4]/div[3]/div/div')
    color_fill = "#1fd18e"
    width_1 = "width: 22.8026%;"
    width_2 = "width: 79.6421%;"
    width_3 = "width: 100%;"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(reading_progress)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1004)")
            time.sleep(5)

            bar = self.browser.find_element(*self.progress_bar)
            assert_that(bar.get_attribute("style")).is_equal_to(self.width_1)
            rgb = bar.value_of_css_property('background-color')
            hex = Color.from_string(rgb).hex
            assert_that(hex).is_equal_to(self.color_fill)
            self.browser.execute_script("window.scrollTo(0, 3560)")
            time.sleep(1)
            assert_that(bar.get_attribute("style")).is_equal_to(self.width_2)
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)
            assert_that(bar.get_attribute("style")).is_equal_to(self.width_3)
            rgb = bar.value_of_css_property('background-color')
            hex = Color.from_string(rgb).hex
            assert_that(hex).is_equal_to(self.color_fill)
