import time

from selenium.webdriver import ActionChains, Keys

from utils.config import *


class ParticleEffect(Helper):
    widget = '//*[@id="post-4577"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'Particles'
    doc_link = '//*[@id="post-4577"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA PARTICLES"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.particle_effect)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1137)")
                time.sleep(1)
                # self.wait_for_bar_to_come()

                cursor = ActionChains(self.browser)
                cursor.move_by_offset(80, 100).perform()
                time.sleep(.5)
                cursor.move_by_offset(200, 300).perform()
                time.sleep(.5)
                cursor.move_by_offset(10, 100).perform()
                time.sleep(.5)
                self.browser.execute_script("window.scrollTo(0, 2121)")
                time.sleep(1)
                cursor.move_by_offset(10, 100).perform()
                time.sleep(.5)
                cursor.move_by_offset(200, 300).perform()
                time.sleep(.5)
                self.browser.execute_script("window.scrollTo(0, 3108)")
                for i in range(3108, 5632, 100):
                    self.browser.execute_script("window.scrollTo(0, " + str(i) + ")")
