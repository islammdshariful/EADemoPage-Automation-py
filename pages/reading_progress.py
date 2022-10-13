from utils.config import *
from selenium.webdriver.support.color import Color


class ReadingProgress(BasePage, Helper):
    widget = '//*[@id="post-255176"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'Reading Progress Bar'
    doc_link = '//*[@id="post-255176"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA READING PROGRESS BAR"

    progress_bar = (By.XPATH, f"//div[@class='eael-reading-progress-fill']")
    color_fill = "#1fd18e"
    width_1 = "width: 0%;"
    width_2 = "width: 76.6803;"
    width_3 = "width: 100%;"

    scroll_1 = (By.XPATH, '//*[@id="post-255176"]/div/div/div/div/section[2]/div/div/div/div/div/section[1]/div/div'
                          '/div[1]/div/div/div[1]/div/h3')
    scroll_2 = (By.XPATH, '//*[@id="post-255176"]/div/div/div/div/section[5]/div/div/div/div/div/section/div/div/'
                          'div[1]/div/div/div[1]/div/h3')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.reading_progress)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to_element(self.scroll_2)
                assert_that(self.get_element(self.progress_bar).get_attribute("style")).is_equal_to(self.width_2)

                self.scroll_to_bottom()
                assert_that(self.get_element(self.progress_bar).get_attribute("style")).is_equal_to(self.width_3)
                rgb = self.get_element(self.progress_bar).value_of_css_property('background-color')
                hex = Color.from_string(rgb).hex
                assert_that(hex).is_equal_to(self.color_fill)
