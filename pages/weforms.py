from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from utils.config import *
from selenium.webdriver.support import expected_conditions as EC

class Weforms:
    widget = '//*[@id="post-1300"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'weForms'
    doc_link = '//*[@id="post-1300"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "WEFORMS"

    name_label = (By.XPATH, f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                            f'/div/div/div/div/div/div/div/div/form/ul/li[1]/div[1]/label')
    fname_field = (By.XPATH, f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                             f'/div/div/div/div/div/div/div/div/form/ul/li[1]/div[2]/div/div[1]/input')
    lname_field = (By.XPATH, f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                             f'/div/div/div/div/div/div/div/div/form/ul/li[1]/div[2]/div/div[2]/input')
    email_label = (By.XPATH, f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                             f'/div/div/div/div/div/div/div/div/form/ul/li[2]/div[1]/label')
    email_field = (By.XPATH, f'//*[@id="email_1302"]')
    message_label = (By.XPATH, f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                               f'/div/div/div/div/div/div/div/div/form/ul/li[3]/div[1]/label')
    message_field = (By.XPATH, f'//*[@id="message_1302"]')

    send_message_btn = (By.XPATH, f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                                  f'/div/div/div/div/div/div/div/div/form/ul/li[4]/input[7]')

    success_msg = f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                  f'/div/div/div/div/div/div/div/div/div'
    success_msg_text = "Thanks for contacting us! We will get in touch with you shortly."

    name_label_text = "Name *"
    email_label_text = "Email *"
    message_label_text = "Message *"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(weforms)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 984)")
            time.sleep(1)

            assert_that(self.browser.find_element(*self.name_label).text).is_equal_to(self.name_label_text)
            assert_that(self.browser.find_element(*self.email_label).text).is_equal_to(self.email_label_text)
            assert_that(self.browser.find_element(*self.message_label).text).is_equal_to(self.message_label_text)

            self.browser.find_element(*self.fname_field).send_keys("Tester")
            self.browser.find_element(*self.lname_field).send_keys("Bhaai")
            self.browser.find_element(*self.email_field).send_keys("testerbhaai@gmail.com")
            self.browser.find_element(*self.message_field).send_keys("Automation Script is Running...\nHi, Don't reply"
                                                                     " to this message. Have a good day.")

            self.browser.find_element(*self.send_message_btn).click()

            WebDriverWait(self.browser, 15).until(
                EC.presence_of_element_located((By.XPATH, self.success_msg)))
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((By.XPATH, self.success_msg),
                                                                                   self.success_msg_text))