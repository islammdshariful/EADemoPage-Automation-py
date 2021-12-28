from selenium.webdriver import ActionChains

from utils.config import *


class ImageHotspots:
    widget = '//*[@id="post-2956"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Image Hotspot'
    doc_link = '//*[@id="post-2956"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "IMAGE HOTSPOTS"

    hotspot_1 = f'//*[@id="post-2956"]/div/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/span[1]/span/span'
    hotspot_1_title = f'/html/body/div[6]/div[2]/span'
    hotspot_1_title_text = "Bag"

    hotspot_2 = f'//*[@id="post-2956"]/div/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/span[5]/span'
    hotspot_2_title = f'/html/body/div[6]/div[2]/span'
    hotspot_2_title_text = "T-shirt"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(image_hotspots)

    def hotspot(self, hotspot, title, title_name):
        cursor = ActionChains(self.browser)
        element = self.browser.find_element(By.XPATH, hotspot)
        time.sleep(.5)
        cursor.move_to_element(element).perform()
        if self.browser.find_element(By.XPATH, title).is_displayed():
            assert_that(self.browser.find_element(By.XPATH, title).text).is_equal_to(title_name)
        else:
            assert_that(display).is_equal_to("Hotspot not working")

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1077)")
            self.hotspot(self.hotspot_1, self.hotspot_1_title, self.hotspot_1_title_text)
            self.hotspot(self.hotspot_2, self.hotspot_2_title, self.hotspot_2_title_text)