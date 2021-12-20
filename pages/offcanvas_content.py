import time

from selenium.webdriver import ActionChains

from utils.config import *


class OffCanvas:
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
    left_img = (By.XPATH, f'/html/body/div[10]/div/div/div/section/div/div/div/div/div/div[1]/div/div/img')
    left_home = (By.XPATH, f'/html/body/div[10]/div/div/div/section/div/div/div/div/div/div[2]/div/ul/li[1]/a/span')
    left_about = (By.XPATH, f'/html/body/div[10]/div/div/div/section/div/div/div/div/div/div[2]/div/ul/li[2]')
    left_service = (By.XPATH, f'/html/body/div[10]/div/div/div/section/div/div/div/div/div/div[2]/div/ul/li[3]')
    left_blog = (By.XPATH, f'/html/body/div[10]/div/div/div/section/div/div/div/div/div/div[2]/div/ul/li[4]')
    left_faq = (By.XPATH, f'/html/body/div[10]/div/div/div/section/div/div/div/div/div/div[2]/div/ul/li[5]')
    left_contact = (By.XPATH, f'/html/body/div[10]/div/div/div/section/div/div/div/div/div/div[2]/div/ul/li[6]')
    left_button = (By.XPATH, f'/html/body/div[10]/div/div/div/section/div/div/div/div/div/div[3]/div/div/a/span/span')
    blank = (By.XPATH, f'/html/body/div[12]')

    right_img = (By.XPATH, f'/html/body/div[9]/div/div/div/section/div/div/div/div/div/div[1]/div/div/img')
    right_home = (By.XPATH, f'/html/body/div[9]/div/div/div/section/div/div/div/div/div/div[2]/div/ul/li[1]/a/span')
    right_about = (By.XPATH, f'/html/body/div[9]/div/div/div/section/div/div/div/div/div/div[2]/div/ul/li[2]')
    right_service = (By.XPATH, f'/html/body/div[9]/div/div/div/section/div/div/div/div/div/div[2]/div/ul/li[3]')
    right_blog = (By.XPATH, f'/html/body/div[9]/div/div/div/section/div/div/div/div/div/div[2]/div/ul/li[4]')
    right_faq = (By.XPATH, f'/html/body/div[9]/div/div/div/section/div/div/div/div/div/div[2]/div/ul/li[5]')
    right_contact = (By.XPATH, f'/html/body/div[9]/div/div/div/section/div/div/div/div/div/div[2]/div/ul/li[6]')
    right_button = (By.XPATH, f'/html/body/div[9]/div/div/div/section/div/div/div/div/div/div[3]/div/div/a/span/span')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(offcanvas_content)

    def testcase(self):
        c = CheckText(self.browser)
        # with soft_assertions():
        c.check_widget_name(self.widget, self.widget_name)
        if check_doc:
            c.check_doc(self.doc_link, self.doc_name)

        self.browser.execute_script("window.scrollTo(0, 958)")

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
        # cursor.reset_actions()
        cursor.move_to_element(l_about).perform()
        # cursor.reset_actions()
        cursor.move_to_element(l_service).perform()
        # cursor.reset_actions()
        cursor.move_to_element(l_blog).perform()
        # cursor.reset_actions()
        cursor.move_to_element(l_faq).perform()
        # cursor.reset_actions()
        cursor.move_to_element(l_contact).perform()
        # cursor.reset_actions()
        cursor.move_to_element(l_button).perform()
        cursor.reset_actions()

        if self.browser.find_element(*self.left_img).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to(0)

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
        # cursor.reset_actions()
        cursor.move_to_element(r_about).perform()
        # cursor.reset_actions()
        cursor.move_to_element(r_service).perform()
        # cursor.reset_actions()
        cursor.move_to_element(r_blog).perform()
        # cursor.reset_actions()
        cursor.move_to_element(r_faq).perform()
        # cursor.reset_actions()
        cursor.move_to_element(r_contact).perform()
        # cursor.reset_actions()
        cursor.move_to_element(r_button).perform()
        cursor.reset_actions()

        if self.browser.find_element(*self.right_img).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to(0)

        self.browser.find_element(*self.blank).click()






