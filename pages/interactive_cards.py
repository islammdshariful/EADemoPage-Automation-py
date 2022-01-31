from selenium.webdriver import ActionChains

from utils.config import *


class InteractiveCards(Helper):
    widget = '//*[@id="post-1716"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Interactive Cards'
    doc_link = '//*[@id="post-1716"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "INTERACTIVE CARDS"

    promo = (By.XPATH, f'//*[@id="interactive-card-368e06c7"]/div[1]/div')
    close_btn = (By.XPATH, f'//*[@id="interactive-card-368e06c7"]/div[2]/span')
    title = (By.XPATH, f'//*[@id="interactive-card-368e06c7"]/div[2]/div/div[1]/div/h2')
    title_text = "Amazing Colorful City"
    des = (By.XPATH, f'//*[@id="interactive-card-368e06c7"]/div[2]/div/div[1]/div/p')
    des_text = "We have only one earth to dwell, don’t destroy the nature and\n" \
               "don’t make it hell. We have only one earth to dwell, don’t destroy."
    button = (By.XPATH, f'//*[@id="interactive-card-368e06c7"]/div[2]/div/div[1]/div/a')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.interactive_cards)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1031)")
            time.sleep(1)

            self.browser.find_element(*self.promo).click()
            time.sleep(1.5)
            assert_that(self.browser.find_element(*self.title).text).is_equal_to(self.title_text)
            assert_that(self.browser.find_element(*self.des).text).is_equal_to(self.des_text)
            cursor = ActionChains(self.browser)
            btn = self.browser.find_element(*self.button)
            cursor.move_to_element(btn).perform()
            time.sleep(1)
            self.browser.find_element(*self.close_btn).click()
