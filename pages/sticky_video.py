from selenium.webdriver import ActionChains

from pages.basepage import BasePage
from utils.config import *


class StickyVideo(BasePage, Helper):
    widget = '//*[@id="post-255935"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Sticky Video'
    doc_link = '//*[@id="post-255935"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "STICKY VIDEO"

    iframe_box = (By.XPATH, f"//iframe[@title='Player for Essential Addons for Elementor: "
                            f"Most Popular Addons & Widgets for Elementor']")
    start_button = (By.XPATH, f'//*[@id="post-255935"]/div/div/div/div/section[2]/div/div/div/div/div/section'
                             f'/div/div/div[2]/div/div/div/div/div/div[1]/div/img')
    video_frame = (By.XPATH, f'//*[@id="movie_player"]/div[1]/video')
    pause_btn = (By.XPATH, f'//*[@id="movie_player"]/div[1]/video')
    play_btn = (By.XPATH, f'//*[@id="post-255935"]/div/div/div/div/section[2]/div/div/div/div/div/section/div/div/'
                          f'div[2]/div/div/div/div/div/div[2]/div/button')
    cross = (By.XPATH, f'//*[@id="videobox"]/span/i')
    player = (By.XPATH, f'//*[@id="movie_player"]/div[1]/video')
    small_play_button = (By.XPATH, f'//*[@id="videobox"]/div/button')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.sticky_video)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(629)
                time.sleep(1)

                """Click Play button"""
                self.do_click(self.start_button)
                time.sleep(1)
                """Switching to iFrame"""
                self.switch_to_frame(self.iframe_box)
                self.move_cursor_to(self.video_frame)
                """Clicking pause button"""
                self.do_click(self.pause_btn)
                time.sleep(1)
                """Switching to default frame"""
                self.switch_frame_to_default()
                """Clicking the play button"""
                self.do_click(self.play_btn)
                time.sleep(1)
                """Scrolling bottom to popup sticky video player"""
                for i in range(629, 1500, 2):
                    self.browser.execute_script("window.scrollTo(0, " + str(i) + ")")
                time.sleep(1)
                """Close the sticky video player"""
                self.do_click(self.cross)
