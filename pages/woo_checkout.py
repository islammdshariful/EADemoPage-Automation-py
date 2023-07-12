from utils.config import *


class WooCheckout(BasePage, Helper):
    widget = '//*[@id="post-259772"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Woo Checkout'
    doc_link = '//*[@id="post-259772"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "WOO CHECKOUT"

    go_to_multi_step_checkout = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div'
                                           f'/section[2]/div/div/div[1]/div/div/div/div/div/a/div/span[2]')

    login_form_icon = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                                 f'/div/div[4]/div[1]')
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
    coupon_form_icon = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                                  f'/div/div[5]/div[1]')
    coupon_form_expand = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div'
                                    f'/div/div/div[5]/div[2]/div/a')
    coupon_form_des = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                                 f'/div/div[5]/form/p[1]')
    coupon_form_field = (By.XPATH, f'//*[@id="coupon_code"]')
    coupon_btn = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div'
                            f'/div[5]/form/p[3]/button')

    multi_login_form_icon = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div' \
                                       f'/div/div/div[2]/div/div[1]/div[2]/div[1]')
    multi_login_form = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                                  f'/div/div[2]/div/div[1]/div[2]/div[2]/div')

    multi_coupon_form = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                                   f'/div/div[2]/div/div[1]/div[3]/div[2]/div')
    multi_coupon_form_icon = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div' \
                                        f'/div/div/div[2]/div/div[1]/div[3]/div[2]/div')

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
    shipping_fname_field = (By.XPATH, f'//*[@id="shipping_first_name"]')
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
    payment_method_bank = (By.XPATH, f'//*[@id="payment"]/ul/li[1]/label')
    payment_method_bank_des = (By.XPATH, f'//*[@id="payment"]/ul/li[1]/div/p')
    payment_method_check = (By.XPATH, f'//*[@id="payment"]/ul/li[2]/label')
    payment_method_check_des = (By.XPATH, f'//*[@id="payment"]/ul/li[2]/div/p')
    payment_method_cash = (By.XPATH, f'//*[@id="payment"]/ul/li[3]/label')
    payment_method_cash_des = (By.XPATH, f'//*[@id="payment"]/ul/li[3]/div/p')
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

    p_img_1 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                         f'/div[2]/div/div[2]/div/div/ul/li[1]/div[1]/div[1]/img')
    p_title_1 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[1]/div[1]/div[2]')
    p_quantity_1 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                              f'/div[2]/div/div[2]/div/div/ul/li[1]/div[1]/div[2]/strong')
    p_price_1 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[1]/div[2]/span')

    p_img_2 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                         f'/div[2]/div/div[2]/div/div/ul/li[2]/div[1]/div[1]/img')
    p_title_2 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[2]/div[1]/div[2]')
    p_quantity_2 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                              f'/div[2]/div/div[2]/div/div/ul/li[2]/div[1]/div[2]/strong')
    p_price_2 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[2]/div[2]/span')

    p_img_3 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                         f'/div[2]/div/div[2]/div/div/ul/li[3]/div[1]/div[1]/img')
    p_title_3 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[3]/div[1]/div[2]')
    p_quantity_3 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                              f'/div[2]/div/div[2]/div/div/ul/li[3]/div[1]/div[2]/strong')
    p_price_3 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[3]/div[2]/span')

    p_img_4 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                         f'/div[2]/div/div[2]/div/div/ul/li[4]/div[1]/div[1]/img')
    p_title_4 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[4]/div[1]/div[2]')
    p_quantity_4 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                              f'/div[2]/div/div[2]/div/div/ul/li[4]/div[1]/div[2]/strong')
    p_price_4 = (By.XPATH, f'//*[@id="post-260239"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div' \
                           f'/div[2]/div/div[2]/div/div/ul/li[4]/div[2]/span')

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

    lost_password = (By.XPATH, "//p[@class='lost_password']")

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

    scroll_1 = (By.XPATH, '//*[@id="post-259772"]/div/div/div/div/section[2]/div/div'
                          '/div/div/div/div/div/div/div/div[2]/div/div/div[1]')
    scroll_2 = (By.XPATH, f'//*[@id="post-259772"]/div/div/div/div/section[2]/div/div'
                          f'/div/div/div/div/div/div/div/div[4]/div[2]/div/a')
    scroll_3 = (By.XPATH, "//span[normalize-space()='Ship to a different address?']")
    scroll_4 = (By.XPATH, "//span[normalize-space()='Split']")
    scroll_5 = (By.XPATH, "//div[@class='shipping-area']")

    scroll_to_multiple_steps_button = (By.XPATH, "//section[@data-id='2d31e423']")
    scroll_to_default_steps_button = (By.XPATH, "//section[@data-id='6c694cb1']")

    def __init__(self, browser):
        super().__init__(browser)

    def check_cart_item(self, title, title_text, price, price_text, image):
        self.is_visible(title, title_text)
        self.is_visible(price, price_text)
        self.is_visible(image, "Product Image is not visible.")

    def check_payment_gateway(self, gateway, gateway_text, gateway_des, gateway_des_text):
        self.check_text_matches_with(gateway, gateway_text)
        self.do_click(gateway)
        self.check_text_matches_with(gateway_des, gateway_des_text)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.woo_checkout)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to_element(self.go_to_multi_step_checkout)

                """Default Checkout Page Checking"""
                """Checking login form"""
                self.is_visible(self.login_form_icon, "Login Form Icon is not visible.")
                self.check_text_matches_with(self.login_form, self.login_form_text)
                if self.is_displaying(*self.login_form_des):
                    assert_that(1).is_equal_to("Login field is visible which should be hidden")
                self.do_click(self.login_form_expand)
                self.check_text_matches_with(self.login_form_des, self.login_form_des_text)
                self.check_text_matches_with(self.login_username_label, self.login_username_label_text)
                self.check_text_matches_with(self.login_pass_label, self.login_pass_label_text)
                self.do_clear_field(self.login_username_field)
                self.do_send_keys(self.login_username_field, "admin")
                self.do_clear_field(self.login_pass_field)
                self.do_send_keys(self.login_pass_field, "123456")
                self.do_click(self.remember_me_field)
                self.check_text_matches_with(self.remember_me_label, self.remember_me_label_text)
                self.check_text_matches_with(self.login_btn, "Login")
                self.check_text_matches_with(self.forget_pass_label, self.forget_pass_label_text)

                """Checking coupon form"""
                self.is_visible(self.coupon_form_icon, "Coupon Icon is not visible.")
                if self.is_displaying(*self.coupon_form_des):
                    assert_that(1).is_equal_to("Coupon field is visible which should be hidden")
                self.scroll_to_element(self.lost_password)
                self.do_click(self.coupon_form_expand)
                self.check_text_matches_with(self.coupon_form_des, self.coupon_form_des_text)
                self.do_clear_field(self.coupon_form_field)
                self.do_send_keys(self.coupon_form_field, "Get50OffNow")
                self.check_text_matches_with(self.coupon_btn, "Apply Coupon")
                self.scroll_to_element(self.scroll_1)
                self.do_click(self.login_form_expand)
                self.scroll_to_element(self.scroll_2)
                time.sleep(1)
                self.do_click(self.coupon_form_expand)

                """Ship to different adress"""
                self.check_text_matches_with(self.ship_diff_address_label, self.ship_diff_address_label_text)
                if self.is_displaying(*self.shipping_fname_field):
                    assert_that(1).is_equal_to("Shipping details is visible which should be hidden.")
                self.do_click(self.ship_diff_address_field)
                self.is_visible(self.shipping_fname_field, "Shipping details is hidden which should be visible.")

                """Create an account"""
                self.scroll_to(2909)
                self.check_text_matches_with(self.create_acc_field_label, self.create_acc_field_label_text)
                if self.is_displaying(*self.create_acc_pass_field):
                    assert_that(1).is_equal_to("Create account password is visible which should be hidden.")
                self.scroll_to(2666)
                self.do_click(self.create_acc_field)
                self.check_text_matches_with(self.create_acc_pass_label, self.create_acc_pass_label_text)
                self.do_clear_field(self.create_acc_pass_field)
                self.do_send_keys(self.create_acc_pass_field, "123456")

                """Payment method"""
                self.scroll_to(2984)
                self.check_text_matches_with(self.payment_method_label, self.payment_method_label_text)
                self.check_payment_gateway(self.payment_method_bank, self.payment_method_bank_text,
                                           self.payment_method_bank_des, self.payment_method_bank_des_text)
                self.check_payment_gateway(self.payment_method_check, self.payment_method_check_text,
                                           self.payment_method_check_des, self.payment_method_check_des_text)
                self.check_payment_gateway(self.payment_method_cash, self.payment_method_cash_text,
                                           self.payment_method_cash_des, self.payment_method_cash_des_text)
                self.check_text_matches_with(self.payment_method_des, self.payment_method_des_text)

                # ------ It needs modification on scrolls ------
                # """Multi Step Checkout Page Checking"""
                # self.scroll_to_element(self.scroll_to_multiple_steps_button)
                # self.do_click(self.go_to_multi_step_checkout)
                # # self.scroll_to_element(self.scroll_to_default_steps_button)
                # """Checking tab labels"""
                # self.check_text_matches_with(self.login_tab, self.login_tab_text)
                # self.check_text_matches_with(self.coupon_tab, self.coupon_tab_text)
                # self.check_text_matches_with(self.billing_tab, self.billing_tab_text)
                # self.check_text_matches_with(self.payment_tab, self.payment_tab_text)
                #
                # """Checking login form"""
                # self.is_visible(self.multi_login_form_icon, "Multi Login form icon is not visible.")
                # assert_that(self.browser.find_element(*self.multi_login_form).text).is_equal_to(self.login_form_text)
                # self.do_click(self.next_btn)
                # """Checking coupon form"""
                # self.is_visible(self.multi_coupon_form_icon, "Multi coupon form icon is not visible.")
                # self.check_text_matches_with(self.multi_coupon_form, self.coupon_form_text)
                # self.do_click(self.next_btn)
                #
                # """Checking billing tab"""
                # self.check_text_matches_with(self.billing_label, self.billing_label_text)
                # self.check_text_matches_with(self.billing_fname_label, self.fname_label_text)
                # self.do_clear_field(self.billing_fname_field)
                # self.do_send_keys(self.billing_fname_field, "Mr.")
                # self.check_text_matches_with(self.billing_lname_label, self.lname_label_text)
                # self.do_clear_field(self.billing_lname_field)
                # self.do_send_keys(self.billing_lname_field, "Sabbir")
                # self.check_text_matches_with(self.billing_com_label, self.com_label_text)
                # self.do_clear_field(self.billing_com_field)
                # self.do_send_keys(self.billing_com_field, "WPDeveloper")
                # self.check_text_matches_with(self.billing_country_label, self.country_label_text)
                # self.browser.find_element(*self.billing_country_list).click()
                # self.browser.find_element(*self.billing_country_list).click()
                # self.check_text_matches_with(self.billing_address_label, self.address_label_text)
                # self.do_clear_field(self.billing_address_field_1)
                # self.do_send_keys(self.billing_address_field_1, "New Street")
                # self.do_clear_field(self.billing_address_field_2)
                # self.do_send_keys(self.billing_address_field_2, "Boxy")
                # self.check_text_matches_with(self.billing_city_label, self.city_label_text)
                # self.do_clear_field(self.billing_city_field)
                # self.do_send_keys(self.billing_city_field, "New Town")
                # self.check_text_matches_with(self.billing_district_label, self.district_label_text)
                # self.do_clear_field(self.billing_district_field)
                # self.do_send_keys(self.billing_district_field, "Geodon")
                # self.check_text_matches_with(self.billing_zip_label, self.zip_label_text)
                # self.do_clear_field(self.billing_zip_field)
                # self.do_send_keys(self.billing_zip_field, "B46 1AA")
                # self.check_text_matches_with(self.billing_phone_label, self.phone_label_text)
                # self.do_clear_field(self.billing_phone_field)
                # self.do_send_keys(self.billing_phone_field, "0123456789")
                # self.check_text_matches_with(self.billing_email_label, self.email_label_text)
                # self.do_clear_field(self.billing_email_field)
                # self.do_send_keys(self.billing_email_field, "testerbhaai@gmail.com")
                # """Create an account"""
                # self.scroll_to_element(self.billing_zip_field)
                # self.check_text_matches_with(self.create_acc_field_label, self.create_acc_field_label_text)
                # self.browser.find_element(*self.create_acc_field).click()
                # self.check_text_matches_with(self.create_acc_pass_label, self.create_acc_pass_label_text)
                # self.do_clear_field(self.create_acc_pass_field)
                # self.do_send_keys(self.create_acc_pass_field, "123456")
                # """Ship to different address"""
                # self.check_text_matches_with(self.ship_diff_address_label, self.ship_diff_address_label_text)
                # self.do_click(self.ship_diff_address_field)
                # self.check_text_matches_with(self.shipping_fname_label, self.fname_label_text)
                # self.do_clear_field(self.shipping_fname_field)
                # self.do_send_keys(self.shipping_fname_field, "Mr.")
                # self.check_text_matches_with(self.shipping_lname_label, self.lname_label_text)
                # self.do_clear_field(self.shipping_lname_field)
                # self.do_send_keys(self.shipping_lname_field, "Sabbir")
                # self.check_text_matches_with(self.shipping_com_label, self.com_label_text)
                # self.do_clear_field(self.shipping_com_field)
                # self.do_send_keys(self.shipping_com_field, "WPDeveloper")
                # self.check_text_matches_with(self.shipping_country_label, self.country_label_text)
                # self.scroll_to_element(self.ship_diff_address_field)
                # self.do_click(self.shipping_country_list)
                # self.scroll_to_element(self.ship_diff_address_field)
                # self.do_click(self.shipping_country_list)
                # self.check_text_matches_with(self.shipping_address_label, self.address_label_text)
                # self.do_clear_field(self.shipping_address_field_1)
                # self.do_send_keys(self.shipping_address_field_1, "New Street")
                # self.do_clear_field(self.shipping_address_field_2)
                # self.do_send_keys(self.shipping_address_field_2, "Boxy")
                # self.check_text_matches_with(self.shipping_city_label, self.city_label_text)
                # self.do_clear_field(self.shipping_city_field)
                # self.do_send_keys(self.shipping_city_field, "New Town")
                # self.check_text_matches_with(self.shipping_district_label, self.district_label_text)
                # self.do_clear_field(self.shipping_district_field)
                # self.do_send_keys(self.shipping_district_field, "Geodon")
                # self.scroll_to_element(self.shipping_address_field_2)
                # self.check_text_matches_with(self.shipping_zip_label, self.zip_label_text)
                # self.do_clear_field(self.shipping_zip_field)
                # self.do_send_keys(self.shipping_zip_field, "B46 1AA")
                #
                # """Billing notes"""
                # self.check_text_matches_with(self.other_note_label, self.other_note_label_text)
                # self.do_clear_field(self.other_note_field)
                # self.do_send_keys(self.other_note_field, "Lorem Ipsum is simply a dummy text.")
                # self.do_click(self.next_btn)
                #
                # """Checking payment tab"""
                # # self.scroll_to_element(self.scroll_to_default_steps_button)
                # self.check_text_matches_with(self.payment_method_label, self.payment_method_label_text)
                # self.check_text_matches_with(self.payment_method_bank, self.payment_method_bank_text)
                # self.do_click(self.payment_method_bank)
                # self.check_text_matches_with(self.payment_method_check, self.payment_method_check_text)
                # self.do_click(self.payment_method_check)
                # self.check_text_matches_with(self.payment_method_cash, self.payment_method_cash_text)
                # self.do_click(self.payment_method_cash)
                # self.check_text_matches_with(self.payment_method_des, self.payment_method_des_text)
                # self.scroll_to_element(self.payment_method_cash)
                # self.do_click(self.prev_btn)
                # self.scroll_to_element(self.scroll_3)
                # self.do_click(self.prev_btn)
                # self.scroll_to_element(self.scroll_4)
                # self.do_click(self.prev_btn)
                # self.do_click(self.next_btn)
                # self.do_click(self.next_btn)
                # self.scroll_to_element(self.scroll_3)
                # self.do_click(self.next_btn)
                # self.check_cart_item(self.p_title_1, self.p_1_title_text, self.p_price_1, self.p_1_price_text,
                #                      self.p_img_1)
                # self.check_text_matches_with(self.t_sub_total_label, self.t_sub_total_label_text)
                # self.check_text_matches_with(self.t_shipping_label, self.t_shipping_label_text)
                # self.check_text_matches_with(self.t_total_label, self.t_total_label_text)
                # self.check_text_matches_with(self.t_sub_total_amount, self.t_sub_total_amount_text)
                # # self.check_text_matches_with(self.t_shipping_amount, self.t_shipping_amount_text)
                # self.check_text_matches_with(self.t_total_amount, self.t_total_amount_text)
                # self.check_text_matches_with(self.place_order_btn, self.place_order_btn_text)
                # self.scroll_to_element(self.scroll_5)
                # self.do_click(self.continue_shop)
                # self.check_text_matches_with(self.shop_page, self.shop_page_text)
                # self.go_back()
