from pages.basepage import BasePage
from utils.config import *


class StaticProduct(BasePage, Helper):
    widget = '//*[@id="post-1521"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = "Static Product"
    doc_link = '//*[@id="post-1521"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/' \
               'section/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "STATIC PRODUCT"

    first_product_thumb = (By.XPATH, f'//*[@id="eael-static-product-7808a0d7"]/div[1]/div[2]/img')
    first_product_des = (By.XPATH, f'//*[@id="eael-static-product-7808a0d7"]/div[2]/h2/a')
    first_product_des_text = "Introducing Analytics NotificationX Now You Can Measure Your Social Proof ROI"
    first_product_rate_price = (By.XPATH, f'//*[@id="eael-static-product-7808a0d7"]/div[2]/p')
    first_product_rate_price_text = "$77.5 (45 reviews)"
    first_product_button = (By.XPATH, f'//*[@id="eael-static-product-7808a0d7"]/div[2]/div/a/span')
    first_product_button_text = "Learn More"

    second_product_thumb = (By.XPATH, f'//*[@id="eael-static-product-43a6a972"]/div[1]/div[2]/img')
    second_product_price = (By.XPATH, f'//*[@id="eael-static-product-43a6a972"]/div[1]/div[1]/a/span')
    second_product_price_text = "$77.5"
    second_product_name = (By.XPATH, f'//*[@id="eael-static-product-43a6a972"]/div[2]/h2/a')
    second_product_name_text = "Creative Artist"
    second_product_des = (By.XPATH, f'//*[@id="eael-static-product-43a6a972"]/div[2]/p')
    second_product_des_text = "Netflix has struck a deal set permanent production base Shepperton Studios from Alien " \
                              "Mary Poppins Returns"
    second_product_button = (By.XPATH, f'//*[@id="eael-static-product-43a6a972"]/div[2]/div/a/span')
    second_product_button_text = "Explore More"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.static_product)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1126)
                """move cursor to product"""
                self.move_cursor_to(self.first_product_thumb)
                """product description"""
                self.check_text_matches_with(self.first_product_des, self.first_product_des_text)
                self.check_text_matches_with(self.first_product_rate_price, self.first_product_rate_price_text)
                """product button"""
                self.move_cursor_to(self.first_product_button)
                self.check_text_matches_with(self.first_product_button, self.first_product_button_text)
                """move cursor to product"""
                self.scroll_to(2759)
                self.move_cursor_to(self.second_product_thumb)
                """product description"""
                if self.is_displaying(*self.second_product_thumb):
                    self.check_text_matches_with(self.second_product_price, self.second_product_price_text)
                self.check_text_matches_with(self.second_product_name, self.second_product_name_text)
                self.check_text_matches_with(self.second_product_des, self.second_product_des_text)
                """product button"""
                self.move_cursor_to(self.second_product_button)
                self.check_text_matches_with(self.second_product_button, self.second_product_button_text)
