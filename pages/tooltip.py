import time

from selenium.webdriver import ActionChains

from utils.config import *


class ToolTip(Helper):
    widget = '//*[@id="post-2455"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Tooltip'
    doc_link = '//*[@id="post-2455"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a'
    doc_name = "TOOLTIP"

    tooltip_1_img = f'//*[@id="post-2455"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                               f'/div/div/div[1]/div/div/div/div/div/span[1]/img'
    tooltip_1 = (By.XPATH, f'//*[@id="post-2455"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                f'/div/div/div[1]/div/div/div/div/div/span[2]')
    tooltip_1_text = "Search Engine Optimization"

    tooltip_2_img = f'//*[@id="post-2455"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                               f'/div/div/div[2]/div/div/div/div/div/span[1]/img'
    tooltip_2 = (By.XPATH, f'//*[@id="post-2455"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                           f'/div/div/div[2]/div/div/div/div/div/span[2]')
    tooltip_2_text = "Search Engine Optimization"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.tooltip)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1010)")
            time.sleep(1)

            cursor_1 = ActionChains(self.browser)
            cursor_2 = ActionChains(self.browser)
            self.check_visibility(self.tooltip_1_img, "Tool Tip 1 image is not visible.")
            self.check_visibility(self.tooltip_2_img, "Tool Tip 2 image is not visible.")

            tip_1 = self.browser.find_element(*self.tooltip_1_img)
            tip_2 = self.browser.find_element(*self.tooltip_2_img)
            cursor_1.move_to_element(tip_1).perform()
            assert_that(self.browser.find_element(*self.tooltip_1).text).is_equal_to(self.tooltip_1_text)
            cursor_2.move_to_element(tip_2).perform()
            assert_that(self.browser.find_element(*self.tooltip_2).text).is_equal_to(self.tooltip_2_text)


