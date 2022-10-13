from utils.config import *


class ImageScroller(BasePage, Helper):
    widget = '//*[@id="post-4586"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Image Scroller'
    doc_link = '//*[@id="post-4586"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA IMAGE SCROLLER"

    img_1 = (By.XPATH, f'//*[@id="post-4586"]/div/div/div/div/section[2]/div/div/div/div/div/section/div/div/div[2]/'
                       f'div/div/div/div/div/img')
    img_2 = (By.XPATH, f'//*[@id="post-4586"]/div/div/div/div/section[2]/div/div/div/div/div/section/div/div/div[3]/'
                       f'div/div/div/div/div/img')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.image_scroller)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(818)

                self.move_cursor_to(self.img_1)
                time.sleep(3)
                transform = self.get_element(self.img_1).get_attribute("style")
                if not transform.__eq__("transform: translateY(-133.766px);"):
                    if not transform.__eq__("transform: translateY(-133.75px);"):
                        assert_that(['transform: translateY(-133.766px);', 'transform: translateY(-133.75px);']).\
                            contains(transform)

                self.move_cursor_to(self.img_2)
                time.sleep(2)

                assert_that(self.get_element(self.img_1).get_attribute("style")).\
                    is_equal_to("transform: translate(0px);")
