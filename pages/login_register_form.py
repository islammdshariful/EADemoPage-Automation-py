from utils.config import *


class LoginRegisterForm(BasePage, Helper):
    widget = '//*[@id="post-262414"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Login Register Form'
    doc_link = '//*[@id="post-262414"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[5]/div/div/a/span/span'
    doc_name = "LOGIN | REGISTER FORM"

    reg_img = (By.XPATH, f'//*[@id="eael-register-form-wrapper"]/div/div[1]')
    reg_title = (By.XPATH, f'//*[@id="eael-register-form-wrapper"]/div/div[2]/div/div/h4')

    reg_fname_field = (By.XPATH, f'//*[@id="form-field-first_name"]')
    reg_lname_field = (By.XPATH, f'//*[@id="form-field-last_name"]')
    reg_email_field = (By.XPATH, f'//*[@id="form-field-email"]')
    reg_pass_field = (By.XPATH, f'//*[@id="form-field-password"]')
    reg_con_pass_field = (By.XPATH, f'//*[@id="form-field-confirm_pass"]')
    reg_terms_toggle = (By.XPATH, f'//*[@id="eael_accept_tnc"]')
    reg_terms_label_1 = (By.XPATH, f'//*[@id="eael-register-form"]/div[6]/label')
    reg_terms_label_2 = (By.XPATH, f'//*[@id="eael-lr-tnc-link"]')
    reg_recaptcha = (By.XPATH, f'//*[@id="recaptcha-anchor"]/div[1]')
    reg_have_acc_label = (By.XPATH, f'//*[@id="eael-lr-login-toggle"]')
    reg_login_label = (By.XPATH, f'//*[@id="eael-login-form-wrapper"]/div/div[2]/div/div/h4')
    reg_reg_now_label = (By.XPATH, f'//*[@id="eael-lr-reg-toggle"]')
    create_acc_btn = (By.XPATH, f'//*[@id="eael-register-submit"]')
    reg_recaptcha_iframe = (By.XPATH, f'//*[@id="register-recaptcha-node-be27d56"]/div/div/iframe')

    login_img = (By.XPATH, f'//*[@id="eael-login-form-wrapper"]/div/div/div/div/img')
    login_username_label = (By.XPATH, f'//*[@id="eael-login-form"]/div[1]/label')
    login_username_field = (By.XPATH, f'//*[@id="eael-user-login"]')
    login_pass_label = (By.XPATH, f'//*[@id="eael-login-form"]/div[2]/label')
    login_pass_field = (By.XPATH, f'//*[@id="eael-user-password"]')
    login_rem_label = (By.XPATH, f'//*[@id="eael-login-form"]/div[3]/p[1]/label')
    login_rem_field = (By.XPATH, f'//*[@id="rememberme"]')
    login_forget_label = (By.XPATH, f'//*[@id="eael-login-form"]/div[3]/p[2]/a')
    login_signup_btn = (By.XPATH, f'//*[@id="eael-login-submit"]')
    login_reg_now_btn = (By.XPATH, f'//*[@id="eael-lr-reg-toggle"]')
    login_have_acc_label = (By.XPATH, f'//*[@id="eael-lr-login-toggle"]')

    login_form_image = (By.XPATH, f'//*[@id="eael-login-form-wrapper"]/div/div/div/div/img')
    login_form_username_label = (By.XPATH, f"//div[@class='elementor-element elementor-element-dc7ae1a elementor-widget"
                                           f" elementor-widget-eael-login-register']//label[@for='eael-user-login']"
                                           f"[normalize-space()='Username or Email Address']")
    login_form_username_field = (By.XPATH, f"//div[@class='eael-login-registration-wrapper ']//"
                                           f"input[@id='eael-user-login']")
    login_form_password_label = (By.XPATH, f"//div[@class='elementor-element elementor-element-dc7ae1a elementor-widget"
                                           f" elementor-widget-eael-login-register']//label[@for='eael-user-password']"
                                           f"[normalize-space()='Password']")
    login_form_password_field = (By.XPATH, f"//div[@class='eael-login-registration-wrapper ']//"
                                           f"input[@id='eael-user-password']")
    login_form_password_visibility_button = (By.XPATH, f'//*[@id="wp-hide-pw"]/span')
    login_form_forgot_password = (By.XPATH, f"//div[@class='elementor-element elementor-element-dc7ae1a "
                                            f"elementor-widget elementor-widget-eael-login-register']//"
                                            f"p[@class='forget-pass']")
    login_form_remember_label = (By.XPATH, f"//div[@class='elementor-element elementor-element-dc7ae1a elementor-widget"
                                           f" elementor-widget-eael-login-register']//label[@for='rememberme']"
                                           f"[normalize-space()='Remember Me']")
    login_form_remember_field = (By.XPATH, f"//div[@class='eael-login-registration-wrapper ']//"
                                           f"input[@id='rememberme']")
    login_form_signin_button = (By.XPATH, f"//div[@class='eael-login-registration-wrapper ']//"
                                          f"input[@id='eael-login-submit']")

    wordpress_login = (By.XPATH, f'//*[@id="login"]/h1/a')

    success_msg = (By.XPATH, f'//*[@id="fluentform_1_success"]')
    success_msg_text = "Thank you for your message. We will get in touch with you shortly"
    error_msg = (By.XPATH, f'//*[@id="eael-login-form"]/div[5]/div')
    error_msg_text = "You have used an invalid email"

    reg_login_label_Text = "Welcome Back, Please login to your account"
    reg_fname_placeholder_text = "First Name"
    reg_lname_placeholder_text = "Last Name"
    reg_email_placeholder_text = "Email"
    reg_pass_placeholder_text = "Password"
    reg_con_pass_placeholder_text = "Confirm Password"
    reg_title_text = "Create an account"
    reg_terms_label_1_text = "I Accept"
    reg_terms_label_2_text = "the Terms and Conditions."
    reg_have_acc_label_text = "Already have an account? Sign In"

    login_username_label_text = "Username or Email Address"
    login_pass_label_text = "Password"
    login_rem_label_text = "Remember Me"
    login_forget_label_text = "Forgot password?"

    scroll = (By.XPATH, f"//div[@class='elementor-element elementor-element-39172dd6 elementor-widget__width-initial "
                        f"elementor-widget elementor-widget-text-editor']")

    def __init__(self, browser):
        super().__init__(browser)

    def registration_form(self):
        self.scroll_to(1063)
        """Switching to login form"""
        self.check_text_matches_with(self.reg_have_acc_label, self.reg_have_acc_label_text)
        self.do_click(self.reg_have_acc_label),
        self.is_visible(self.login_img, "Login Image not visible.")
        """Check login form"""
        self.check_text_matches_with(self.reg_login_label, self.reg_login_label_Text)
        self.check_text_matches_with(self.login_username_label, self.login_username_label_text)
        self.check_text_matches_with(self.login_pass_label, self.login_pass_label_text)
        """Entering login field"""
        self.do_send_keys(self.login_username_field, "testerbhaai@gmail.com")
        self.do_send_keys(self.login_pass_field, "123456")
        """Switching to registration form"""
        self.do_click(self.reg_reg_now_label)
        """Checking registration form"""
        assert_that(self.get_element(self.reg_fname_field).get_attribute("placeholder")). \
            is_equal_to(self.reg_fname_placeholder_text)
        assert_that(self.get_element(self.reg_lname_field).get_attribute("placeholder")). \
            is_equal_to(self.reg_lname_placeholder_text)
        assert_that(self.get_element(self.reg_email_field).get_attribute("placeholder")). \
            is_equal_to(self.reg_email_placeholder_text)
        assert_that(self.get_element(self.reg_pass_field).get_attribute("placeholder")). \
            is_equal_to(self.reg_pass_placeholder_text)
        assert_that(self.get_element(self.reg_con_pass_field).get_attribute("placeholder")). \
            is_equal_to(self.reg_con_pass_placeholder_text)
        self.is_visible(self.reg_img, " Registration Image not visible.")
        """"Entering registration fields"""
        self.do_send_keys(self.reg_fname_field, "Tester")
        self.do_send_keys(self.reg_lname_field, "Bhaai")
        self.do_send_keys(self.reg_email_field, "testerbhaai@gmail.com")
        self.do_send_keys(self.reg_pass_field, "123456")
        self.do_send_keys(self.reg_con_pass_field, "123456")
        """Verify reCAPTCHA"""
        self.do_click(self.reg_terms_toggle)
        self.switch_to_frame(self.reg_recaptcha_iframe)
        self.do_click(self.reg_recaptcha)
        self.switch_frame_to_default()

    def login_form(self):
        self.scroll_to_element(self.scroll)
        self.do_click(self.login_form_username_field)
        self.do_send_keys(self.login_form_username_field, 'testerbhaai')
        self.do_click(self.login_form_password_field)
        self.do_send_keys(self.login_form_password_field, '123456')
        # self.do_click(self.login_form_password_visibility_button)
        self.do_click(self.login_form_remember_field)
        time.sleep(1)
        self.get_element(self.login_form_remember_field).is_selected()

        # self.do_click(self.login_form_signin_button)
        # self.does_element_has_text(self.error_msg, self.error_msg_text)

        self.check_text_matches_with(self.login_form_username_label, self.login_username_label_text)
        self.check_text_matches_with(self.login_form_password_label, self.login_pass_label_text)
        self.check_text_matches_with(self.login_form_remember_label, self.login_rem_label_text)
        self.check_text_matches_with(self.login_form_forgot_password, self.login_forget_label_text)
        assert_that(self.get_element(self.login_form_signin_button).get_attribute("value")). \
            is_equal_to('Sign In')

        # self.do_click(self.login_form_forgot_password)
        # self.is_visible(self.wordpress_login, "Logo not visible")
        # self.check_title("Lost Password ‹ Essential Addons for Elementor — WordPress")
        # self.go_back()

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.login_register_form)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                # Check Registration Form 1
                # self.registration_form()
                # Check Login Form
                self.login_form()







