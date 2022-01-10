from selenium.webdriver import ActionChains

from utils.config import *


class TestimonialSlider:
    widget = '//*[@id="post-1053"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Testimonial Slider'
    doc_link = "//span[contains(text(),'Documentation')]"
    doc_name = "TESTIMONIAL SLIDER"

    prev_button = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[3]')
    next_button = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[2]')

    slide_1_img = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[1]/figure/img')
    slide_1_quote = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[2]/span')
    slide_1_des = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[2]/div/p')
    slide_1_des_text = "GEMs are robotics algorithm for modules that built & optimized for NVIDIA AGX Data should" \
                       " underlie every business decision. Data should underlie every business Yet too often some " \
                       "very down the certain routes."
    slide_1_rate = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[2]/ul')
    slide_1_name = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[2]/p[1]')
    slide_1_name_text = "John Doe"
    slide_1_com = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[2]/p[2]')
    slide_1_com_text = "Codetic"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(testimonial_slider)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)
            self.browser.execute_script("window.scrollTo(0, 2191)")
            time.sleep(1)

            if self.browser.find_element(*self.slide_1_img).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to(0)

            if self.browser.find_element(*self.slide_1_quote).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to(0)

            assert_that(self.browser.find_element(*self.slide_1_des).text).is_equal_to(self.slide_1_des_text)

            if self.browser.find_element(*self.slide_1_rate).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to(0)

            assert_that(self.browser.find_element(*self.slide_1_name).text).is_equal_to(self.slide_1_name_text)
            assert_that(self.browser.find_element(*self.slide_1_com).text).is_equal_to(self.slide_1_com_text)
