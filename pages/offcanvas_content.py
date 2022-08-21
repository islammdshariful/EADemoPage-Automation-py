import time

from selenium.webdriver import ActionChains, Keys

from pages.basepage import BasePage
from utils.config import *


class OffCanvas(BasePage, Helper):
    widget = '//*[@id="post-3926"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Offcanvas'
    doc_link = '//*[@id="post-3926"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "OFFCANVAS"

    left_side = (By.XPATH, f'//*[@id="post-3926"]/div/div/div/div/section[2]/div/div/div/div/div/div[2]'
                           f'/div/div/div/div/span[2]')
    right_side = (By.XPATH, f'//*[@id="post-3926"]/div/div/div/div/section[2]/div/div/div/div/div/div[3]'
                            f'/div/div/div/div/span[2]')
    left_img = (By.XPATH, f"//div[starts-with(@class, 'elementor-element elementor-element-7fa94fd2 elementor-widget "
                          f"elementor-widget-image')]//div//div//img")
    left = f"//div[starts-with(@class, 'elementor-element elementor-element-379af5cf elementor-icon-list--layout-" \
           f"traditional elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list')]//div//ul"
    left_home = (By.XPATH, left + f"//li[1]/a/span")
    left_about = (By.XPATH, left + f"//li[2]/a/span")
    left_service = (By.XPATH, left + f"//li[3]/a/span")
    left_blog = (By.XPATH, left + f"//li[4]/a/span")
    left_faq = (By.XPATH, left + f"//li[5]/a/span")
    left_contact = (By.XPATH, left + f"//li[6]/a/span")
    left_button = (By.XPATH, f"//div[starts-with(@class, 'elementor-element elementor-element-3e177b12 elementor-widget"
                             f" elementor-widget-button')]//div//div//a//span")
    blank = (By.XPATH, f"//div[starts-with(@class, 'eael-offcanvas-container eael-offcanvas-container-70ec7ef')]")

    right_img = (By.XPATH, f"//div[starts-with(@class, 'elementor-element elementor-element-4f7933bf "
                           f"elementor-widget elementor-widget-image')]//div//div//img")
    right = f"//div[starts-with(@class, 'elementor-element elementor-element-56c183dc elementor-icon-list--layout-" \
           f"traditional elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list')]//div//ul"
    right_home = (By.XPATH, right + f"//li[1]/a/span")
    right_about = (By.XPATH, right + f"//li[2]/a/span")
    right_service = (By.XPATH, right + f"//li[3]/a/span")
    right_blog = (By.XPATH, right + f"//li[4]/a/span")
    right_faq = (By.XPATH, right + f"//li[5]/a/span")
    right_contact = (By.XPATH, right + f"//li[6]/a/span")
    right_button = (By.XPATH, f"//div[starts-with(@class, 'elementor-element elementor-element-31ac75f elementor-"
                              f"widget elementor-widget-button')]//div//div//a//span")

    def __init__(self, browser):
        super().__init__(browser)

    def left_canvas(self):
        self.do_click(self.left_side)
        time.sleep(1)

        self.cursor.move_to_element(self.get_element(self.left_home)).\
            move_to_element(self.get_element(self.left_about)).\
            move_to_element(self.get_element(self.left_service)).\
            move_to_element(self.get_element(self.left_blog)).\
            move_to_element(self.get_element(self.left_faq)).\
            move_to_element(self.get_element(self.left_contact)).\
            move_to_element(self.get_element(self.left_button)).perform()

        self.is_visible(self.left_img, "Left Image is not visible.")

        self.do_click(self.blank)

    def right_canvas(self):
        self.do_click(self.right_side)
        time.sleep(1)

        self.cursor.move_to_element(self.get_element(self.right_home)). \
            move_to_element(self.get_element(self.right_about)). \
            move_to_element(self.get_element(self.right_service)). \
            move_to_element(self.get_element(self.right_blog)). \
            move_to_element(self.get_element(self.right_faq)). \
            move_to_element(self.get_element(self.right_contact)). \
            move_to_element(self.get_element(self.right_button)).perform()

        self.is_visible(self.right_img, "Right Image is not visible.")

        self.do_click(self.blank)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.offcanvas_content)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(958)

                """Left canvas open"""
                self.left_canvas()

                """Right canvas open"""
                self.right_canvas()






