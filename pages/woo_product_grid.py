from selenium.webdriver import ActionChains, Keys

from utils.config import *


class WooProductGrid(Helper):
    widget = '//*[@id="post-1161"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Woo Product Grid'
    doc_link = '//*[@id="post-1161"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "WOOCOMMERCE PRODUCT GRID"

    p_1_title = f"//div[@class='elementor-element elementor-element-7c9d163 eael-product-grid-column-4 elementor-widget" \
                f" elementor-widget-eicon-woocommerce']//h2[@class='woocommerce-loop-product__title']" \
                f"[normalize-space()='Mens Trendy T Shirt']"
    p_1_ratings = f"//div[@class='elementor-element elementor-element-7c9d163 eael-product-grid-column-4 elementor-" \
                  f"widget elementor-widget-eicon-woocommerce']//div[@aria-label='Rated 4.00 out of 5']"
    p_1_price = f"//li[1]//div[4]"
    p_1_cart_btn = f"//div[@class='button-wrap clearfix']//a[@aria-label='Add “Mens Trendy T Shirt” to your cart']" \
                   f"[normalize-space()='Add to cart']"
    p_1_vcart_btn = f"//a[normalize-space()='View cart']"
    p_1_link_btn = f"//section[@class='elementor-section elementor-top-section elementor-element elementor-element-" \
                   f"2a8ceca elementor-section-boxed elementor-section-height-default elementor-section-height-" \
                   f"default']//li[1]//div[1]//div[1]//a[1]"
    p_1_img = f"//div[@class='overlay']//img[@title='Woo Product Grid for Elementor 85']"

    p_2_title = f"//div[@class='elementor-element elementor-element-7c9d163 eael-product-grid-column-4 elementor-widget" \
                f" elementor-widget-eicon-woocommerce']//h2[@class='woocommerce-loop-product__title']" \
                f"[normalize-space()='Mens Stylish Shirt']"
    p_2_ratings = f"//div[@class='elementor-element elementor-element-7c9d163 eael-product-grid-column-4 elementor-" \
                  f"widget elementor-widget-eicon-woocommerce']//div[@aria-label='Rated 3.50 out of 5']"
    p_2_price = f"//li[2]//div[4]//span[1]//bdi[1]"
    p_2_cart_btn = f"//div[@class='button-wrap clearfix']//a[@aria-label='Add “Mens Stylish Shirt” to your cart']" \
                   f"[normalize-space()='Add to cart']"
    p_2_vcart_btn = f"//li[2]//div[1]//div[1]//a[3]"
    p_2_link_btn = f"//a[@href='https://essential-addons.com/elementor/product/mens-stylish-shirt/']" \
                   f"//span[@class='fas fa-link']"
    p_2_img = f"//div[@class='overlay']//img[@title='Woo Product Grid for Elementor 86']"

    p_3_title = f"//div[@class='elementor-element elementor-element-7c9d163 eael-product-grid-column-4 elementor-widget" \
                f" elementor-widget-eicon-woocommerce']//h2[@class='woocommerce-loop-product__title']" \
                f"[normalize-space()='Mens Comfy T Shirt']"
    p_3_ratings = f"//div[@class='elementor-element elementor-element-7c9d163 eael-product-grid-column-4 elementor-" \
                  f"widget elementor-widget-eicon-woocommerce']//div[@aria-label='Rated 3.00 out of 5']"
    p_3_price = f"//li[3]//div[4]//span[1]//bdi[1]"
    p_3_cart_btn = f"//div[@class='button-wrap clearfix']//a[@aria-label='Add “Mens Comfy T Shirt” to your cart']" \
                   f"[normalize-space()='Add to cart']"
    p_3_vcart_btn = f"//li[3]//div[1]//div[1]//a[3]"
    p_3_link_btn = f"//a[@href='https://essential-addons.com/elementor/product/mens-comfy-t-shirt/']" \
                   f"//span[@class='fas fa-link']"
    p_3_img = f"//div[@class='overlay']//img[@title='Woo Product Grid for Elementor 87']"

    p_4_title = f"//div[@class='elementor-element elementor-element-7c9d163 eael-product-grid-column-4 elementor-widget" \
                f" elementor-widget-eicon-woocommerce']//h2[@class='woocommerce-loop-product__title']" \
                f"[normalize-space()='Mens Black Shirt']"
    p_4_ratings = f"//div[@class='elementor-element elementor-element-7c9d163 eael-product-grid-column-4 elementor-" \
                  f"widget elementor-widget-eicon-woocommerce']//div[@aria-label='Rated 5.00 out of 5']"
    p_4_price = f"//li[4]//div[4]//span[1]//bdi[1]"
    p_4_cart_btn = f"//div[@class='button-wrap clearfix']//a[@aria-label='Add “Mens Black Shirt” to your cart']" \
                   f"[normalize-space()='Add to cart']"
    p_4_vcart_btn = f"//li[4]//div[1]//div[1]//a[3]"
    p_4_link_btn = f"//section[@class='elementor-section elementor-top-section elementor-element elementor-element-" \
                   f"2a8ceca elementor-section-boxed elementor-section-height-default elementor-section-height-" \
                   f"default']//li[4]//div[1]//div[1]//a[1]"
    p_4_img = f"//div[@class='overlay']//img[@title='Woo Product Grid for Elementor 88']"

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
        self.browser = browser

    def load(self):
        self.browser.get(self.woo_product_grid)

    def check_product_info(self, title, title_text, price, price_text, ratings, ratings_text, cart_btn, link_btn,
                           img, vcart_btn):
        time.sleep(1)
        assert_that(self.browser.find_element(By.XPATH, title).text).is_equal_to(title_text.upper())
        assert_that(self.browser.find_element(By.XPATH, price).text).is_equal_to(price_text)
        rate = self.browser.find_element(By.XPATH, ratings)
        assert_that(rate.get_attribute('aria-label')).is_equal_to(ratings_text)

        cursor = ActionChains(self.browser)
        img = self.browser.find_element(By.XPATH, img)
        cart = self.browser.find_element(By.XPATH, cart_btn)
        link = self.browser.find_element(By.XPATH, link_btn)

        cursor.move_to_element(img).perform()
        cursor.move_to_element(link).perform()
        cursor.move_to_element(cart).perform()
        cart.click()
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, vcart_btn)))
        cursor.move_to_element(element).perform()

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1607)")
                time.sleep(1)

                self.check_product_info(self.p_1_title, self.p_1_title_text, self.p_1_price, self.p_1_price_text,
                                        self.p_1_ratings, self.p_1_ratings_text, self.p_1_cart_btn, self.p_1_link_btn,
                                        self.p_1_img, self.p_1_vcart_btn)

                self.check_product_info(self.p_2_title, self.p_2_title_text, self.p_2_price, self.p_2_price_text,
                                        self.p_2_ratings, self.p_2_ratings_text, self.p_2_cart_btn, self.p_2_link_btn,
                                        self.p_2_img, self.p_2_vcart_btn)

                self.check_product_info(self.p_3_title, self.p_3_title_text, self.p_3_price, self.p_3_price_text,
                                        self.p_3_ratings, self.p_3_ratings_text, self.p_3_cart_btn, self.p_3_link_btn,
                                        self.p_3_img, self.p_3_vcart_btn)

                self.check_product_info(self.p_4_title, self.p_4_title_text, self.p_4_price, self.p_4_price_text,
                                        self.p_4_ratings, self.p_4_ratings_text, self.p_4_cart_btn, self.p_4_link_btn,
                                        self.p_4_img, self.p_4_vcart_btn)

                p_title = self.browser.find_element(By.XPATH, self.p_2_title).text
                self.browser.find_element(By.XPATH, self.p_2_title).click()
                assert_that(self.browser.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/main/div[2]/div[2]/h1')
                            .text.upper()).is_equal_to(p_title)
                self.browser.back()
                # self.browser.execute_script("window.scrollTo(0, 1537)")
