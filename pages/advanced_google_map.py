from selenium.webdriver import Keys, ActionChains

from utils.config import *


class AdvancedGoogleMap(Helper):
    widget = '//*[@id="post-2506"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Advanced Google Map'
    doc_link = '//*[@id="post-2506"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "ADVANCED GOOGLE MAP"

    zoom_in_btn = (By.XPATH, f'//*[@id="eael-google-map-5930a8e8"]/div/div/div[4]/div[1]/div/div/button[1]')
    zoom_out_btn = (By.XPATH, f'//*[@id="eael-google-map-5930a8e8"]/div/div/div[4]/div[1]/div/div/button[2]')

    map_btn = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[2]/div/div/div'
                         f'/div/div/div[3]/div/div[1]/div/div/div[4]/div[2]/div[1]/button')
    satellite_btn = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[2]/div/'
                               f'div/div/div/div/div[3]/div/div[1]/div/div/div[4]/div[2]/div[2]/button')

    full_screen_btn = (By.XPATH, f"//div[@id='eael-google-map-5930a8e8']//div//div[@class='gm-style']//div//"
                                 f"button[@title='Toggle fullscreen view']")

    map = (By.XPATH, f'//*[@id="eael-google-map-5930a8e8"]')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.advanced_google_map)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 933)")
                time.sleep(1)
                snap = ImageComparison(self.browser)
                # snap.take_new_snap("AdvancedGoogleMap")
                # snap.image_comparison("AdvancedGoogleMap")

                time.sleep(1)
                self.browser.find_element(*self.satellite_btn).click()
                time.sleep(1)
                self.browser.find_element(*self.full_screen_btn).click()
                time.sleep(1)
                self.browser.find_element(*self.full_screen_btn).click()
                time.sleep(1)
                self.browser.find_element(*self.map_btn).click()
                time.sleep(1)
                self.browser.find_element(*self.zoom_in_btn).click()
                time.sleep(1)
                self.browser.find_element(*self.zoom_out_btn).click()

                # self.browser.execute_script("window.scrollTo(0, 1952)")
                # snap.take_new_snap("AdvancedGoogleMapThemes")
                # snap.image_comparison("AdvancedGoogleMapThemes")
