from utils.config import *


class Weforms(BasePage, Helper):
    widget = '//*[@id="post-1300"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'weForms'
    doc_link = '//*[@id="post-1300"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "WEFORMS"

    name_label = (By.XPATH, f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                            f'/div/div/div/div/div/div/div/div/form/ul/li[1]/div[1]/label')
    fname_field = (By.XPATH, f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                             f'/div/div/div/div/div/div/div/div/form/ul/li[1]/div[2]/div/div[1]/input')
    lname_field = (By.XPATH, f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                             f'/div/div/div/div/div/div/div/div/form/ul/li[1]/div[2]/div/div[2]/input')
    email_label = (By.XPATH, f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                             f'/div/div/div/div/div/div/div/div/form/ul/li[2]/div[1]/label')
    email_field = (By.XPATH, f'//*[@id="email_1302"]')
    message_label = (By.XPATH, f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                               f'/div/div/div/div/div/div/div/div/form/ul/li[3]/div[1]/label')
    message_field = (By.XPATH, f'//*[@id="message_1302"]')

    send_message_btn = (By.XPATH, f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                  f'/div/div/div/div/div/div/div/div/form/ul/li[4]/input[7]')

    success_msg = (By.XPATH, f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                             f'/div/div/div/div/div/div/div/div/div')
    success_msg_text = "Thanks for contacting us! We will get in touch with you shortly."

    name_label_text = "Name *"
    email_label_text = "Email *"
    message_label_text = "Message *"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.weforms)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(984)

                self.check_text_matches_with(self.name_label, self.name_label_text)
                self.check_text_matches_with(self.email_label, self.email_label_text)
                self.check_text_matches_with(self.message_label, self.message_label_text)

                self.do_send_keys(self.fname_field, "Tester")
                self.do_send_keys(self.lname_field, "Bhaai")
                self.do_send_keys(self.email_field, "testerbhaai@gmail.com")
                self.do_send_keys(self.message_field, "Automation Script is Running...\nHi, Don't reply"
                                                      " to this message. Have a good day.")
                # self.do_click(self.send_message_btn)
                #
                # self.does_element_has_text(self.success_msg, self.success_msg_text)
