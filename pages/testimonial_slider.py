from pages.basepage import BasePage
from utils.config import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestimonialSlider(BasePage, Helper):
    widget = '//*[@id="post-1053"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Testimonial Slider'
    doc_link = "//span[contains(text(),'Documentation')]"
    doc_name = "TESTIMONIAL SLIDER"

    prev_button = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[3]')
    next_button = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[2]')

    slide_1_img = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[3]/div/div[1]/figure/img')
    slide_1_quote = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[3]/div/div[2]/span')
    slide_1_des = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[3]/div/div[2]/div')
    slide_1_rate = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[3]/div/div[2]/ul')
    slide_1_name = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[3]/div/div[2]/p[1]')
    slide_1_com = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[3]/div/div[2]/p[2]')

    slide_2_img = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[1]/figure/img')
    slide_2_quote = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[2]/span')
    slide_2_des = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[2]/div')
    slide_2_rate = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[2]/ul')
    slide_2_name = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[2]/p[1]')
    slide_2_com = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[2]/p[2]')

    slide_des_text = "GEMs are robotics algorithm for modules that built & optimized for NVIDIA AGX Data should" \
                     " underlie every business decision. Data should underlie every business Yet too often some " \
                     "very down the certain routes."
    slide_name_text = "John Doe"
    slide_com_text = "Codetic"

    def __init__(self, browser):
        super().__init__(browser)

    def check_slider(self, img, quote, des, name, com):
        self.is_visible(img, "Slider Image is not visible.")
        self.is_visible(quote, "Slider Quote icon is not visible")

        self.check_text_matches_with(des, self.slide_des_text)
        self.is_visible(self.slide_1_rate, "Slider Rating icons are not visible")

        self.check_text_matches_with(name, self.slide_name_text)
        self.check_text_matches_with(com, self.slide_com_text)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.testimonial_slider)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(2191)
                """Check navigation"""
                self.do_click(self.prev_button)
                time.sleep(1)
                self.do_click(self.next_button)

                self.check_slider(self.slide_1_img, self.slide_1_quote, self.slide_1_des, self.slide_1_name,
                                  self.slide_1_com)
                self.do_click(self.next_button)
                time.sleep(1)
                self.check_slider(self.slide_2_img, self.slide_2_quote, self.slide_2_des, self.slide_2_name,
                                  self.slide_2_com)
