from selenium.webdriver import ActionChains, Keys

from pages.basepage import BasePage
from utils.config import *


class Testimonial(BasePage, Helper):
    widget = '//*[@id="post-1020"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section[1]' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Testimonials'
    doc_link = '//*[@id="post-1020"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section[1]' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "TESTIMONIAL"

    des = (By.XPATH, f'//*[@id="eael-testimonial-5799b0f7"]/div/div[1]/p')
    des_text = "GEMs are robotics algorithm for modules that built and optimized for NVIDIA AGX Data should " \
               "underlie every business decision. Data should underlie every business Yet too often some very" \
               " human cultural artifacts really lead the business down the certain routes."
    img = (By.XPATH, f'//*[@id="eael-testimonial-5799b0f7"]/div/div[2]/figure/img')
    name = (By.XPATH, f'//*[@id="eael-testimonial-5799b0f7"]/div/div[3]/p[1]')
    name_text = "Alison Burgas"
    com = (By.XPATH, f'//*[@id="eael-testimonial-5799b0f7"]/div/div[3]/p[2]')
    com_text = "Product Designer @microsoft"
    rate = (By.XPATH, f'//*[@id="eael-testimonial-5799b0f7"]/div/ul')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.testimonials)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(852)

                """Testimonial info"""
                self.check_text_matches_with(self.des, self.des_text)
                self.check_text_matches_with(self.name, self.name_text)
                self.check_text_matches_with(self.com, self.com_text)
                self.is_visible(self.img, "Image is not visible")
                self.is_visible(self.rate, "Rate is not visible")
