from utils.config import *


class PricingTable(BasePage, Helper):
    widget = '//*[@id="post-1639"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Pricing Table'
    doc_link = '//*[@id="post-1639"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "PRICING TABLE"

    basic_table = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                             f'/div/div/div[1]/div/div/div/div/div')
    basic_table_title = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                   f'/div/div/div[1]/div/div/div/div/div/div/div[1]/h2')
    basic_table_title_text = "Basic"
    basic_table_price = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                   f'/div/div/div[1]/div/div/div/div/div/div/div[2]/span[1]/span')
    basic_table_price_text = "$49"
    basic_table_month = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                   f'/div/div/div[1]/div/div/div/div/div/div/div[2]/span[2]')
    basic_table_month_text = "/ Mo"

    basic_table_list_1_icon = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/' \
                                         f'section[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[1]/span/i')
    basic_table_list_1 = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                    f'/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[1]')
    basic_table_list_1_text = "Unlimited calls"

    basic_table_list_2_icon = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/' \
                                         f'section[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[2]/span/i')
    basic_table_list_2 = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                    f'/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[2]')
    basic_table_list_2_text = "Free hosting"

    basic_table_list_3_icon = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/' \
                                         f'section[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[3]/span/i')
    basic_table_list_3 = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                    f'/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[3]')
    basic_table_list_3_text = "500 MB of storage space"

    basic_table_list_4_icon = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/' \
                                         f'section[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[4]/span/i')
    basic_table_list_4 = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                    f'/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[4]')
    basic_table_list_4_text = "500 MB Bandwidth"

    basic_table_list_5_icon = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/' \
                                         f'section[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[5]/span/i')
    basic_table_list_5 = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                    f'/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[5]')
    basic_table_list_5_text = "24/7 support"

    basic_table_button = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                    f'/div/div/div[1]/div/div/div/div/div/div/div[4]/a')

    def __init__(self, browser):
        super().__init__(browser)

    def check_list(self, list_icon, table_list, table_list_text):
        self.is_visible(list_icon, "Icon not visible.")
        self.check_text_matches_with(table_list, table_list_text)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.pricing_table)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(962)

                self.move_cursor_to(self.basic_table)
                self.check_text_matches_with(self.basic_table_title, self.basic_table_title_text)
                self.check_text_matches_with(self.basic_table_price, self.basic_table_price_text)
                self.check_text_matches_with(self.basic_table_month, self.basic_table_month_text)

                self.check_list(self.basic_table_list_1_icon, self.basic_table_list_1, self.basic_table_list_1_text)
                self.check_list(self.basic_table_list_2_icon, self.basic_table_list_2, self.basic_table_list_2_text)
                self.check_list(self.basic_table_list_3_icon, self.basic_table_list_3, self.basic_table_list_3_text)
                self.check_list(self.basic_table_list_4_icon, self.basic_table_list_4, self.basic_table_list_4_text)
                self.check_list(self.basic_table_list_5_icon, self.basic_table_list_5, self.basic_table_list_5_text)

                self.move_cursor_to(self.basic_table_button)
