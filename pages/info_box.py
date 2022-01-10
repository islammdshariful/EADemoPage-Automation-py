from selenium.webdriver import ActionChains

from utils.config import *


class InfoBox:
    widget = '//*[@id="post-1509"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Info Box'
    doc_link = '//*[@id="post-1509"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "INFO BOX"

    info_box_icon_1 = (By.XPATH, f'//*[@id="post-1509"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                            f'/div/div/div[1]/div/div/div/div/div/div[1]/div')
    info_box_1 = (By.XPATH, f'//*[@id="post-1509"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                            f'/div/div/div[1]/div/div/div/div/div/div[2]/h4')
    info_box_1_text = "Development"
    info_box_icon_2 = (By.XPATH, f'//*[@id="post-1509"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                 f'/div/div/div[2]/div/div/div/div/div/div[1]/div')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(info_box)

    def testcase(self):

        with soft_assertions():
            with soft_assertions():
                c = CheckText(self.browser)

                with soft_assertions():
                    c.check_widget_name(self.widget, self.widget_name)
                    if check_doc:
                        c.check_doc(self.doc_link, self.doc_name)

                self.browser.execute_script("window.scrollTo(0, 1028)")
                time.sleep(1)

                box_1 = self.browser.find_element(*self.info_box_icon_1)
                box_2 = self.browser.find_element(*self.info_box_icon_2)
                cursor = ActionChains(self.browser)
                cursor.move_to_element(box_1).perform()

                assert_that(self.browser.find_element(*self.info_box_1).text).is_equal_to(self.info_box_1_text)
                cursor.move_to_element(box_2).perform()

