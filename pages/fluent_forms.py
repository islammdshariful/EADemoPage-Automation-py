from utils.config import *


class FluentForms(BasePage, Helper):
    widget = '//*[@id="post-260959"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'Fluent Forms'
    doc_link = '//*[@id="post-260959"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[4]/div/div/a/span/span'
    doc_name = "FLUENT FORMS"

    name_label = (By.XPATH, f'//form[@class="frm-fluent-form fluent_form_1 ff-el-form-top ff_form_instance_1_1 '
                            f'ff-form-loaded"]/fieldset/div[1]/div[1]/label')
    name_field = (By.XPATH, f'//form[@class="frm-fluent-form fluent_form_1 ff-el-form-top ff_form_instance_1_1 '
                            f'ff-form-loaded"]/fieldset/div[1]/div[2]/input')
    email_label = (By.XPATH, f'//form[@class="frm-fluent-form fluent_form_1 ff-el-form-top ff_form_instance_1_1 '
                             f'ff-form-loaded"]/fieldset/div[2]/div[1]/label')
    email_field = (By.XPATH, f'//form[@class="frm-fluent-form fluent_form_1 ff-el-form-top ff_form_instance_1_1 '
                             f'ff-form-loaded"]/fieldset/div[2]/div[2]/input')
    sub_label = (By.XPATH, f'//form[@class="frm-fluent-form fluent_form_1 ff-el-form-top ff_form_instance_1_1 '
                           f'ff-form-loaded"]/fieldset/div[3]/div[1]/label')
    sub_field = (By.XPATH, f'//form[@class="frm-fluent-form fluent_form_1 ff-el-form-top ff_form_instance_1_1 '
                           f'ff-form-loaded"]/fieldset/div[3]/div[2]/input')
    message_label = (By.XPATH, f'//form[@class="frm-fluent-form fluent_form_1 ff-el-form-top ff_form_instance_1_1 '
                               f'ff-form-loaded"]/fieldset/div[4]/div[1]/label')
    message_field = (By.XPATH, f'//form[@class="frm-fluent-form fluent_form_1 ff-el-form-top ff_form_instance_1_1 '
                               f'ff-form-loaded"]/fieldset/div[4]/div[2]/textarea')

    send_message_btn = (By.XPATH, f'//form[@class="frm-fluent-form fluent_form_1 ff-el-form-top ff_form_instance_1_1 '
                                  f'ff-form-loaded"]/fieldset/div[5]/button')

    success_msg = (By.ID, f'fluentform_1_success')
    success_msg_text = "Thank you for your message. We will get in touch with you shortly"

    name_label_text = "YOUR NAME (REQUIRED)"
    email_label_text = "YOUR EMAIL (REQUIRED)"
    sub_label_text = "SUBJECT"
    message_label_text = "YOUR MESSAGE"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.fluent_forms)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(997)

                self.check_text_matches_with(self.name_label, self.name_label_text)
                self.check_text_matches_with(self.email_label, self.email_label_text)
                self.check_text_matches_with(self.sub_label, self.sub_label_text)
                self.check_text_matches_with(self.message_label, self.message_label_text)

                self.do_send_keys(self.name_field, "Tester Bhaai")
                self.do_send_keys(self.email_field, "testerbhaai@gmail.com")
                self.do_send_keys(self.sub_field, "Automation Script is Running...")
                self.do_send_keys(self.message_field, "Hi, Don't reply to this message. Have a good day.")
                self.do_click(self.send_message_btn)

                self.does_element_has_text(self.success_msg, self.success_msg_text)
