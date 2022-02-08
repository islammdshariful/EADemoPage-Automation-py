from selenium.webdriver import ActionChains, Keys

from utils.config import *


class ImageComparison(Helper):
    widget = '//*[@id="post-17"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Image Comparison'
    doc_link = '//*[@id="post-17"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "IMAGE COMPARISON"

    img_com = (By.XPATH, f'//*[@id="eael-image-comparison-23558b85"]')
    img_1 = f'//*[@id="eael-image-comparison-23558b85"]/img[1]'
    img_2 = f'//*[@id="eael-image-comparison-23558b85"]/img[2]'

    handle = (By.XPATH, f'//*[@id="eael-image-comparison-23558b85"]/div[2]')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.image_comparison)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1082)")
                time.sleep(1)

                self.check_visibility(self.img_1, "Image 1 is not visible.")
                self.check_visibility(self.img_2, "Image 2 is not visible.")

                cursor = ActionChains(self.browser)
                com = self.browser.find_element(*self.img_com)
                hand = self.browser.find_element(*self.handle)
                cursor.move_to_element(com).perform()
                assert_that(com.get_attribute("data-before_label")).is_equal_to("Before")
                assert_that(com.get_attribute("data-after_label")).is_equal_to("After")
                cursor.reset_actions()

                cursor.move_to_element(hand).click(hand).pause(1).move_by_offset(300, 0).release(hand).perform()


