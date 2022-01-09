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

    iframe_box = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[2]'
                            f'/div/div/div/div/div/section/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/iframe')
    play_button = (By.XPATH, f'//*[@id="post-255935"]/div/div/div/div/section[2]/div/div/div/div/div/section'
                             f'/div/div/div[2]/div/div/div/div/div/div[1]/div/img')
    video_frame = (By.XPATH, f'/html/body/div[1]/div/div[1]/video')
    pause_btn = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[2]/div/div/div'
                           f'/div/div/section/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/button[1]')
    cross = (By.XPATH, f'//*[@id="videobox"]/span/i')
    player = (By.XPATH, f'//*[@id="movie_player"]/div[1]/video')
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

            self.browser.execute_script("window.scrollTo(0, 629)")
            time.sleep(1)

            self.browser.find_element(*self.play_button).click()
            # iframe = self.browser.find_element(*self.iframe_box)
            # self.browser.switch_to.frame(iframe)
            # cursor = ActionChains(self.browser)
            # player = self.browser.find_element(*self.video_frame)
            # cursor.move_to_element(player).perform()
            # self.browser.find_element(*self.pause_btn).click()
            # time.sleep(1)
            # self.browser.find_element(*self.pause_btn).click()
            # self.browser.switch_to.default_content()
            for i in range(629, 1500, 2):
                self.browser.execute_script("window.scrollTo(0, " + str(i) + ")")
            time.sleep(1)

            # self.browser.find_element(*self.player).click()
            # time.sleep(.5)
            # self.browser.find_element(*self.small_play_button).click()
            # time.sleep(.5)

            self.browser.find_element(*self.cross).click()
