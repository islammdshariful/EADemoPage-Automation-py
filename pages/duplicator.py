from selenium.webdriver import ActionChains

from utils.config import *


class Duplicator:
    widget = '//*[@id="page"]/div[1]/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Post Duplicator'
    doc_link = '//*[@id="page"]/div[1]/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]/div/div' \
               '/div[3]/div/div/a/span/span'
    doc_name = "EA DUPLICATOR"

    img_1 = f'//*[@id="page"]/div[1]/div/div/section[2]/div/div/div/div/div/section[2]/div/div/div/div' \
                       f'/div/div/div/div/img'

    img_2 = f'//*[@id="page"]/div[1]/div/div/section[3]/div/div/div/div/div/section[2]/div/div/div/div' \
                       f'/div/div/div/div/img'

    img_3 = f'//*[@id="page"]/div[1]/div/div/section[4]/div/div/div/div/div/section[2]/div/div/div/div' \
                       f'/div/div/div/div/img'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(duplicator)

    def check_visibility(self, img):
        if self.browser.find_element(By.XPATH, img).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Image is not visible")

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1003)")

            self.check_visibility(self.img_1)
            self.browser.execute_script("window.scrollTo(0, 1938)")
            self.check_visibility(self.img_2)
            self.browser.execute_script("window.scrollTo(0, 2958)")
            self.check_visibility(self.img_3)
