from selenium.webdriver import ActionChains

from utils.config import *


class StaticProduct:
    PAGE_TITLE_TEXT = "Static Product | Essential Addons for Elementor"
    DOC_LINK = '//*[@id="post-1521"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/' \
               'section/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "STATIC PRODUCT"

    first_product_thumb = (By.XPATH, f'//*[@id="eael-static-product-7808a0d7"]/div[1]/div[1]')
    first_product_des = (By.XPATH, f'//*[@id="eael-static-product-7808a0d7"]/div[2]/h2/a')
    first_product_des_text = "Introducing Analytics NotificationX Now You Can Measure Your Social Proof ROI"
    first_product_rate_price = (By.XPATH, f'//*[@id="eael-static-product-7808a0d7"]/div[2]/p')
    first_product_rate_price_text = "$77.5 (45 reviews)"
    first_product_button = (By.XPATH, f'//*[@id="eael-static-product-7808a0d7"]/div[2]/div/a/span')
    first_product_button_text = "Learn More"

    second_product_thumb = (By.XPATH, f'//*[@id="eael-static-product-43a6a972"]/div[1]/div[1]/a')
    second_product_thumb_text = "$77.5"
    second_product_name = (By.XPATH, f'//*[@id="eael-static-product-43a6a972"]/div[2]/h2/a')
    second_product_name_text = "Creative Artist"
    second_product_des = (By.XPATH, f'//*[@id="eael-static-product-43a6a972"]/div[2]/p')
    second_product_des_text = "Netflix has struck a deal set permanent production base Shepperton Studios from Alien Mary Poppins Returns"
    second_product_button = (By.XPATH, f'//*[@id="eael-static-product-43a6a972"]/div[2]/div/a/span')
    second_product_button_text = "Explore More"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(static_product)

    def testcase(self):

        with soft_assertions():
            assert_that(self.browser.title).is_equal_to(self.PAGE_TITLE_TEXT)

            doc = Documentation(self.browser)
            if check_doc:
                doc.check_doc(self.DOC_LINK, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1126)")

            cursor = ActionChains(self.browser)

            first_product = self.browser.find_element(*self.first_product_thumb)
            first_product_button = self.browser.find_element(*self.first_product_button)

            second_product = self.browser.find_element(*self.second_product_thumb)
            second_product_button = self.browser.find_element(*self.second_product_button)

            cursor.move_to_element(first_product).perform()
            assert_that(self.browser.find_element(*self.first_product_des).text).is_equal_to(self.first_product_des_text)
            assert_that(self.browser.find_element(*self.first_product_rate_price).text).\
                is_equal_to(self.first_product_rate_price_text)
            cursor.move_to_element(first_product_button).perform()
            assert_that(self.browser.find_element(*self.first_product_button).text).\
                is_equal_to(self.first_product_button_text)

            self.browser.execute_script("window.scrollTo(0, 2762)")
            cursor.move_to_element(second_product).perform()

            if self.browser.find_element(*self.second_product_thumb).is_displayed():
                assert_that(self.browser.find_element(*self.second_product_thumb).text). \
                    is_equal_to(self.second_product_thumb_text)

            assert_that(self.browser.find_element(*self.second_product_name).text).\
                is_equal_to(self.second_product_name_text)

            assert_that(self.browser.find_element(*self.second_product_des).text).\
                is_equal_to(self.second_product_des_text)

            cursor.move_to_element(second_product_button).perform()
            assert_that(self.browser.find_element(*self.second_product_button).text).\
                is_equal_to(self.second_product_button_text)


