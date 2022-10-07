from utils.config import *


class FlipCarousel(BasePage, Helper):
    widget = '//*[@id="post-1616"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Flip Carousel'
    doc_link = '//*[@id="post-1616"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "FLIP CAROUSEL"

    flip_1 = (By.XPATH, f'//*[@id="post-1616"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div'
                        f'/div/div/div/div/div/div/ul/li[1]/div/img')
    flip_2 = (By.XPATH, f'//*[@id="post-1616"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div'
                        f'/div/div/div/div/div/div/ul/li[2]/div/img')
    flip_3 = (By.XPATH, f'//*[@id="post-1616"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div'
                        f'/div/div/div/div/div/div/ul/li[3]/div/img')
    flip_4 = (By.XPATH, f'//*[@id="post-1616"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div'
                        f'/div/div/div/div/div/div/ul/li[4]/div/img')
    flip_5 = (By.XPATH, f'//*[@id="post-1616"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div'
                        f'/div/div/div/div/div/div/ul/li[5]/div/img')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.flip_carousel)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(905)

                self.do_click(self.flip_2)
                self.do_click(self.flip_1)
                self.do_click(self.flip_2)
                self.do_click(self.flip_3)
                self.do_click(self.flip_4)
                self.do_click(self.flip_5)
