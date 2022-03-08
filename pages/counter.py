from selenium.webdriver import Keys

from utils.config import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Counter(Helper):
    widget = '//*[@id="post-2948"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Counter'
    doc_link = '//*[@id="post-2948"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "COUNTER"
    icon = f'//*[@id="post-2948"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                      f'/div/div/div[1]/div/div/div/div/div/div/span/span'
    number = f'//*[@id="post-2948"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div/div[1]/div/div' \
             f'/div/div/div/div/div/div[1]/div/div'
    number_text = "2\n,\n5\n4\n0"
    counter_text = (By.XPATH, f'//*[@id="post-2948"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                              f'/div/div/div[1]/div/div/div/div/div/div/div/div[2]')
    counter_text_text = "Projects Completed"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.counter)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 959)")
                time.sleep(1)
                self.check_visibility(self.icon, "Icon is not visible.")

                assert_that(self.browser.find_element(*self.counter_text).text).is_equal_to(self.counter_text_text)

                WebDriverWait(self.browser, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.number), self.number_text))

                assert_that(self.browser.find_element(By.XPATH, self.number).text).is_equal_to(self.number_text)
