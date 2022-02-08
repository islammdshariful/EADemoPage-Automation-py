import time

from selenium.webdriver import ActionChains, Keys

from utils.config import *


class ProtectedContent(Helper):
    widget = '//*[@id="post-3712"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Protected Content'
    doc_link = '//*[@id="post-3712"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA PROTECTED CONTENT"

    message = (By.XPATH, f'//*[@id="post-3712"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                         f'/div/div/div[2]/div/div/div/div/div[1]/div/p')
    message_text = "This section is password protected. So use 1234 to access the content."
    password = (By.XPATH, f'//*[@id="eael_protected_content_form_3d01145b"]/input[1]')
    button = (By.XPATH, f'//*[@id="eael_protected_content_form_3d01145b"]/input[3]')
    img = f'//*[@id="eael-protected-content-render-3d01145b"]/div/div/div/section/div/div/div/div/div/div[1]' \
          f'/div/div/img'
    title = (By.XPATH, f'//*[@id="eael-protected-content-render-3d01145b"]/div/div/div/section'
                       f'/div/div/div/div/div/div[2]/div/h2')
    title_text = "Ya! You Have Typed The Right Password"
    des = (By.XPATH, f'//*[@id="eael-protected-content-render-3d01145b"]/div/div/div/section'
                     f'/div/div/div/div/div/div[3]/div/div')
    des_text = "Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or " \
               "web designs. The passage is attributed to an unknown typesetter in the 15th century who is thought" \
               " to have scrambled parts of Cicero’s De Finibus Bonorum et Malorum for use in a type specimen book."

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.protected_content)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1007)")
                time.sleep(1)
                self.wait_for_bar_to_come()

                assert_that(self.browser.find_element(*self.message).text).is_equal_to(self.message_text)

                self.browser.find_element(*self.password).click()
                self.browser.find_element(*self.password).clear()
                self.browser.find_element(*self.password).send_keys("1234")
                self.browser.find_element(*self.button).click()

                time.sleep(2)
                self.check_visibility(self.img, "Image is not visible.")

                assert_that(self.browser.find_element(*self.title).text).is_equal_to(self.title_text)
                assert_that(self.browser.find_element(*self.des).text).is_equal_to(self.des_text)


