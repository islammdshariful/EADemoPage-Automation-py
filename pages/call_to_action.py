from utils.config import *


class CallToAction(BasePage, Helper):
    widget = '//*[@id="post-1512"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Call To Action'
    doc_link = '//*[@id="post-1512"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "CALL TO ACTION"

    title = (By.XPATH, f'//*[@id="post-1512"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div/div/div/h2')
    title_text = "Essential Addons For Elementor"
    des = (By.XPATH, f'//*[@id="post-1512"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div/div/div/p')
    des_text = "Enhance your Elementor page building experience with 57+ creative\nelements. Add powers to your " \
               "page builder using our easy-to-use elements"

    button = (By.XPATH, f'//*[@id="post-1512"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div/div/div/a')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.call_to_action)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1020)

                self.check_text_matches_with(self.title, self.title_text)
                self.check_text_matches_with(self.des, self.des_text)
                self.move_cursor_to(self.button)
