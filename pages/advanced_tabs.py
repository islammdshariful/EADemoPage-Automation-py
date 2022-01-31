import time

from selenium.webdriver import ActionChains

from utils.config import *


class AdvancedTabs(Helper):
    widget = '//*[@id="post-2436"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Advanced Tabs'
    doc_link = '//*[@id="post-2436"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "ADVANCED TABS"

    tab_1_icon = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                            f'/div/div/div/div/div/div/div/div/div[1]/ul/li[1]/svg')
    tab_1 = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                       f'/div/div/div/div/div/div/div/div/div[1]/ul/li[1]/span')
    tab_1_text = "PHILOSOPHY"
    tab_1_des = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                           f'/div/div/div/div/div/div/div/div/div[2]/div[1]')
    tab_des_text = "Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus. Praesent elementum feugiat dignissim. Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus. Praesent elementum feugiat dignissim. Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam."
    tab_nested_ver_des_text = "Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus. Praesent elementum feugiat dignissim. Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus. Praesent elementum feugiat dignissim. Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus. Praesent elementum feugiat dignissim."
    tab_nested_hor_des_text = "Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus. Praesent elementum feugiat dignissim. Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus. Praesent elementum feugiat dignissim. Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus."

    tab_2_icon = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                            f'/div/div/div/div/div/div/div/div/div[1]/ul/li[2]/svg')
    tab_2 = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                       f'/div/div/div/div/div/div/div/div/div[1]/ul/li[2]/span')
    tab_2_text = "MISSION"
    tab_2_1 = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                         f'/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/section/div/div/div/div'
                         f'/div/div/div/div/div[1]/ul/li[1]/span')
    tab_2_1_text = "Easy To Use"
    tab_2_1_des = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                             f'/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/section/div/div/div/div/'
                             f'div/div/div/div/div[2]/div[1]')
    tab_2_2 = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                         f'/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/section/div/div/div/div'
                         f'/div/div/div/div/div[1]/ul/li[2]/span')
    tab_2_2_text = "Mission & Vision"
    tab_2_2_des = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                             f'/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/section/div/div/div/div'
                             f'/div/div/div/div/div[2]/div[2]')
    tab_2_3 = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                         f'/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/section/div/div/div/div/div'
                         f'/div/div/div/div[1]/ul/li[3]/span')
    tab_2_3_text = "Goals"
    tab_2_3_des = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                             f'/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/section/div/div/div/div/'
                             f'div/div/div/div/div[2]/div[3]')
    tab_2_4 = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                         f'/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/section/div/div/div/div/'
                         f'div/div/div/div/div[1]/ul/li[4]/span')
    tab_2_4_text = "Privacy Policy"
    tab_2_4_des = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                             f'/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/section/div/div/div/div'
                             f'/div/div/div/div/div[2]/div[4]')

    tab_3_icon = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                            f'/div/div/div/div/div/div/div/div/div[1]/ul/li[3]/svg')
    tab_3 = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                       f'/div/div/div/div/div/div/div/div/div[1]/ul/li[3]/span')
    tab_3_text = "VISION"
    tab_3_1 = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                         f'/div/div/div/div/div/div/div/div/div[2]/div[3]/div/div/section/div/div/div/div/div/'
                         f'div/div/div/div[1]/ul/li[1]/span')
    tab_3_1_text = "Easy To Use"
    tab_3_1_des = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                             f'/div/div/div/div/div/div/div/div/div[2]/div[3]/div/div/section/div/div/div/div/'
                             f'div/div/div/div/div[2]/div[1]')
    tab_3_2 = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                         f'/div/div/div/div/div/div/div/div/div[2]/div[3]/div/div/section/div/div/div/div/'
                         f'div/div/div/div/div[1]/ul/li[2]/span')
    tab_3_2_text = "Mission & Vision"
    tab_3_2_des = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                             f'/div/div/div/div/div/div/div/div/div[2]/div[3]/div/div/section/div/div/div/div'
                             f'/div/div/div/div/div[2]/div[2]')
    tab_3_3 = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                         f'/div/div/div/div/div/div/div/div/div[2]/div[3]/div/div/section/div/div/div/div/'
                         f'div/div/div/div/div[1]/ul/li[3]/span')
    tab_3_3_text = "Goals"
    tab_3_3_des = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                             f'/div/div/div/div/div/div/div/div/div[2]/div[3]/div/div/section/div/div/div/div/'
                             f'div/div/div/div/div[2]/div[3]')
    tab_3_4 = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                         f'/div/div/div/div/div/div/div/div/div[2]/div[3]/div/div/section/div/div/div/div/'
                         f'div/div/div/div/div[1]/ul/li[4]/span')
    tab_3_4_text = "Privacy Policy"
    tab_3_4_des = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                             f'/div/div/div/div/div/div/div/div/div[2]/div[3]/div/div/section/div/div/div/div/'
                             f'div/div/div/div/div[2]/div[4]')

    tab_4_icon = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                            f'/div/div/div/div/div/div/div/div/div[1]/ul/li[4]/svg')
    tab_4 = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                       f'/div/div/div/div/div/div/div/div/div[1]/ul/li[4]/span')
    tab_4_text = "GOALS"
    tab_4_des = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                           f'/div/div/div/div/div/div/div/div/div[2]/div[4]')

    tab_5_icon = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                            f'/div/div/div/div/div/div/div/div/div[1]/ul/li[5]/svg')
    tab_5 = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                       f'/div/div/div/div/div/div/div/div/div[1]/ul/li[5]/span')
    tab_5_text = "PRIVACY"
    tab_5_des = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[4]'
                           f'/div/div/div/div/div/div/div/div/div[2]/div[5]')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.advanced_tabs)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 2378)")
            self.wait_for_bar_to_come()

            assert_that(self.browser.find_element(*self.tab_1).text).is_equal_to(self.tab_1_text)
            self.browser.find_element(*self.tab_1).click()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.tab_1_des).text).is_equal_to(self.tab_des_text)

            assert_that(self.browser.find_element(*self.tab_2).text).is_equal_to(self.tab_2_text)
            time.sleep(.5)
            self.browser.find_element(*self.tab_2).click()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.tab_2_1).text).is_equal_to(self.tab_2_1_text)
            self.browser.find_element(*self.tab_2_1).click()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.tab_2_1_des).text).is_equal_to(self.tab_nested_ver_des_text)

            assert_that(self.browser.find_element(*self.tab_2_2).text).is_equal_to(self.tab_2_2_text)
            self.browser.find_element(*self.tab_2_2).click()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.tab_2_2_des).text).is_equal_to(self.tab_nested_ver_des_text)

            assert_that(self.browser.find_element(*self.tab_2_3).text).is_equal_to(self.tab_2_3_text)
            self.browser.find_element(*self.tab_2_3).click()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.tab_2_3_des).text).is_equal_to(self.tab_nested_ver_des_text)

            assert_that(self.browser.find_element(*self.tab_2_4).text).is_equal_to(self.tab_2_4_text)
            self.browser.find_element(*self.tab_2_4).click()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.tab_2_4_des).text).is_equal_to(self.tab_nested_ver_des_text)

            assert_that(self.browser.find_element(*self.tab_3).text).is_equal_to(self.tab_3_text)
            self.browser.find_element(*self.tab_3).click()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.tab_3_1).text).is_equal_to(self.tab_2_1_text)
            self.browser.find_element(*self.tab_3_1).click()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.tab_3_1_des).text).is_equal_to(self.tab_nested_hor_des_text)

            assert_that(self.browser.find_element(*self.tab_3_2).text).is_equal_to(self.tab_3_2_text)
            self.browser.find_element(*self.tab_3_2).click()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.tab_3_2_des).text).is_equal_to(self.tab_nested_hor_des_text)

            assert_that(self.browser.find_element(*self.tab_3_3).text).is_equal_to(self.tab_3_3_text)
            self.browser.find_element(*self.tab_3_3).click()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.tab_3_3_des).text).is_equal_to(self.tab_nested_hor_des_text)

            assert_that(self.browser.find_element(*self.tab_3_4).text).is_equal_to(self.tab_3_4_text)
            self.browser.find_element(*self.tab_3_4).click()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.tab_3_4_des).text).is_equal_to(self.tab_nested_hor_des_text)

            assert_that(self.browser.find_element(*self.tab_4).text).is_equal_to(self.tab_4_text)
            self.browser.find_element(*self.tab_4).click()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.tab_4_des).text).is_equal_to(self.tab_des_text)

            assert_that(self.browser.find_element(*self.tab_5).text).is_equal_to(self.tab_5_text)
            self.browser.find_element(*self.tab_5).click()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.tab_5_des).text).is_equal_to(self.tab_des_text)




