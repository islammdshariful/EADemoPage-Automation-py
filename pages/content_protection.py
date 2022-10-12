from utils.config import *


class ContentProtection(BasePage, Helper):
    widget = '//*[@id="post-255091"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Content Protection'
    doc_link = '//*[@id="post-255091"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA CONTENT PROTECTION"

    input = (By.XPATH, f'//*[@id="post-255091"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div'
                       f'/div/div/div/div/div/div/div[2]/form/input[1]')
    submit_btn = (By.XPATH, f'//*[@id="post-255091"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                            f'/div/div/div/div/div/div/div/div[2]/form/input[3]')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.content_protection)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(947)

                self.do_send_keys(self.input, "HOLIDAY")

                self.is_visible(self.submit_btn, "Submit button is not visible.")
