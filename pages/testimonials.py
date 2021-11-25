from selenium.webdriver import ActionChains

from utils.config import *


class Testimonial:
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
        self.browser = browser

    def load(self):
        self.browser.get(testimonials)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1001)")

            assert_that(self.browser.find_element(*self.des).text).is_equal_to(self.des_text)
            assert_that(self.browser.find_element(*self.name).text).is_equal_to(self.name_text)
            assert_that(self.browser.find_element(*self.com).text).is_equal_to(self.com_text)

            if self.browser.find_element(*self.img).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to(0)

            if self.browser.find_element(*self.rate).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to(0)
