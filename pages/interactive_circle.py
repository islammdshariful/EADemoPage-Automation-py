from selenium.webdriver import ActionChains

from utils.config import *


class InteractiveCircle:
    widget = '//*[@id="post-271398"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Interactive Circle'
    doc_link = '//*[@id="post-271398"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA INTERACTIVE CIRCLE"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(interactive_circle)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 986)")
            time.sleep(1)

            for i in range(1, 7):
                self.browser.find_element(By.XPATH, f'//*[@id="eael-circle-item-' + str(i) + '"]/div[2]').click()
                time.sleep(.5)
                if self.browser.find_element(By.XPATH, f'//*[@id="eael-circle-item-' + str(i) + '"]/div[2]/div/i').\
                        is_displayed():
                    assert_that(display).is_equal_to(1)
                else:
                    assert_that(display).is_equal_to("Icon not displaying")

                assert_that(self.browser.
                            find_element(By.XPATH, f'//*[@id="eael-circle-item-' + str(i) + '"]/div[2]/div/span').
                            text).is_equal_to("Item " + str(i))
                assert_that(self.browser.
                            find_element(By.XPATH, f'//*[@id="eael-interactive-circle-e0f5838"]/div/div/div/div[' +
                                         str(i) + ']/div[2]/div').text).\
                    is_equal_to("Present your content in an attractive Circle layout item " + str(i)
                                + ". You can highlight key information with click or hover effects and style it as "
                                  "per your preference.")
