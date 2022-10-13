from selenium.webdriver import ActionChains

from pages.basepage import BasePage
from utils.config import *


class TeamMember(BasePage, Helper):
    widget = '//*[@id="post-1022"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Team Member'
    doc_link = '//*[@id="post-1022"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "TEAM MEMBERS"

    mem_1_img = (By.XPATH, f'//*[@id="eael-team-member-2bac67d3"]/div/div[1]/figure/img')
    mem_1_name = (By.XPATH, f'//*[@id="eael-team-member-2bac67d3"]/div/div[2]/h3')
    mem_1_name_text = "Jemes Barber"
    mem_1_pos = (By.XPATH, f'//*[@id="eael-team-member-2bac67d3"]/div/div[2]/h4')
    mem_1_pos_text = "Beard Trimmer"
    mem_1_fb = (By.XPATH, f'//*[@id="eael-team-member-2bac67d3"]/div/div[2]/ul/li[1]/a/i')
    mem_1_tw = (By.XPATH, f'//*[@id="eael-team-member-2bac67d3"]/div/div[2]/ul/li[2]/a/i')
    mem_1_in = (By.XPATH, f'//*[@id="eael-team-member-2bac67d3"]/div/div[2]/ul/li[3]/a/i')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.team_members)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(4204)
                """Check member image"""
                self.is_visible(self.mem_1_img, "Team Member 1 image is not visible.")
                """Check member information"""
                self.check_text_matches_with(self.mem_1_name, self.mem_1_name_text)
                self.check_text_matches_with(self.mem_1_pos, self.mem_1_pos_text)
                """Move cursor to social links"""
                self.cursor.move_to_element(self.get_element(self.mem_1_fb)).\
                    move_to_element(self.get_element(self.mem_1_tw)).\
                    move_to_element(self.get_element(self.mem_1_in)).perform()



