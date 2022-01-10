from selenium.webdriver import ActionChains

from utils.config import *


class AdvancedDataTable:
    widget = '//*[@id="post-256377"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Advanced Data Table'
    doc_link = '//*[@id="post-256377"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a'
    doc_name = "EA ADVANCED DATA TABLE"
    # ---------------------------------------------
    thaead_1 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                          f'/div[1]/table/thead/tr/th[1]')
    thaead_1_text = "#"
    thaead_2 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                          f'/div[1]/table/thead/tr/th[2]')
    thaead_2_text = "Employee"
    thaead_3 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                          f'/div[1]/table/thead/tr/th[3]')
    thaead_3_text = "Working Days"
    thaead_4 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                          f'/div[1]/table/thead/tr/th[4]')
    thaead_4_text = "Hours"
    thaead_5 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                          f'/div[1]/table/thead/tr/th[5]')
    thaead_5_text = "Rate"
    thaead_6 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                          f'/div[1]/table/thead/tr/th[6]')
    thaead_6_text = "PAY"
    # ---------------------------------------------
    tbody_tr1_td1 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[1]/td[1]')
    tbody_tr1_td1_text = "1"
    tbody_tr1_td2 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[1]/td[2]')
    tbody_tr1_td2_text = "Garrett Winters"
    tbody_tr1_td3 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[1]/td[3]')
    tbody_tr1_td3_text = "Attend"
    tbody_tr1_td4 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[1]/td[4]')
    tbody_tr1_td4_text = "7:59:00"
    tbody_tr1_td5 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[1]/td[5]')
    tbody_tr1_td5_text = "$25.15"
    tbody_tr1_td6 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[1]/td[6]')
    tbody_tr1_td6_text = "$1,483.85"
    # ---------------------------------------------
    tbody_tr2_td1 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[2]/td[1]')
    tbody_tr2_td1_text = "2"
    tbody_tr2_td2 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[2]/td[2]')
    tbody_tr2_td2_text = "Brielle Williamson"
    tbody_tr2_td3 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[2]/td[3]')
    tbody_tr2_td3_text = "Attend"
    tbody_tr2_td4 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[2]/td[4]')
    tbody_tr2_td4_text = "9:39:00"
    tbody_tr2_td5 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[2]/td[5]')
    tbody_tr2_td5_text = "$18.15"
    tbody_tr2_td6 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[2]/td[6]')
    tbody_tr2_td6_text = "$4,483.85"
    # ---------------------------------------------
    tbody_tr3_td1 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[3]/td[1]')
    tbody_tr3_td1_text = "3"
    tbody_tr3_td2 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[3]/td[2]')
    tbody_tr3_td2_text = "Haley Kennedy"
    tbody_tr3_td3 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[3]/td[3]')
    tbody_tr3_td3_text = "Attend"
    tbody_tr3_td4 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[3]/td[4]')
    tbody_tr3_td4_text = "6:35:00"
    tbody_tr3_td5 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[3]/td[5]')
    tbody_tr3_td5_text = "$25.15"
    tbody_tr3_td6 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[3]/td[6]')
    tbody_tr3_td6_text = "$3,483.85"
    # ---------------------------------------------
    tbody_tr4_td1 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[4]/td[1]')
    tbody_tr4_td1_text = "4"
    tbody_tr4_td2 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[4]/td[2]')
    tbody_tr4_td2_text = "Garrett Winters"
    tbody_tr4_td3 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[4]/td[3]')
    tbody_tr4_td3_text = "1 Day Absent"
    tbody_tr4_td4 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[4]/td[4]')
    tbody_tr4_td4_text = "6:35:00"
    tbody_tr4_td5 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[4]/td[5]')
    tbody_tr4_td5_text = "$18.15"
    tbody_tr4_td6 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[4]/td[6]')
    tbody_tr4_td6_text = "$2,483.85"
    # ---------------------------------------------
    tbody_tr5_td1 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[5]/td[1]')
    tbody_tr5_td1_text = "5"
    tbody_tr5_td2 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[5]/td[2]')
    tbody_tr5_td2_text = "Brielle Williamson"
    tbody_tr5_td3 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[5]/td[3]')
    tbody_tr5_td3_text = "Attend"
    tbody_tr5_td4 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[5]/td[4]')
    tbody_tr5_td4_text = "9:39:00"
    tbody_tr5_td5 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[5]/td[5]')
    tbody_tr5_td5_text = "$18.15"
    tbody_tr5_td6 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[5]/td[6]')
    tbody_tr5_td6_text = "$1,483.85"
    # ---------------------------------------------
    tbody_tr6_td1 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[6]/td[1]')
    tbody_tr6_td1_text = "6"
    tbody_tr6_td2 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[6]/td[2]')
    tbody_tr6_td2_text = "Garrett Winters"
    tbody_tr6_td3 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[6]/td[3]')
    tbody_tr6_td3_text = "Attend"
    tbody_tr6_td4 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[6]/td[4]')
    tbody_tr6_td4_text = "7:59:00"
    tbody_tr6_td5 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[6]/td[5]')
    tbody_tr6_td5_text = "$25.15"
    tbody_tr6_td6 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[6]/td[6]')
    tbody_tr6_td6_text = "$2,483.85"
    # ---------------------------------------------
    tbody_tr7_td1 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[7]/td[1]')
    tbody_tr7_td1_text = "7"
    tbody_tr7_td2 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[7]/td[2]')
    tbody_tr7_td2_text = "Brielle Williamson"
    tbody_tr7_td3 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[7]/td[3]')
    tbody_tr7_td3_text = "3 Day Absent"
    tbody_tr7_td4 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[7]/td[4]')
    tbody_tr7_td4_text = "6:35:00"
    tbody_tr7_td5 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[7]/td[5]')
    tbody_tr7_td5_text = "$18.15"
    tbody_tr7_td6 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[7]/td[6]')
    tbody_tr7_td6_text = "$3,483.85"
    # ---------------------------------------------
    tbody_tr8_td1 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[8]/td[1]')
    tbody_tr8_td1_text = "8"
    tbody_tr8_td2 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[8]/td[2]')
    tbody_tr8_td2_text = "Haley Kennedy"
    tbody_tr8_td3 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[8]/td[3]')
    tbody_tr8_td3_text = "Attend"
    tbody_tr8_td4 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[8]/td[4]')
    tbody_tr8_td4_text = "6:35:00"
    tbody_tr8_td5 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[8]/td[5]')
    tbody_tr8_td5_text = "$25.15"
    tbody_tr8_td6 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[8]/td[6]')
    tbody_tr8_td6_text = "$1,483.85"
    # ---------------------------------------------
    tbody_tr9_td1 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[9]/td[1]')
    tbody_tr9_td1_text = "9"
    tbody_tr9_td2 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[9]/td[2]')
    tbody_tr9_td2_text = "Brielle Williamson"
    tbody_tr9_td3 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[9]/td[3]')
    tbody_tr9_td3_text = "Attend"
    tbody_tr9_td4 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[9]/td[4]')
    tbody_tr9_td4_text = "9:39:00"
    tbody_tr9_td5 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[9]/td[5]')
    tbody_tr9_td5_text = "$18.15"
    tbody_tr9_td6 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[9]/td[6]')
    tbody_tr9_td6_text = "$2,483.85"
    # ---------------------------------------------
    tbody_tr10_td1 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[10]/td[1]')
    tbody_tr10_td1_text = "10"
    tbody_tr10_td2 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[10]/td[2]')
    tbody_tr10_td2_text = "Garrett Winters"
    tbody_tr10_td3 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[10]/td[3]')
    tbody_tr10_td3_text = "1 Day Absent"
    tbody_tr10_td4 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[10]/td[4]')
    tbody_tr10_td4_text = "7:59:00"
    tbody_tr10_td5 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[10]/td[5]')
    tbody_tr10_td5_text = "$25.15"
    tbody_tr10_td6 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/'
                               f'div/div[1]/table/tbody/tr[10]/td[6]')
    tbody_tr10_td6_text = "$1,483.85"
    # ---------------------------------------------
    page_1 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                        f'/div[2]/a[2]')
    page_2 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                        f'/div[2]/a[3]')
    page_pre = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                          f'/div[2]/a[1]')
    page_next = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                           f'/div[2]/a[4]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(advanced_data_table)

    def first_page_list(self):
        with soft_assertions():
            # 1
            assert_that(self.browser.find_element(*self.tbody_tr1_td1).text).is_equal_to(self.tbody_tr1_td1_text)
            assert_that(self.browser.find_element(*self.tbody_tr1_td2).text).is_equal_to(self.tbody_tr1_td2_text)
            assert_that(self.browser.find_element(*self.tbody_tr1_td3).text).is_equal_to(self.tbody_tr1_td3_text)
            assert_that(self.browser.find_element(*self.tbody_tr1_td4).text).is_equal_to(self.tbody_tr1_td4_text)
            assert_that(self.browser.find_element(*self.tbody_tr1_td5).text).is_equal_to(self.tbody_tr1_td5_text)
            assert_that(self.browser.find_element(*self.tbody_tr1_td6).text).is_equal_to(self.tbody_tr1_td6_text)
            # 2
            assert_that(self.browser.find_element(*self.tbody_tr2_td1).text).is_equal_to(self.tbody_tr2_td1_text)
            assert_that(self.browser.find_element(*self.tbody_tr2_td2).text).is_equal_to(self.tbody_tr2_td2_text)
            assert_that(self.browser.find_element(*self.tbody_tr2_td3).text).is_equal_to(self.tbody_tr2_td3_text)
            assert_that(self.browser.find_element(*self.tbody_tr2_td4).text).is_equal_to(self.tbody_tr2_td4_text)
            assert_that(self.browser.find_element(*self.tbody_tr2_td5).text).is_equal_to(self.tbody_tr2_td5_text)
            assert_that(self.browser.find_element(*self.tbody_tr2_td6).text).is_equal_to(self.tbody_tr2_td6_text)
            # 3
            assert_that(self.browser.find_element(*self.tbody_tr3_td1).text).is_equal_to(self.tbody_tr3_td1_text)
            assert_that(self.browser.find_element(*self.tbody_tr3_td2).text).is_equal_to(self.tbody_tr3_td2_text)
            assert_that(self.browser.find_element(*self.tbody_tr3_td3).text).is_equal_to(self.tbody_tr3_td3_text)
            assert_that(self.browser.find_element(*self.tbody_tr3_td4).text).is_equal_to(self.tbody_tr3_td4_text)
            assert_that(self.browser.find_element(*self.tbody_tr3_td5).text).is_equal_to(self.tbody_tr3_td5_text)
            assert_that(self.browser.find_element(*self.tbody_tr3_td6).text).is_equal_to(self.tbody_tr3_td6_text)
            # 4
            assert_that(self.browser.find_element(*self.tbody_tr4_td1).text).is_equal_to(self.tbody_tr4_td1_text)
            assert_that(self.browser.find_element(*self.tbody_tr4_td2).text).is_equal_to(self.tbody_tr4_td2_text)
            assert_that(self.browser.find_element(*self.tbody_tr4_td3).text).is_equal_to(self.tbody_tr4_td3_text)
            assert_that(self.browser.find_element(*self.tbody_tr4_td4).text).is_equal_to(self.tbody_tr4_td4_text)
            assert_that(self.browser.find_element(*self.tbody_tr4_td5).text).is_equal_to(self.tbody_tr4_td5_text)
            assert_that(self.browser.find_element(*self.tbody_tr4_td6).text).is_equal_to(self.tbody_tr4_td6_text)
            # 5
            assert_that(self.browser.find_element(*self.tbody_tr5_td1).text).is_equal_to(self.tbody_tr5_td1_text)
            assert_that(self.browser.find_element(*self.tbody_tr5_td2).text).is_equal_to(self.tbody_tr5_td2_text)
            assert_that(self.browser.find_element(*self.tbody_tr5_td3).text).is_equal_to(self.tbody_tr5_td3_text)
            assert_that(self.browser.find_element(*self.tbody_tr5_td4).text).is_equal_to(self.tbody_tr5_td4_text)
            assert_that(self.browser.find_element(*self.tbody_tr5_td5).text).is_equal_to(self.tbody_tr5_td5_text)
            assert_that(self.browser.find_element(*self.tbody_tr5_td6).text).is_equal_to(self.tbody_tr5_td6_text)
            # 6
            assert_that(self.browser.find_element(*self.tbody_tr6_td1).text).is_equal_to(self.tbody_tr6_td1_text)
            assert_that(self.browser.find_element(*self.tbody_tr6_td2).text).is_equal_to(self.tbody_tr6_td2_text)
            assert_that(self.browser.find_element(*self.tbody_tr6_td3).text).is_equal_to(self.tbody_tr6_td3_text)
            assert_that(self.browser.find_element(*self.tbody_tr6_td4).text).is_equal_to(self.tbody_tr6_td4_text)
            assert_that(self.browser.find_element(*self.tbody_tr6_td5).text).is_equal_to(self.tbody_tr6_td5_text)
            assert_that(self.browser.find_element(*self.tbody_tr6_td6).text).is_equal_to(self.tbody_tr6_td6_text)
            # 7
            assert_that(self.browser.find_element(*self.tbody_tr7_td1).text).is_equal_to(self.tbody_tr7_td1_text)
            assert_that(self.browser.find_element(*self.tbody_tr7_td2).text).is_equal_to(self.tbody_tr7_td2_text)
            assert_that(self.browser.find_element(*self.tbody_tr7_td3).text).is_equal_to(self.tbody_tr7_td3_text)
            assert_that(self.browser.find_element(*self.tbody_tr7_td4).text).is_equal_to(self.tbody_tr7_td4_text)
            assert_that(self.browser.find_element(*self.tbody_tr7_td5).text).is_equal_to(self.tbody_tr7_td5_text)
            assert_that(self.browser.find_element(*self.tbody_tr7_td6).text).is_equal_to(self.tbody_tr7_td6_text)

    def second_page_list(self):
        with soft_assertions():
            # 8
            assert_that(self.browser.find_element(*self.tbody_tr8_td1).text).is_equal_to(self.tbody_tr8_td1_text)
            assert_that(self.browser.find_element(*self.tbody_tr8_td2).text).is_equal_to(self.tbody_tr8_td2_text)
            assert_that(self.browser.find_element(*self.tbody_tr8_td3).text).is_equal_to(self.tbody_tr8_td3_text)
            assert_that(self.browser.find_element(*self.tbody_tr8_td4).text).is_equal_to(self.tbody_tr8_td4_text)
            assert_that(self.browser.find_element(*self.tbody_tr8_td5).text).is_equal_to(self.tbody_tr8_td5_text)
            assert_that(self.browser.find_element(*self.tbody_tr8_td6).text).is_equal_to(self.tbody_tr8_td6_text)
            # 9
            assert_that(self.browser.find_element(*self.tbody_tr9_td1).text).is_equal_to(self.tbody_tr9_td1_text)
            assert_that(self.browser.find_element(*self.tbody_tr9_td2).text).is_equal_to(self.tbody_tr9_td2_text)
            assert_that(self.browser.find_element(*self.tbody_tr9_td3).text).is_equal_to(self.tbody_tr9_td3_text)
            assert_that(self.browser.find_element(*self.tbody_tr9_td4).text).is_equal_to(self.tbody_tr9_td4_text)
            assert_that(self.browser.find_element(*self.tbody_tr9_td5).text).is_equal_to(self.tbody_tr9_td5_text)
            assert_that(self.browser.find_element(*self.tbody_tr9_td6).text).is_equal_to(self.tbody_tr9_td6_text)
            # 10
            assert_that(self.browser.find_element(*self.tbody_tr10_td1).text).is_equal_to(self.tbody_tr10_td1_text)
            assert_that(self.browser.find_element(*self.tbody_tr10_td2).text).is_equal_to(self.tbody_tr10_td2_text)
            assert_that(self.browser.find_element(*self.tbody_tr10_td3).text).is_equal_to(self.tbody_tr10_td3_text)
            assert_that(self.browser.find_element(*self.tbody_tr10_td4).text).is_equal_to(self.tbody_tr10_td4_text)
            assert_that(self.browser.find_element(*self.tbody_tr10_td5).text).is_equal_to(self.tbody_tr10_td5_text)
            assert_that(self.browser.find_element(*self.tbody_tr10_td6).text).is_equal_to(self.tbody_tr10_td6_text)

    def after_sort(self):
        with soft_assertions():
            # 1
            assert_that(self.browser.find_element(*self.tbody_tr1_td1).text).is_equal_to(self.tbody_tr7_td1_text)
            assert_that(self.browser.find_element(*self.tbody_tr1_td2).text).is_equal_to(self.tbody_tr7_td2_text)
            assert_that(self.browser.find_element(*self.tbody_tr1_td3).text).is_equal_to(self.tbody_tr7_td3_text)
            assert_that(self.browser.find_element(*self.tbody_tr1_td4).text).is_equal_to(self.tbody_tr7_td4_text)
            assert_that(self.browser.find_element(*self.tbody_tr1_td5).text).is_equal_to(self.tbody_tr7_td5_text)
            assert_that(self.browser.find_element(*self.tbody_tr1_td6).text).is_equal_to(self.tbody_tr7_td6_text)
            # 7
            assert_that(self.browser.find_element(*self.tbody_tr7_td1).text).is_equal_to(self.tbody_tr1_td1_text)
            assert_that(self.browser.find_element(*self.tbody_tr7_td2).text).is_equal_to(self.tbody_tr1_td2_text)
            assert_that(self.browser.find_element(*self.tbody_tr7_td3).text).is_equal_to(self.tbody_tr1_td3_text)
            assert_that(self.browser.find_element(*self.tbody_tr7_td4).text).is_equal_to(self.tbody_tr1_td4_text)
            assert_that(self.browser.find_element(*self.tbody_tr7_td5).text).is_equal_to(self.tbody_tr1_td5_text)
            assert_that(self.browser.find_element(*self.tbody_tr7_td6).text).is_equal_to(self.tbody_tr1_td6_text)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 2811)")
            time.sleep(1)

            assert_that(self.browser.find_element(*self.thaead_1).text).is_equal_to(self.thaead_1_text)
            assert_that(self.browser.find_element(*self.thaead_2).text).is_equal_to(self.thaead_2_text)
            assert_that(self.browser.find_element(*self.thaead_3).text).is_equal_to(self.thaead_3_text)
            assert_that(self.browser.find_element(*self.thaead_4).text).is_equal_to(self.thaead_4_text)
            assert_that(self.browser.find_element(*self.thaead_5).text).is_equal_to(self.thaead_5_text)
            assert_that(self.browser.find_element(*self.thaead_6).text).is_equal_to(self.thaead_6_text)
            self.first_page_list()
            self.browser.find_element(*self.page_2).click()
            time.sleep(.5)
            self.second_page_list()
            self.browser.find_element(*self.page_1).click()
            time.sleep(.5)
            self.first_page_list()
            self.browser.find_element(*self.page_next).click()
            time.sleep(.5)
            self.second_page_list()
            self.browser.find_element(*self.page_pre).click()
            time.sleep(.5)
            self.first_page_list()
            time.sleep(.5)
            self.browser.find_element(*self.thaead_1).click()
            self.browser.find_element(*self.thaead_1).click()
            time.sleep(.5)
            self.after_sort()




