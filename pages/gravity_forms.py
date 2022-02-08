from selenium.webdriver import Keys

from utils.config import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GravityForms(Helper):
    widget = '//*[@id="post-1802"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Gravity Forms'
    doc_link = '//*[@id="post-1802"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA GRAVITY FORMS"

    fname_field = (By.XPATH, f'//*[@id="input_1_4_3"]')
    lname_field = (By.XPATH, f'//*[@id="input_1_4_6"]')
    email_field = (By.XPATH, f'//*[@id="input_1_3"]')
    message_field = (By.XPATH, f'//*[@id="input_1_5"]')

    submit_btn = (By.XPATH, f'//*[@id="gform_submit_button_1"]')

    success_msg = f'//*[@id="gform_confirmation_message_1"]'
    success_msg_text = "Thanks for contacting us! We will get in touch with you shortly."

    fname_label_text = "First Name"
    lname_label_text = "Last Name"
    email_label_text = "Email"
    message_label_text = "Message"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.gravity_forms)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1002)")
                time.sleep(1)

                assert_that(self.browser.find_element(*self.fname_field).get_attribute("placeholder")).\
                    is_equal_to(self.fname_label_text)
                assert_that(self.browser.find_element(*self.lname_field).get_attribute("placeholder")).\
                    is_equal_to(self.lname_label_text)
                assert_that(self.browser.find_element(*self.email_field).get_attribute("placeholder")).\
                    is_equal_to(self.email_label_text)
                assert_that(self.browser.find_element(*self.message_field).get_attribute("placeholder")).\
                    is_equal_to(self.message_label_text)

                self.browser.find_element(*self.fname_field).send_keys("Tester")
                self.browser.find_element(*self.lname_field).send_keys("Bhaai")
                self.browser.find_element(*self.email_field).send_keys("testerbhaai@gmail.com")
                self.browser.find_element(*self.message_field).send_keys("Automation Script is Running...\nHi, Don't reply"
                                                                         " to this message. Have a good day.")

                self.browser.find_element(*self.submit_btn).click()
                time.sleep(1)
                self.browser.execute_script("window.scrollTo(0, 1002)")
                WebDriverWait(self.browser, 15).until(
                    EC.presence_of_element_located((By.XPATH, self.success_msg)))
                WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((By.XPATH, self.success_msg),
                                                                                       self.success_msg_text))