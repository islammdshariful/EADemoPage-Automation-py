from utils.config import *


class InteractiveCards(BasePage, Helper):
    widget = '//*[@id="post-1716"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Interactive Cards'
    doc_link = '//*[@id="post-1716"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "INTERACTIVE CARDS"

    promo = (By.XPATH, f'//*[@id="interactive-card-368e06c7"]/div[1]/div')
    close_btn = (By.XPATH, f'//*[@id="interactive-card-368e06c7"]/div[2]/span')
    title = (By.XPATH, f'//*[@id="interactive-card-368e06c7"]/div[2]/div/div[1]/div/h2')
    title_text = "Amazing Colorful City"
    des = (By.XPATH, f'//*[@id="interactive-card-368e06c7"]/div[2]/div/div[1]/div/p')
    des_text = "We have only one earth to dwell, don’t destroy the nature and\n" \
               "don’t make it hell. We have only one earth to dwell, don’t destroy."
    button = (By.XPATH, f'//*[@id="interactive-card-368e06c7"]/div[2]/div/div[1]/div/a')

    scroll = (By.CSS_SELECTOR, '.elementor-element-66b9ccf8')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.interactive_cards)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to_element(self.scroll)

                self.do_click(self.promo)
                self.check_text_matches_with(self.title, self.title_text)
                self.check_text_matches_with(self.des, self.des_text)
                self.move_cursor_to(self.button)
                self.do_click(self.close_btn)
                time.sleep(2)

                if self.is_displaying(*self.title):
                    assert_that("Card closed").is_equal_to("Card not closed")

