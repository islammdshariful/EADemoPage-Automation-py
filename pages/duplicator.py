from utils.config import *


class Duplicator(Helper):
    widget = '//*[@id="page"]/div[1]/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Post Duplicator'
    doc_link = '//*[@id="page"]/div[1]/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]/div/div' \
               '/div[3]/div/div/a/span/span'
    doc_name = "EA DUPLICATOR"

    img_1 = f'//*[@id="page"]/div[1]/div/div/section[2]/div/div/div/div/div/section[2]/div/div/div/div' \
                       f'/div/div/div/div/img'

    img_2 = f'//*[@id="page"]/div[1]/div/div/section[3]/div/div/div/div/div/section[2]/div/div/div/div' \
                       f'/div/div/div/div/img'

    img_3 = f'//*[@id="page"]/div[1]/div/div/section[4]/div/div/div/div/div/section[2]/div/div/div/div' \
                       f'/div/div/div/div/img'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.duplicator)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1003)")
            time.sleep(1)

            self.check_visibility(self.img_1, "Image 1 is not visible.")
            self.browser.execute_script("window.scrollTo(0, 1938)")
            self.check_visibility(self.img_2, "Image 2 is not visible.")
            self.browser.execute_script("window.scrollTo(0, 2958)")
            self.check_visibility(self.img_3, "Image 3 is not visible.")
