from pages.basepage import BasePage
from utils.config import *


class AdvancedSearch(BasePage, Helper):
    widget = '//*[@id="post-271377"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Advanced Search'
    doc_link = '//*[@id="post-271377"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA ADVANCED SEARCH"

    placeholder_text = "Enter Search Keyword"
    search_keyword = "Essential addons for elementor lite"
    icon = (By.XPATH, f'//*[@id="eael-advanced-search-widget-4ccceaa9"]/form/div/span[3]')
    search_btn = (By.XPATH, f'//*[@id="eael-advanced-search-widget-4ccceaa9"]/form/button')
    input_field = (By.XPATH, f'//*[@id="eael-advanced-search-widget-4ccceaa9"]/form/div/input')
    clear_btn = (By.XPATH, f'//*[@id="eael-advanced-search-widget-4ccceaa9"]/form/div/span[2]')
    load_more = (By.XPATH, f'//*[@id="eael-advanced-search-widget-4ccceaa9"]/div/div[5]/a')
    search_title = (By.XPATH, f'//*[@id="eael-advanced-search-widget-4ccceaa9"]/div/div[3]/a[1]/div[2]/h4')
    search_result = (By.XPATH, f'//*[@id="eael-advanced-search-widget-4ccceaa9"]/div/div[3]/a[1]/div[2]/h4')
    search_description = (By.XPATH, f'//*[@id="eael-advanced-search-widget-4ccceaa9"]/div/div[3]/a[1]/div[2]/p')

    # Article
    article_title = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                               f'/div/div/div/div/div/div[1]/div/h1')
    article_date = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                              f'/div/div/div/div/div/div[2]/div/ul/li[1]/a/span[2]')

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.advanced_search)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1481)
                assert_that(self.get_element(self.input_field).get_attribute("placeholder")).\
                    is_equal_to(self.placeholder_text)
                """Search a query"""
                self.do_click(self.input_field)
                self.do_send_keys(self.input_field, self.search_keyword)
                if self.check_element_present(self.search_result):
                    """Clear the field"""
                    self.do_click(self.clear_btn)
                """Search a query and check it's result"""
                self.do_click(self.input_field)
                self.do_send_keys(self.input_field, self.search_keyword)
                self.do_click(self.search_btn)
                self.do_click(self.load_more)
                self.is_visible(self.search_description, "Search description not visible.")
                title = self.get_element_text(self.search_title)
                self.do_click(self.search_title)
                self.check_text_matches_with(self.article_title, title)
                self.go_back()


