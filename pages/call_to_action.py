from selenium.webdriver import ActionChains

from utils.config import *


class CallToAction(Helper):
    widget = '//*[@id="post-1512"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Call To Action'
    doc_link = '//*[@id="post-1512"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "CALL TO ACTION"

    title = (By.XPATH, f'//*[@id="post-1512"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div/div/div/h2')
    title_text = "Essential Addons For Elementor"
    des = (By.XPATH, f'//*[@id="post-1512"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div/div/div/p')
    des_text = "Enhance your Elementor page building experience with 57+ creative\nelements. Add powers to your " \
               "page builder using our easy-to-use elements"

    button = (By.XPATH, f'//*[@id="post-1512"]/div/div/div/div/section[3]/div/div/div[1]/div/div/div/div/div/a')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.call_to_action)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1020)")
            time.sleep(1)

            assert_that(self.browser.find_element(*self.title).text).is_equal_to(self.title_text)
            assert_that(self.browser.find_element(*self.des).text).is_equal_to(self.des_text)
            cursor = ActionChains(self.browser)
            btn = self.browser.find_element(*self.button)
            cursor.move_to_element(btn).perform()
