from selenium.webdriver import ActionChains

from utils.config import *


class Counter:
    widget = '//*[@id="post-2948"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Counter'
    doc_link = '//*[@id="post-2948"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "COUNTER"
    icon = (By.XPATH, f'//*[@id="post-2948"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                      f'/div/div/div[1]/div/div/div/div/div/div/span/span')
    number = (By.XPATH, f'//*[@id="post-2948"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                        f'/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/div')
    number_text = "2\n,\n5\n4\n0"
    counter_text = (By.XPATH, f'//*[@id="post-2948"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                              f'/div/div/div[1]/div/div/div/div/div/div/div/div[2]')
    counter_text_text = "Projects Completed"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(counter)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 959)")
            if self.browser.find_element(*self.icon).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to("Icon is visible")

            assert_that(self.browser.find_element(*self.counter_text).text).is_equal_to(self.counter_text_text)
            time.sleep(2)
            assert_that(self.browser.find_element(*self.number).text).is_equal_to(self.number_text)