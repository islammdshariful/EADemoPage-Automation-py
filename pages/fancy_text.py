from utils.config import *


class FancyText(BasePage, Helper):
    widget = '//*[@id="post-14"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Fancy Text'
    doc_link = '//*[@id="post-14"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "FANCY TEXT"

    normal = (By.XPATH, f'//*[@id="post-14"]/div/div/div/div/section[2]/div/div/div/div/div/div[1]/div/div[1]/span[1]')
    normal_text = "You Can Customize"
    fancy_txt = (By.XPATH, f'//*[@id="eael-fancy-text-27d8d834"]')
    fancy_1_text = "Typography"
    fancy_2_text = "Color"
    fancy_3_text = "Background"
    cursor = (By.XPATH, f'//*[@id="post-14"]/div/div/div/div/section[2]/div/div/div/div/div/div[1]/div/div[1]/span[3]')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.fancy_text)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(903)

                self.check_text_matches_with(self.normal, self.normal_text)
                # self.is_visible(self.cursor, "Blink cursor is not visible.")

                self.does_element_has_text(self.fancy_txt, self.fancy_1_text)
                self.does_element_has_text(self.fancy_txt, self.fancy_2_text)
                self.does_element_has_text(self.fancy_txt, self.fancy_3_text)
