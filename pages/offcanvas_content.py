import time

from selenium.webdriver import ActionChains, Keys

from utils.config import *


class OffCanvas(Helper):
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
    left_img = f"//div[starts-with(@class, 'elementor-element elementor-element-7fa94fd2 elementor-widget elementor-" \
               f"widget-image')]//div//div//img"
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

    right_img = f"//div[starts-with(@class, 'elementor-element elementor-element-4f7933bf elementor-widget elementor-" \
               f"widget-image')]//div//div//img"
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
        self.browser = browser

    def load(self):
        self.browser.get(self.offcanvas_content)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 958)")
                time.sleep(1)

                # Left
                self.browser.find_element(*self.left_side).click()
                time.sleep(1)
                cursor = ActionChains(self.browser)
                l_home = self.browser.find_element(*self.left_home)
                l_about = self.browser.find_element(*self.left_about)
                l_service = self.browser.find_element(*self.left_service)
                l_blog = self.browser.find_element(*self.left_blog)
                l_faq = self.browser.find_element(*self.left_faq)
                l_contact = self.browser.find_element(*self.left_contact)
                l_button = self.browser.find_element(*self.left_button)

                cursor.move_to_element(l_home).perform()
                cursor.move_to_element(l_about).perform()
                cursor.move_to_element(l_service).perform()
                cursor.move_to_element(l_blog).perform()
                cursor.move_to_element(l_faq).perform()
                cursor.move_to_element(l_contact).perform()
                cursor.move_to_element(l_button).perform()
                cursor.reset_actions()

                self.check_visibility(self.left_img, "Left Image is not visible.")

                self.browser.find_element(*self.blank).click()

                # Right
                self.browser.find_element(*self.right_side).click()
                time.sleep(1)
                cursor = ActionChains(self.browser)
                r_home = self.browser.find_element(*self.right_home)
                r_about = self.browser.find_element(*self.right_about)
                r_service = self.browser.find_element(*self.right_service)
                r_blog = self.browser.find_element(*self.right_blog)
                r_faq = self.browser.find_element(*self.right_faq)
                r_contact = self.browser.find_element(*self.right_contact)
                r_button = self.browser.find_element(*self.right_button)

                cursor.move_to_element(r_home).perform()
                cursor.move_to_element(r_about).perform()
                cursor.move_to_element(r_service).perform()
                cursor.move_to_element(r_blog).perform()
                cursor.move_to_element(r_faq).perform()
                cursor.move_to_element(r_contact).perform()
                cursor.move_to_element(r_button).perform()

                self.check_visibility(self.right_img, "Right image is not visible.")

                self.browser.find_element(*self.blank).click()






