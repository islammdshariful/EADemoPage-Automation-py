from utils.config import *


class TableOfContent(Helper):
    widget = '//*[@id="post-257840"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'Table of Contents'
    doc_link = '//*[@id="post-257840"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA TABLE OF CONTENTS"

    toc = (By.XPATH, f'//*[@id="eael-toc"]/button/span')
    toc_cp = f'//*[@id="eael-toc-list"]/li[5]/a/span'
    toc_cp_text = "EA Content Protection"
    toc_cp_content = f'//*[@id="92-eael-table-of-content"]'

    toc_ds = f'//*[@id="eael-toc-list"]/li[2]/a/span'
    toc_ds_text = "Different Styles Of Table Of Contents"
    toc_ds_content = f'//*[@id="83-eael-table-of-content"]'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.table_of_content)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1504)")
            time.sleep(1)

            self.browser.find_element(*self.toc).click()
            time.sleep(.5)

            assert_that(self.browser.find_element(By.XPATH, self.toc_cp).text).is_equal_to(self.toc_cp_text)
            self.browser.find_element(By.XPATH, self.toc_cp).click()
            time.sleep(1)
            self.check_visibility(self.toc_cp_content, "Table of content is not working.")

            assert_that(self.browser.find_element(By.XPATH, self.toc_ds).text).is_equal_to(self.toc_ds_text)
            self.browser.find_element(By.XPATH, self.toc_ds).click()
            time.sleep(1)
            self.check_visibility(self.toc_ds_content, "Table of content is not working.")
