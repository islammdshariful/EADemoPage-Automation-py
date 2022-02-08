from selenium.webdriver import ActionChains, Keys

from utils.config import *


class ParallaxScrolling(Helper):
    widget = '//*[@id="post-4578"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Parallax Effect'
    doc_link = '//*[@id="post-4578"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]/div' \
               '/div/div[3]/div/div/a/span/span'
    doc_name = "EA PARALLAX"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.parallax_scrolling)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1004)")
                self.wait_for_bar_to_come()

                for i in range(1004, 2360, 3):
                    self.browser.execute_script("window.scrollTo(0, " + str(i) + ")")

                cursor = ActionChains(self.browser)
                cursor.move_by_offset(10, 100).perform()
                time.sleep(.5)
                cursor.move_by_offset(200, 300).perform()
                time.sleep(.5)
                # cursor.move_by_offset(10, 100).perform()

                self.browser.execute_script("window.scrollTo(0, 3468)")
                for i in range(3468, 5481, 3):
                    self.browser.execute_script("window.scrollTo(0, " + str(i) + ")")


