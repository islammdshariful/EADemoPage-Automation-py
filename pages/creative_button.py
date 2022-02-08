from selenium.webdriver import ActionChains, Keys

from utils.config import *


class CreativeButton(Helper):
    widget = '//*[@id="post-21"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = "Creative Buttons"
    doc_link = '//*[@id="post-21"]/div/div/div/div/section[1]/div[3]/div/div[2]' \
               '/div/div/section/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "CREATIVE BUTTONS"

    FIRST_BUTTON = (By.XPATH, f'//*[@id="post-21"]/div/div/div/div/section[2]/div/div/'
                              f'div/div/div/section[2]/div/div/div[1]/div/div/div/div/div/a/div/span[2]')
    FIRST_BUTTON_TEXT = "EXPLORE THE GLOBE"
    LAST_BUTTON = (By.XPATH, f'//*[@id="post-21"]/div/div/div/div/section[2]/div/div/div/'
                             f'div/div/section[6]/div/div/div[4]/div/div/div/div/div/a/div/span[2]')
    LAST_BUTTON_TEXT = "EXPLORE MORE"
    LAST_BUTTON_ATTRIBUTE = (By.XPATH, f'//*[@id="post-21"]/div/div/div/div/section[2]/div/div/div/div'
                                       f'/div/section[6]/div/div/div[4]/div/div/div/div/div/a')
    LAST_BUTTON_ATTRIBUTE_TEXT = "Go!"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.create_button)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1023)")
                time.sleep(1)

                cursor = ActionChains(self.browser)

                first_button_ele = self.browser.find_element(*self.FIRST_BUTTON)
                last_button_ele = self.browser.find_element(*self.LAST_BUTTON)
                last_button_attribute = self.browser.find_element(*self.LAST_BUTTON_ATTRIBUTE).get_attribute("data-text")

                cursor.move_to_element(first_button_ele).perform()
                assert_that(first_button_ele.text).is_equal_to(self.FIRST_BUTTON_TEXT)

                cursor.move_to_element(last_button_ele).perform()
                assert_that(last_button_ele.text).is_equal_to(self.LAST_BUTTON_TEXT)
                assert_that(last_button_attribute).is_equal_to(self.LAST_BUTTON_ATTRIBUTE_TEXT)


