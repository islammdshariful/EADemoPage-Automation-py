from selenium.webdriver import ActionChains, Keys

from utils.config import *


class StickyVideo(Helper):
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
        self.browser = browser

    def load(self):
        self.browser.get(self.sticky_video)

    def testcase(self):
        c = Helper(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 629)")
                time.sleep(1)

                self.browser.find_element(*self.start_button).click()
                time.sleep(1)
                self.browser.switch_to.frame(self.browser.find_element(*self.iframe_box))
                cursor = ActionChains(self.browser)
                player = self.browser.find_element(*self.video_frame)
                cursor.move_to_element(player).perform()
                self.browser.find_element(*self.pause_btn).click()
                time.sleep(1)
                self.browser.switch_to.default_content()
                self.browser.find_element(*self.play_btn).click()
                time.sleep(1)
                for i in range(629, 1500, 2):
                    self.browser.execute_script("window.scrollTo(0, " + str(i) + ")")
                time.sleep(1)
                self.browser.find_element(*self.cross).click()
