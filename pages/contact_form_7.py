from utils.config import *


class ContactForm7(BasePage, Helper):
    widget = '//*[@id="post-1231"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Contact Form 7'
    doc_link = '//*[@id="post-1231"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "CONTACT FORM 7"

    name_label = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[1]/label')
    name_label_text = "YOUR NAME (REQUIRED)"
    email_label = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[2]/label')
    email_label_text = "YOUR EMAIL (REQUIRED)"
    sub_label = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[3]/label')
    sub_label_text = "SUBJECT"
    msg_label = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[4]/label')
    msg_label_text = "YOUR MESSAGE"

    name_field = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[1]/label/span/input')
    email_field = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[2]/label/span/input')
    sub_field = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[3]/label/span/input')
    msg_field = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[4]/label/span/textarea')

    send_btn = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[5]/input')

    success_msg = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/div[2]')
    success_msg_text = "Thank you for your message. It has been sent."

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.contact_form_7)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(2374)

                self.check_text_matches_with(self.name_label, self.name_label_text)
                self.check_text_matches_with(self.email_label, self.email_label_text)
                self.check_text_matches_with(self.sub_label, self.sub_label_text)
                self.check_text_matches_with(self.msg_label, self.msg_label_text)

                self.do_send_keys(self.name_field, "Tester Bhaai")
                self.do_send_keys(self.email_field, "testerbhaai@gmail.com")
                self.do_send_keys(self.sub_field, "Automation Script is Running...")
                self.do_send_keys(self.msg_field, "Hi, Don't reply to this message. Have a good day.")
                # self.do_click(self.send_btn)
                #
                # self.does_element_has_text(self.success_msg, self.success_msg_text)