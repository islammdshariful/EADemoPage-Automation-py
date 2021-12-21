from utils.config import *


class AdvancedGoogleMap:
    widget = '//*[@id="post-2506"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Advanced Google Map'
    doc_link = '//*[@id="post-2506"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = ""

    zoom_in_btn = (By.XPATH, f'//*[@id="eael-google-map-5930a8e8"]/div/div/div[4]/div[1]/div/div/button[1]')
    zoom_out_btn = (By.XPATH, f'//*[@id="eael-google-map-5930a8e8"]/div/div/div[4]/div[1]/div/div/button[2]')

    map_btn = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[2]'
                         f'/div/div/div/div/div/div[3]/div/div[1]/div/div/div[4]/div[2]/div[1]/button')
    satellite_btn = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[2]'
                               f'/div/div/div/div/div/div[3]/div/div[1]/div/div/div[4]/div[2]/div[2]/button')

    full_screen_btn = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[2]'
                                 f'/div/div/div/div/div/div[3]/div/div[1]/div/div/div[8]/button')

    map = (By.XPATH, f'//*[@id="eael-google-map-5930a8e8"]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(advanced_google_map)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 933)")
            snap = ImageComparison(self.browser)
            # snap.take_new_snap("AdvancedGoogleMap")
            snap.image_comparison("AdvancedGoogleMap")

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

            self.browser.execute_script("window.scrollTo(0, 1952)")
            # snap.take_new_snap("AdvancedGoogleMapThemes")
            snap.image_comparison("AdvancedGoogleMapThemes")
