from utils.config import *


class FancyText(Helper):
    widget = '//*[@id="post-14"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Fancy Text'
    doc_link = '//*[@id="post-14"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "FANCY TEXT"

    normal = (By.XPATH, f'//*[@id="post-14"]/div/div/div/div/section[2]/div/div/div/div/div/div[1]/div'
                             f'/div[1]/span[1]')
    normal_text = "You Can Customize"
    fancy_txt = f'//*[@id="eael-fancy-text-27d8d834"]'
    fancy_1_text = "Typography"
    fancy_2_text = "Color"
    fancy_3_text = "Background"
    cursor = f'//*[@id="post-14"]/div/div/div/div/section[2]/div/div/div/div/div/div[1]/div/div[1]/span[3]'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.fancy_text)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 903)")

            assert_that(self.browser.find_element(*self.normal).text).is_equal_to(self.normal_text)
            self.check_visibility(self.cursor, "Blink cursor is not visible.")

            WebDriverWait(self.browser, 5000).until(EC.text_to_be_present_in_element((By.XPATH, self.fancy_txt),
                                                                                     self.fancy_1_text))
            WebDriverWait(self.browser, 5000).until(EC.text_to_be_present_in_element((By.XPATH, self.fancy_txt),
                                                                                     self.fancy_2_text))
            WebDriverWait(self.browser, 5000).until(EC.text_to_be_present_in_element((By.XPATH, self.fancy_txt),
                                                                                     self.fancy_3_text))
