from selenium.webdriver import ActionChains

from utils.config import *
from selenium.webdriver.support.color import Color


class ContentTimeline:
    widget = '//*[@id="post-1804"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Content Timeline'
    doc_link = '//*[@id="post-1804"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "CONTENT TIMELINE"

    post_1_title = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[1]/div[3]/h2'
    post_1_title_text = "How to Include Elementor Template using a Shortcode"
    post_1_des = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[1]/div[3]/p'
    post_1_des_text = "Thanks to Elementor PRO, you can now easily include your ...."
    post_1_date = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[1]/div[3]/span'
    post_1_date_text = "02 September 2019"
    post_1_icon = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[1]/div[2]/i'

    post_2_title = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[2]/div[3]/h2'
    post_2_title_text = "What’s New in Essential Addons for Elementor Version 3.0?"
    post_2_des = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[2]/div[3]/p'
    post_2_des_text = "With the Introduction of Essential Addons 3.0, you are about …"
    post_2_date = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[2]/div[3]/span'
    post_2_date_text = "05 September 2019"
    post_2_icon = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[2]/div[2]/i'

    post_3_title = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[3]/div[3]/h2'
    post_3_title_text = "How to Filter Your WordPress Blogs Based on Categories or Tags"
    post_3_des = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[3]/div[3]/p'
    post_3_des_text = "To get more traffic on your content, it is important …"
    post_3_date = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[3]/div[3]/span'
    post_3_date_text = "08 September 2019"
    post_3_icon = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[3]/div[2]/i'

    post_4_title = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[4]/div[3]/h2'
    post_4_title_text = "How To Hide Your Existing Page From Certain Users in Elementor"
    post_4_des = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[4]/div[3]/p'
    post_4_des_text = "Once you turn on the Elementor Role Manager option, users …"
    post_4_date = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[4]/div[3]/span'
    post_4_date_text = "05 September 2019"
    post_4_icon = f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[4]/div[2]/i'
    post_4_icon_background = (By.XPATH, f'//*[@id="eael-content-timeline-72c859bb"]/div/div/div[4]/div[2]')
    post_4_icon_background_code = "#7f41ff"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(content_timeline)

    def check_post(self, title, title_text, post_des, des_text, date, date_text):
        assert_that(self.browser.find_element(By.XPATH, title).text).is_equal_to(title_text)
        assert_that(self.browser.find_element(By.XPATH, post_des).text).is_equal_to(des_text)
        assert_that(self.browser.find_element(By.XPATH, date).text).is_equal_to(date_text)

    def check_visibility(self, icon):
        if self.browser.find_element(By.XPATH, icon).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Post Image is not showing")

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1004)")
            time.sleep(1)

            self.check_visibility(self.post_1_icon)
            self.check_post(self.post_1_title, self.post_1_title_text, self.post_1_des,
                            self.post_1_des_text, self.post_1_date, self.post_1_date_text)

            self.check_visibility(self.post_2_icon)
            self.browser.execute_script("window.scrollTo(0, 1393)")

            self.check_post(self.post_2_title, self.post_2_title_text, self.post_2_des,
                            self.post_2_des_text, self.post_2_date, self.post_2_date_text)

            self.check_visibility(self.post_3_icon)
            self.browser.execute_script("window.scrollTo(0, 1554)")
            self.check_post(self.post_3_title, self.post_3_title_text, self.post_3_des,
                            self.post_3_des_text, self.post_3_date, self.post_3_date_text)

            self.check_visibility(self.post_4_icon)
            self.browser.execute_script("window.scrollTo(0, 1677)")
            self.check_post(self.post_4_title, self.post_4_title_text, self.post_4_des,
                            self.post_4_des_text, self.post_4_date, self.post_4_date_text)
            time.sleep(1)
            bg_color = self.browser.find_element(*self.post_4_icon_background).value_of_css_property('background-color')
            hex = Color.from_string(bg_color).hex
            assert_that(hex).is_equal_to(self.post_4_icon_background_code)