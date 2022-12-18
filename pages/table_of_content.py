from utils.config import *


class TableOfContent(BasePage, Helper):
    widget = '//*[@id="post-257840"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'Table of Contents'
    doc_link = '//*[@id="post-257840"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA TABLE OF CONTENTS"

    toc = (By.XPATH, f'//*[@id="eael-toc"]/button/span')
    toc_cp = (By.XPATH, f'//*[@id="eael-toc-list"]/li[5]/a/span')
    toc_cp_text = "EA Content Protection"
    toc_cp_content = (By.XPATH, f'//*[@id="92-eael-table-of-content"]')

    toc_ds = (By.XPATH, f'//*[@id="eael-toc-list"]/li[2]/a/span')
    toc_ds_text = "Different Styles Of Table Of Contents"
    toc_ds_content = (By.XPATH, f"(//h3[normalize-space()='Different Styles Of Table Of Contents'])[1]")

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.table_of_content)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1504)

                self.do_click(self.toc)

                self.check_text_matches_with(self.toc_cp, self.toc_cp_text)
                self.do_click(self.toc_cp)
                self.is_visible(self.toc_cp_content, "Table of content is not working.")

                self.check_text_matches_with(self.toc_ds, self.toc_ds_text)
                self.do_click(self.toc_ds)
                self.is_visible(self.toc_ds_content, "Table of content is not working.")
