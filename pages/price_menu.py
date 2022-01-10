from selenium.webdriver import ActionChains

from utils.config import *


class PriceMenu:
    widget = '//*[@id="post-2953"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Price Menu'
    doc_link = '//*[@id="post-2953"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "PRICE MENU"

    menu_img = (By.XPATH, f'//*[@id="post-2953"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div[1]/div/div/img')
    menu_title = (By.XPATH, f'//*[@id="post-2953"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div[2]/div/h3')
    menu_title_text = "Breakfast Menu"

    menu_list_1_name = (By.XPATH, f'//*[@id="post-2953"]/div/div/div/div/section[3]/div/div/div[1]/div/div'
                             f'/div[3]/div/div/div/div[1]/div/div/div/h4/span')
    menu_list_1_name_text = "Fig And Lemon Cake"
    menu_list_1_price = (By.XPATH, f'//*[@id="post-2953"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div[3]'
                                   f'/div/div/div/div[1]/div/div/div/span[2]/span')
    menu_list_1_price_text = "$10"

    menu_list_2_name = (By.XPATH, f'//*[@id="post-2953"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div[3]'
                                  f'/div/div/div/div[2]/div/div/div/h4/span')
    menu_list_2_name_text = "Heirloom Tomato"
    menu_list_2_price = (By.XPATH, f'//*[@id="post-2953"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div[3]'
                                   f'/div/div/div/div[2]/div/div/div/span[2]/span')
    menu_list_2_price_text = "$25"

    menu_list_3_name = (By.XPATH, f'//*[@id="post-2953"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div[3]'
                                  f'/div/div/div/div[3]/div/div/div/h4/span')
    menu_list_3_name_text = "Italian Spaghetti"
    menu_list_3_price = (By.XPATH, f'//*[@id="post-2953"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div[3]'
                                   f'/div/div/div/div[3]/div/div/div/span[2]/span')
    menu_list_3_price_text = "$28"

    menu_list_4_name = (By.XPATH, f'//*[@id="post-2953"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div[3]'
                                  f'/div/div/div/div[4]/div/div/div/h4/span')
    menu_list_4_name_text = "Calamari Diavolo"
    menu_list_4_price = (By.XPATH, f'//*[@id="post-2953"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div[3]'
                                   f'/div/div/div/div[4]/div/div/div/span[2]/span')
    menu_list_4_price_text = "$10"

    menu_list_5_name = (By.XPATH, f'//*[@id="post-2953"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div[3]'
                                  f'/div/div/div/div[5]/div/div/div/h4/span')
    menu_list_5_name_text = "Home Made Bread"
    menu_list_5_price = (By.XPATH, f'//*[@id="post-2953"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div[3]'
                                   f'/div/div/div/div[5]/div/div/div/span[2]/span')
    menu_list_5_price_text = "$8"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(price_menu)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 965)")
            time.sleep(1)

            if self.browser.find_element(*self.menu_img).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to("Image is not visible")

            assert_that(self.browser.find_element(*self.menu_list_1_name).text).\
                is_equal_to(self.menu_list_1_name_text)
            assert_that(self.browser.find_element(*self.menu_list_1_price).text).\
                is_equal_to(self.menu_list_1_price_text)

            assert_that(self.browser.find_element(*self.menu_list_2_name).text).\
                is_equal_to(self.menu_list_2_name_text)
            assert_that(self.browser.find_element(*self.menu_list_2_price).text).\
                is_equal_to(self.menu_list_2_price_text)

            assert_that(self.browser.find_element(*self.menu_list_3_name).text).\
                is_equal_to(self.menu_list_3_name_text)
            assert_that(self.browser.find_element(*self.menu_list_3_price).text).\
                is_equal_to(self.menu_list_3_price_text)

            assert_that(self.browser.find_element(*self.menu_list_4_name).text).\
                is_equal_to(self.menu_list_4_name_text)
            assert_that(self.browser.find_element(*self.menu_list_4_price).text).\
                is_equal_to(self.menu_list_4_price_text)

            assert_that(self.browser.find_element(*self.menu_list_5_name).text).\
                is_equal_to(self.menu_list_5_name_text)
            assert_that(self.browser.find_element(*self.menu_list_5_price).text).\
                is_equal_to(self.menu_list_5_price_text)

