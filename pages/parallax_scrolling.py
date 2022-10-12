from utils.config import *


class ParallaxScrolling(BasePage, Helper):
    widget = '//*[@id="post-4578"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Parallax Effect'
    doc_link = '//*[@id="post-4578"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]/div' \
               '/div/div[3]/div/div/a/span/span'
    doc_name = "EA PARALLAX"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.parallax_scrolling)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1004)

                for i in range(1004, 2360, 5):
                    self.browser.execute_script("window.scrollTo(0, " + str(i) + ")")

                self.cursor.move_by_offset(10, 100).perform()
                time.sleep(.5)
                self.cursor.move_by_offset(200, 300).perform()
                time.sleep(.5)

                self.scroll_to(3468)
                for i in range(3468, 5481, 3):
                    self.browser.execute_script("window.scrollTo(0, " + str(i) + ")")


