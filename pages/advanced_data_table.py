from pages.basepage import BasePage
from utils.config import *


class AdvancedDataTable(BasePage, Helper):
    widget = '//*[@id="post-256377"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Advanced Data Table'
    doc_link = '//*[@id="post-256377"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a'
    doc_name = "EA ADVANCED DATA TABLE"
    # ---------------------------------------------
    thead_1 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                          f'/div[1]/table/thead/tr/th[1]')
    thead_1_text = "#"
    thead_2 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                          f'/div[1]/table/thead/tr/th[2]')
    thead_2_text = "Employee"
    thead_3 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                          f'/div[1]/table/thead/tr/th[3]')
    thead_3_text = "Working Days"
    thead_4 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                          f'/div[1]/table/thead/tr/th[4]')
    thead_4_text = "Hours"
    thead_5 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                          f'/div[1]/table/thead/tr/th[5]')
    thead_5_text = "Rate"
    thead_6 = (By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/div'
                          f'/div[1]/table/thead/tr/th[6]')
    thead_6_text = "PAY"
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

    sort = (By.XPATH, "//th[normalize-space()='#']")

    scroll = (By.CSS_SELECTOR, '.elementor-element-466afb7b')
    scroll_1 = (By.CSS_SELECTOR, '.elementor-element-72de6d0c')

    # Data Table Style 05
    thead_dt5_1 = (By.XPATH, "//span[normalize-space()='Custom CSS']")
    thead_dt5_2 = (By.XPATH, "//span[normalize-space()='Forms']")
    thead_dt5_3 = (By.XPATH, "//span[normalize-space()='Mobile Editing']")
    thead_dt5_4 = (By.XPATH, "//span[normalize-space()='Nav Menu']")
    thead_dt5_5 = (By.XPATH, "//span[normalize-space()='Nav Menu']")
    thead_dt5_6 = (By.XPATH, "//span[normalize-space()='Shape Divider']")
    thead_dt5_7 = (By.XPATH, "//span[normalize-space()='Template Library']")

    thead_dt5_1_text = "Custom CSS"
    thead_dt5_2_text = "Forms"
    thead_dt5_3_text = "Mobile Editing"
    thead_dt5_4_text = "Nav Menu"
    thead_dt5_5_text = "Nav Menu"
    thead_dt5_6_text = "Shape Divider"
    thead_dt5_7_text = "Template Library"

    def __init__(self, browser):
        super().__init__(browser)

    def first_page_list(self):
        # 1
        self.check_text_matches_with(self.tbody_tr1_td1, self.tbody_tr1_td1_text)
        self.check_text_matches_with(self.tbody_tr1_td2, self.tbody_tr1_td2_text)
        self.check_text_matches_with(self.tbody_tr1_td3, self.tbody_tr1_td3_text)
        self.check_text_matches_with(self.tbody_tr1_td4, self.tbody_tr1_td4_text)
        self.check_text_matches_with(self.tbody_tr1_td5, self.tbody_tr1_td5_text)
        self.check_text_matches_with(self.tbody_tr1_td6, self.tbody_tr1_td6_text)
        # 2
        self.check_text_matches_with(self.tbody_tr2_td1, self.tbody_tr2_td1_text)
        self.check_text_matches_with(self.tbody_tr2_td2, self.tbody_tr2_td2_text)
        self.check_text_matches_with(self.tbody_tr2_td3, self.tbody_tr2_td3_text)
        self.check_text_matches_with(self.tbody_tr2_td4, self.tbody_tr2_td4_text)
        self.check_text_matches_with(self.tbody_tr2_td5, self.tbody_tr2_td5_text)
        self.check_text_matches_with(self.tbody_tr2_td6, self.tbody_tr2_td6_text)
        # 3
        self.check_text_matches_with(self.tbody_tr3_td1, self.tbody_tr3_td1_text)
        self.check_text_matches_with(self.tbody_tr3_td2, self.tbody_tr3_td2_text)
        self.check_text_matches_with(self.tbody_tr3_td3, self.tbody_tr3_td3_text)
        self.check_text_matches_with(self.tbody_tr3_td4, self.tbody_tr3_td4_text)
        self.check_text_matches_with(self.tbody_tr3_td5, self.tbody_tr3_td5_text)
        self.check_text_matches_with(self.tbody_tr3_td6, self.tbody_tr3_td6_text)
        # 4
        self.check_text_matches_with(self.tbody_tr4_td1, self.tbody_tr4_td1_text)
        self.check_text_matches_with(self.tbody_tr4_td2, self.tbody_tr4_td2_text)
        self.check_text_matches_with(self.tbody_tr4_td3, self.tbody_tr4_td3_text)
        self.check_text_matches_with(self.tbody_tr4_td4, self.tbody_tr4_td4_text)
        self.check_text_matches_with(self.tbody_tr4_td5, self.tbody_tr4_td5_text)
        self.check_text_matches_with(self.tbody_tr4_td6, self.tbody_tr4_td6_text)
        # 5
        self.check_text_matches_with(self.tbody_tr5_td1, self.tbody_tr5_td1_text)
        self.check_text_matches_with(self.tbody_tr5_td2, self.tbody_tr5_td2_text)
        self.check_text_matches_with(self.tbody_tr5_td3, self.tbody_tr5_td3_text)
        self.check_text_matches_with(self.tbody_tr5_td4, self.tbody_tr5_td4_text)
        self.check_text_matches_with(self.tbody_tr5_td5, self.tbody_tr5_td5_text)
        self.check_text_matches_with(self.tbody_tr5_td6, self.tbody_tr5_td6_text)
        # 6
        self.check_text_matches_with(self.tbody_tr6_td1, self.tbody_tr6_td1_text)
        self.check_text_matches_with(self.tbody_tr6_td2, self.tbody_tr6_td2_text)
        self.check_text_matches_with(self.tbody_tr6_td3, self.tbody_tr6_td3_text)
        self.check_text_matches_with(self.tbody_tr6_td4, self.tbody_tr6_td4_text)
        self.check_text_matches_with(self.tbody_tr6_td5, self.tbody_tr6_td5_text)
        self.check_text_matches_with(self.tbody_tr6_td6, self.tbody_tr6_td6_text)
        # 7
        self.check_text_matches_with(self.tbody_tr7_td1, self.tbody_tr7_td1_text)
        self.check_text_matches_with(self.tbody_tr7_td2, self.tbody_tr7_td2_text)
        self.check_text_matches_with(self.tbody_tr7_td3, self.tbody_tr7_td3_text)
        self.check_text_matches_with(self.tbody_tr7_td4, self.tbody_tr7_td4_text)
        self.check_text_matches_with(self.tbody_tr7_td5, self.tbody_tr7_td5_text)
        self.check_text_matches_with(self.tbody_tr7_td6, self.tbody_tr7_td6_text)

    def second_page_list(self):
        # 8
        self.check_text_matches_with(self.tbody_tr8_td1, self.tbody_tr8_td1_text)
        self.check_text_matches_with(self.tbody_tr8_td2, self.tbody_tr8_td2_text)
        self.check_text_matches_with(self.tbody_tr8_td3, self.tbody_tr8_td3_text)
        self.check_text_matches_with(self.tbody_tr8_td4, self.tbody_tr8_td4_text)
        self.check_text_matches_with(self.tbody_tr8_td5, self.tbody_tr8_td5_text)
        self.check_text_matches_with(self.tbody_tr8_td6, self.tbody_tr8_td6_text)
        # 9
        self.check_text_matches_with(self.tbody_tr9_td1, self.tbody_tr9_td1_text)
        self.check_text_matches_with(self.tbody_tr9_td2, self.tbody_tr9_td2_text)
        self.check_text_matches_with(self.tbody_tr9_td3, self.tbody_tr9_td3_text)
        self.check_text_matches_with(self.tbody_tr9_td4, self.tbody_tr9_td4_text)
        self.check_text_matches_with(self.tbody_tr9_td5, self.tbody_tr9_td5_text)
        self.check_text_matches_with(self.tbody_tr9_td6, self.tbody_tr9_td6_text)
        # 10
        self.check_text_matches_with(self.tbody_tr10_td1, self.tbody_tr10_td1_text)
        self.check_text_matches_with(self.tbody_tr10_td2, self.tbody_tr10_td2_text)
        self.check_text_matches_with(self.tbody_tr10_td3, self.tbody_tr10_td3_text)
        self.check_text_matches_with(self.tbody_tr10_td4, self.tbody_tr10_td4_text)
        self.check_text_matches_with(self.tbody_tr10_td5, self.tbody_tr10_td5_text)
        self.check_text_matches_with(self.tbody_tr10_td6, self.tbody_tr10_td6_text)

    def after_sort(self):
        # 1
        self.check_text_matches_with(self.tbody_tr1_td1, self.tbody_tr10_td1_text)
        self.check_text_matches_with(self.tbody_tr1_td2, self.tbody_tr10_td2_text)
        self.check_text_matches_with(self.tbody_tr1_td3, self.tbody_tr10_td3_text)
        self.check_text_matches_with(self.tbody_tr1_td4, self.tbody_tr10_td4_text)
        self.check_text_matches_with(self.tbody_tr1_td5, self.tbody_tr10_td5_text)
        self.check_text_matches_with(self.tbody_tr1_td6, self.tbody_tr10_td6_text)
        self.do_click(self.page_next)
        # 10
        self.check_text_matches_with(self.tbody_tr10_td1, self.tbody_tr1_td1_text)
        self.check_text_matches_with(self.tbody_tr10_td2, self.tbody_tr1_td2_text)
        self.check_text_matches_with(self.tbody_tr10_td3, self.tbody_tr1_td3_text)
        self.check_text_matches_with(self.tbody_tr10_td4, self.tbody_tr1_td4_text)
        self.check_text_matches_with(self.tbody_tr10_td5, self.tbody_tr1_td5_text)
        self.check_text_matches_with(self.tbody_tr10_td6, self.tbody_tr1_td6_text)

    def data_table_style_05(self):
        self.check_text_matches_with(self.thead_dt5_1, self.thead_dt5_1_text)
        self.check_text_matches_with(self.thead_dt5_2, self.thead_dt5_2_text)
        self.check_text_matches_with(self.thead_dt5_3, self.thead_dt5_3_text)
        self.check_text_matches_with(self.thead_dt5_4, self.thead_dt5_4_text)
        self.check_text_matches_with(self.thead_dt5_5, self.thead_dt5_5_text)
        self.check_text_matches_with(self.thead_dt5_6, self.thead_dt5_6_text)
        self.check_text_matches_with(self.thead_dt5_7, self.thead_dt5_7_text)

        for i in range(2, 4):
            self.is_visible((By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[7]/div/div/div/div/div/div/'
                                       f'div/div/div/table/tbody/tr[1]/td[{i}]/img'),
                            f'Image {i - 1} is not visible')

        for i in range(2, 5):
            for j in range(2, 9):
                self.is_visible((By.XPATH, f'//*[@id="post-256377"]/div/div/div/div/section[7]/div/div/div/div/div/'
                                           f'div/div/div/div/table/tbody/tr[{j}]/td[{i}]/i'),
                                f'Column {i-1} raw {j} not visible')

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.advanced_data_table)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to_element(self.scroll)
                """Check headers"""
                self.check_text_matches_with(self.thead_1, self.thead_1_text)
                self.check_text_matches_with(self.thead_2, self.thead_2_text)
                self.check_text_matches_with(self.thead_3, self.thead_3_text)
                self.check_text_matches_with(self.thead_4, self.thead_4_text)
                self.check_text_matches_with(self.thead_5, self.thead_5_text)
                self.check_text_matches_with(self.thead_6, self.thead_6_text)
                """Check first page"""
                self.first_page_list()
                """Click second pagination and check second page"""
                self.do_click(self.page_2)
                self.second_page_list()
                """Click first pagination and check first page"""
                self.do_click(self.page_1)
                self.first_page_list()
                """Click next pagination and check second page"""
                self.do_click(self.page_next)
                self.second_page_list()
                """Click previous pagination and check first page"""
                self.do_click(self.page_pre)
                self.first_page_list()
                """Short Table"""
                self.do_click(self.sort)
                self.scroll_to_element(self.scroll)
                self.do_click(self.sort)
                """Check shorted table"""
                self.after_sort()

                # Data table Style 05
                self.scroll_to_element(self.scroll_1)
                self.data_table_style_05()

