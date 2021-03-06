from selenium.webdriver import ActionChains, Keys

from utils.config import *


class TeamMember(Helper):
    widget = '//*[@id="post-1022"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Team Member'
    doc_link = '//*[@id="post-1022"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "TEAM MEMBERS"

    mem_1_img = f'//*[@id="eael-team-member-2bac67d3"]/div/div[1]/figure/img'
    mem_1_name = (By.XPATH, f'//*[@id="eael-team-member-2bac67d3"]/div/div[2]/h3')
    mem_1_name_text = "Jemes Barber"
    mem_1_pos = (By.XPATH, f'//*[@id="eael-team-member-2bac67d3"]/div/div[2]/h4')
    mem_1_pos_text = "Beard Trimmer"
    mem_1_fb = (By.XPATH, f'//*[@id="eael-team-member-2bac67d3"]/div/div[2]/ul/li[1]/a/i')
    mem_1_tw = (By.XPATH, f'//*[@id="eael-team-member-2bac67d3"]/div/div[2]/ul/li[2]/a/i')
    mem_1_in = (By.XPATH, f'//*[@id="eael-team-member-2bac67d3"]/div/div[2]/ul/li[3]/a/i')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.team_members)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 4204)")
                time.sleep(1)
                self.check_visibility(self.mem_1_img, "Team Member 1 image is not visible.")

                assert_that(self.browser.find_element(*self.mem_1_name).text).is_equal_to(self.mem_1_name_text)
                assert_that(self.browser.find_element(*self.mem_1_pos).text).is_equal_to(self.mem_1_pos_text)

                fb = self.browser.find_element(*self.mem_1_fb)
                tw = self.browser.find_element(*self.mem_1_tw)
                ln = self.browser.find_element(*self.mem_1_in)

                cursor = ActionChains(self.browser)
                cursor.move_to_element(fb).move_to_element(tw).move_to_element(ln).perform()



