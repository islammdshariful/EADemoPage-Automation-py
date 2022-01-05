from selenium.webdriver import ActionChains

from utils.config import *


class WooProductCarousel:
    widget = '//*[@id="post-266120"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Woo Product Carousel'
    doc_link = '//*[@id="post-266120"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "WOO PRODUCT CAROUSEL"

    p_1_title = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[4]/div/div[2]/div[1]/div[1]/h2'
    p_1_ratings = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[4]/div/div[2]/div[1]/div[2]'
    p_1_price = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[4]/div/div[2]/div[2]/span'
    p_1_cart_btn = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[4]/div/div[1]/div[2]/ul/li[1]'
    p_1_quickview_btn = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[4]/div/div[1]/div[2]/ul/li[2]'
    p_1_link_btn = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[4]/div/div[1]/div[2]/ul/li[3]'
    p_1_img = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[4]/div/div[1]/div[1]/img'

    p_2_title = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[5]/div/div[2]/div[1]/div[1]/h2'
    p_2_ratings = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[5]/div/div[2]/div[1]/div[2]'
    p_2_price = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[5]/div/div[2]/div[2]/span'
    p_2_cart_btn = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[5]/div/div[1]/div[2]/ul/li[1]'
    p_2_quickview_btn = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[5]/div/div[1]/div[2]/ul/li[2]'
    p_2_link_btn = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[5]/div/div[1]/div[2]/ul/li[3]'
    p_2_img = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[5]/div/div[1]/div[1]/img'

    p_3_title = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[6]/div/div[2]/div[1]/div[1]/h2'
    p_3_ratings = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[6]/div/div[2]/div[1]/div[2]'
    p_3_price = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[6]/div/div[2]/div[2]/span'
    p_3_cart_btn = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[6]/div/div[1]/div[2]/ul/li[1]'
    p_3_quickview_btn = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[6]/div/div[1]/div[2]/ul/li[2]'
    p_3_link_btn = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[6]/div/div[1]/div[2]/ul/li[3]'
    p_3_img = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[6]/div/div[1]/div[1]/img'

    p_4_title = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[7]/div/div[2]/div[1]/div[1]/h2'
    p_4_ratings = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[7]/div/div[2]/div[1]/div[2]'
    p_4_price = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[7]/div/div[2]/div[2]/span'
    p_4_cart_btn = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[7]/div/div[1]/div[2]/ul/li[1]'
    p_4_quickview_btn = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[7]/div/div[1]/div[2]/ul/li[2]'
    p_4_link_btn = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[7]/div/div[1]/div[2]/ul/li[3]'
    p_4_img = f'//*[@id="eael-product-carousel-ace5bb1"]/div[1]/ul/li[7]/div/div[1]/div[1]/img'

    prev_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[4]')
    next_btn = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[3]')

    dot_1 = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[2]/span[1]')
    dot_2 = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[2]/span[2]')
    dot_3 = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[2]/span[3]')
    dot_4 = (By.XPATH, f'//*[@id="eael-product-carousel-ace5bb1"]/div[2]/span[4]')

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

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(woo_product_carousel)

    def check_product_info(self, img, title, title_text, price, price_text, ratings, ratings_text, cart_btn, link_btn, qv_btn):
        time.sleep(.5)
        assert_that(self.browser.find_element(By.XPATH, title).text).is_equal_to(title_text)
        assert_that(self.browser.find_element(By.XPATH, price).text).is_equal_to(price_text)
        rate = self.browser.find_element(By.XPATH, ratings)
        assert_that(rate.get_attribute('aria-label')).is_equal_to(ratings_text)

        cursor = ActionChains(self.browser)
        img = self.browser.find_element(By.XPATH, img)
        cart = self.browser.find_element(By.XPATH, cart_btn)
        link = self.browser.find_element(By.XPATH, link_btn)
        qview = self.browser.find_element(By.XPATH, qv_btn)
        cursor.move_to_element(img).perform()
        cursor.move_to_element(cart).move_to_element(qview).move_to_element(link).perform()

    def testcase(self):
        c = CheckText(self.browser)
        # with soft_assertions():
        c.check_widget_name(self.widget, self.widget_name)
        if check_doc:
            c.check_doc(self.doc_link, self.doc_name)

        self.browser.execute_script("window.scrollTo(0, 1103)")
        time.sleep(2)

        self.browser.find_element(*self.dot_1).click()

        self.check_product_info(self.p_1_img, self.p_1_title, self.p_1_title_text, self.p_1_price, self.p_1_price_text,
                                self.p_1_ratings, self.p_1_ratings_text, self.p_1_cart_btn,
                                self.p_1_link_btn, self.p_1_quickview_btn)

        self.browser.find_element(*self.dot_2).click()
        self.check_product_info(self.p_2_img, self.p_2_title, self.p_2_title_text, self.p_2_price, self.p_2_price_text,
                                self.p_2_ratings, self.p_2_ratings_text, self.p_2_cart_btn,
                                self.p_2_link_btn, self.p_2_quickview_btn)

        self.browser.find_element(*self.dot_3).click()
        self.check_product_info(self.p_3_img, self.p_3_title, self.p_3_title_text, self.p_3_price, self.p_3_price_text,
                                self.p_3_ratings, self.p_3_ratings_text, self.p_3_cart_btn,
                                self.p_3_link_btn, self.p_3_quickview_btn)

        self.browser.find_element(*self.dot_4).click()
        self.check_product_info(self.p_4_img, self.p_4_title, self.p_4_title_text, self.p_4_price, self.p_4_price_text,
                                self.p_4_ratings, self.p_4_ratings_text, self.p_4_cart_btn,
                                self.p_4_link_btn, self.p_4_quickview_btn)
        self.browser.find_element(*self.dot_4).click()
        time.sleep(.5)

        self.browser.find_element(*self.prev_btn).click()
        time.sleep(.5)
        self.browser.find_element(*self.prev_btn).click()
        time.sleep(.5)
        self.browser.find_element(*self.prev_btn).click()
        time.sleep(.5)

        self.browser.find_element(*self.next_btn).click()
        time.sleep(.5)
        self.browser.find_element(*self.next_btn).click()
        time.sleep(.5)
        cursor = ActionChains(self.browser)
        p_3 = self.browser.find_element(By.XPATH, self.p_3_img)
        cursor.move_to_element(p_3).perform()
        self.browser.find_element(By.XPATH, self.p_3_link_btn).click()
        assert_that(self.browser.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/main/div[2]/div[2]/h1')
                    .text).is_equal_to(self.p_3_title_text)

        self.browser.back()
        self.browser.execute_script("window.scrollTo(0, 1103)")
        time.sleep(1)
        self.browser.find_element(*self.dot_3).click()
        time.sleep(.5)
        self.browser.find_element(*self.dot_1).click()
        time.sleep(.5)
        self.browser.find_element(*self.dot_2).click()
        time.sleep(.5)
        self.browser.find_element(*self.dot_4).click()
        time.sleep(.5)
