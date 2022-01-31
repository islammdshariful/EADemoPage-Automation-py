from selenium.webdriver import ActionChains

from utils.config import *


class ImageScroller(Helper):
    widget = '//*[@id="post-4586"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Image Scroller'
    doc_link = '//*[@id="post-4586"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA IMAGE SCROLLER"

    img_1 = (By.XPATH, f'//*[@id="post-4586"]/div/div/div/div/section[2]/div/div/div/div/div/section/div/div'
                       f'/div[2]/div/div/div/div/div/img')
    img_2 = (By.XPATH, f'//*[@id="post-4586"]/div/div/div/div/section[2]/div/div/div/div/div/section/div/div'
                       f'/div[3]/div/div/div/div/div/img')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.image_scroller)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 818)")
            time.sleep(1)

            img_com = ImageComparison(self.browser)
            cursor = ActionChains(self.browser)
            image_1 = self.browser.find_element(*self.img_1)
            image_2 = self.browser.find_element(*self.img_2)

            cursor.move_to_element(image_1).perform()
            time.sleep(2)
            # img_com.take_new_snap("ImageScroller")
            # time.sleep(1)
            img_com.image_comparison("ImageScroller")

            cursor.move_to_element(image_2).perform()
