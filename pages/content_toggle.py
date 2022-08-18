from pages.basepage import BasePage
from utils.config import *


class ContentToggle(BasePage, Helper):
    widget = '//*[@id="post-2605"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Content Toggle'
    doc_link = '//*[@id="post-2605"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "CONTENT TOGGLE"
    toggle_button = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[1]/div/div[2]/label/span')
    primary_btn = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[1]/div/div[1]')
    primary_btn_text = "Single"
    secondary_btn = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[1]/div/div[3]')
    secondary_btn_text = "Unlimited"

    p_1_title = (By.XPATH, f"//h2[normalize-space()='Single']")
    p_1_title_text = "Single"
    p_1_price = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                           f'/div/div/div/div/div/div/div/div/div/div[1]/span[1]/span')
    p_1_price_text = "$49.50"
    p_1_month = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                           f'/div/div/div/div/div/div/div/div/div/div[1]/span[2]')
    p_1_month_text = "Permonth"
    p_1_item_1_icon = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div['
                                 f'1]/div/div/section/div/div/div/div/div/div/div/div/div/div[3]/ul/li[1]/span/i')
    p_1_item_1 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section/div/div/div/'
                            f'div/div/div/div/div/div/div[3]/ul/li[1]')
    p_1_item_1_text = "Unlimited calls"

    p_1_item_2 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[2]')
    p_1_item_2_text = "Free hosting"

    p_1_item_3 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[3]')
    p_1_item_3_text = "500 MB of storage space"

    p_1_item_4 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[4]')
    p_1_item_4_text = "500 MB Bandwidth"

    p_1_item_5 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[5]')
    p_1_item_5_text = "24/7 support"

    p_1_button = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[4]/a')

    # Secondary
    s_1_title = (By.XPATH, f"//div[@class='eael-pricing style-3']//h2[@class='title'][normalize-space()='Unlimited']")
    s_1_title_text = "Unlimited"
    s_1_price = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                           f'/div/div/div/div/div/div/div/div/div/div[1]/span[1]/span')
    s_1_price_text = "$89.50"
    s_1_month = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                           f'/div/div/div/div/div/div/div/div/div/div[1]/span[2]')
    s_1_month_text = "Permonth"
    s_1_item_1_icon = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div['
                                 f'2]/div/div/section/div/div/div/div/div/div/div/div/div/div[3]/ul/li[1]/span/i')
    s_1_item_1 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section/div/div/div/'
                            f'div/div/div/div/div/div/div[3]/ul/li[1]')
    s_1_item_1_text = "Unlimited calls"

    s_1_item_2 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[2]')
    s_1_item_2_text = "Free hosting"

    s_1_item_3 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[3]')
    s_1_item_3_text = "500 MB of storage space"

    s_1_item_4 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[4]')
    s_1_item_4_text = "500 MB Bandwidth"

    s_1_item_5 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[5]')
    s_1_item_5_text = "24/7 support"

    s_1_button = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[4]/a')

    close_scrips_chat_btn = (By.XPATH, f'//*[@id="crisp-chatbox"]/div/a/span[1]/span/span[1]/span[1]/span')

    def __init__(self, browser):
        super().__init__(browser)

    def load(self):
        self.browser.get(self.content_toggle)

    def toggle_page_one(self):
        """Toggle page one"""

        """Check page heading"""
        self.move_to(self.p_1_title)

        """Check page heading"""
        self.check_text_matches_with(self.p_1_title, self.p_1_title_text)
        self.check_text_matches_with(self.p_1_price, self.p_1_price_text)
        self.check_text_matches_with(self.p_1_month, self.p_1_month_text)

        """Check icon"""
        self.is_visible(self.p_1_item_1_icon, "Content Toggle page 1 is not visible.")

        """Check page info lists"""
        self.check_text_matches_with(self.p_1_item_1, self.p_1_item_1_text)
        self.check_text_matches_with(self.p_1_item_2, self.p_1_item_2_text)
        self.check_text_matches_with(self.p_1_item_3, self.p_1_item_3_text)
        self.check_text_matches_with(self.p_1_item_4, self.p_1_item_4_text)
        self.check_text_matches_with(self.p_1_item_5, self.p_1_item_5_text)

        """Moves to button"""
        self.move_to(self.p_1_button)

    def toggle_page_two(self):
        """Toggle page two"""

        """Check page heading"""
        self.move_to(self.s_1_title)

        """Check page heading"""
        self.check_text_matches_with(self.s_1_title, self.s_1_title_text)
        self.check_text_matches_with(self.s_1_price, self.s_1_price_text)
        self.check_text_matches_with(self.s_1_month, self.s_1_month_text)

        """Check icon"""
        self.is_visible(self.s_1_item_1_icon, "Content Toggle page 2 is not visible.")

        """Check page info lists"""
        self.check_text_matches_with(self.s_1_item_1, self.s_1_item_1_text)
        self.check_text_matches_with(self.s_1_item_2, self.s_1_item_2_text)
        self.check_text_matches_with(self.s_1_item_3, self.s_1_item_3_text)
        self.check_text_matches_with(self.s_1_item_4, self.s_1_item_4_text)
        self.check_text_matches_with(self.s_1_item_5, self.s_1_item_5_text)

        """Moves to button"""
        self.move_to(self.s_1_button)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.load()
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1967)")
                time.sleep(1)
                """Checking button labels"""
                self.check_text_matches_with(self.primary_btn, self.primary_btn_text)
                self.check_text_matches_with(self.secondary_btn, self.secondary_btn_text)

                """Checking Toggle Page one"""
                self.toggle_page_one()

                """Click Toggle button"""
                self.do_click(self.toggle_button)
                time.sleep(.5)

                """Checking Toggle Page two"""
                self.toggle_page_two()
