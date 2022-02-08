from selenium.webdriver import Keys

from utils.config import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestimonialSlider(Helper):
    widget = '//*[@id="post-1053"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Testimonial Slider'
    doc_link = "//span[contains(text(),'Documentation')]"
    doc_name = "TESTIMONIAL SLIDER"

    prev_button = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[3]')
    next_button = (By.XPATH, f'//*[@id="eael-testimonial-695ee53e"]/div/div[2]')

    slide_1_img = f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[3]/div/div[1]/figure/img'
    slide_1_quote = f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[3]/div/div[2]/span'
    slide_1_des = f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[3]/div/div[2]/div/p'
    slide_1_rate = f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[3]/div/div[2]/ul'
    slide_1_name = f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[3]/div/div[2]/p[1]'
    slide_1_com = f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[3]/div/div[2]/p[2]'

    slide_2_img = f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[1]/figure/img'
    slide_2_quote = f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[2]/span'
    slide_2_des = f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[2]/div/p'
    slide_2_rate = f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[2]/ul'
    slide_2_name = f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[2]/p[1]'
    slide_2_com = f'//*[@id="eael-testimonial-695ee53e"]/div/div[1]/div[4]/div/div[2]/p[2]'

    slide_des_text = "GEMs are robotics algorithm for modules that built & optimized for NVIDIA AGX Data should" \
                     " underlie every business decision. Data should underlie every business Yet too often some " \
                     "very down the certain routes."
    slide_name_text = "John Doe"
    slide_com_text = "Codetic"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.testimonial_slider)

    def check_slider(self, img, quote, des, name, com):
        self.check_visibility(img, "Slider 1 Image is not visible.")
        self.browser.find_element(*self.prev_button).click()
        time.sleep(1)
        self.browser.find_element(*self.next_button).click()
        self.check_visibility(quote, "Slider 1 Quote icon is not visible")

        assert_that(self.browser.find_element(By.XPATH, des).text).is_equal_to(self.slide_des_text)

        self.check_visibility(self.slide_1_rate, "Slider 1 Rating icons are not visible")

        assert_that(self.browser.find_element(By.XPATH, name).text).is_equal_to(self.slide_name_text)
        assert_that(self.browser.find_element(By.XPATH, com).text).is_equal_to(self.slide_com_text)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 2191)")
                time.sleep(1)

                WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.slide_1_img)))
                self.check_slider(self.slide_1_img, self.slide_1_quote, self.slide_1_des, self.slide_1_name,
                                  self.slide_1_com)
