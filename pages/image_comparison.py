from utils.config import *


class ImageComparison(BasePage, Helper):
    widget = '//*[@id="post-17"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Image Comparison'
    doc_link = '//*[@id="post-17"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "IMAGE COMPARISON"

    img_com = (By.XPATH, f'//*[@id="eael-image-comparison-23558b85"]')
    img_1 = (By.XPATH, f'//*[@id="eael-image-comparison-23558b85"]/img[1]')
    img_2 = (By.XPATH, f'//*[@id="eael-image-comparison-23558b85"]/img[2]')

    handle = (By.XPATH, f'//*[@id="eael-image-comparison-23558b85"]/div[2]')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.image_comparison)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1082)

                self.is_visible(self.img_1, "Image 1 is not visible.")
                self.is_visible(self.img_2, "Image 2 is not visible.")

                self.move_cursor_to(self.img_com)
                assert_that(self.get_element(self.img_com).get_attribute("data-before_label")).is_equal_to("Before")
                assert_that(self.get_element(self.img_com).get_attribute("data-after_label")).is_equal_to("After")

                self.cursor.move_to_element(self.get_element(self.handle)).click(self.get_element(self.handle)).\
                    pause(1).move_by_offset(300, 0).release(self.get_element(self.handle)).perform()


