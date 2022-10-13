from utils.config import *


class ContentTicker(BasePage, Helper):
    widget = '//*[@id="post-2323"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Content Ticker'
    doc_link = '//*[@id="post-2323"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "CONTENT TICKER"

    label = (By.XPATH, f'//*[@id="eael-ticker-wrap-5107a1de"]/div[1]/span')
    label_text = "Trending Today"
    content_1 = (By.XPATH, f'//*[@id="eael-ticker-wrap-5107a1de"]/div[2]/div[1]/div/div[4]/div/a')
    content_1_text = "How to Include Elementor Template using a Shortcode"
    content_2 = (By.XPATH, f'//*[@id="eael-ticker-wrap-5107a1de"]/div[2]/div[1]/div/div[3]/div/a')
    content_2_text = "How to Include Elementor Template"
    prev_btn = (By.XPATH, f'//*[@id="eael-ticker-wrap-5107a1de"]/div[2]/div[2]/div[2]/i')
    next_btn = (By.XPATH, f'//*[@id="eael-ticker-wrap-5107a1de"]/div[2]/div[2]/div[1]/i')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.content_ticker)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(982)

            self.check_text_matches_with(self.label, self.label_text)

            if self.is_displaying(*self.content_1):
                self.does_element_has_text(self.content_1, self.content_1_text)
                self.check_text_matches_with(self.content_1, self.content_1_text)
                self.do_click(self.next_btn)

                self.does_element_has_text(self.content_2, self.content_2_text)
                self.check_text_matches_with(self.content_2, self.content_2_text)
                self.do_click(self.prev_btn)

                self.does_element_has_text(self.content_1, self.content_1_text)
                self.check_text_matches_with(self.content_1, self.content_1_text)
            else:
                self.does_element_has_text(self.content_2, self.content_2_text)
                self.check_text_matches_with(self.content_2, self.content_2_text)
                self.do_click(self.next_btn)

                self.does_element_has_text(self.content_1, self.content_1_text)
                self.check_text_matches_with(self.content_1, self.content_1_text)
                self.do_click(self.prev_btn)

                self.does_element_has_text(self.content_2, self.content_2_text)
                self.check_text_matches_with(self.content_2, self.content_2_text)
