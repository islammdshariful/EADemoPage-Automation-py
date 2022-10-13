from utils.config import *


class Formstack(BasePage, Helper):
    widget = '//*[@id="post-259465"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Formstack'
    doc_link = '//*[@id="post-259465"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "FORMSTACK"

    title = (By.XPATH, f'//*[@id="fsSection94545411"]/div[1]/h2')
    des = (By.XPATH, f'//*[@id="fsSection94545411"]/div[1]/div')

    name_label = (By.XPATH, f'//*[@id="label94545412"]')
    fname_field = (By.XPATH, f'//*[@id="field94545412-first"]')
    lname_field = (By.XPATH, f'//*[@id="field94545412-last"]')
    address_label = (By.XPATH, f'//*[@id="label94545413"]')
    address_field = (By.XPATH, f'//*[@id="field94545413-address"]')
    hphone_label = (By.XPATH, f'//*[@id="label94545414"]')
    hphone_field = (By.XPATH, f'//*[@id="field94545414"]')
    wphone_label = (By.XPATH, f'//*[@id="label94545415"]')
    wphone_field = (By.XPATH, f'//*[@id="field94545415"]')
    email_label = (By.XPATH, f'//*[@id="label94545416"]')
    email_field = (By.XPATH, f'//*[@id="field94545416"]')
    comment_label = (By.XPATH, f'//*[@id="label94545417"]')
    comment_field = (By.XPATH, f'//*[@id="field94545417"]')

    fname_bottom_label = (By.XPATH, f'//*[@id="fsCell94545412"]/div[1]/div[1]/label')
    lname_bottom_label = (By.XPATH, f'//*[@id="fsCell94545412"]/div[1]/div[2]/label')
    address_bottom_label = (By.XPATH, f'//*[@id="fsCell94545413"]/div[1]/div/label')

    submit_btn = (By.XPATH, f'//*[@id="fsSubmitButton3799616"]')

    success_msg = (By.XPATH, f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                             f'/div/div/div/div/div/div/div/div/div')
    success_msg_text = "Thanks for contacting us! We will get in touch with you shortly."

    name_label_text = "Name*"
    fname_bottom_label_text = "First Name"
    lname_bottom_label_text = "Last Name"
    address_bottom_label_text = "Address*"
    address_label_text = "Address Line 1"
    hphone_label_text = "Home Phone*"
    wphone_label_text = "Work Phone"
    email_label_text = "Email*"
    comment_label_text = "Comments"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.formstack)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(905)

                self.check_text_matches_with(self.name_label, self.name_label_text)
                self.check_text_matches_with(self.fname_bottom_label, self.fname_bottom_label_text)
                self.check_text_matches_with(self.lname_bottom_label, self.lname_bottom_label_text)
                self.check_text_matches_with(self.fname_bottom_label, self.fname_bottom_label_text)
                self.check_text_matches_with(self.address_label, self.address_bottom_label_text)
                self.check_text_matches_with(self.hphone_label, self.hphone_label_text)
                self.check_text_matches_with(self.wphone_label, self.wphone_label_text)
                self.check_text_matches_with(self.email_label, self.email_label_text)
                self.check_text_matches_with(self.comment_label, self.comment_label_text)

                self.do_send_keys(self.fname_field, "Tester")
                self.do_send_keys(self.lname_field, "Bhaai")
                self.do_send_keys(self.address_field, "planet Earth, Universe Level 7")
                self.do_send_keys(self.hphone_field, "01234567890")
                self.do_send_keys(self.wphone_field, "09876543210")
                self.do_send_keys(self.email_field, "testerbhaai@gmail.com")
                self.do_send_keys(self.comment_field, "Automation Script is Running...\nHi, Don't reply"
                                                      " to this message. Have a good day.")
                # self.do_click(self.submit_btn)
                #
                # self.does_element_has_text(self.success_msg, self.success_msg_text)
