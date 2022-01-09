from selenium.webdriver import ActionChains

from utils.config import *


class ImageComparison:
    widget = '//*[@id="post-17"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Image Comparison'
    doc_link = '//*[@id="post-17"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "IMAGE COMPARISON"

    img_com = (By.XPATH, f'//*[@id="eael-image-comparison-23558b85"]')
    img_1 = (By.XPATH, f'//*[@id="eael-image-comparison-23558b85"]/img[1]')
    img_2 = (By.XPATH, f'//*[@id="eael-image-comparison-23558b85"]/img[2]')

    handle = (By.XPATH, f'//*[@id="eael-image-comparison-23558b85"]/div[2]/span[2]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(image_comparison)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1082)")
            time.sleep(1)
            if self.browser.find_element(*self.img_1).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to("Image is not visible.")
            if self.browser.find_element(*self.img_2).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to("Image is not visible.")

            cursor = ActionChains(self.browser)
            com = self.browser.find_element(*self.img_com)
            hand = self.browser.find_element(*self.handle)
            cursor.move_to_element(com).perform()
            assert_that(com.get_attribute("data-before_label")).is_equal_to("Before")
            assert_that(com.get_attribute("data-after_label")).is_equal_to("After")
            cursor.reset_actions()

            cursor.move_to_element(hand).click(hand).pause(1).move_by_offset(300, 0).release(hand).perform()


