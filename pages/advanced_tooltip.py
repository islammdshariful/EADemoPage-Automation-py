from selenium.webdriver import ActionChains

from utils.config import *


class AdvancedTooltip(Helper):
    widget = '//*[@id="post-5622"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'Advanced Tooltip'
    doc_link = '//*[@id="post-5622"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA ADVANCED TOOLTIP"

    card = (By.XPATH, f'//*[@id="eael-section-tooltip-4b0da25c"]/div/div/div')
    tooltip = f'//*[@id="tippy-1"]/div'
    tooltip_text = "Save 10% in Basic Plan"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.advanced_tooltip)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1002)")
            time.sleep(1)
            cursor = ActionChains(self.browser)
            c = self.browser.find_element(*self.card)
            cursor.move_to_element(c).perform()
            self.check_visibility(self.tooltip, "Tooltip is not visible.")

            assert_that(self.browser.find_element(By.XPATH, self.tooltip).text).is_equal_to(self.tooltip_text)
