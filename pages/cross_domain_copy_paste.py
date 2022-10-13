from utils.config import *


class CrossDomainCopyPaste(BasePage, Helper):
    widget = '//*[@id="post-271333"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Cross-Domain Copy Paste'
    doc_link = '//*[@id="post-271333"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA CROSS-DOMAIN COPY PASTE"

    img = (By.XPATH, f'//*[@id="post-271333"]/div/div/div/div/section[3]/div[2]/div/div/div/div/section' \
                     f'/div/div/div/div/div/div/div/div/img')
    src = "https://aadhmqulyo.cloudimg.io/v7/essential-addons.com/elementor/wp-content/uploads/2021/12/Section-1.gif"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.cross_domain_copy_paste)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1038)

                assert_that(self.get_element(self.img).get_attribute("src")).is_equal_to(self.src)
                self.is_visible(self.img, "Image is not visible")
