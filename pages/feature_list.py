from selenium.webdriver import ActionChains

from utils.config import *


class FeatureList:
    widget = '//*[@id="post-5403"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Feature List'
    doc_link = '//*[@id="post-5403"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA FEATURE LIST"

    list_1_icon = (By.XPATH, f'//*[@id="eael-feature-list-2686bb44"]/li[1]/div[1]/div/span')
    list_1_title = (By.XPATH, f'//*[@id="eael-feature-list-2686bb44"]/li[1]/div[2]/h3')
    list_1_title_text = "Easy To Use"
    list_1_des = (By.XPATH, f'//*[@id="eael-feature-list-2686bb44"]/li[1]/div[2]/p')
    list_1_des_text = "Configure content settings by adding icon or images,choose icon shape, " \
                      "shape view and enable the connector"
    list_2_icon = (By.XPATH, f'//*[@id="eael-feature-list-2686bb44"]/li[2]/div[1]/div/span')
    list_2_title = (By.XPATH, f'//*[@id="eael-feature-list-2686bb44"]/li[2]/div[2]/h3')
    list_2_title_text = "Daily Report"
    list_2_des = (By.XPATH, f'//*[@id="eael-feature-list-2686bb44"]/li[2]/div[2]/p')
    list_2_des_text = "Influence your potential buyers by giving an engaging icon title and choose your preferred " \
                      "header title tag to make it look appealing"
    list_3_icon = (By.XPATH, f'//*[@id="eael-feature-list-2686bb44"]/li[3]/div[1]/div/span')
    list_3_title = (By.XPATH, f'//*[@id="eael-feature-list-2686bb44"]/li[3]/div[2]/h3')
    list_3_title_text = "Real Time"
    list_3_des = (By.XPATH, f'//*[@id="eael-feature-list-2686bb44"]/li[3]/div[2]/p')
    list_3_des_text = "Add as much as key aspects you want and enable the toggle to connector and connect" \
                      " each section in an interactive way"
    list_4_icon = (By.XPATH, f'//*[@id="eael-feature-list-2686bb44"]/li[4]/div[1]/div/span')
    list_4_title = (By.XPATH, f'//*[@id="eael-feature-list-2686bb44"]/li[4]/div[2]/h3')
    list_4_title_text = "Extreme Security"
    list_4_des = (By.XPATH, f'//*[@id="eael-feature-list-2686bb44"]/li[4]/div[2]/p')
    list_4_des_text = "Style your icon, content and connector from list tab outstandingly by playing with " \
                      "colors and other style sections"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(feature_list)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 852)")

            assert_that(self.browser.find_element(*self.list_1_title).text).is_equal_to(self.list_1_title_text)
            assert_that(self.browser.find_element(*self.list_1_des).text).is_equal_to(self.list_1_des_text)

            assert_that(self.browser.find_element(*self.list_2_title).text).is_equal_to(self.list_2_title_text)
            assert_that(self.browser.find_element(*self.list_2_des).text).is_equal_to(self.list_2_des_text)

            assert_that(self.browser.find_element(*self.list_3_title).text).is_equal_to(self.list_3_title_text)
            assert_that(self.browser.find_element(*self.list_3_des).text).is_equal_to(self.list_3_des_text)

            assert_that(self.browser.find_element(*self.list_4_title).text).is_equal_to(self.list_4_title_text)
            assert_that(self.browser.find_element(*self.list_4_des).text).is_equal_to(self.list_4_des_text)

            if self.browser.find_element(*self.list_1_icon).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to(0)
            if self.browser.find_element(*self.list_2_icon).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to(0)
            if self.browser.find_element(*self.list_3_icon).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to(0)
            if self.browser.find_element(*self.list_4_icon).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to(0)