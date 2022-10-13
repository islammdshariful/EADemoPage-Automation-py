from pages.basepage import BasePage
from utils.config import *


class FlipBox(BasePage, Helper):
    widget = '//*[@id="post-1519"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = "Flip Box"
    doc_link = '//*[@id="post-1519"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/' \
               'div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "FLIP BOX"
    BOX_1 = (By.XPATH, f'//*[@id="post-1519"]/div/div/div/div/section[2]/div/div/div/div/div/section['
                     f'2]/div/div/div[1]/div/div/div/div/div')
    BOX_2 = (By.XPATH, f'//*[@id="post-1519"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                       f'/div/div/div[2]/div/div')
    BOX_FRONT_HEADER = (By.XPATH, f'//*[@id="post-1519"]/div/div/div/div/section[2]/div/div/div/div/div/section['
                                  f'2]/div/div/div[1]/div/div/div/div/div/a/div[1]/div/div/div/h2')
    BOX_BACK_HEADER = (By.XPATH, f'//*[@id="post-1519"]/div/div/div/div/section[2]/div/div/div/div/div/section['
                          f'2]/div/div/div[1]/div/div/div/div/div/a/div[2]/div/div/div/h2')
    BOX_BACK_DES = (By.XPATH, f'//*[@id="post-1519"]/div/div/div/div/section[2]/div/div/div/div/div/section['
                         f'2]/div/div/div[1]/div/div/div/div/div/a/div[2]/div/div/div/div[2]/p[2]')

    BOX_FRONT_HEADER_TEXT = "Interface Design"
    BOX_BACK_HEADER_TEXT = "Style Your Flip Box Exclusively"
    BOX_DES_TEXT = "Add your preferred content or use saved templates here, choose your 'Icon Type', " \
                   "add title, select title tag for front & back, set your content position, alignment " \
                   "and style your Flip Box the way you want.    "

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.flip_box)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1023)
                """Flip box front side checking"""
                if self.is_displaying(*self.BOX_FRONT_HEADER):
                    self.check_text_matches_with(self.BOX_FRONT_HEADER, self.BOX_FRONT_HEADER_TEXT)
                """Move cursor to flip box"""
                self.move_cursor_to(self.BOX_1)
                """Flip box back side checking"""
                if self.is_displaying(*self.BOX_BACK_HEADER):
                    if self.is_displaying(*self.BOX_BACK_DES):
                        self.check_text_matches_with(self.BOX_BACK_HEADER, self.BOX_BACK_HEADER_TEXT)
                        self.check_text_matches_with(self.BOX_BACK_DES, self.BOX_DES_TEXT)
                """Move out cursor from flip box"""
                self.move_cursor_to(self.BOX_2)




