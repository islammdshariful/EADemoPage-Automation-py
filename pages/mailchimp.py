from utils.config import *


class Mailchimp(BasePage, Helper):
    widget = '//*[@id="post-2603"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]/div' \
             '/div/div[1]/div/h2'
    widget_name = 'MailChimp'
    doc_link = '//*[@id="post-2603"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]/div' \
               '/div/div[3]/div/div/a/span/span'
    doc_name = "MAILCHIMP"

    email_field = (By.XPATH, f'//*[@id="eael-mailchimp-form-50de1e0a"]/div[1]/div[1]/input')
    fname_field = (By.XPATH, f'//*[@id="eael-mailchimp-form-50de1e0a"]/div[1]/div[2]/input')
    lname_field = (By.XPATH, f'//*[@id="eael-mailchimp-form-50de1e0a"]/div[1]/div[3]/input')
    subs_btn = (By.XPATH, f'//*[@id="eael-subscribe-50de1e0a"]/span')

    success_message = (By.XPATH, f'//*[@id="eael-mailchimp-form-50de1e0a"]/div[2]/p')
    success_message_text = "You have subscribed successfully!"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.mailchimp)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1030)

                self.do_send_keys(self.email_field, "testerbhaai@gmail.com")
                self.do_send_keys(self.fname_field, "Tester")
                self.do_send_keys(self.lname_field, "Bhaai")
                self.browser.find_element(*self.subs_btn).click()

                self.does_element_has_text(self.success_message, self.success_message_text)