from utils.config import *


class CalderaForms(BasePage, Helper):
    widget = '//*[@id="post-1829"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'Caldera Forms'
    doc_link = '//*[@id="post-1829"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA CALDERA FORMS"

    fname_label = (By.XPATH, f'//*[@id="fld_8768091Label"]')
    fname_field = (By.XPATH, f'//*[@id="fld_8768091_1"]')
    lname_label = (By.XPATH, f'//*[@id="fld_9970286Label"]')
    lname_field = (By.XPATH, f'//*[@id="fld_9970286_1"]')
    email_label = (By.XPATH, f'//*[@id="fld_6009157Label"]')
    email_field = (By.XPATH, f'//*[@id="fld_6009157_1"]')
    comment_label = (By.XPATH, f'//*[@id="fld_7683514Label"]')
    comment_field = (By.XPATH, f'//*[@id="fld_7683514_1"]')

    send_message_btn = (By.XPATH, f'//*[@id="fld_7908577_1"]')

    success_msg = (By.XPATH, f'//*[@id="caldera_notices_1"]/div')
    success_msg_text = "Form has been successfully submitted. Thank you."

    fname_label_text = "First Name *"
    lname_label_text = "Last Name *"
    email_label_text = "Email Address *"
    comment_label_text = "Comments / Questions *"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.caldera_forms)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1130)

                self.check_text_matches_with(self.fname_label, self.fname_label_text)
                self.check_text_matches_with(self.lname_label, self.lname_label_text)
                self.check_text_matches_with(self.email_label, self.email_label_text)
                self.check_text_matches_with(self.comment_label, self.comment_label_text)

                self.do_send_keys(self.fname_field, "Tester")
                self.do_send_keys(self.lname_field, "Bhaai")
                self.do_send_keys(self.email_field, "testerbhaai@gmail.com")
                self.do_send_keys(self.comment_field, "Automation Script is Running...\nHi, Don't reply"
                                                      " to this message. Have a good day.")
                # self.browser.find_element(*self.send_message_btn).click()
                #
                # self.does_element_has_text(self.success_msg, self.success_msg_text)
