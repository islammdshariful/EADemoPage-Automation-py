from utils.config import *


class WooProductCarousel(BasePage, Helper):
    widget = '//*[@id="post-266120"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Woo Product Carousel'
    doc_link = '//*[@id="post-266120"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "WOO PRODUCT CAROUSEL"

    p_1_title = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[4]/div/div[2]/div[1]/div[1]/h2')
    p_1_ratings = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[4]/div/div[2]/div[1]/div[2]')
    p_1_price = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[4]/div/div[2]/div[2]/span')
    p_1_cart_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[4]/div/div[1]/div[2]/ul/li[1]')
    p_1_quickview_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[4]/div/div[1]/div[2]/ul/li[2]')
    p_1_link_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[4]/div/div[1]/div[2]/ul/li[3]')
    p_1_img = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[4]/div/div[1]/div[1]/img')

    p_2_title = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[5]/div/div[2]/div[1]/div[1]/h2')
    p_2_ratings = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[5]/div/div[2]/div[1]/div[2]')
    p_2_price = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[5]/div/div[2]/div[2]/span')
    p_2_cart_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[5]/div/div[1]/div[2]/ul/li[1]')
    p_2_quickview_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[5]/div/div[1]/div[2]/ul/li[2]')
    p_2_link_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[5]/div/div[1]/div[2]/ul/li[3]')
    p_2_img = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[5]/div/div[1]/div[1]/img')

    p_3_title = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[6]/div/div[2]/div[1]/div[1]/h2')
    p_3_ratings = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[6]/div/div[2]/div[1]/div[2]')
    p_3_price = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[6]/div/div[2]/div[2]/span')
    p_3_cart_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[6]/div/div[1]/div[2]/ul/li[1]')
    p_3_quickview_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[6]/div/div[1]/div[2]/ul/li[2]')
    p_3_link_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[6]/div/div[1]/div[2]/ul/li[3]')
    p_3_img = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[6]/div/div[1]/div[1]/img')

    p_4_title = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[7]/div/div[2]/div[1]/div[1]/h2')
    p_4_ratings = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[7]/div/div[2]/div[1]/div[2]')
    p_4_price = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[7]/div/div[2]/div[2]/span')
    p_4_cart_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[7]/div/div[1]/div[2]/ul/li[1]')
    p_4_quickview_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[7]/div/div[1]/div[2]/ul/li[2]')
    p_4_link_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[7]/div/div[1]/div[2]/ul/li[3]')
    p_4_img = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[7]/div/div[1]/div[1]/img')

    prev_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[4]')
    next_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[3]')

    dot_1 = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[2]/span[1]')
    dot_2 = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[2]/span[2]')
    dot_3 = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[2]/span[3]')
    dot_4 = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[2]/span[4]')

    item_name = (By.XPATH, f'/html/body/div[1]/div/div/div/main/div[2]/div[2]/h1')

    p_1_title_text = "Mens Trendy T Shirt"
    p_1_ratings_text = "Rated 4.00 out of 5"
    p_1_price_text = "£35.00"

    p_2_title_text = "Mens Stylish Shirt"
    p_2_ratings_text = "Rated 3.50 out of 5"
    p_2_price_text = "£75.00"

    p_3_title_text = "Mens Comfy T Shirt"
    p_3_ratings_text = "Rated 3.00 out of 5"
    p_3_price_text = "£20.00"

    p_4_title_text = "Mens Black Shirt"
    p_4_ratings_text = "Rated 5.00 out of 5"
    p_4_price_text = "£45.00"

    scroll = (By.XPATH, f'//*[@id="post-266120"]/div/div/div/div/section[2]/div/div/div/div/div/section'
                        f'/div/div/div/div/div/div[2]/div/p')

    def __init__(self, browser):
        super().__init__(browser)

    def check_product_info(self, img, title, title_text, price, price_text, ratings, ratings_text,
                           cart_btn, link_btn, qv_btn, dot):
        self.do_click(self.dot_4, click_after_wait='yes')
        self.do_click(dot, click_after_wait='yes')
        self.move_cursor_to(img)
        self.cursor.move_to_element(self.get_element(cart_btn)).\
            move_to_element(self.get_element(qv_btn)).\
            move_to_element(self.get_element(link_btn)).perform()

        self.do_click(dot, click_after_wait='yes')
        assert_that(self.get_element(ratings).get_attribute('aria-label')).is_equal_to(ratings_text)
        self.check_text_matches_with(title, title_text)
        self.check_text_matches_with(price, price_text)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.woo_product_carousel)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to_element(self.scroll)
                self.check_product_info(self.p_1_img, self.p_1_title, self.p_1_title_text, self.p_1_price,
                                        self.p_1_price_text, self.p_1_ratings, self.p_1_ratings_text,
                                        self.p_1_cart_btn, self.p_1_link_btn, self.p_1_quickview_btn, self.dot_1)

                self.check_product_info(self.p_2_img, self.p_2_title, self.p_2_title_text, self.p_2_price,
                                        self.p_2_price_text, self.p_2_ratings, self.p_2_ratings_text,
                                        self.p_2_cart_btn, self.p_2_link_btn, self.p_2_quickview_btn, self.dot_2)

                self.check_product_info(self.p_3_img, self.p_3_title, self.p_3_title_text, self.p_3_price,
                                        self.p_3_price_text, self.p_3_ratings, self.p_3_ratings_text,
                                        self.p_3_cart_btn, self.p_3_link_btn, self.p_3_quickview_btn, self.dot_3)

                self.check_product_info(self.p_4_img, self.p_4_title, self.p_4_title_text, self.p_4_price,
                                        self.p_4_price_text, self.p_4_ratings, self.p_4_ratings_text,
                                        self.p_4_cart_btn, self.p_4_link_btn, self.p_4_quickview_btn, self.dot_4)

                self.scroll_to(1103)
                self.do_click(self.prev_btn, click_after_wait='yes')
                self.scroll_to_element(self.scroll)
                self.do_click(self.next_btn, click_after_wait='yes')
                self.move_cursor_to(self.p_3_img)
                self.do_click(self.p_3_link_btn)
                self.check_text_matches_with(self.item_name, self.p_3_title_text)

                self.go_back()
                self.scroll_to(1103)
                self.do_click(self.dot_3, click_after_wait='yes')
