from selenium.webdriver import ActionChains

from utils.config import *


class LoginRegisterForm:
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

    success_msg = f'//*[@id="fluentform_1_success"]'
    success_msg_text = "Thank you for your message. We will get in touch with you shortly"

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

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(login_register_form)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1063)")

            assert_that(self.browser.find_element(*self.reg_have_acc_label).text).\
                is_equal_to(self.reg_have_acc_label_text)
            self.browser.find_element(*self.reg_have_acc_label).click()
            time.sleep(1)
            if self.browser.find_element(*self.login_img).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to("Image not visible.")
            assert_that(self.browser.find_element(*self.reg_login_label).text).is_equal_to(self.reg_login_label_Text)
            assert_that(self.browser.find_element(*self.login_username_label).text).\
                is_equal_to(self.login_username_label_text)
            assert_that(self.browser.find_element(*self.login_pass_label).text).is_equal_to(self.login_pass_label_text)

            self.browser.find_element(*self.login_username_field).send_keys("testerbhaai@gmail.com")
            self.browser.find_element(*self.login_pass_field).send_keys("123456")
            self.browser.find_element(*self.reg_reg_now_label).click()

            assert_that(self.browser.find_element(*self.reg_fname_field).get_attribute("placeholder")).\
                is_equal_to(self.reg_fname_placeholder_text)
            assert_that(self.browser.find_element(*self.reg_lname_field).get_attribute("placeholder")).\
                is_equal_to(self.reg_lname_placeholder_text)
            assert_that(self.browser.find_element(*self.reg_email_field).get_attribute("placeholder")).\
                is_equal_to(self.reg_email_placeholder_text)
            assert_that(self.browser.find_element(*self.reg_pass_field).get_attribute("placeholder")).\
                is_equal_to(self.reg_pass_placeholder_text)
            assert_that(self.browser.find_element(*self.reg_con_pass_field).get_attribute("placeholder")).\
                is_equal_to(self.reg_con_pass_placeholder_text)

            if self.browser.find_element(*self.reg_img).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to("Image not visible.")

            self.browser.find_element(*self.reg_fname_field).send_keys("Tester")
            self.browser.find_element(*self.reg_lname_field).send_keys("Bhaai")
            self.browser.find_element(*self.reg_email_field).send_keys("testerbhaai@gmail.com")
            self.browser.find_element(*self.reg_pass_field).send_keys("123456")
            self.browser.find_element(*self.reg_con_pass_field).send_keys("123456")

            self.browser.find_element(*self.reg_terms_toggle).click()
            iframe = self.browser.find_element(*self.reg_recaptcha_iframe)
            self.browser.switch_to.frame(iframe)
            self.browser.find_element(*self.reg_recaptcha).click()
            time.sleep(1)
            self.browser.switch_to.default_content()



