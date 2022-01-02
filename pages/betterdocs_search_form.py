from selenium.webdriver import ActionChains

from utils.config import *


class BetterdocsSearchForm:
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

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(betterdocs_search_form)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1005)")

            ph = self.browser.find_element(*self.input)
            assert_that(ph.get_attribute('placeholder')).is_equal_to(self.input_placeholder_name)
            time.sleep(.5)
            self.browser.find_element(*self.input).click()
            self.browser.find_element(*self.input).send_keys("Interactive Circle")
            time.sleep(1.5)
            title = self.browser.find_element(*self.search_result_title).text
            cat = self.browser.find_element(*self.search_result_cat).text
            self.browser.find_element(*self.search_result_title).click()
            assert_that(self.browser.find_element(*self.doc_title).text).is_equal_to(title.upper())
            assert_that(self.browser.find_element(*self.doc_cat).text).is_equal_to(cat)
            self.browser.back()
