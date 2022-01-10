from selenium.webdriver import ActionChains

from utils.config import *


class AdvancedTooltip:
    widget = '//*[@id="post-5622"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'Advanced Tooltip'
    doc_link = '//*[@id="post-5622"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA ADVANCED TOOLTIP"

    card = (By.XPATH, f'//*[@id="eael-section-tooltip-4b0da25c"]/div/div/div')
    tooltip = (By.XPATH, f'//*[@id="tippy-1"]/div')
    tooltip_text = "Save 10% in Basic Plan"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(advanced_tooltip)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1002)")
            time.sleep(1)
            cursor = ActionChains(self.browser)
            c = self.browser.find_element(*self.card)
            cursor.move_to_element(c).perform()
            if self.browser.find_element(*self.tooltip).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to("Tooltip is not visible")

            assert_that(self.browser.find_element(*self.tooltip).text).is_equal_to(self.tooltip_text)
