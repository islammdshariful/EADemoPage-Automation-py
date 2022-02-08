from selenium.webdriver import ActionChains, Keys

from utils.config import *


class InteractivePromo(Helper):
    widget = '//*[@id="post-19"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Interactive Promo'
    doc_link = '//*[@id="post-19"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "INTERACTIVE PROMO"

    promo_1 = (By.XPATH, f'//*[@id="eael-promo-696e3946"]/figure/figcaption/a')
    promo_1_img = f'//*[@id="eael-promo-696e3946"]/figure/img'
    promo_1_title = (By.XPATH, f'//*[@id="eael-promo-696e3946"]/figure/figcaption/div/h2')
    promo_1_title_text = "It’S A Pleasure"
    promo_1_des = f'//*[@id="eael-promo-696e3946"]/figure/figcaption/div/p'
    promo_1_des_text = "We Have Only One Earth To Dwell, Don’T Destroy The Nature And Don’T Make It Hell."

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.interactive_promo)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 905)")
                time.sleep(1)

                cursor = ActionChains(self.browser)
                promo = self.browser.find_element(*self.promo_1)
                self.check_visibility(self.promo_1_img, "Image not visible.")
                assert_that(self.browser.find_element(*self.promo_1_title).text).is_equal_to(self.promo_1_title_text)
                cursor.move_to_element(promo).perform()
                time.sleep(1)
                self.check_visibility(self.promo_1_des, "Description not visible.")
