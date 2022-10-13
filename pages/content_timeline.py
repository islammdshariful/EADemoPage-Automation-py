from utils.config import *
from selenium.webdriver.support.color import Color


class ContentTimeline(BasePage, Helper):
    widget = '//*[@id="post-1804"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Content Timeline'
    doc_link = '//*[@id="post-1804"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "CONTENT TIMELINE"

    post_1_title = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[1]/div[3]/h2')
    post_1_title_text = "How to Include Elementor Template using a Shortcode"
    post_1_des = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[1]/div[3]/p')
    post_1_des_text = "Thanks to Elementor PRO, you can now easily include your ...."
    post_1_date = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[1]/div[3]/span')
    post_1_date_text = "02 September 2019"
    post_1_icon = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[1]/div[2]/i')

    post_2_title = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[2]/div[3]/h2')
    post_2_title_text = "What’s New in Essential Addons for Elementor Version 3.0?"
    post_2_des = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[2]/div[3]/p')
    post_2_des_text = "With the Introduction of Essential Addons 3.0, you are about …"
    post_2_date = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[2]/div[3]/span')
    post_2_date_text = "05 September 2019"
    post_2_icon = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[2]/div[2]/i')

    post_3_title = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[3]/div[3]/h2')
    post_3_title_text = "How to Filter Your WordPress Blogs Based on Categories or Tags"
    post_3_des = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[3]/div[3]/p')
    post_3_des_text = "To get more traffic on your content, it is important …"
    post_3_date = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[3]/div[3]/span')
    post_3_date_text = "08 September 2019"
    post_3_icon = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[3]/div[2]/i')

    post_4_title = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[4]/div[3]/h2')
    post_4_title_text = "How To Hide Your Existing Page From Certain Users in Elementor"
    post_4_des = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[4]/div[3]/p')
    post_4_des_text = "Once you turn on the Elementor Role Manager option, users …"
    post_4_date = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[4]/div[3]/span')
    post_4_date_text = "05 September 2019"
    post_4_icon = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[4]/div[2]/i')
    post_4_icon_background = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[4]/div[2]')
    post_4_icon_background_code = "#7f41ff"

    def __init__(self, browser):
        super().__init__(browser)

    def check_post(self, icon, title, title_text, post_des, des_text, date, date_text):
        self.is_visible(icon, "Post icon not visible")

        self.check_text_matches_with(title, title_text)
        # self.check_text_matches_with(post_des, des_text)
        self.check_text_matches_with(date, date_text)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.content_timeline)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1004)

                self.check_post(self.post_1_icon, self.post_1_title, self.post_1_title_text, self.post_1_des,
                                self.post_1_des_text, self.post_1_date, self.post_1_date_text)

                self.scroll_to(1393)
                self.check_post(self.post_2_icon, self.post_2_title, self.post_2_title_text, self.post_2_des,
                                self.post_2_des_text, self.post_2_date, self.post_2_date_text)

                self.scroll_to(1554)
                self.check_post(self.post_3_icon, self.post_3_title, self.post_3_title_text, self.post_3_des,
                                self.post_3_des_text, self.post_3_date, self.post_3_date_text)

                self.scroll_to(1677)
                self.check_post(self.post_4_icon, self.post_4_title, self.post_4_title_text, self.post_4_des,
                                self.post_4_des_text, self.post_4_date, self.post_4_date_text)

                background_color = self.get_element(self.post_4_icon_background).value_of_css_property('background-color')
                hex = Color.from_string(background_color).hex
                assert_that(hex).is_equal_to(self.post_4_icon_background_code)
