from utils.config import *


class ScrollToTop(BasePage, Helper):
    widget = (By.XPATH, '//*[@id="post-271396"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
                        '/div/div/div[2]/div/div/div[1]/div/h2')
    widget_name = 'Scroll to Top'
    doc_link = '//*[@id="post-271396"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA SCROLL TO TOP"

    scroll_to_top_btn = (By.XPATH, f"//span[@class='eael-ext-scroll-to-top-button']")

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.scroll_to_top_extension)
            """Checking widget name"""
            # self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to_bottom()

                self.run_script("arguments[0].click();", self.scroll_to_top_btn)

                self.is_visible(self.widget, "Scroll to top not working.")
