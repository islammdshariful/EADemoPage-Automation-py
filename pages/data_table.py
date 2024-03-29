from utils.config import *


class DataTable(BasePage, Helper):
    widget = '//*[@id="post-1836"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section[1]' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Data Table'
    doc_link = '//*[@id="post-1836"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section[1]' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "DATA TABLE"
    # ---------------------------------------------
    thaead_1 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/thead/tr/th[1]')
    thaead_1_text = "#"
    thaead_2 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/thead/tr/th[2]')
    thaead_2_text = "Employee"
    thaead_3 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/thead/tr/th[3]')
    thaead_3_text = "Working Days"
    thaead_4 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/thead/tr/th[4]')
    thaead_4_text = "Hours"
    thaead_5 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/thead/tr/th[5]')
    thaead_5_text = "Rate"
    thaead_6 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/thead/tr/th[6]')
    thaead_6_text = "Pay"
    # ---------------------------------------------
    tbody_tr1_td1 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[1]/td[1]')
    tbody_tr1_td1_text = "1"
    tbody_tr1_td2 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[1]/td[2]')
    tbody_tr1_td2_text = "Garrett Winters"
    tbody_tr1_td3 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[1]/td[3]')
    tbody_tr1_td3_text = "Attend"
    tbody_tr1_td4 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[1]/td[4]')
    tbody_tr1_td4_text = "7:59:00"
    tbody_tr1_td5 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[1]/td[5]')
    tbody_tr1_td5_text = "$25.15"
    tbody_tr1_td6 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[1]/td[6]')
    tbody_tr1_td6_text = "$1,483.85"
    # ---------------------------------------------
    tbody_tr2_td1 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[2]/td[1]')
    tbody_tr2_td1_text = "2"
    tbody_tr2_td2 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[2]/td[2]')
    tbody_tr2_td2_text = "Brielle Williamson"
    tbody_tr2_td3 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[2]/td[3]')
    tbody_tr2_td3_text = "Attend"
    tbody_tr2_td4 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[2]/td[4]')
    tbody_tr2_td4_text = "9:39:00"
    tbody_tr2_td5 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[2]/td[5]')
    tbody_tr2_td5_text = "$18.15"
    tbody_tr2_td6 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[2]/td[6]')
    tbody_tr2_td6_text = "$886.5"
    # ---------------------------------------------
    tbody_tr3_td1 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[3]/td[1]')
    tbody_tr3_td1_text = "3"
    tbody_tr3_td2 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[3]/td[2]')
    tbody_tr3_td2_text = "Haley Kennedy"
    tbody_tr3_td3 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[3]/td[3]')
    tbody_tr3_td3_text = "Attend"
    tbody_tr3_td4 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[3]/td[4]')
    tbody_tr3_td4_text = "6:35:00"
    tbody_tr3_td5 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[3]/td[5]')
    tbody_tr3_td5_text = "$32.15"
    tbody_tr3_td6 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[3]/td[6]')
    tbody_tr3_td6_text = "$1,116,9"
    # ---------------------------------------------
    tbody_tr4_td1 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[4]/td[1]')
    tbody_tr4_td1_text = "4"
    tbody_tr4_td2 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[4]/td[2]')
    tbody_tr4_td2_text = "Template Library"
    tbody_tr4_td3 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[4]/td[3]')
    tbody_tr4_td3_text = "1 Day Absent"
    tbody_tr4_td4 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[4]/td[4]')
    tbody_tr4_td4_text = "9:39:00"
    tbody_tr4_td5 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[4]/td[5]')
    tbody_tr4_td5_text = "$25.15"
    tbody_tr4_td6 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[4]/td[6]')
    tbody_tr4_td6_text = "$1,028.6"
    # ---------------------------------------------
    tbody_tr5_td1 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[5]/td[1]')
    tbody_tr5_td1_text = "5"
    tbody_tr5_td2 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[5]/td[2]')
    tbody_tr5_td2_text = "Garrett Winters"
    tbody_tr5_td3 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[5]/td[3]')
    tbody_tr5_td3_text = "Attend"
    tbody_tr5_td4 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[5]/td[4]')
    tbody_tr5_td4_text = "7:59:00"
    tbody_tr5_td5 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[5]/td[5]')
    tbody_tr5_td5_text = "$23.15"
    tbody_tr5_td6 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[5]/td[6]')
    tbody_tr5_td6_text = "$1,483.85"
    # ---------------------------------------------
    tbody_tr6_td1 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[6]/td[1]')
    tbody_tr6_td1_text = "6"
    tbody_tr6_td2 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[6]/td[2]')
    tbody_tr6_td2_text = "Brielle Williamson"
    tbody_tr6_td3 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[6]/td[3]')
    tbody_tr6_td3_text = "3 Day Absent"
    tbody_tr6_td4 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[6]/td[4]')
    tbody_tr6_td4_text = "9:39:00"
    tbody_tr6_td5 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[6]/td[5]')
    tbody_tr6_td5_text = "$15.15"
    tbody_tr6_td6 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[6]/td[6]')
    tbody_tr6_td6_text = "$534"
    # ---------------------------------------------
    tbody_tr7_td1 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[7]/td[1]')
    tbody_tr7_td1_text = "7"
    tbody_tr7_td2 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[7]/td[2]')
    tbody_tr7_td2_text = "Haley Kennedy"
    tbody_tr7_td3 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[7]/td[3]')
    tbody_tr7_td3_text = "Attend"
    tbody_tr7_td4 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[7]/td[4]')
    tbody_tr7_td4_text = "6:35:00"
    tbody_tr7_td5 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[7]/td[5]')
    tbody_tr7_td5_text = "$33.15"
    tbody_tr7_td6 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[7]/td[6]')
    tbody_tr7_td6_text = "$2,070.45"
    # ---------------------------------------------
    tbody_tr8_td1 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[8]/td[1]')
    tbody_tr8_td1_text = "8"
    tbody_tr8_td2 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[8]/td[2]')
    tbody_tr8_td2_text = "Template Library"
    tbody_tr8_td3 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[8]/td[3]')
    tbody_tr8_td3_text = "Attend"
    tbody_tr8_td4 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[8]/td[4]')
    tbody_tr8_td4_text = "9:39:00"
    tbody_tr8_td5 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[8]/td[5]')
    tbody_tr8_td5_text = "$12.15"
    tbody_tr8_td6 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[8]/td[6]')
    tbody_tr8_td6_text = "$1,246.2"
    # ---------------------------------------------
    tbody_tr9_td1 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[9]/td[1]')
    tbody_tr9_td1_text = "9"
    tbody_tr9_td2 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[9]/td[2]')
    tbody_tr9_td2_text = "Garrett Winters"
    tbody_tr9_td3 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[9]/td[3]')
    tbody_tr9_td3_text = "Attend"
    tbody_tr9_td4 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[9]/td[4]')
    tbody_tr9_td4_text = "7:59:00"
    tbody_tr9_td5 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[9]/td[5]')
    tbody_tr9_td5_text = "$5.15"
    tbody_tr9_td6 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[9]/td[6]')
    tbody_tr9_td6_text = "$1,135.75"
    # ---------------------------------------------
    tbody_tr10_td1 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[10]/td[1]')
    tbody_tr10_td1_text = "10"
    tbody_tr10_td2 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[10]/td[2]')
    tbody_tr10_td2_text = "Brielle Williamson"
    tbody_tr10_td3 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[10]/td[3]')
    tbody_tr10_td3_text = "1 Day Absent"
    tbody_tr10_td4 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[10]/td[4]')
    tbody_tr10_td4_text = "6:35:00"
    tbody_tr10_td5 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[10]/td[5]')
    tbody_tr10_td5_text = "$25.15"
    tbody_tr10_td6 = (By.XPATH, f'//*[@id="eael-data-table-1c75c528"]/tbody/tr[10]/td[6]')
    tbody_tr10_td6_text = "$736"

    scroll = (By.CSS_SELECTOR, '.elementor-element-386c9184')

    def __init__(self, browser):
        super().__init__(browser)

    def first_page_list(self):
        with soft_assertions():
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
        with soft_assertions():
            # 1
            self.check_text_matches_with(self.tbody_tr1_td1, self.tbody_tr10_td1_text)
            self.check_text_matches_with(self.tbody_tr1_td2, self.tbody_tr10_td2_text)
            self.check_text_matches_with(self.tbody_tr1_td3, self.tbody_tr10_td3_text)
            self.check_text_matches_with(self.tbody_tr1_td4, self.tbody_tr10_td4_text)
            self.check_text_matches_with(self.tbody_tr1_td5, self.tbody_tr10_td5_text)
            self.check_text_matches_with(self.tbody_tr1_td6, self.tbody_tr10_td6_text)
            # 10
            self.check_text_matches_with(self.tbody_tr10_td1, self.tbody_tr1_td1_text)
            self.check_text_matches_with(self.tbody_tr10_td2, self.tbody_tr1_td2_text)
            self.check_text_matches_with(self.tbody_tr10_td3, self.tbody_tr1_td3_text)
            self.check_text_matches_with(self.tbody_tr10_td4, self.tbody_tr1_td4_text)
            self.check_text_matches_with(self.tbody_tr10_td5, self.tbody_tr1_td5_text)
            self.check_text_matches_with(self.tbody_tr10_td6, self.tbody_tr1_td6_text)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.data_table)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to_element(self.scroll)
                """Checking table header"""
                self.check_text_matches_with(self.thaead_1, self.thaead_1_text)
                self.check_text_matches_with(self.thaead_2, self.thaead_2_text)
                self.check_text_matches_with(self.thaead_3, self.thaead_3_text)
                self.check_text_matches_with(self.thaead_4, self.thaead_4_text)
                self.check_text_matches_with(self.thaead_5, self.thaead_5_text)
                self.check_text_matches_with(self.thaead_6, self.thaead_6_text)
                """Checking column data"""
                self.first_page_list()
                """Sort table"""
                self.do_click(self.thaead_1)
                self.do_click(self.thaead_1)
                """Checking column data after sort"""
                self.after_sort()
