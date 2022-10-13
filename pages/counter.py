from utils.config import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Counter(BasePage, Helper):
    widget = '//*[@id="post-2948"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Counter'
    doc_link = '//*[@id="post-2948"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "COUNTER"
    icon = (By.XPATH, f'//*[@id="post-2948"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div/'
                      f'div[1]/div/div/div/div/div/div/span/span')
    number = (By.XPATH, f'//*[@id="post-2948"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div/'
                        f'div[1]/div/div/div/div/div/div/div/div[1]/div/div')
    number_text = "2\n,\n5\n4\n0"
    counter_text = (By.XPATH, f'//*[@id="post-2948"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                              f'/div/div/div[1]/div/div/div/div/div/div/div/div[2]')
    counter_text_text = "Projects Completed"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.counter)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(959)

                self.is_visible(self.icon, "Icon is not visible.")

                self.check_text_matches_with(self.counter_text, self.counter_text_text)

                self.does_element_has_text(self.number, self.number_text)
                self.check_text_matches_with(self.number, self.number_text)
