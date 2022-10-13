from selenium.common import StaleElementReferenceException

from utils.config import *


class ImageHotspots(BasePage, Helper):
    widget = '//*[@id="post-2956"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Image Hotspot'
    doc_link = '//*[@id="post-2956"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "IMAGE HOTSPOTS"

    hotspot_1 = (By.XPATH, f'//*[@id="post-2956"]/div/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/a[1]')
    hotspot_tooltip_title = (By.XPATH, f"//span[@class='eael-single-tooltip eael-tooltip-1a3dd460']")
    hotspot_1_title_text = "Bag"

    hotspot_2 = (By.XPATH, f'//*[@id="post-2956"]/div/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/a[5]')
    hotspot_2_title_text = "T-shirt"

    def __init__(self, browser):
        super().__init__(browser)

    def hotspot(self, hotspot, title, title_name):
        self.move_cursor_to(hotspot)
        if self.is_displaying(*title):
            try:
                self.check_text_matches_with(title, title_name)
            except StaleElementReferenceException:
                if self.is_displaying(*title):
                    self.check_text_matches_with(title, title_name)
        else:
            assert_that("Hotspot working").is_equal_to("Hotspot not working")

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.image_hotspots)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1077)

                self.hotspot(self.hotspot_1, self.hotspot_tooltip_title, self.hotspot_1_title_text)
                self.hotspot(self.hotspot_2, self.hotspot_tooltip_title, self.hotspot_2_title_text)
