from utils.config import *


class GravityForms(BasePage, Helper):
    widget = '//*[@id="post-1802"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Gravity Forms'
    doc_link = '//*[@id="post-1802"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA GRAVITY FORMS"

    fname_field = (By.XPATH, f'//*[@id="input_1_4_3"]')
    lname_field = (By.XPATH, f'//*[@id="input_1_4_6"]')
    email_field = (By.XPATH, f'//*[@id="input_1_3"]')
    message_field = (By.XPATH, f'//*[@id="input_1_5"]')

    submit_btn = (By.XPATH, f'//*[@id="gform_submit_button_1"]')

    success_msg = (By.XPATH, f'//*[@id="gform_confirmation_message_1"]')
    success_msg_text = "Thanks for contacting us! We will get in touch with you shortly."

    fname_label_text = "First Name"
    lname_label_text = "Last Name"
    email_label_text = "Email"
    message_label_text = "Message"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.gravity_forms)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1002)

                assert_that(self.get_element(self.fname_field).get_attribute("placeholder")). \
                    is_equal_to(self.fname_label_text)
                assert_that(self.get_element(self.lname_field).get_attribute("placeholder")). \
                    is_equal_to(self.lname_label_text)
                assert_that(self.get_element(self.email_field).get_attribute("placeholder")). \
                    is_equal_to(self.email_label_text)
                assert_that(self.get_element(self.message_field).get_attribute("placeholder")). \
                    is_equal_to(self.message_label_text)

                self.do_send_keys(self.fname_field, "Tester")
                self.do_send_keys(self.lname_field, "Bhaai")
                self.do_send_keys(self.email_field, "testerbhaai@gmail.com")
                self.do_send_keys(self.message_field, "Automation Script is Running...\nHi, Don't reply"
                                                      " to this message. Have a good day.")
                self.do_click(self.submit_btn)

                self.scroll_to(1002)
                self.does_element_has_text(self.success_msg, self.success_msg_text)
