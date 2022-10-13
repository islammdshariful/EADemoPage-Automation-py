from selenium.webdriver import ActionChains, Keys

from pages.basepage import BasePage
from utils.config import *


class FeatureList(BasePage, Helper):
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
        super().__init__(browser)

    def check_list_item(self, title_locator, title_text, des_locator, des_text):
        self.check_text_matches_with(title_locator, title_text)
        self.check_text_matches_with(des_locator, des_text)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.feature_list)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(852)

                """List 1"""
                self.check_list_item(self.list_1_title, self.list_1_title_text, self.list_1_des, self.list_1_des_text)
                """List 2"""
                self.check_list_item(self.list_2_title, self.list_2_title_text, self.list_2_des, self.list_2_des_text)
                """List 3"""
                self.check_list_item(self.list_3_title, self.list_3_title_text, self.list_3_des, self.list_3_des_text)
                """List 4"""
                self.check_list_item(self.list_4_title, self.list_4_title_text, self.list_4_des, self.list_4_des_text)

                """List 1 Icon"""
                self.is_visible(self.list_1_icon, "List Icon 1 is not visible.")
                """List 2 Icon"""
                self.is_visible(self.list_2_icon, "List Icon 2 is not visible.")
                """List 3 Icon"""
                self.is_visible(self.list_3_icon, "List Icon 3 is not visible.")
                """List 4 Icon"""
                self.is_visible(self.list_4_icon, "List Icon 4 is not visible.")
