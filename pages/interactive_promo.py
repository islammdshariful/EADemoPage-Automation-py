from utils.config import *


class InteractivePromo(BasePage, Helper):
    widget = '//*[@id="post-19"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Interactive Promo'
    doc_link = '//*[@id="post-19"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "INTERACTIVE PROMO"

    promo_1 = (By.XPATH, f'//*[@id="eael-promo-696e3946"]/figure')
    promo_1_img = (By.XPATH, f'//*[@id="eael-promo-696e3946"]/figure/img')
    promo_1_title = (By.XPATH, f'//*[@id="eael-promo-696e3946"]/figure/figcaption/div/h2')
    promo_1_title_text = "It’S A Pleasure"
    promo_1_des = (By.XPATH, f'//*[@id="eael-promo-696e3946"]/figure/figcaption/div/p')
    promo_1_des_text = "We Have Only One Earth To Dwell, Don’T Destroy The Nature And Don’T Make It Hell."

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.interactive_promo)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(905)

                self.is_visible(self.promo_1_img, "Image not visible.")
                self.check_text_matches_with(self.promo_1_title, self.promo_1_title_text)
                self.move_cursor_to(self.promo_1)
                self.is_visible(self.promo_1_des, "Description not visible.")
