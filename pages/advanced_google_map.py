from pages.basepage import BasePage
from utils.config import *


class AdvancedGoogleMap(BasePage, Helper):
    widget = '//*[@id="post-2506"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Advanced Google Map'
    doc_link = '//*[@id="post-2506"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "ADVANCED GOOGLE MAP"

    map = (By.XPATH, f'//*[@id="post-2506"]/div/div/div/div/section[2]/div/div/div/div/div/div[3]')
    zoom_in_btn = (By.XPATH, f'//*[@id="eael-google-map-5930a8e8"]/div/div/div[4]/div[1]/div/div/button[1]')
    zoom_out_btn = (By.XPATH, f'//*[@id="eael-google-map-5930a8e8"]/div/div/div[4]/div[1]/div/div/button[2]')

    map_btn = (By.XPATH, f'//*[@id="eael-google-map-5930a8e8"]/div/div/div[4]/div[2]/div[1]')
    satellite_btn = (By.XPATH, f'//*[@id="eael-google-map-5930a8e8"]/div/div/div[4]/div[2]/div[2]')

    full_screen_btn = (By.XPATH, f'//*[@id="eael-google-map-5930a8e8"]/div/div/div[8]/button')

    scroll = (By.XPATH, f'//*[@id="post-2506"]/div/div/div/div/section[2]/div/div/div/div/div/div[1]')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.advanced_google_map)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to_element(self.scroll)

                self.do_click(self.satellite_btn)
                self.do_click(self.full_screen_btn)
                self.do_click(self.full_screen_btn)
                self.do_click(self.map_btn)
                self.do_click(self.zoom_in_btn)
                self.do_click(self.zoom_out_btn)

                # snap = Snapshot(self.browser)
                # # snap.take_snap(self.map, 'advanced_google_map')
                # snap.snap_comparison(self.map, 'advanced_google_map')



