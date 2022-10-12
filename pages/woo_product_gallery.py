from utils.config import *


class WooProductGallery(BasePage, Helper):
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

    p_1_title = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[1]/div/div[2]/div[2]/a/h2')
    p_1_price = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[1]/div/div[2]/div[1]/span')
    p_1_cart_btn = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[1]/div/div[1]/div[2]/ul/li[1]')
    p_1_qview_btn = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[1]/div/div[1]/div[2]/ul/li[2]')
    p_1_link_btn = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[1]/div/div[1]/div[2]/ul/li[3]')
    p_1_img = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[1]/div/div[1]/div[1]/img')

    p_2_title = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[2]/div/div[2]/div[2]/a/h2')
    p_2_price = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[2]/div/div[2]/div[1]/span')
    p_2_cart_btn = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[2]/div/div[1]/div[2]/ul/li[1]')
    p_2_qview_btn = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[2]/div/div[1]/div[2]/ul/li[2]')
    p_2_link_btn = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[2]/div/div[1]/div[2]/ul/li[3]')
    p_2_img = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[2]/div/div[1]/div[1]/img')

    p_3_title = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[3]/div/div[2]/div[2]/a/h2')
    p_3_price = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[3]/div/div[2]/div[1]/span')
    p_3_cart_btn = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[3]/div/div[1]/div[2]/ul/li[1]')
    p_3_qview_btn = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[3]/div/div[1]/div[2]/ul/li[2]')
    p_3_link_btn = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[3]/div/div[1]/div[2]/ul/li[3]')
    p_3_img = (By.XPATH, f'//*[@id="eael-product-gallery"]/div/ul/li[3]/div/div[1]/div[1]/img')

    quick_view = f"//div[@class='eael-popup-details-render eael-woo-slider-popup elementor-269692']//div//div//"
    q_title = (By.XPATH, quick_view + f"div[2]//h1")
    q_price = (By.XPATH, quick_view + f"div[2]//p//span")
    q_cat = (By.XPATH, quick_view + f"div[2]//div//span[1]")
    q_tag = (By.XPATH, quick_view + f"div[2]//div//span[2]")
    q_image = (By.XPATH, '//*[@id="product-"]/div[1]/div/figure/div/a')
    q_cart_btn = (By.XPATH, f'//*[@id="product-"]/div[2]/form/button')
    q_cross = (By.XPATH, f"//button[@class='eael-product-popup-close']")
    q_zoom = (By.XPATH, quick_view + f"div[1]//div//a")

    item_name = (By.XPATH, f"//h1[@class='product_title entry-title']")

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

    def check_product_info(self, img, title, title_text, price, price_text, cart_btn, qv_btn, link_btn):
        self.cursor.move_to_element(self.get_element(cart_btn)).move_to_element(self.get_element(qv_btn)).\
            move_to_element(self.get_element(link_btn)).perform()
        self.is_visible(img, "Product Image is not visible.")

        self.check_text_matches_with(title, title_text)
        self.check_text_matches_with(price, price_text)

    def check_tab_items(self, p_1_img, p_1_title, p_1_title_text, p_1_price, p_1_price_text, p_1_cart_btn,
                        p_1_qview_btn, p_1_link_btn, p_2_img, p_2_title, p_2_title_text, p_2_price, p_2_price_text, p_2_cart_btn,
                        p_2_qview_btn, p_2_link_btn, p_3_img, p_3_title, p_3_title_text, p_3_price, p_3_price_text, p_3_cart_btn,
                        p_3_qview_btn, p_3_link_btn):
        self.check_product_info(p_1_img, p_1_title, p_1_title_text, p_1_price, p_1_price_text, p_1_cart_btn,
                                p_1_qview_btn, p_1_link_btn)
        self.check_product_info(p_2_img, p_2_title, p_2_title_text, p_2_price, p_2_price_text, p_2_cart_btn,
                                p_2_qview_btn, p_2_link_btn)
        self.check_product_info(p_3_img, p_3_title, p_3_title_text, p_3_price, p_3_price_text, p_3_cart_btn,
                                p_3_qview_btn, p_3_link_btn)

    def check_quick_view(self, title, title_text, price, price_text, cart_btn, cat, cat_text, tag, tag_text,
                         img, zoom, cross):
        self.check_text_matches_with(title, title_text)
        self.check_text_matches_with(price, price_text)
        self.check_text_matches_with(cat, cat_text)
        self.check_text_matches_with(tag, tag_text)
        self.is_visible(img, title_text + " Quick View Image not visible")
        self.is_visible(cart_btn, title_text + " Add to Cart button not visible.")
        self.is_visible(zoom, title_text + " Zoom button not visible")

        self.do_click(cross)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.woo_product_gallery)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1002)

                self.move_cursor_to_and_click(self.all_tab)
                self.scroll_to(1002)
                self.check_tab_items(self.p_1_img, self.p_1_title, self.p_1_title_text, self.p_1_price, self.p_1_price_text,
                                     self.p_1_cart_btn, self.p_1_qview_btn, self.p_1_link_btn, self.p_2_img, self.p_2_title,
                                     self.p_2_title_text, self.p_2_price, self.p_2_price_text, self.p_2_cart_btn,
                                     self.p_2_qview_btn, self.p_2_link_btn, self.p_3_img, self.p_3_title, self.p_3_title_text,
                                     self.p_3_price, self.p_3_price_text, self.p_3_cart_btn, self.p_3_qview_btn, self.p_3_link_btn)
                self.scroll_to(1002)
                self.do_click(self.p_2_qview_btn)
                self.check_quick_view(self.q_title, self.p_2_title_text, self.q_price, self.p_2_price_text, self.q_cart_btn,
                                      self.q_cat, self.p_2_cat_text, self.q_tag, self.p_2_tag_text, self.q_image,
                                      self.q_zoom, self.q_cross)
                self.scroll_to(1002)
                self.move_cursor_to_and_click(self.fashion_tab)
                self.scroll_to(1002)
                self.check_tab_items(self.p_1_img, self.p_1_title, self.p_1_title_text, self.p_1_price, self.p_1_price_text,
                                     self.p_1_cart_btn, self.p_1_qview_btn, self.p_1_link_btn, self.p_2_img, self.p_2_title,
                                     self.p_2_title_text, self.p_2_price, self.p_2_price_text, self.p_2_cart_btn,
                                     self.p_2_qview_btn, self.p_2_link_btn, self.p_3_img, self.p_3_title, self.p_3_title_text,
                                     self.p_3_price, self.p_3_price_text, self.p_3_cart_btn, self.p_3_qview_btn, self.p_3_link_btn)
                self.scroll_to(1002)
                self.move_cursor_to_and_click(self.men_tab)
                self.scroll_to(1002)
                self.check_tab_items(self.p_1_img, self.p_1_title, self.p_1_title_text, self.p_1_price, self.p_1_price_text,
                                     self.p_1_cart_btn, self.p_1_qview_btn, self.p_1_link_btn, self.p_2_img, self.p_2_title,
                                     self.p_2_title_text, self.p_2_price, self.p_2_price_text, self.p_2_cart_btn,
                                     self.p_2_qview_btn, self.p_2_link_btn, self.p_3_img, self.p_3_title, self.p_3_title_text,
                                     self.p_3_price, self.p_3_price_text, self.p_3_cart_btn, self.p_3_qview_btn, self.p_3_link_btn)
                self.scroll_to(1002)
                self.move_cursor_to_and_click(self.women_tab)
                self.scroll_to(1002)
                self.check_tab_items(self.p_1_img, self.p_1_title, self.p_4_title_text, self.p_1_price, self.p_4_price_text,
                                     self.p_1_cart_btn, self.p_1_qview_btn, self.p_1_link_btn, self.p_2_img, self.p_2_title,
                                     self.p_5_title_text, self.p_2_price, self.p_5_price_text, self.p_2_cart_btn,
                                     self.p_2_qview_btn, self.p_2_link_btn, self.p_3_img, self.p_3_title, self.p_6_title_text,
                                     self.p_3_price, self.p_6_price_text, self.p_3_cart_btn, self.p_3_qview_btn, self.p_3_link_btn)

                self.do_click(self.p_3_qview_btn)
                self.check_quick_view(self.q_title, self.p_6_title_text, self.q_price, self.p_6_price_text, self.q_cart_btn,
                                      self.q_cat, self.p_6_cat_text, self.q_tag, self.p_6_tag_text, self.q_image,
                                      self.q_zoom, self.q_cross)
                self.scroll_to(1002)
                # WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.p_2_title)))
                product_title = self.get_element_text(self.p_2_title)
                self.do_click(self.p_2_title)
                self.check_text_matches_with(self.item_name, product_title)
                self.go_back()
                self.scroll_to(1002)

                # WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.p_3_title)))
                product_title = self.get_element_text(self.p_3_title)
                self.do_click(self.p_3_title)
                self.check_text_matches_with(self.item_name, product_title)
                self.go_back()
                self.scroll_to(1002)
