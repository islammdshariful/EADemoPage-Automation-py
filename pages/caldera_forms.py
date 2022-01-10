from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import *


class CalderaForms:
    widget = '//*[@id="post-1829"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'Caldera Forms'
    doc_link = '//*[@id="post-1829"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA CALDERA FORMS"

    fname_label = (By.XPATH, f'//*[@id="fld_8768091Label"]')
    fname_field = (By.XPATH, f'//*[@id="fld_8768091_1"]')
    lname_label = (By.XPATH, f'//*[@id="fld_9970286Label"]')
    lname_field = (By.XPATH, f'//*[@id="fld_9970286_1"]')
    email_label = (By.XPATH, f'//*[@id="fld_6009157Label"]')
    email_field = (By.XPATH, f'//*[@id="fld_6009157_1"]')
    comment_label = (By.XPATH, f'//*[@id="fld_7683514Label"]')
    comment_field = (By.XPATH, f'//*[@id="fld_7683514_1"]')

    send_message_btn = (By.XPATH, f'//*[@id="fld_7908577_1"]')

    success_msg = f'//*[@id="caldera_notices_1"]/div'
    success_msg_text = "Form has been successfully submitted. Thank you."

    fname_label_text = "First Name *"
    lname_label_text = "Last Name *"
    email_label_text = "Email Address *"
    comment_label_text = "Comments / Questions *"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(caldera_forms)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1130)")
            time.sleep(1)

            assert_that(self.browser.find_element(*self.fname_label).text).is_equal_to(self.fname_label_text)
            assert_that(self.browser.find_element(*self.lname_label).text).is_equal_to(self.lname_label_text)
            assert_that(self.browser.find_element(*self.email_label).text).is_equal_to(self.email_label_text)
            assert_that(self.browser.find_element(*self.comment_label).text).is_equal_to(self.comment_label_text)

            self.browser.find_element(*self.fname_field).send_keys("Tester")
            self.browser.find_element(*self.lname_field).send_keys("Bhaai")
            self.browser.find_element(*self.email_field).send_keys("testerbhaai@gmail.com")
            self.browser.find_element(*self.comment_field).send_keys("Automation Script is Running...\nHi, Don't reply"
                                                                     " to this message. Have a good day.")

            self.browser.find_element(*self.send_message_btn).click()

            WebDriverWait(self.browser, 15).until(
                EC.presence_of_element_located((By.XPATH, self.success_msg)))
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((By.XPATH, self.success_msg),
                                                                                   self.success_msg_text))
