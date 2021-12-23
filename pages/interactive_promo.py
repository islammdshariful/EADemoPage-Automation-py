from selenium.webdriver import ActionChains

from utils.config import *


class InteractivePromo:
    widget = '//*[@id="post-19"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Interactive Promo'
    doc_link = '//*[@id="post-19"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "INTERACTIVE PROMO"

    promo_1 = (By.XPATH, f'//*[@id="eael-promo-696e3946"]/figure/figcaption/a')
    promo_1_img = (By.XPATH, f'//*[@id="eael-promo-696e3946"]/figure/img')
    promo_1_title = (By.XPATH, f'//*[@id="eael-promo-696e3946"]/figure/figcaption/div/h2')
    promo_1_title_text = "It’S A Pleasure"
    promo_1_des = (By.XPATH, f'//*[@id="eael-promo-696e3946"]/figure/figcaption/div/p')
    promo_1_des_text = "We Have Only One Earth To Dwell, Don’T Destroy The Nature And Don’T Make It Hell."

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(interactive_promo)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 905)")
            cursor = ActionChains(self.browser)
            promo = self.browser.find_element(*self.promo_1)

            if self.browser.find_element(*self.promo_1_img).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to("Image not visible")
            assert_that(self.browser.find_element(*self.promo_1_title).text).is_equal_to(self.promo_1_title_text)
            cursor.move_to_element(promo).perform()
            if self.browser.find_element(*self.promo_1_des).is_displayed():
                assert_that(self.browser.find_element(*self.promo_1_des).text).is_equal_to(self.promo_1_des_text)
            else:
                assert_that(display).is_equal_to("Description not visible")
