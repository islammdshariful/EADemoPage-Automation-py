from utils.config import *


class ImageAccordion(BasePage, Helper):
    widget = '//*[@id="post-2324"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Image Accordion'
    doc_link = '//*[@id="post-2324"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "IMAGE ACCORDION"

    h_accor_1 = (By.XPATH, f'//*[@id="eael-img-accordion-156c3de2"]/a[1]')
    h_accor_2 = (By.XPATH, f'//*[@id="eael-img-accordion-156c3de2"]/a[2]')
    h_accor_3 = (By.XPATH, f'//*[@id="eael-img-accordion-156c3de2"]/a[3]')
    h_accor_4 = (By.XPATH, f'//*[@id="eael-img-accordion-156c3de2"]/a[4]')
    h_accor_5 = (By.XPATH, f'//*[@id="eael-img-accordion-156c3de2"]/a[5]')

    h_accor_1_head = (By.XPATH, f'//*[@id="eael-img-accordion-156c3de2"]/a[1]/div/div/div/h2')
    h_accor_2_head = (By.XPATH, f'//*[@id="eael-img-accordion-156c3de2"]/a[2]/div/div/div/h2')
    h_accor_3_head = (By.XPATH, f'//*[@id="eael-img-accordion-156c3de2"]/a[3]/div/div/div/h2')
    h_accor_4_head = (By.XPATH, f'//*[@id="eael-img-accordion-156c3de2"]/a[4]/div/div/div/h2')
    h_accor_5_head = (By.XPATH, f'//*[@id="eael-img-accordion-156c3de2"]/a[5]/div/div/div/h2')

    h_accor_1_des = (By.XPATH, f'//*[@id="eael-img-accordion-156c3de2"]/a[1]/div/div/div/p')
    h_accor_2_des = (By.XPATH, f'//*[@id="eael-img-accordion-156c3de2"]/a[2]/div/div/div/p[2]')
    h_accor_3_des = (By.XPATH, f'//*[@id="eael-img-accordion-156c3de2"]/a[3]/div/div/div/p[2]')
    h_accor_4_des = (By.XPATH, f'//*[@id="eael-img-accordion-156c3de2"]/a[4]/div/div/div/p[2]')
    h_accor_5_des = (By.XPATH, f'//*[@id="eael-img-accordion-156c3de2"]/a[5]/div/div/div/p[2]')

    c_accor_1 = (By.XPATH, f'//*[@id="eael-img-accordion-12eebae2"]/a[1]')
    c_accor_2 = (By.XPATH, f'//*[@id="eael-img-accordion-12eebae2"]/a[2]')
    c_accor_3 = (By.XPATH, f'//*[@id="eael-img-accordion-12eebae2"]/a[3]')
    c_accor_4 = (By.XPATH, f'//*[@id="eael-img-accordion-12eebae2"]/a[4]')
    c_accor_5 = (By.XPATH, f'//*[@id="eael-img-accordion-12eebae2"]/a[5]')

    c_accor_1_head = (By.XPATH, f'//*[@id="eael-img-accordion-12eebae2"]/a[1]/div/div/div/h2')
    c_accor_2_head = (By.XPATH, f'//*[@id="eael-img-accordion-12eebae2"]/a[2]/div/div/div/h2')
    c_accor_3_head = (By.XPATH, f'//*[@id="eael-img-accordion-12eebae2"]/a[3]/div/div/div/h2')
    c_accor_4_head = (By.XPATH, f'//*[@id="eael-img-accordion-12eebae2"]/a[4]/div/div/div/h2')
    c_accor_5_head = (By.XPATH, f'//*[@id="eael-img-accordion-12eebae2"]/a[5]/div/div/div/h2')

    c_accor_1_des = (By.XPATH, f'//*[@id="eael-img-accordion-12eebae2"]/a[1]/div/div/div/p')
    c_accor_2_des = (By.XPATH, f'//*[@id="eael-img-accordion-12eebae2"]/a[2]/div/div/div/p[2]')
    c_accor_3_des = (By.XPATH, f'//*[@id="eael-img-accordion-12eebae2"]/a[3]/div/div/div/p[2]')
    c_accor_4_des = (By.XPATH, f'//*[@id="eael-img-accordion-12eebae2"]/a[4]/div/div/div/p[2]')
    c_accor_5_des = (By.XPATH, f'//*[@id="eael-img-accordion-12eebae2"]/a[5]/div/div/div/p[2]')

    def __init__(self, browser):
        super().__init__(browser)

    def check_accordion_by_hover(self, accordion, header, des):
        self.move_cursor_to(accordion)
        self.is_visible(header, "Header is not visible.")
        self.is_visible(des, "Description is not visible.")

    def check_accordion_by_click(self, accordion, header, des):
        self.do_click(accordion)
        self.is_visible(header, "Header is not visible.")
        self.is_visible(des, "Description is not visible.")

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.image_accordion)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(974)
                self.check_accordion_by_hover(self.h_accor_1, self.h_accor_1_head, self.h_accor_1_des)
                self.check_accordion_by_hover(self.h_accor_2, self.h_accor_2_head, self.h_accor_2_des)
                self.check_accordion_by_hover(self.h_accor_3, self.h_accor_3_head, self.h_accor_3_des)
                self.check_accordion_by_hover(self.h_accor_4, self.h_accor_4_head, self.h_accor_4_des)
                self.check_accordion_by_hover(self.h_accor_5, self.h_accor_5_head, self.h_accor_5_des)

                self.scroll_to(2579)
                self.check_accordion_by_click(self.c_accor_1, self.c_accor_1_head, self.c_accor_1_des)
                self.check_accordion_by_click(self.c_accor_2, self.c_accor_2_head, self.c_accor_2_des)
                self.check_accordion_by_click(self.c_accor_3, self.c_accor_3_head, self.c_accor_3_des)
                self.check_accordion_by_click(self.c_accor_4, self.c_accor_4_head, self.c_accor_4_des)
                self.check_accordion_by_click(self.c_accor_5, self.c_accor_5_head, self.c_accor_5_des)






