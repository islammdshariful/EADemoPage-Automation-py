from utils.config import *


class Duplicator(BasePage, Helper):
    widget = '//*[@id="page"]/div[1]/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Post Duplicator'
    doc_link = '//*[@id="page"]/div[1]/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]/div/div' \
               '/div[3]/div/div/a/span/span'
    doc_name = "EA DUPLICATOR"

    img_1 = (By.XPATH, f'//*[@id="page"]/div[1]/div/div/section[2]/div/div/div/div/div/section[2]/div/div/div/div' \
                       f'/div/div/div/div/img')

    img_2 = (By.XPATH, f'//*[@id="page"]/div[1]/div/div/section[3]/div/div/div/div/div/section[2]/div/div/div/div' \
                       f'/div/div/div/div/img')

    img_3 = (By.XPATH, f'//*[@id="page"]/div[1]/div/div/section[4]/div/div/div/div/div/section[2]/div/div/div/div' \
                       f'/div/div/div/div/img')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.duplicator)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1003)

                self.is_visible(self.img_1, "Image 1 is not visible.")
                self.scroll_to(1938)
                self.is_visible(self.img_2, "Image 2 is not visible.")
                self.scroll_to(2958)
                self.is_visible(self.img_3, "Image 3 is not visible.")
