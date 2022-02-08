from selenium.webdriver import Keys

from utils.config import *


class WooCart(Helper):
    widget = '//*[@id="post-271400"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Woo Cart'
    doc_link = '//*[@id="post-271400"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA WOO CART"
    p_title_header = (By.XPATH, f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                f'/div/div/div/div/div/div/div/div/form/div[1]/div[1]/div/div[1]/div')
    p_price_header = (By.XPATH, f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                f'/div/div/div/div/div/div/div/div/form/div[1]/div[1]/div/div[2]/div[1]')
    p_quantity_header = (By.XPATH, f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                   f'/div/div/div/div/div/div/div/div/form/div[1]/div[1]/div/div[2]/div[2]')
    p_subtotal_header = (By.XPATH, f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                   f'/div/div/div/div/div/div/div/div/form/div[1]/div[1]/div/div[2]/div[3]')

    p_img_1 = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
              f'/div/div/div/div/div/div/form/div[1]/div[2]/div[1]/div[1]/div[1]/a/img'
    p_title_1 = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                f'/div/div/div/div/div/div/form/div[1]/div[2]/div[1]/div[1]/div[2]/a'
    p_price_1 = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                f'/div/div/div/div/div/div/form/div[1]/div[2]/div[1]/div[2]/div[1]/span'
    p_quantity_1 = f'/html/body/div[3]/div/div/div/main/article/div/div/div/div/section[2]/div/div/div/div/div/' \
                   f'section[2]/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div[1]/div[2]/div[2]/div/input'
    p_quantity_1_minus = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div' \
                         f'/section[2]/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div[1]' \
                         f'/div[2]/div[2]/div/span[1]'
    p_quantity_1_plus = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div' \
                        f'/section[2]/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div[1]/' \
                        f'div[2]/div[2]/div/span[2]'
    p_subtotal_1 = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                   f'/div/div/div/div/div/div/div/form/div[1]/div[2]/div[1]/div[2]/div[3]/span'
    p_cross_1 = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                f'/div/div/div/div/div/div/form/div[1]/div[2]/div[1]/div[2]/div[4]/a/i'

    p_img_2 = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
              f'/div/div/div/div/div/div/div/form/div[1]/div[2]/div[2]/div[1]/div[1]/a/img'
    p_title_2 = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                f'/div/div/div/div/div/div/div/form/div[1]/div[2]/div[2]/div[1]/div[2]/a'
    p_price_2 = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                f'/div/div/div/div/div/div/div/form/div[1]/div[2]/div[2]/div[2]/div[1]/span'
    p_quantity_2 = f'/html/body/div[3]/div/div/div/main/article/div/div/div/div/section[2]/div/div/div/div/div' \
                   f'/section[2]/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div[2]/div[2]/div[2]/div/input'
    p_quantity_2_minus = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                         f'/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div[2]/div[2]' \
                         f'/div[2]/div/span[1]'
    p_quantity_2_plus = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                        f'/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div[2]/div[2]' \
                        f'/div[2]/div/span[2]'
    p_subtotal_2 = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                   f'/div/div/div/div/div/div/div/form/div[1]/div[2]/div[2]/div[2]/div[3]/span'
    p_cross_2 = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                f'/div/div/div/div/div/div/div/form/div[1]/div[2]/div[2]/div[2]/div[4]/a/i'

    p_coupon_code = (By.ID, f'coupon_code')
    coupon_btn = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                            f'/div/div/div/div/div/div/div/form/div[2]/div[1]/div/button'
    shop_page_btn = (By.XPATH, f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                           f'/div/div/div/div/div/div/div/div/form/div[2]/div[1]/a')
    update_cart_btn = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                 f'/div/div/div/div/div/div/div/div/form/div[2]/div[2]/div[1]/button'

    c_subtotal = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/' \
                            f'div/div/div/div/div/div/div/form/div[2]/div[2]/div[2]/table/tbody/tr[1]/th'
    c_subtotal_amount = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div' \
                                   f'/section[2]/div/div/div/div/div/div/div/div/form/div[2]/div[2]/div[2]/' \
                                   f'table/tbody/tr[1]/td/span'
    c_shipping = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                            f'/div/div/div/div/div/div/div/form/div[2]/div[2]/div[2]/table/tbody/tr[2]/th'
    c_shipping_flat = f'//*[@id="shipping_method"]'
    c_shipping_des = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                f'/div/div/div/div/div/div/div/div/form/div[2]/div[2]/div[2]/table/tbody/tr[2]/td/p'
    c_shipping_cal = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                                f'/div/div/div/div/div/div/div/form/div[2]/div[2]/div[2]/table/tbody/tr[2]/td/a'
    c_total = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                         f'/div/div/div/div/div/div/form/div[2]/div[2]/div[2]/table/tbody/tr[3]/th'
    c_total_amount = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                f'/div/div/div/div/div/div/div/div/form/div[2]/div[2]/div[2]' \
                                f'/table/tbody/tr[3]/td/strong/span'
    checkout_btn = f'//*[@id="post-271400"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                            f'/div/div/div/div/div/div/div/form/div[2]/div[2]/div[2]/div/a'

    checkout_page = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section'
                               f'/div/div/div[2]/div/div/div[1]/div/h2')
    checkout_page_text = "Woo Checkout"
    shop_page = (By.XPATH, f'//*[@id="main"]/header/h1')
    shop_page_text = "Shop"

    p_title_header_text = "PRODUCT TITLE"
    p_price_header_text = "PRICE"
    p_quantity_header_text = "QUANTITY"
    p_subtotal_header_text = "SUBTOTAL"

    p_title_1_text = "Mens Comfy T Shirt"
    p_price_1_text = "£20.00"
    p_quantity_1_text = "1"
    p_subtotal_1_text = "£20.00"

    p_title_2_text = "Mens Trendy T Shirt"
    p_price_2_text = "£35.00"
    p_quantity_2_text = "1"
    p_subtotal_2_text = "£35.00"

    shop_page_btn_text = "Continue Shopping"
    coupon_btn_text = "Apply Coupon"
    update_cart_btn_text = "Update Cart"

    c_subtotal_text = "Subtotal"
    c_subtotal_amount_text = "£55.00"
    c_shipping_text = "Shipping"
    c_shipping_flat_text = "Flat rate: £10.00"
    c_shipping_des_text = "Shipping options will be updated during checkout."
    c_shipping_cal_text = "Calculate shipping"

    c_total_text = "Total"
    c_total_amount_text = "£65.00"

    c_checkout_text = "Proceed to Checkout"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.woo_cart)

    def check_cart_item(self, title, title_text, price, price_text, quantity, quantity_text, subtotal, subtotal_text,
                        image, cross):
        assert_that(self.browser.find_element(By.XPATH, title).text).is_equal_to(title_text)
        assert_that(self.browser.find_element(By.XPATH, price).text).is_equal_to(price_text)
        qty = self.browser.find_element(By.XPATH, quantity)
        assert_that(qty.get_attribute('value')).is_equal_to(quantity_text)

        assert_that(self.browser.find_element(By.XPATH, subtotal).text).is_equal_to(subtotal_text)
        self.check_visibility(image, "Product Image is not visible.")
        self.check_visibility(cross, "Remove Product icon is not visible.")

    def update_quantity(self, plus, minus, p_qty, m_qty):
        for i in range(1, p_qty):
            self.browser.find_element(By.XPATH, plus).click()

        for i in range(1, m_qty):
            self.browser.find_element(By.XPATH, minus).click()

    def check_visibility_of_buttons(self, btn, btn_text):
        self.check_visibility(btn, "Button not visible.")
        assert_that(self.browser.find_element(By.XPATH, btn).text).is_equal_to(btn_text)

    def check_total_table(self, label, label_amount):
        assert_that(self.browser.find_element(By.XPATH, label).text).is_equal_to(label_amount)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1000)")
                self.wait_for_bar_to_come()

                assert_that(self.browser.find_element(*self.p_title_header).text).is_equal_to(self.p_title_header_text)
                assert_that(self.browser.find_element(*self.p_price_header).text).is_equal_to(self.p_price_header_text)
                assert_that(self.browser.find_element(*self.p_quantity_header).text).is_equal_to(self.p_quantity_header_text)
                assert_that(self.browser.find_element(*self.p_subtotal_header).text).is_equal_to(self.p_subtotal_header_text)

                self.update_quantity(self.p_quantity_1_plus, self.p_quantity_1_minus, 4, 3)
                self.update_quantity(self.p_quantity_2_plus, self.p_quantity_2_minus, 3, 2)

                input_coupon = self.browser.find_element(*self.p_coupon_code)
                assert_that(input_coupon.get_attribute('placeholder')).is_equal_to("Coupon code")
                input_coupon.send_keys("FreeForLife")

                self.check_visibility_of_buttons(self.coupon_btn, self.coupon_btn_text)
                self.check_visibility_of_buttons(self.update_cart_btn, self.update_cart_btn_text)

                self.check_total_table(self.c_subtotal, self.c_subtotal_text)
                self.check_total_table(self.c_subtotal_amount, self.c_subtotal_amount_text)
                self.check_total_table(self.c_shipping, self.c_shipping_text)
                self.check_total_table(self.c_shipping_flat, self.c_shipping_flat_text)
                self.check_total_table(self.c_shipping_des, self.c_shipping_des_text)
                self.check_total_table(self.c_shipping_cal, self.c_shipping_cal_text)
                self.check_total_table(self.c_total, self.c_total_text)
                self.check_total_table(self.c_total_amount, self.c_total_amount_text)

                self.check_visibility(self.checkout_btn, "Checkout not visible")
                assert_that(self.browser.find_element(By.XPATH, self.checkout_btn).text).is_equal_to(self.c_checkout_text)

                self.browser.find_element(By.XPATH, self.checkout_btn).click()
                assert_that(self.browser.find_element(*self.checkout_page).text).is_equal_to(self.checkout_page_text)
                self.browser.back()
                self.browser.execute_script("window.scrollTo(0, 1000)")
                time.sleep(1)

                assert_that(self.browser.find_element(*self.shop_page_btn).text).is_equal_to(self.shop_page_btn_text)
                self.browser.find_element(*self.shop_page_btn).click()
                assert_that(self.browser.find_element(*self.shop_page).text).is_equal_to(self.shop_page_text)
                self.browser.back()
                self.browser.execute_script("window.scrollTo(0, 1000)")
                time.sleep(1)

                self.check_cart_item(self.p_title_1, self.p_title_1_text, self.p_price_1, self.p_price_1_text,
                                     self.p_quantity_1, self.p_quantity_1_text, self.p_subtotal_1,
                                     self.p_subtotal_1_text, self.p_img_1, self.p_cross_1)

                self.check_cart_item(self.p_title_2, self.p_title_2_text, self.p_price_2, self.p_price_2_text,
                                     self.p_quantity_2, self.p_quantity_2_text, self.p_subtotal_2,
                                     self.p_subtotal_2_text, self.p_img_2, self.p_cross_2)





