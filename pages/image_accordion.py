import time

from selenium.webdriver import ActionChains

from utils.config import *


class ImageAccordion:
    widget = '//*[@id="post-2324"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Image Accordion'
    doc_link = '//*[@id="post-2324"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "IMAGE ACCORDION"

    h_accor_1 = f'//*[@id="eael-img-accordion-156c3de2"]/a[1]'
    h_accor_2 = f'//*[@id="eael-img-accordion-156c3de2"]/a[2]'
    h_accor_3 = f'//*[@id="eael-img-accordion-156c3de2"]/a[3]'
    h_accor_4 = f'//*[@id="eael-img-accordion-156c3de2"]/a[4]'
    h_accor_5 = f'//*[@id="eael-img-accordion-156c3de2"]/a[5]'

    h_accor_1_head = f'//*[@id="eael-img-accordion-156c3de2"]/a[1]/div/div/div/h2'
    h_accor_2_head = f'//*[@id="eael-img-accordion-156c3de2"]/a[2]/div/div/div/h2'
    h_accor_3_head = f'//*[@id="eael-img-accordion-156c3de2"]/a[3]/div/div/div/h2'
    h_accor_4_head = f'//*[@id="eael-img-accordion-156c3de2"]/a[4]/div/div/div/h2'
    h_accor_5_head = f'//*[@id="eael-img-accordion-156c3de2"]/a[5]/div/div/div/h2'

    h_accor_1_des = f'//*[@id="eael-img-accordion-156c3de2"]/a[1]/div/div/div/p'
    h_accor_2_des = f'//*[@id="eael-img-accordion-156c3de2"]/a[2]/div/div/div/p[2]'
    h_accor_3_des = f'//*[@id="eael-img-accordion-156c3de2"]/a[3]/div/div/div/p[2]'
    h_accor_4_des = f'//*[@id="eael-img-accordion-156c3de2"]/a[4]/div/div/div/p[2]'
    h_accor_5_des = f'//*[@id="eael-img-accordion-156c3de2"]/a[5]/div/div/div/p[2]'

    c_accor_1 = f'//*[@id="eael-img-accordion-12eebae2"]/a[1]'
    c_accor_2 = f'//*[@id="eael-img-accordion-12eebae2"]/a[2]'
    c_accor_3 = f'//*[@id="eael-img-accordion-12eebae2"]/a[3]'
    c_accor_4 = f'//*[@id="eael-img-accordion-12eebae2"]/a[4]'
    c_accor_5 = f'//*[@id="eael-img-accordion-12eebae2"]/a[5]'

    c_accor_1_head = f'//*[@id="eael-img-accordion-12eebae2"]/a[1]/div/div/div/h2'
    c_accor_2_head = f'//*[@id="eael-img-accordion-12eebae2"]/a[2]/div/div/div/h2'
    c_accor_3_head = f'//*[@id="eael-img-accordion-12eebae2"]/a[3]/div/div/div/h2'
    c_accor_4_head = f'//*[@id="eael-img-accordion-12eebae2"]/a[4]/div/div/div/h2'
    c_accor_5_head = f'//*[@id="eael-img-accordion-12eebae2"]/a[5]/div/div/div/h2'

    c_accor_1_des = f'//*[@id="eael-img-accordion-12eebae2"]/a[1]/div/div/div/p'
    c_accor_2_des = f'//*[@id="eael-img-accordion-12eebae2"]/a[2]/div/div/div/p[2]'
    c_accor_3_des = f'//*[@id="eael-img-accordion-12eebae2"]/a[3]/div/div/div/p[2]'
    c_accor_4_des = f'//*[@id="eael-img-accordion-12eebae2"]/a[4]/div/div/div/p[2]'
    c_accor_5_des = f'//*[@id="eael-img-accordion-12eebae2"]/a[5]/div/div/div/p[2]'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(image_accordion)

    def check_accordion_by_hover(self, accordion, header, des):
        cursor = ActionChains(self.browser)
        element = self.browser.find_element(By.XPATH, accordion)
        cursor.move_to_element(element).perform()
        time.sleep(.5)
        if self.browser.find_element(By.XPATH, header).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Header is not visible")

        if self.browser.find_element(By.XPATH, des).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Description is not visible")

    def check_accordion_by_click(self, accordion, header, des):
        self.browser.find_element(By.XPATH, accordion).click()
        time.sleep(.5)
        if self.browser.find_element(By.XPATH, header).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Header is not visible")

        if self.browser.find_element(By.XPATH, des).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Description is not visible")

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 974)")
            self.check_accordion_by_hover(self.h_accor_1, self.h_accor_1_head, self.h_accor_1_des)
            self.check_accordion_by_hover(self.h_accor_2, self.h_accor_2_head, self.h_accor_2_des)
            self.check_accordion_by_hover(self.h_accor_3, self.h_accor_3_head, self.h_accor_3_des)
            self.check_accordion_by_hover(self.h_accor_4, self.h_accor_4_head, self.h_accor_4_des)
            self.check_accordion_by_hover(self.h_accor_5, self.h_accor_5_head, self.h_accor_5_des)

            self.browser.execute_script("window.scrollTo(0, 2579)")
            self.check_accordion_by_click(self.c_accor_1, self.c_accor_1_head, self.c_accor_1_des)
            self.check_accordion_by_click(self.c_accor_2, self.c_accor_2_head, self.c_accor_2_des)
            self.check_accordion_by_click(self.c_accor_3, self.c_accor_3_head, self.c_accor_3_des)
            self.check_accordion_by_click(self.c_accor_4, self.c_accor_4_head, self.c_accor_4_des)
            self.check_accordion_by_click(self.c_accor_5, self.c_accor_5_head, self.c_accor_5_des)






