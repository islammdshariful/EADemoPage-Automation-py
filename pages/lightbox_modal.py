from utils.config import *


class LightboxModal(BasePage, Helper):
    widget = '//*[@id="post-40"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Lightbox & Modal'
    doc_link = '//*[@id="post-40"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "LIGHTBOX & MODAL"

    button = (By.XPATH, f'//*[@id="post-40"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div/div[4]'
                        f'/div/div/div/div/div[1]/div')
    cross_btn = (By.XPATH, f"//button[normalize-space()='×']")
    img = (By.XPATH, f'/html/body/div[2]/div/div[1]/div/div/img')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.lightbox_modal)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(903)

                self.do_click(self.button)

                self.is_visible(self.img, "Image is not visible.")

                self.do_click(self.cross_btn)
