from selenium.webdriver import ActionChains

from utils.config import *


class ParallaxScrolling:
    widget = '//*[@id="post-4578"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Parallax Effect'
    doc_link = '//*[@id="post-4578"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]/div' \
               '/div/div[3]/div/div/a/span/span'
    doc_name = "EA PARALLAX"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(parallax_scrolling)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1004)")
            wait_for_bar_to_come(self.browser)

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


