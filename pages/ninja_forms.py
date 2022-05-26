from selenium.webdriver import Keys

from utils.config import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NinjaForms(Helper):
    widget = '//*[@id="post-1762"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'Ninja Forms'
    doc_link = '//*[@id="post-1762"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]/div' \
               '/div/div[3]/div/div/a/span/span'
    doc_name = "EA NINJA FORMS"

    title = (By.XPATH, f'//*[@id="nf-form-title-1"]/h3')
    des = (By.XPATH, f'//*[@id="nf-form-1-cont"]/div/div[4]/form/div/div[1]/nf-section/div')

    name_label = (By.XPATH, f'//*[@id="nf-label-field-1"]')
    name_field = (By.XPATH, f'//*[@id="nf-field-1"]')
    email_label = (By.XPATH, f'//*[@id="nf-label-field-2"]')
    email_field = (By.XPATH, f'//*[@id="nf-field-2"]')
    message_label = (By.XPATH, f'//*[@id="nf-label-field-3"]')
    message_field = (By.XPATH, f'//*[@id="nf-field-3"]')
    submit_btn = (By.XPATH, f'//*[@id="nf-field-4"]')

    success_message = f'//*[@id="nf-form-1-cont"]/div/div[1]'

    title_text = "Contact Me"
    des_text = "Fields marked with an * are required"

    name_label_text = "NAME *"
    email_label_text = "EMAIL *"
    message_label_text = "MESSAGE *"
    success_message_text = "Form submitted successfully.\nA confirmation email was sent to testerbhaai@gmail.com."

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.ninja_forms)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1177)")
                time.sleep(1)

                # assert_that(self.browser.find_element(*self.title).text).is_equal_to(self.title_text)
                assert_that(self.browser.find_element(*self.des).text).is_equal_to(self.des_text)
                assert_that(self.browser.find_element(*self.name_label).text).is_equal_to(self.name_label_text)
                assert_that(self.browser.find_element(*self.email_label).text).is_equal_to(self.email_label_text)
                assert_that(self.browser.find_element(*self.message_label).text).is_equal_to(self.message_label_text)

                self.browser.find_element(*self.name_field).send_keys("Tester Bhaai")
                self.browser.find_element(*self.email_field).send_keys("testerbhaai@gmail.com")
                self.browser.find_element(*self.message_field).send_keys("Automation Script is Running...\nHi, Don't reply"
                                                                         " to this message. Have a good day.")

                self.browser.find_element(*self.submit_btn).click()

                WebDriverWait(self.browser, 15).until(
                    EC.presence_of_element_located((By.XPATH, self.success_message)))
                WebDriverWait(self.browser, 5000).until(EC.text_to_be_present_in_element((By.XPATH, self.success_message),
                                                                                         self.success_message_text))