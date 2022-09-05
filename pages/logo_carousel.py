from pages.basepage import BasePage
from utils.config import *


class LogoCarousel(BasePage, Helper):
    widget = '//*[@id="post-2942"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = "Logo Carousel"
    doc_link = '//*[@id="post-2942"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "LOGO CAROUSEL"

    dot_1 = (By.XPATH, f'//*[@id="post-2942"]/div/div/div/div/section[2]/div/div/div'
                       f'/div/div/div/div/div/div[2]/span[1]')

    dot_2 = (By.XPATH, f'//*[@id="post-2942"]/div/div/div/div/section[2]/div/div/div/div'
                       f'/div/div/div/div/div[2]/span[6]')

    img_1 = (By.XPATH, f'//*[@id="post-2942"]/div/div/div/div/section[2]/div/div/div/div'
                       f'/div/div/div/div/div[1]/div/div[7]/div/div/a/img')
    img_2 = (By.XPATH, f'//*[@id="post-2942"]/div/div/div/div/section[2]/div/div/div/div'
                       f'/div/div/div/div/div[1]/div/div[17]/div/div/a/img')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.logo_carousel)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(943)
                """Click on navigation dot 1"""
                self.do_click(self.dot_1)
                """move cursor to logo 1"""
                self.move_cursor_to(self.img_1)
                """Click on navigation dot 2"""
                self.do_click(self.dot_2)
                time.sleep(1)
                """move cursor to logo 2"""
                self.move_cursor_to(self.img_2)



