from utils.config import *


class Wpforms(BasePage, Helper):
    widget = '//*[@id="post-2913"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'WPForms'
    doc_link = '//*[@id="post-2913"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]/div' \
               '/div/div[3]/div/div/a/span/span'
    doc_name = "EA WPFORMS"

    name_label = (By.XPATH, f'//*[@id="wpforms-260985-field_0-container"]/label')
    fname_field = (By.ID, f'wpforms-260985-field_0')
    lname_field = (By.ID, f'wpforms-260985-field_0-last')
    email_label = (By.XPATH, f'//*[@id="wpforms-260985-field_1-container"]/label')
    email_field = (By.ID, f'wpforms-260985-field_1')
    message_label = (By.XPATH, f'//*[@id="wpforms-260985-field_2-container"]/label')
    message_field = (By.ID, f'wpforms-260985-field_2')
    submit_btn = (By.ID, f'wpforms-submit-260985')
    success_message = (By.XPATH, f'//*[@id="wpforms-confirmation-260985"]')

    name_label_text = "NAME *"
    email_label_text = "EMAIL *"
    message_label_text = "COMMENT OR MESSAGE *"
    success_message_text = "Thanks for contacting us! We will be in touch with you shortly."

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.wpforms)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1040)

                self.check_text_matches_with(self.name_label, self.name_label_text)
                self.check_text_matches_with(self.email_label, self.email_label_text)
                self.check_text_matches_with(self.message_label, self.message_label_text)

                self.do_send_keys(self.fname_field, "Tester")
                self.do_send_keys(self.lname_field, "Bhaai")
                self.do_send_keys(self.email_field, "testerbhaai@gmail.com")
                self.do_send_keys(self.message_field, "Automation Script is Running...\nHi, Don't reply"
                                                      " to this message. Have a good day.")
                # self.do_click(self.submit_btn)
                #
                # self.does_element_has_text(self.success_message, self.success_message_text)
