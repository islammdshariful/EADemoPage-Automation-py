from utils.config import *


class BetterdocsSearchForm(BasePage, Helper):
    widget = '//*[@id="post-255923"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'BetterDocs Search Form'
    doc_link = '//*[@id="post-255923"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "BETTERDOCS SEARCH FORM"

    icon = (By.XPATH, f'//*[@id="post-255923"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                      f'/div/div/div/div/div/div/div/div/form/div/svg[1]')
    input = (By.XPATH, f'//*[@id="post-255923"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                       f'/div/div/div/div/div/div/div/div/form/div/input')
    input_placeholder_name = "Search"

    search_result_title = (By.XPATH, f'//*[@id="post-255923"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                     f'/div/div/div/div/div/div/div/div/form/div[2]/ul/li[1]/a/span[1]')
    search_result_cat = (By.XPATH, f'//*[@id="post-255923"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                   f'/div/div/div/div/div/div/div/div/form/div[2]/ul/li[1]/a/span[2]')

    cross = (By.XPATH, f'//*[@id="post-255923"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div/div'
                       f'/div/div/div/div/div/form/div[1]/svg[3]/path[1]')

    doc_cat = (By.XPATH, f'//*[@id="betterdocs-breadcrumb"]/ul/li[5]/a')
    doc_title = (By.ID, f'betterdocs-entry-title')

    betterdocs_entry_title = (By.ID, 'betterdocs-entry-title')
    betterdocs_entry_heading = (By.XPATH, f'//*[@id="main"]/div/div[1]/h3')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.betterdocs_search_form)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1005)

                assert_that(self.get_element(self.input).get_attribute('placeholder')).\
                    is_equal_to(self.input_placeholder_name)
                self.do_click(self.input)
                self.do_send_keys(self.input, "Interactive Circle")
                title = self.get_element_text(self.search_result_title)
                category = self.get_element_text(self.search_result_cat)
                self.do_click(self.search_result_title)
                self.check_text_matches_with(self.doc_title, title.upper())
                self.check_text_matches_with(self.doc_cat, category)
                self.go_back()
