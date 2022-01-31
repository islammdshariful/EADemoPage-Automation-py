from utils.config import *


class AdvancedSearch(Helper):
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
    search_result = f'//*[@id="eael-advanced-search-widget-4ccceaa9"]/div/div[3]/a[1]/div[2]/h4'
    search_description = f'//*[@id="eael-advanced-search-widget-4ccceaa9"]/div/div[3]/a[1]/div[2]/p'

    # Article
    article_title = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                               f'/div/div/div/div/div/div[1]/div/h1')
    article_date = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                              f'/div/div/div/div/div/div[2]/div/ul/li[1]/a/span[2]')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.advanced_search)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1481)")
            time.sleep(1)

            assert_that(self.browser.find_element(*self.input_field).get_attribute('placeholder')).\
                is_equal_to(self.placeholder_text)
            self.browser.find_element(*self.input_field).click()
            self.browser.find_element(*self.input_field).send_keys(self.search_keyword)
            time.sleep(1)
            WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.XPATH, self.search_result))
            )
            self.browser.find_element(*self.clear_btn).click()
            time.sleep(1)
            self.browser.find_element(*self.input_field).click()
            self.browser.find_element(*self.input_field).send_keys(self.search_keyword)
            self.browser.find_element(*self.search_btn).click()
            time.sleep(1)
            self.browser.find_element(*self.load_more).click()
            time.sleep(1)
            self.check_visibility(self.search_description, "Search description not visible.")
            title = self.browser.find_element(*self.search_title).text
            self.browser.find_element(*self.search_title).click()
            assert_that(self.browser.find_element(*self.article_title).text).is_equal_to(title)
            self.browser.back()


