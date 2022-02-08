from selenium.webdriver import ActionChains, Keys

from utils.config import *


class WooProductGallery(Helper):
    widget = '//*[@id="post-269692"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Woo Product Gallery'
    doc_link = '//*[@id="post-269692"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "WOO PRODUCT GALLERY"

    all_tab = (By.XPATH, f'//*[@id="eael-product-gallery"]/ul/li[1]')
    fashion_tab = (By.XPATH, f'//*[@id="eael-product-gallery"]/ul/li[2]')
    men_tab = (By.XPATH, f'//*[@id="eael-product-gallery"]/ul/li[3]')
    women_tab = (By.XPATH, f'//*[@id="eael-product-gallery"]/ul/li[4]')

    p_1_title = f'//*[@id="eael-product-gallery"]/div/ul/li[1]/div/div[2]/div[2]/a/h2'
    p_1_price = f'//*[@id="eael-product-gallery"]/div/ul/li[1]/div/div[2]/div[1]/span'
    p_1_cart_btn = f'//*[@id="eael-product-gallery"]/div/ul/li[1]/div/div[1]/div[2]/ul/li[1]'
    p_1_qview_btn = f'//*[@id="eael-product-gallery"]/div/ul/li[1]/div/div[1]/div[2]/ul/li[2]'
    p_1_img = f'//*[@id="eael-product-gallery"]/div/ul/li[1]/div/div[1]/div[1]/img'

    p_2_title = f'//*[@id="eael-product-gallery"]/div/ul/li[2]/div/div[2]/div[2]/a/h2'
    p_2_price = f'//*[@id="eael-product-gallery"]/div/ul/li[2]/div/div[2]/div[1]/span'
    p_2_cart_btn = f'//*[@id="eael-product-gallery"]/div/ul/li[2]/div/div[1]/div[2]/ul/li[1]'
    p_2_qview_btn = f'//*[@id="eael-product-gallery"]/div/ul/li[2]/div/div[1]/div[2]/ul/li[2]'
    p_2_img = f'//*[@id="eael-product-gallery"]/div/ul/li[2]/div/div[1]/div[1]/img'

    p_3_title = f'//*[@id="eael-product-gallery"]/div/ul/li[3]/div/div[2]/div[2]/a/h2'
    p_3_price = f'//*[@id="eael-product-gallery"]/div/ul/li[3]/div/div[2]/div[1]/span'
    p_3_cart_btn = f'//*[@id="eael-product-gallery"]/div/ul/li[3]/div/div[1]/div[2]/ul/li[1]'
    p_3_qview_btn = f'//*[@id="eael-product-gallery"]/div/ul/li[3]/div/div[1]/div[2]/ul/li[2]'
    p_3_img = f'//*[@id="eael-product-gallery"]/div/ul/li[3]/div/div[1]/div[1]/img'

    q_title = f'/html/body/div[3]/div[2]/div/div/div[2]/h1'
    q_price = f'/html/body/div[3]/div[2]/div/div/div[2]/p/span'
    q_cat = f'/html/body/div[3]/div[2]/div/div/div[2]/div/span[1]'
    q_tag = f'/html/body/div[3]/div[2]/div/div/div[2]/div/span[2]'
    q_image = f'/html/body/div[3]/div[2]/div/div/div[1]/div/figure/div/a'
    q_cart_btn = f'/html/body/div[3]/div[2]/div/div/div[2]/form/button'
    q_cross = f'/html/body/div[3]/div[2]/div/button'
    q_zoom = f'/html/body/div[3]/div[2]/div/div/div[1]/div/a'

    p_1_title_text = "Mens Trendy T Shirt"
    p_1_price_text = "£35.00"

    p_2_title_text = "Mens Stylish Shirt"
    p_2_price_text = "£75.00"
    p_2_cat_text = "Categories: Fashion, Men"
    p_2_tag_text = "Tag: Men"

    p_3_title_text = "Mens Comfy T Shirt"
    p_3_price_text = "£20.00"

    p_4_title_text = "Women Light Dress"
    p_4_price_text = "£40.00"

    p_5_title_text = "Women Chocolate Dress"
    p_5_price_text = "£75.00"

    p_6_title_text = "Women Hot Dress"
    p_6_price_text = "£99.00"
    p_6_cat_text = "Categories: Fashion, Women"
    p_6_tag_text = "Tag: Women"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.woo_product_gallery)

    def check_product_info(self, img, title, title_text, price, price_text, cart_btn, qv_btn):
        time.sleep(1.5)
        assert_that(self.browser.find_element(By.XPATH, title).text).is_equal_to(title_text)
        assert_that(self.browser.find_element(By.XPATH, price).text).is_equal_to(price_text)

        cursor = ActionChains(self.browser)
        cart = self.browser.find_element(By.XPATH, cart_btn)
        qview = self.browser.find_element(By.XPATH, qv_btn)
        cursor.move_to_element(cart).move_to_element(qview).perform()
        self.check_visibility(img, "Product Image is not visible.")

    def check_tab_items(self, p_1_img, p_1_title, p_1_title_text, p_1_price, p_1_price_text, p_1_cart_btn,
                        p_1_qview_btn, p_2_img, p_2_title, p_2_title_text, p_2_price, p_2_price_text, p_2_cart_btn,
                        p_2_qview_btn, p_3_img, p_3_title, p_3_title_text, p_3_price, p_3_price_text, p_3_cart_btn,
                        p_3_qview_btn):
        time.sleep(1)
        self.check_product_info(p_1_img, p_1_title, p_1_title_text, p_1_price, p_1_price_text, p_1_cart_btn,
                                p_1_qview_btn)
        self.check_product_info(p_2_img, p_2_title, p_2_title_text, p_2_price, p_2_price_text, p_2_cart_btn,
                                p_2_qview_btn)
        self.check_product_info(p_3_img, p_3_title, p_3_title_text, p_3_price, p_3_price_text, p_3_cart_btn,
                                p_3_qview_btn)

    def check_quick_view(self, title, title_text, price, price_text, cart_btn, cat, cat_text, tag, tag_text,
                         img, zoom, cross):
        time.sleep(.5)
        assert_that(self.browser.find_element(By.XPATH, title).text).is_equal_to(title_text)
        assert_that(self.browser.find_element(By.XPATH, price).text).is_equal_to(price_text)
        self.check_visibility(cart_btn, "Add to Cart button not visible.")

        assert_that(self.browser.find_element(By.XPATH, cat).text).is_equal_to(cat_text)
        assert_that(self.browser.find_element(By.XPATH, tag).text).is_equal_to(tag_text)
        time.sleep(1)
        self.check_visibility(zoom, "Zoom button not visible")
        time.sleep(3)
        self.check_visibility(img, "Quick View Image not visible")

        self.browser.find_element(By.XPATH, cross).click()

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1002)")
                time.sleep(1)

                cursor = ActionChains(self.browser)
                all = self.browser.find_element(*self.all_tab)
                fashion = self.browser.find_element(*self.fashion_tab)
                men = self.browser.find_element(*self.men_tab)
                women = self.browser.find_element(*self.women_tab)

                cursor.move_to_element(all).click().perform()
                self.browser.execute_script("window.scrollTo(0, 1002)")
                self.check_tab_items(self.p_1_img, self.p_1_title, self.p_1_title_text, self.p_1_price, self.p_1_price_text,
                                     self.p_1_cart_btn, self.p_1_qview_btn, self.p_2_img, self.p_2_title,
                                     self.p_2_title_text, self.p_2_price, self.p_2_price_text, self.p_2_cart_btn,
                                     self.p_2_qview_btn, self.p_3_img, self.p_3_title, self.p_3_title_text,
                                     self.p_3_price, self.p_3_price_text, self.p_3_cart_btn, self.p_3_qview_btn)
                self.browser.execute_script("window.scrollTo(0, 1002)")
                self.browser.find_element(By.XPATH, self.p_2_qview_btn).click()
                self.check_quick_view(self.q_title, self.p_2_title_text, self.q_price, self.p_2_price_text, self.q_cart_btn,
                                      self.q_cat, self.p_2_cat_text, self.q_tag, self.p_2_tag_text, self.q_image,
                                      self.q_zoom, self.q_cross)
                self.browser.execute_script("window.scrollTo(0, 1002)")
                cursor.move_to_element(fashion).click().perform()
                self.browser.execute_script("window.scrollTo(0, 1002)")
                self.check_tab_items(self.p_1_img, self.p_1_title, self.p_1_title_text, self.p_1_price, self.p_1_price_text,
                                     self.p_1_cart_btn, self.p_1_qview_btn, self.p_2_img, self.p_2_title,
                                     self.p_2_title_text, self.p_2_price, self.p_2_price_text, self.p_2_cart_btn,
                                     self.p_2_qview_btn, self.p_3_img, self.p_3_title, self.p_3_title_text,
                                     self.p_3_price, self.p_3_price_text, self.p_3_cart_btn, self.p_3_qview_btn)
                self.browser.execute_script("window.scrollTo(0, 1002)")
                cursor.move_to_element(men).click().perform()
                self.browser.execute_script("window.scrollTo(0, 1002)")
                self.check_tab_items(self.p_1_img, self.p_1_title, self.p_1_title_text, self.p_1_price, self.p_1_price_text,
                                     self.p_1_cart_btn, self.p_1_qview_btn, self.p_2_img, self.p_2_title,
                                     self.p_2_title_text, self.p_2_price, self.p_2_price_text, self.p_2_cart_btn,
                                     self.p_2_qview_btn, self.p_3_img, self.p_3_title, self.p_3_title_text,
                                     self.p_3_price, self.p_3_price_text, self.p_3_cart_btn, self.p_3_qview_btn)
                self.browser.execute_script("window.scrollTo(0, 1002)")
                cursor.move_to_element(women).click().perform()
                self.browser.execute_script("window.scrollTo(0, 1002)")
                self.check_tab_items(self.p_1_img, self.p_1_title, self.p_4_title_text, self.p_1_price, self.p_4_price_text,
                                     self.p_1_cart_btn, self.p_1_qview_btn, self.p_2_img, self.p_2_title,
                                     self.p_5_title_text, self.p_2_price, self.p_5_price_text, self.p_2_cart_btn,
                                     self.p_2_qview_btn, self.p_3_img, self.p_3_title, self.p_6_title_text,
                                     self.p_3_price, self.p_6_price_text, self.p_3_cart_btn, self.p_3_qview_btn)
                time.sleep(.5)
                self.browser.find_element(By.XPATH, self.p_3_qview_btn).click()
                self.check_quick_view(self.q_title, self.p_6_title_text, self.q_price, self.p_6_price_text, self.q_cart_btn,
                                      self.q_cat, self.p_6_cat_text, self.q_tag, self.p_6_tag_text, self.q_image,
                                      self.q_zoom, self.q_cross)
                self.browser.execute_script("window.scrollTo(0, 1002)")
                p_title = self.browser.find_element(By.XPATH, self.p_2_title).text
                self.browser.find_element(By.XPATH, self.p_2_title).click()
                assert_that(self.browser.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/main/div[2]/div[2]/h1')
                            .text).is_equal_to(p_title)
                self.browser.back()
                self.browser.execute_script("window.scrollTo(0, 1002)")
                time.sleep(1)
                p_title = self.browser.find_element(By.XPATH, self.p_2_title).text
                self.browser.find_element(By.XPATH, self.p_2_title).click()
                assert_that(self.browser.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/main/div[2]/div[2]/h1')
                            .text).is_equal_to(p_title)
                self.browser.back()
                self.browser.execute_script("window.scrollTo(0, 1002)")
