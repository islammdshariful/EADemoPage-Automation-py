from utils.config import *


class WooProductSlider(BasePage, Helper):
    widget = '//*[@id="post-266629"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Woo Product Slider'
    doc_link = '//*[@id="post-266629"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "WOO PRODUCT SLIDER"

    p_1_title = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[4]/div/div[1]/div/div[1]/h2')
    p_1_ratings = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[4]/div/div[1]/div/div[2]')
    p_1_price = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[4]/div/div[1]/div/div[3]/span/bdi')
    p_1_cart_btn = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[4]/div/div[1]/ul/li[1]/a')
    p_1_link_btn = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[4]/div/div[1]/ul/li[2]/a')
    p_1_tag_1 = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[4]/div/div[1]/div/ul/li/a[1]')
    p_1_tag_2 = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[4]/div/div[1]/div/ul/li/a[2]')
    p_1_img = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[4]/div/div[2]/div/img')

    p_2_title = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[5]/div/div[1]/div/div[1]/h2')
    p_2_ratings = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[5]/div/div[1]/div/div[2]')
    p_2_price = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[5]/div/div[1]/div/div[3]/span/bdi')
    p_2_cart_btn = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[5]/div/div[1]/ul/li[1]/a')
    p_2_link_btn = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[5]/div/div[1]/ul/li[2]/a')
    p_2_tag_1 = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[5]/div/div[1]/div/ul/li/a[1]')
    p_2_tag_2 = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[5]/div/div[1]/div/ul/li/a[2]')
    p_2_img = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[5]/div/div[2]/div/img')

    p_3_title = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[6]/div/div[1]/div/div[1]/h2')
    p_3_ratings = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[6]/div/div[1]/div/div[2]')
    p_3_price = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[6]/div/div[1]/div/div[3]/span/bdi')
    p_3_cart_btn = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[6]/div/div[1]/ul/li[1]/a')
    p_3_link_btn = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[6]/div/div[1]/ul/li[2]/a')
    p_3_tag_1 = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[6]/div/div[1]/div/ul/li/a[1]')
    p_3_tag_2 = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[6]/div/div[1]/div/ul/li/a[2]')
    p_3_img = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[6]/div/div[2]/div/img')

    p_4_title = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[7]/div/div[1]/div/div[1]/h2')
    p_4_ratings = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[7]/div/div[1]/div/div[2]')
    p_4_price = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[7]/div/div[1]/div/div[3]/span/bdi')
    p_4_cart_btn = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[7]/div/div[1]/ul/li[1]/a')
    p_4_link_btn = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[7]/div/div[1]/ul/li[2]/a')
    p_4_tag_1 = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[7]/div/div[1]/div/ul/li/a[1]')
    p_4_tag_2 = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[7]/div/div[1]/div/ul/li/a[2]')
    p_4_img = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[1]/ul/li[7]/div/div[2]/div/img')

    prev_btn = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[4]')
    next_btn = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[3]')

    dot_1 = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[2]/span[1]')
    dot_2 = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[2]/span[2]')
    dot_3 = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[2]/span[3]')
    dot_4 = (By.XPATH, f'//*[@id="eael-product-slider-349931a"]/div[2]/span[4]')

    item_name = (By.XPATH, f'/html/body/div[1]/div/div/div/main/div[2]/div[2]/h1')

    p_1_title_text = "Mens Trendy T Shirt"
    p_1_ratings_text = "Rated 4.00 out of 5"
    p_1_price_text = "£35.00"
    p_1_tag_1_text = "Fashion"
    p_1_tag_2_text = "Men"

    p_2_title_text = "Mens Stylish Shirt"
    p_2_ratings_text = "Rated 3.50 out of 5"
    p_2_price_text = "£75.00"
    p_2_tag_1_text = "Fashion"
    p_2_tag_2_text = "Men"

    p_3_title_text = "Mens Comfy T Shirt"
    p_3_ratings_text = "Rated 3.00 out of 5"
    p_3_price_text = "£20.00"
    p_3_tag_1_text = "Fashion"
    p_3_tag_2_text = "Men"

    p_4_title_text = "Mens Black Shirt"
    p_4_ratings_text = "Rated 5.00 out of 5"
    p_4_price_text = "£45.00"
    p_4_tag_1_text = "Fashion"
    p_4_tag_2_text = "Men"

    def __init__(self, browser):
        super().__init__(browser)

    def check_product_info(self, title, title_text, price, price_text, tag_1, tag_1_text, tag_2, tag_2_text, ratings,
                           ratings_text, cart_btn, link_btn):
        self.check_text_matches_with(title, title_text)
        self.does_element_has_text(price, price_text)
        self.check_text_matches_with(tag_1, tag_1_text)
        self.check_text_matches_with(tag_2, tag_2_text)
        assert_that(self.get_element(ratings).get_attribute('aria-label')).is_equal_to(ratings_text)
        self.move_cursor_to(cart_btn)
        self.move_cursor_and_click(cart_btn)
        self.move_cursor_to(link_btn)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.woo_product_slider)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1070)

                self.check_product_info(self.p_1_title, self.p_1_title_text, self.p_1_price, self.p_1_price_text,
                                        self.p_1_tag_1, self.p_1_tag_1_text, self.p_1_tag_2, self.p_1_tag_2_text,
                                        self.p_1_ratings, self.p_1_ratings_text, self.p_1_cart_btn, self.p_1_link_btn)
                self.do_click(self.next_btn)

                self.check_product_info(self.p_2_title, self.p_2_title_text, self.p_2_price, self.p_2_price_text,
                                        self.p_2_tag_1, self.p_2_tag_1_text, self.p_2_tag_2, self.p_2_tag_2_text,
                                        self.p_2_ratings, self.p_2_ratings_text, self.p_2_cart_btn, self.p_2_link_btn)
                self.do_click(self.next_btn)

                self.check_product_info(self.p_3_title, self.p_3_title_text, self.p_3_price, self.p_3_price_text,
                                        self.p_3_tag_1, self.p_3_tag_1_text, self.p_3_tag_2, self.p_3_tag_2_text,
                                        self.p_3_ratings, self.p_3_ratings_text, self.p_3_cart_btn, self.p_3_link_btn)
                self.do_click(self.next_btn)

                self.check_product_info(self.p_4_title, self.p_4_title_text, self.p_4_price, self.p_4_price_text,
                                        self.p_4_tag_1, self.p_4_tag_1_text, self.p_4_tag_2, self.p_4_tag_2_text,
                                        self.p_4_ratings, self.p_4_ratings_text, self.p_4_cart_btn, self.p_4_link_btn)
                self.do_click(self.prev_btn)

                self.do_click(self.prev_btn)

                self.do_click(self.prev_btn)

                self.do_click(self.dot_2)
                self.do_click(self.p_2_link_btn)
                self.check_text_matches_with(self.item_name, self.p_2_title_text)

                self.go_back()
                self.scroll_to(1070)
                self.do_click(self.dot_1)

                self.do_click(self.dot_2)

                self.do_click(self.dot_3)

                self.do_click(self.dot_4)


