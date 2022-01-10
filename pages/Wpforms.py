from selenium.webdriver import ActionChains

from utils.config import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Wpforms:
    widget = '//*[@id="post-2913"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'WPForms'
    doc_link = '//*[@id="post-2913"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]/div' \
               '/div/div[3]/div/div/a/span/span'
    doc_name = "EA WPFORMS"

    name_label = (By.XPATH, f'//*[@id="wpforms-260985-field_0-container"]/label')
    fname_field = (By.ID, f'wpforms-260985-field_0')
    lname_field = (By.ID, f'wpforms-260985-field_0-last')
    email_label = (By.XPATH, f'//*[@id="wpforms-260985-field_1-container"]/label')
    email_field = (By.ID, f'wpforms-260985-field_1')
    message_label = (By.XPATH, f'//*[@id="wpforms-260985-field_2-container"]/label')
    message_field = (By.ID, f'wpforms-260985-field_2')
    submit_btn = (By.ID, f'wpforms-submit-260985')
    success_message = f'//*[@id="wpforms-confirmation-260985"]'

    name_label_text = "NAME *"
    email_label_text = "EMAIL *"
    message_label_text = "COMMENT OR MESSAGE *"
    success_message_text = "Thanks for contacting us! We will be in touch with you shortly."

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(wpforms)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1040)")
            time.sleep(1)

            assert_that(self.browser.find_element(*self.name_label).text).is_equal_to(self.name_label_text)
            assert_that(self.browser.find_element(*self.email_label).text).is_equal_to(self.email_label_text)
            assert_that(self.browser.find_element(*self.message_label).text).is_equal_to(self.message_label_text)

            self.browser.find_element(*self.fname_field).send_keys("Tester")
            self.browser.find_element(*self.lname_field).send_keys("Bhaai")
            self.browser.find_element(*self.email_field).send_keys("testerbhaai@gmail.com")
            self.browser.find_element(*self.message_field).send_keys("Automation Script is Running...\nHi, Don't reply"
                                                                     " to this message. Have a good day.")

            self.browser.find_element(*self.submit_btn).click()

            WebDriverWait(self.browser, 15).until(
                EC.presence_of_element_located((By.XPATH, self.success_message)))
            WebDriverWait(self.browser, 5000).until(EC.text_to_be_present_in_element((By.XPATH, self.success_message),
                                                                                     self.success_message_text))
