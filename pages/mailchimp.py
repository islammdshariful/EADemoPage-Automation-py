from selenium.webdriver import ActionChains

from utils.config import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Mailchimp:
    widget = '//*[@id="post-2603"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]/div' \
             '/div/div[1]/div/h2'
    widget_name = 'MailChimp'
    doc_link = '//*[@id="post-2603"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]/div' \
               '/div/div[3]/div/div/a/span/span'
    doc_name = "MAILCHIMP"

    email_field = (By.XPATH, f'//*[@id="eael-mailchimp-form-50de1e0a"]/div[1]/div[1]/input')
    fname_field = (By.XPATH, f'//*[@id="eael-mailchimp-form-50de1e0a"]/div[1]/div[2]/input')
    lname_field = (By.XPATH, f'//*[@id="eael-mailchimp-form-50de1e0a"]/div[1]/div[3]/input')
    subs_btn = (By.XPATH, f'//*[@id="eael-subscribe-50de1e0a"]/span')

    success_message = f'//*[@id="eael-mailchimp-form-50de1e0a"]/div[2]/p'
    success_message_text = "You have subscribed successfully!"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(mailchimp)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1030)")
            time.sleep(1)

            self.browser.find_element(*self.email_field).send_keys("testerbhaai@gmail.com")
            self.browser.find_element(*self.fname_field).send_keys("Tester")
            self.browser.find_element(*self.lname_field).send_keys("Bhaai")

            self.browser.find_element(*self.subs_btn).click()

            WebDriverWait(self.browser, 15).until(
                EC.presence_of_element_located((By.XPATH, self.success_message)))
            WebDriverWait(self.browser, 5000).until(EC.text_to_be_present_in_element((By.XPATH, self.success_message),
                                                                                     self.success_message_text))