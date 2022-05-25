from selenium.webdriver import ActionChains, Keys

from utils.config import *


class ImageHotspots(Helper):
    widget = '//*[@id="post-2956"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Image Hotspot'
    doc_link = '//*[@id="post-2956"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "IMAGE HOTSPOTS"

    hotspot_1 = f"//div[@class='elementor-element elementor-element-1a3dd460 eael-image-hotspot-align-centered " \
                f"elementor-widget elementor-widget-eael-image-hotspots']//a[@class='eael-hot-spot-wrap elementor-" \
                f"repeater-item-9af7382 eael-hot-spot-tooptip tipso_style']//span[@class='eael-hotspot-icon eael-" \
                f"hotspot-tooltip fas fa-plus']"
    hotspot_tooltip_title = f"//span[@class='eael-single-tooltip eael-tooltip-1a3dd460']"
    hotspot_1_title_text = "Bag"

    hotspot_2 = f"//div[@class='elementor-element elementor-element-1a3dd460 eael-image-hotspot-align-centered " \
                f"elementor-widget elementor-widget-eael-image-hotspots']//a[@class='eael-hot-spot-wrap elementor-" \
                f"repeater-item-da20b6d eael-hot-spot-tooptip tipso_style']//span[@class='eael-hotspot-icon eael-" \
                f"hotspot-tooltip fas fa-plus']"
    hotspot_2_title_text = "T-shirt"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.image_hotspots)

    def hotspot(self, hotspot, title, title_name):
        cursor = ActionChains(self.browser)
        element = self.browser.find_element(By.XPATH, hotspot)
        time.sleep(.5)
        cursor.move_to_element(element).perform()
        if self.browser.find_element(By.XPATH, title).is_displayed():
            assert_that(self.browser.find_element(By.XPATH, title).text).is_equal_to(title_name)
        else:
            assert_that(1).is_equal_to("Hotspot not working")

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1077)")
                time.sleep(1)
                self.hotspot(self.hotspot_1, self.hotspot_tooltip_title, self.hotspot_1_title_text)
                self.hotspot(self.hotspot_2, self.hotspot_tooltip_title, self.hotspot_2_title_text)
