from utils.config import *


class WooCheckout(Helper):
    widget = '//*[@id="post-259772"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Woo Checkout'
    doc_link = '//*[@id="post-259772"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "WOO CHECKOUT "

    go_to_multi_step_checkout = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div'
                                           f'/section[2]/div/div/div[1]/div/div/div/div/div/a/div/span[2]')

    login_form_icon = f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                      f'/div/div[4]/div[1]'
    login_form = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div'
                            f'/div[4]/div[2]/div')
    login_form_expand = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                                   f'/div/div[4]/div[2]/div/a')
    login_form_des = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div'
                                f'/div[4]/form/p[1]')
    login_username_label = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div'
                                      f'/div/div/div/div[4]/form/p[2]/label')
    login_pass_label = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                                  f'/div/div[4]/form/p[3]/label')
    login_username_field = (By.XPATH, f'//*[@id="username"]')
    login_pass_field = (By.XPATH, f'//*[@id="password"]')
    remember_me_label = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                                   f'/div/div[4]/form/p[4]/label/span')
    remember_me_field = (By.XPATH, f'//*[@id="rememberme"]')
    login_btn = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div'
                           f'/div[4]/form/p[4]/button')
    forget_pass_label = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                                   f'/div/div[4]/form/p[5]/a')

    coupon_form = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div'
                             f'/div[5]/div[2]/div/a')
    coupon_form_icon = f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                       f'/div/div[5]/div[1]'
    coupon_form_expand = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div'
                                    f'/div/div/div[5]/div[2]/div/a')
    coupon_form_des = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                                 f'/div/div[5]/form/p[1]')
    coupon_form_field = (By.XPATH, f'//*[@id="coupon_code"]')
    coupon_btn = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div'
                            f'/div[5]/form/p[3]/button')

    multi_login_form_icon = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div' \
                                       f'/div/div/div[2]/div/div[1]/div[2]/div[1]'
    multi_login_form = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                                  f'/div/div[2]/div/div[1]/div[2]/div[2]/div')

    multi_coupon_form = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                                   f'/div/div[2]/div/div[1]/div[3]/div[2]/div')
    multi_coupon_form_icon = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div' \
                                        f'/div/div/div[2]/div/div[1]/div[3]/div[2]/div'

    billing_label = (By.XPATH, f'//*[@id="customer_details"]/div[1]/div[1]/h3')
    billing_fname_label = (By.XPATH, f'//*[@id="billing_first_name_field"]/label')
    billing_fname_field = (By.XPATH, f'//*[@id="billing_first_name"]')
    billing_lname_label = (By.XPATH, f'//*[@id="billing_last_name_field"]/label')
    billing_lname_field = (By.XPATH, f'//*[@id="billing_last_name"]')
    billing_com_label = (By.XPATH, f'//*[@id="billing_company_field"]/label')
    billing_com_field = (By.XPATH, f'//*[@id="billing_company"]')
    billing_country_label = (By.XPATH, f'//*[@id="billing_country_field"]/label')
    billing_country_list = (By.XPATH, f'//*[@id="billing_country"]')
    billing_country_list_field = (By.XPATH, f'/html/body/span/span/span[1]/input')
    billing_address_label = (By.XPATH, f'//*[@id="billing_address_1_field"]/label')
    billing_address_field_1 = (By.XPATH, f'//*[@id="billing_address_1"]')
    billing_address_field_2 = (By.XPATH, f'//*[@id="billing_address_2"]')
    billing_city_label = (By.XPATH, f'//*[@id="billing_city_field"]/label')
    billing_city_field = (By.XPATH, f'//*[@id="billing_city"]')
    billing_district_label = (By.XPATH, f'//*[@id="billing_state_field"]/label')
    billing_district_field = (By.XPATH, f'//*[@id="billing_state"]')
    billing_district_list_field = (By.XPATH, f'/html/body/span/span/span[1]/input')
    billing_zip_label = (By.XPATH, f'//*[@id="billing_postcode_field"]/label')
    billing_zip_field = (By.XPATH, f'//*[@id="billing_postcode"]')
    billing_phone_label = (By.XPATH, f'//*[@id="billing_phone_field"]/label')
    billing_phone_field = (By.XPATH, f'//*[@id="billing_phone"]')
    billing_email_label = (By.XPATH, f'//*[@id="billing_email_field"]/label')
    billing_email_field = (By.XPATH, f'//*[@id="billing_email"]')
    create_acc_field = (By.XPATH, f'//*[@id="createaccount"]')
    create_acc_field_label = (By.XPATH, f'//*[@id="customer_details"]/div[1]/div[2]/p/label/span')
    create_acc_pass_label = (By.XPATH, f'//*[@id="account_password_field"]/label')
    create_acc_pass_field = (By.XPATH, f'//*[@id="account_password"]')

    ship_diff_address_label = (By.XPATH, f'//*[@id="ship-to-different-address"]/label/span')
    ship_diff_address_field = (By.XPATH, f'//*[@id="ship-to-different-address-checkbox"]')

    shipping_label = (By.XPATH, f'//*[@id="customer_details"]/div[1]/div[1]/h3')
    shipping_fname_label = (By.XPATH, f'//*[@id="shipping_first_name_field"]/label')
    shipping_fname_field = f'//*[@id="shipping_first_name"]'
    shipping_lname_label = (By.XPATH, f'//*[@id="shipping_last_name_field"]/label')
    shipping_lname_field = (By.XPATH, f'//*[@id="shipping_last_name"]')
    shipping_com_label = (By.XPATH, f'//*[@id="shipping_company_field"]/label')
    shipping_com_field = (By.XPATH, f'//*[@id="shipping_company"]')
    shipping_country_label = (By.XPATH, f'//*[@id="shipping_country_field"]/label')
    shipping_country_list = (By.XPATH, f'//*[@id="shipping_state"]')
    shipping_country_list_field = (By.XPATH, f'/html/body/span/span/span[1]/input')
    shipping_address_label = (By.XPATH, f'//*[@id="shipping_address_1_field"]/label')
    shipping_address_field_1 = (By.XPATH, f'//*[@id="shipping_address_1"]')
    shipping_address_field_2 = (By.XPATH, f'//*[@id="shipping_address_2"]')
    shipping_city_label = (By.XPATH, f'//*[@id="shipping_city_field"]/label')
    shipping_city_field = (By.XPATH, f'//*[@id="shipping_city"]')
    shipping_district_label = (By.XPATH, f'//*[@id="shipping_state_field"]/label')
    shipping_district_field = (By.XPATH, f'//*[@id="shipping_state"]')
    shipping_zip_label = (By.XPATH, f'//*[@id="shipping_postcode_field"]/label')
    shipping_zip_field = (By.XPATH, f'//*[@id="shipping_postcode"]')

    other_note_label = (By.XPATH, f'//*[@id="order_comments_field"]/label')
    other_note_field = (By.XPATH, f'//*[@id="order_comments"]')

    payment_method_label = (By.XPATH, f'//*[@id="payment-title"]')
    payment_method_bank = f'//*[@id="payment"]/ul/li[1]/label'
    payment_method_bank_des = f'//*[@id="payment"]/ul/li[1]/div/p'
    payment_method_check = f'//*[@id="payment"]/ul/li[2]/label'
    payment_method_check_des = f'//*[@id="payment"]/ul/li[2]/div/p'
    payment_method_cash = f'//*[@id="payment"]/ul/li[3]/label'
    payment_method_cash_des = f'//*[@id="payment"]/ul/li[3]/div/p'
    payment_method_des = (By.XPATH, f'//*[@id="payment"]/div/div/div/p')
    place_order_btn = (By.XPATH, f'//*[@id="ea_place_order"]')

    next_btn = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div'
                          f'/div/div/div/div[2]/div/div[1]/div[4]/button[2]')
    prev_btn = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div'
                          f'/div/div/div/div[2]/div/div[1]/div[4]/button[1]')

    login_tab = (By.XPATH, f'//*[@id="step-0"]')
    coupon_tab = (By.XPATH, f'//*[@id="step-1"]')
    billing_tab = (By.XPATH, f'//*[@id="step-2"]')
    payment_tab = (By.XPATH, f'//*[@id="step-3"]')

    p_img_1 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                         f'/div[2]/div/div[2]/div/div/ul/li[1]/div[1]/div[1]/img'
    p_title_1 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[1]/div[1]/div[2]'
    p_quantity_1 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                         f'/div[2]/div/div[2]/div/div/ul/li[1]/div[1]/div[2]/strong'
    p_price_1 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[1]/div[2]/span'

    p_img_2 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                         f'/div[2]/div/div[2]/div/div/ul/li[2]/div[1]/div[1]/img'
    p_title_2 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[2]/div[1]/div[2]'
    p_quantity_2 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                         f'/div[2]/div/div[2]/div/div/ul/li[2]/div[1]/div[2]/strong'
    p_price_2 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[2]/div[2]/span'

    p_img_3 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                         f'/div[2]/div/div[2]/div/div/ul/li[3]/div[1]/div[1]/img'
    p_title_3 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[3]/div[1]/div[2]'
    p_quantity_3 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                         f'/div[2]/div/div[2]/div/div/ul/li[3]/div[1]/div[2]/strong'
    p_price_3 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[3]/div[2]/span'

    p_img_4 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                         f'/div[2]/div/div[2]/div/div/ul/li[4]/div[1]/div[1]/img'
    p_title_4 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[4]/div[1]/div[2]'
    p_quantity_4 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                         f'/div[2]/div/div[2]/div/div/ul/li[4]/div[1]/div[2]/strong'
    p_price_4 = f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[4]/div[2]/span'

    t_sub_total_label = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                                   f'/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div[1]')
    t_sub_total_amount = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                                    f'/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/span')

    t_shipping_label = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                                  f'/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]')
    t_shipping_amount = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div'
                                         f'/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/span')

    t_total_label = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div'
                               f'/div[2]/div/div[2]/div/div/div/div[2]/div[3]/div[1]')
    t_total_amount = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                                f'/div/div[2]/div/div[2]/div/div/div/div[2]/div[3]/div[2]/strong/span')
    continue_shop = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div'
                               f'/div[2]/div/div[2]/div/div/div/div[1]/a')

    login_form_text = "Returning Customer? Click Here To Login"
    login_form_des_text = "If you have shopped with us before, please enter your details below. If you are a new " \
                          "customer, please proceed to the Billing section."
    login_username_label_text = "Username or email *"
    login_pass_label_text = "Password *"
    remember_me_label_text = "Remember me"
    forget_pass_label_text = "Lost your password?"

    coupon_form_text = "Have A Coupon? Click Here To Enter Your Code"
    coupon_form_des_text = "If you have a coupon code, please apply it below."

    billing_label_text = "Billing Details"
    fname_label_text = "First name *"
    lname_label_text = "Last name *"
    com_label_text = "Company name (optional)"
    country_label_text = "Country / Region *"
    address_label_text = "Street address *"
    city_label_text = "Town / City *"
    district_label_text = "County (optional)"
    zip_label_text = "Postcode *"
    phone_label_text = "Phone *"
    email_label_text = "Email address *"
    create_acc_field_label_text = "Create an account?"
    create_acc_pass_label_text = "Create account password *"

    ship_diff_address_label_text = "Ship To A Different Address?"
    other_note_label_text = "Order notes (optional)"

    payment_method_label_text = "Payment Methods"
    payment_method_bank_text = "Direct bank transfer"
    payment_method_bank_des_text = "Make your payment directly into our bank account. Please use your Order ID as " \
                                   "the payment reference. Your order will not be shipped until the funds have " \
                                   "cleared in our account."
    payment_method_check_text = "Check payments"
    payment_method_check_des_text = "Please send a check to Store Name, Store Street, Store Town, Store State / County," \
                                    " Store Postcode."
    payment_method_cash_text = "Cash on delivery"
    payment_method_cash_des_text = "Pay with cash upon delivery."
    payment_method_des_text = "Your personal data will be used to process your order, support your experience " \
                              "throughout this website, and for other purposes described in our privacy policy."

    login_tab_text = "Login"
    coupon_tab_text = "Coupon"
    billing_tab_text = "Billing & Shipping"
    payment_tab_text = "Payment"

    p_1_title_text = "Mens Comfy T Shirt  × 3"
    p_1_price_text = "£60.00"

    p_2_title_text = "Mens Trendy T Shirt  × 3"
    p_2_price_text = "£105.00"

    p_3_title_text = "Mens Stylish Shirt  × 2"
    p_3_price_text = "£150.00"

    p_4_title_text = "Mens Black Shirt  × 2"
    p_4_price_text = "£90.00"

    t_sub_total_label_text = "Subtotal"
    t_sub_total_amount_text = "£405.00"
    t_shipping_label_text = "Shipping\nFlat rate: £10.00"
    # t_shipping_amount_text = "Enter your address to view shipping options."
    t_total_label_text = "Total"
    t_total_amount_text = "£415.00"

    place_order_btn_text = "Place Order"

    shop_page = (By.XPATH, f'//*[@id="main"]/header/h1')
    shop_page_text = "Shop"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.woo_checkout)

    def check_cart_item(self, title, title_text, price, price_text, image):
        assert_that(self.browser.find_element(By.XPATH, title).text).is_equal_to(title_text)
        assert_that(self.browser.find_element(By.XPATH, price).text).is_equal_to(price_text)
        self.check_visibility(image, "Product Image is not visible.")

    def check_payment_gateway(self, gateway, gateway_text, gateway_des, gateway_des_text):
        assert_that(self.browser.find_element(By.XPATH, gateway).text).is_equal_to(gateway_text)
        self.browser.find_element(By.XPATH, gateway).click()
        time.sleep(.5)
        assert_that(self.browser.find_element(By.XPATH, gateway_des).text).is_equal_to(gateway_des_text)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1514)")
            time.sleep(1)

            # Login Form
            self.check_visibility(self.login_form_icon, "Login Form Icon is not visible.")

            assert_that(self.browser.find_element(*self.login_form).text).is_equal_to(self.login_form_text)

            if self.browser.find_element(*self.login_form_des).is_displayed():
                assert_that(1).is_equal_to("Login field is visible which should be hidden")
            else:
                assert_that(1).is_equal_to(1)

            self.browser.find_element(*self.login_form_expand).click()
            time.sleep(1)
            assert_that(self.browser.find_element(*self.login_form_des).text).is_equal_to(self.login_form_des_text)
            assert_that(self.browser.find_element(*self.login_username_label).text). \
                is_equal_to(self.login_username_label_text)
            assert_that(self.browser.find_element(*self.login_pass_label).text). \
                is_equal_to(self.login_pass_label_text)
            self.browser.find_element(*self.login_username_field).send_keys("admin")
            self.browser.find_element(*self.login_pass_field).send_keys("123456")

            self.browser.find_element(*self.remember_me_field).click()
            assert_that(self.browser.find_element(*self.remember_me_label).text). \
                is_equal_to(self.remember_me_label_text)
            assert_that(self.browser.find_element(*self.login_btn).text).is_equal_to("Login")

            assert_that(self.browser.find_element(*self.forget_pass_label).text). \
                is_equal_to(self.forget_pass_label_text)

            # Coupon Form
            self.check_visibility(self.coupon_form_icon, "Coupon Icon is not visible.")
            if self.browser.find_element(*self.coupon_form_des).is_displayed():
                assert_that(1).is_equal_to("Coupon field is visible which should be hidden")
            else:
                assert_that(1).is_equal_to(1)
            self.browser.find_element(*self.coupon_form_expand).click()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.coupon_form_des).text).is_equal_to(self.coupon_form_des_text)
            self.browser.find_element(*self.coupon_form_field).send_keys("Get50OffNow")
            assert_that(self.browser.find_element(*self.coupon_btn).text).is_equal_to("Apply Coupon")

            self.browser.find_element(*self.login_form_expand).click()
            time.sleep(1)
            self.browser.find_element(*self.coupon_form_expand).click()

            # Ship to Diff
            assert_that(self.browser.find_element(*self.ship_diff_address_label).text). \
                is_equal_to(self.ship_diff_address_label_text)

            if self.browser.find_element(By.XPATH, self.shipping_fname_field).is_displayed():
                assert_that(1).is_equal_to("Shipping details is visible which should be hidden.")
            else:
                assert_that(1).is_equal_to(1)

            time.sleep(.5)
            self.browser.find_element(*self.ship_diff_address_field).click()
            time.sleep(.5)
            self.check_visibility(self.shipping_fname_field, "Shipping details is hidden which should be visible.")

            # Create an Account
            self.browser.execute_script("window.scrollTo(0, 2909)")
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.create_acc_field_label).text). \
                is_equal_to(self.create_acc_field_label_text)

            if self.browser.find_element(*self.create_acc_pass_field).is_displayed():
                assert_that(1).is_equal_to("Create account password is visible which should be hidden.")
            else:
                assert_that(1).is_equal_to(1)

            self.browser.execute_script("window.scrollTo(0, 2666)")
            time.sleep(1)
            self.browser.find_element(*self.create_acc_field).click()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.create_acc_pass_label).text). \
                is_equal_to(self.create_acc_pass_label_text)
            self.browser.find_element(*self.create_acc_pass_field).send_keys("123456")

            # Payment Method
            assert_that(self.browser.find_element(*self.payment_method_label).text). \
                is_equal_to(self.payment_method_label_text)
            self.check_payment_gateway(self.payment_method_bank, self.payment_method_bank_text,
                                       self.payment_method_bank_des, self.payment_method_bank_des_text)
            self.check_payment_gateway(self.payment_method_check, self.payment_method_check_text,
                                       self.payment_method_check_des, self.payment_method_check_des_text)
            self.check_payment_gateway(self.payment_method_cash, self.payment_method_cash_text,
                                       self.payment_method_cash_des, self.payment_method_cash_des_text)
            assert_that(self.browser.find_element(*self.payment_method_des).text).is_equal_to(self.payment_method_des_text)

            # Go to Multi Step
            self.browser.execute_script("window.scrollTo(0, 642)")
            time.sleep(1)
            self.browser.find_element(*self.go_to_multi_step_checkout).click()
            time.sleep(1)
            self.browser.execute_script("window.scrollTo(0, 963)")
            time.sleep(.5)

            assert_that(self.browser.find_element(*self.login_tab).text).is_equal_to(self.login_tab_text)
            assert_that(self.browser.find_element(*self.coupon_tab).text).is_equal_to(self.coupon_tab_text)
            assert_that(self.browser.find_element(*self.billing_tab).text).is_equal_to(self.billing_tab_text)
            assert_that(self.browser.find_element(*self.payment_tab).text).is_equal_to(self.payment_tab_text)

            # Login Tab
            self.check_visibility(self.multi_login_form_icon, "Multi Login form icon is not visible.")
            assert_that(self.browser.find_element(*self.multi_login_form).text).is_equal_to(self.login_form_text)
            self.browser.find_element(*self.next_btn).click()
            # Coupon Tab
            self.check_visibility(self.multi_coupon_form_icon, "Multi coupon form icon is not visible.")
            assert_that(self.browser.find_element(*self.multi_coupon_form).text).is_equal_to(self.coupon_form_text)
            self.browser.find_element(*self.next_btn).click()

            # Billing & Shipping Tab
            assert_that(self.browser.find_element(*self.billing_label).text).is_equal_to(self.billing_label_text)
            # Billing
            assert_that(self.browser.find_element(*self.billing_fname_label).text).is_equal_to(self.fname_label_text)
            self.browser.find_element(*self.billing_fname_field).send_keys("Mr.")
            assert_that(self.browser.find_element(*self.billing_lname_label).text).is_equal_to(self.lname_label_text)
            self.browser.find_element(*self.billing_lname_field).send_keys("Sabbir")
            assert_that(self.browser.find_element(*self.billing_com_label).text).is_equal_to(self.com_label_text)
            self.browser.find_element(*self.billing_com_field).send_keys("WPDeveloper")
            assert_that(self.browser.find_element(*self.billing_country_label).text).is_equal_to(self.country_label_text)
            self.browser.find_element(*self.billing_country_list).click()
            time.sleep(.5)
            self.browser.find_element(*self.billing_country_list).click()
            assert_that(self.browser.find_element(*self.billing_address_label).text).is_equal_to(self.address_label_text)
            self.browser.find_element(*self.billing_address_field_1).send_keys("New Street")
            self.browser.find_element(*self.billing_address_field_2).send_keys("Boxy")
            assert_that(self.browser.find_element(*self.billing_city_label).text).is_equal_to(self.city_label_text)
            self.browser.find_element(*self.billing_city_field).send_keys("New Town")
            assert_that(self.browser.find_element(*self.billing_district_label).text). \
                is_equal_to(self.district_label_text)
            self.browser.find_element(*self.billing_district_field).send_keys("Geodon")
            assert_that(self.browser.find_element(*self.billing_zip_label).text).is_equal_to(self.zip_label_text)
            self.browser.find_element(*self.billing_zip_field).send_keys("1206")
            assert_that(self.browser.find_element(*self.billing_phone_label).text).is_equal_to(self.phone_label_text)
            self.browser.find_element(*self.billing_phone_field).send_keys("0123456789")
            assert_that(self.browser.find_element(*self.billing_email_label).text).is_equal_to(self.email_label_text)
            self.browser.find_element(*self.billing_email_field).send_keys("testerbhaai@gmail.com")
            # Create an Account
            self.browser.execute_script("window.scrollTo(0, 2093)")
            time.sleep(1)
            assert_that(self.browser.find_element(*self.create_acc_field_label).text). \
                is_equal_to(self.create_acc_field_label_text)
            self.browser.find_element(*self.create_acc_field).click()
            time.sleep(1)
            assert_that(self.browser.find_element(*self.create_acc_pass_label).text). \
                is_equal_to(self.create_acc_pass_label_text)
            self.browser.find_element(*self.create_acc_pass_field).send_keys("123456")
            # Ship to Diff
            assert_that(self.browser.find_element(*self.ship_diff_address_label).text). \
                is_equal_to(self.ship_diff_address_label_text)
            self.browser.find_element(*self.ship_diff_address_field).click()
            time.sleep(1)
            assert_that(self.browser.find_element(*self.shipping_fname_label).text).is_equal_to(self.fname_label_text)
            self.browser.find_element(By.XPATH, self.shipping_fname_field).send_keys("Mr.")
            assert_that(self.browser.find_element(*self.shipping_lname_label).text).is_equal_to(self.lname_label_text)
            self.browser.find_element(*self.shipping_lname_field).send_keys("Sabbir")
            assert_that(self.browser.find_element(*self.shipping_com_label).text).is_equal_to(self.com_label_text)
            self.browser.find_element(*self.shipping_com_field).send_keys("WPDeveloper")
            assert_that(self.browser.find_element(*self.shipping_country_label).text).is_equal_to(self.country_label_text)
            self.browser.execute_script("window.scrollTo(0, 2420)")
            time.sleep(.5)
            self.browser.find_element(*self.shipping_country_list).click()
            time.sleep(.5)
            self.browser.execute_script("window.scrollTo(0, 2420)")
            self.browser.find_element(*self.shipping_country_list).click()
            assert_that(self.browser.find_element(*self.shipping_address_label).text).is_equal_to(self.address_label_text)
            self.browser.find_element(*self.shipping_address_field_1).send_keys("New Street")
            self.browser.find_element(*self.shipping_address_field_2).send_keys("Boxy")
            assert_that(self.browser.find_element(*self.shipping_city_label).text).is_equal_to(self.city_label_text)
            self.browser.find_element(*self.shipping_city_field).send_keys("New Town")
            assert_that(self.browser.find_element(*self.shipping_district_label).text). \
                is_equal_to(self.district_label_text)
            self.browser.find_element(*self.shipping_district_field).send_keys("Geodon")
            self.browser.execute_script("window.scrollTo(0, 2902)")
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.shipping_zip_label).text).is_equal_to(self.zip_label_text)
            self.browser.find_element(*self.shipping_zip_field).send_keys("1206")

            # Other notes
            assert_that(self.browser.find_element(*self.other_note_label).text).is_equal_to(self.other_note_label_text)
            self.browser.find_element(*self.other_note_field).send_keys("Lorem Ipsum is simply a dummy text.")
            self.browser.find_element(*self.next_btn).click()

            # payment Tab
            time.sleep(2)
            assert_that(self.browser.find_element(*self.payment_method_label).text). \
                is_equal_to(self.payment_method_label_text)
            assert_that(self.browser.find_element(By.XPATH, self.payment_method_bank).text). \
                is_equal_to(self.payment_method_bank_text)
            time.sleep(1.5)
            self.browser.find_element(By.XPATH, self.payment_method_bank).click()
            assert_that(self.browser.find_element(By.XPATH, self.payment_method_check).text). \
                is_equal_to(self.payment_method_check_text)
            time.sleep(1.5)
            self.browser.find_element(By.XPATH, self.payment_method_check).click()
            assert_that(self.browser.find_element(By.XPATH, self.payment_method_cash).text). \
                is_equal_to(self.payment_method_cash_text)
            time.sleep(1.5)
            self.browser.find_element(By.XPATH, self.payment_method_cash).click()
            assert_that(self.browser.find_element(*self.payment_method_des).text).is_equal_to(self.payment_method_des_text)
            self.browser.find_element(*self.prev_btn).click()
            time.sleep(1.5)
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1.5)
            self.browser.find_element(*self.prev_btn).click()
            time.sleep(1.5)
            self.browser.execute_script("window.scrollTo(0, 902)")
            time.sleep(1.5)
            self.browser.find_element(*self.prev_btn).click()
            time.sleep(1.5)
            self.browser.find_element(*self.next_btn).click()
            time.sleep(1.5)
            self.browser.find_element(*self.next_btn).click()
            time.sleep(1.5)
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1.5)
            self.browser.find_element(*self.next_btn).click()
            time.sleep(1.5)

            self.check_cart_item(self.p_title_1, self.p_1_title_text, self.p_price_1, self.p_1_price_text, self.p_img_1)
            assert_that(self.browser.find_element(*self.t_sub_total_label).text).is_equal_to(self.t_sub_total_label_text)
            assert_that(self.browser.find_element(*self.t_shipping_label).text).is_equal_to(self.t_shipping_label_text)
            assert_that(self.browser.find_element(*self.t_total_label).text).is_equal_to(self.t_total_label_text)

            assert_that(self.browser.find_element(*self.t_sub_total_amount).text).is_equal_to(self.t_sub_total_amount_text)
            # assert_that(self.browser.find_element(*self.t_shipping_amount).text).is_equal_to(self.t_shipping_amount_text)
            assert_that(self.browser.find_element(*self.t_total_amount).text).is_equal_to(self.t_total_amount_text)

            assert_that(self.browser.find_element(*self.place_order_btn).text).is_equal_to(self.place_order_btn_text)

            self.browser.find_element(*self.continue_shop).click()
            assert_that(self.browser.find_element(*self.shop_page).text).is_equal_to(self.shop_page_text)
            self.browser.back()




