from selenium.webdriver import ActionChains, Keys

from utils.config import *


class PricingTable(Helper):
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

    basic_table_list_1_icon = f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/' \
                                         f'section[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[1]/span/i'
    basic_table_list_1 = f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                    f'/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[1]'
    basic_table_list_1_text = "Unlimited calls"

    basic_table_list_2_icon = f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/' \
                                         f'section[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[2]/span/i'
    basic_table_list_2 = f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                    f'/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[2]'
    basic_table_list_2_text = "Free hosting"

    basic_table_list_3_icon = f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/' \
                                         f'section[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[3]/span/i'
    basic_table_list_3 = f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                    f'/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[3]'
    basic_table_list_3_text = "500 MB of storage space"

    basic_table_list_4_icon = f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/' \
                                         f'section[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[4]/span/i'
    basic_table_list_4 = f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                    f'/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[4]'
    basic_table_list_4_text = "500 MB Bandwidth"

    basic_table_list_5_icon = f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/' \
                                         f'section[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[5]/span/i'
    basic_table_list_5 = f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                    f'/div/div/div[1]/div/div/div/div/div/div/div[3]/ul/li[5]'
    basic_table_list_5_text = "24/7 support"

    basic_table_button = (By.XPATH, f'//*[@id="post-1639"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                    f'/div/div/div[1]/div/div/div/div/div/div/div[4]/a')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.pricing_table)

    def check_list(self, list_icon, table_list, table_list_text):
        self.check_visibility(list_icon, "Icon not visible.")
        assert_that(self.browser.find_element(By.XPATH, table_list).text).is_equal_to(table_list_text)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 962)")
                time.sleep(1)

                cursor = ActionChains(self.browser)
                table = self.browser.find_element(*self.basic_table)
                button = self.browser.find_element(*self.basic_table_button)
                cursor.move_to_element(table).perform()
                assert_that(self.browser.find_element(*self.basic_table_title).text)\
                    .is_equal_to(self.basic_table_title_text)
                assert_that(self.browser.find_element(*self.basic_table_price).text)\
                    .is_equal_to(self.basic_table_price_text)
                assert_that(self.browser.find_element(*self.basic_table_month).text)\
                    .is_equal_to(self.basic_table_month_text)
                self.check_list(self.basic_table_list_1_icon, self.basic_table_list_1, self.basic_table_list_1_text)
                self.check_list(self.basic_table_list_2_icon, self.basic_table_list_2, self.basic_table_list_2_text)
                self.check_list(self.basic_table_list_3_icon, self.basic_table_list_3, self.basic_table_list_3_text)
                self.check_list(self.basic_table_list_4_icon, self.basic_table_list_4, self.basic_table_list_4_text)
                self.check_list(self.basic_table_list_5_icon, self.basic_table_list_5, self.basic_table_list_5_text)

                cursor.move_to_element(button).perform()



