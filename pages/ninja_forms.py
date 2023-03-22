from utils.config import *


class NinjaForms(BasePage, Helper):
    widget = '//*[@id="post-1762"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'Ninja Forms'
    doc_link = '//*[@id="post-1762"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]/div' \
               '/div/div[3]/div/div/a/span/span'
    doc_name = "EA NINJA FORMS"

    title = (By.XPATH, f'//*[@id="nf-form-title-1"]/hundefined')
    des = (By.XPATH, f'//*[@id="nf-form-1-cont"]/div/div[4]/form/div/div[1]/nf-section/div')

    name_label = (By.XPATH, f'//*[@id="nf-label-field-1"]')
    name_field = (By.XPATH, f'//*[@id="nf-field-1"]')
    email_label = (By.XPATH, f'//*[@id="nf-label-field-2"]')
    email_field = (By.XPATH, f'//*[@id="nf-field-2"]')
    message_label = (By.XPATH, f'//*[@id="nf-label-field-3"]')
    message_field = (By.XPATH, f'//*[@id="nf-field-3"]')
    submit_btn = (By.XPATH, f'//*[@id="nf-field-4"]')

    success_message = (By.XPATH, f'//*[@id="nf-form-1-cont"]/div/div[1]')

    title_text = "Contact Me"
    des_text = "Fields marked with an * are required"

    name_label_text = "NAME *"
    email_label_text = "EMAIL *"
    message_label_text = "MESSAGE *"
    success_message_text = "Form submitted successfully.\nA confirmation email was sent to testerbhaai@gmail.com."

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.ninja_forms)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1171)

                self.check_text_matches_with(self.title, self.title_text)
                self.check_text_matches_with(self.des, self.des_text)
                self.check_text_matches_with(self.name_label, self.name_label_text)
                self.check_text_matches_with(self.email_label, self.email_label_text)
                self.check_text_matches_with(self.message_label, self.message_label_text)

                self.do_send_keys(self.name_field, "Tester Bhaai")
                self.do_send_keys(self.email_field, "testerbhaai@gmail.com")
                self.do_send_keys(self.message_field, "Automation Script is Running...\nHi, Don't reply"
                                                      " to this message. Have a good day.")
                self.do_click(self.submit_btn)

                self.does_element_has_text(self.success_message, self.success_message_text)
