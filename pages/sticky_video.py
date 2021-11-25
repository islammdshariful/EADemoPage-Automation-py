import time

from selenium.webdriver import ActionChains

from utils.config import *

# This code won't run, the main site has some problem


class StickyVideo:
    widget = '//*[@id="post-255935"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Sticky Video'
    doc_link = '//*[@id="post-255935"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "STICKY VIDEO"

    play_button = (By.XPATH, f'//*[@id="post-255935"]/div/div/div/div/section[4]/div/div/div/div/div/section'
                             f'/div/div/div[2]/div/div/div/div/div/div[1]/div/img')
    cross = (By.XPATH, f'//*[@id="videobox"]/span/i')
    player = (By.XPATH, f'//*[@id="player"]')
    small_play_button = (By.XPATH, f'//*[@id="videobox"]/div/button')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(sticky_video)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 969)")
            time.sleep(1)

            self.browser.find_element(*self.play_button).click()
            for i in range(969, 2170):
                self.browser.execute_script("window.scrollTo(0, " + str(i) + ")")
            time.sleep(1)

            self.browser.find_element(*self.player).click()
            time.sleep(1)
            self.browser.find_element(*self.small_play_button).click()

            for i in range(2170, 2772):
                self.browser.execute_script("window.scrollTo(0, " + str(i) + ")")
            self.browser.execute_script("window.scrollTo(0, 2869)")
            time.sleep(1)
            self.browser.find_element(*self.cross).click()
