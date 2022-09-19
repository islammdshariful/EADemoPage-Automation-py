from selenium.webdriver import ActionChains, Keys

from utils.config import *


class ImageScroller(Helper, Snapshot):
    widget = '//*[@id="post-4586"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Image Scroller'
    doc_link = '//*[@id="post-4586"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA IMAGE SCROLLER"

    img_1 = f'//*[@id="post-4586"]/div/div/div/div/section[2]/div/div/div/div/div/section/div/div/div[2]/div/div/div' \
            f'/div/div/img'
    img_2 = f'//*[@id="post-4586"]/div/div/div/div/section[2]/div/div/div/div/div/section/div/div/div[3]/div/div/div' \
            f'/div/div/img'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.image_scroller)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 818)")
                time.sleep(1)

                cursor = ActionChains(self.browser)
                image_1 = self.browser.find_element(By.XPATH, self.img_1)
                image_2 = self.browser.find_element(By.XPATH, self.img_2)

                # For Download The Image
                # self.download_image(self.img_1, "ImageScroller")

                cursor.move_to_element(image_1).perform()
                time.sleep(3)
                assert_that(image_1.get_attribute("style")).is_equal_to("transform: translateY(-133.75px);")
                # For Comparison iamges
                self.download_image_comparison(self.img_1, "ImageScroller")
                cursor.move_to_element(image_2).perform()
                time.sleep(2)
                assert_that(image_1.get_attribute("style")).is_equal_to("transform: translate(0px);")
