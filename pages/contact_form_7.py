from utils.config import *
from selenium.webdriver.support import expected_conditions as EC


class ContactForm7(Helper):
    widget = '//*[@id="post-1231"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Contact Form 7'
    doc_link = '//*[@id="post-1231"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "CONTACT FORM 7"

    name_label = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[1]/label')
    name_label_text = "YOUR NAME (REQUIRED)"
    email_label = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[2]/label')
    email_label_text = "YOUR EMAIL (REQUIRED)"
    sub_label = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[3]/label')
    sub_label_text = "SUBJECT"
    msg_label = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[4]/label')
    msg_label_text = "YOUR MESSAGE"

    name_field = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[1]/label/span/input')
    email_field = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[2]/label/span/input')
    sub_field = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[3]/label/span/input')
    msg_field = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[4]/label/span/textarea')

    send_btn = (By.XPATH, f'//*[@id="wpcf7-f4-p1231-o2"]/form/p[5]/input')

    success_msg = f'//*[@id="wpcf7-f4-p1231-o2"]/form/div[2]'
    success_msg_text = "Thank you for your message. It has been sent."

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.contact_form_7)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 2374)")
            assert_that(self.browser.find_element(*self.name_label).text).is_equal_to(self.name_label_text)
            assert_that(self.browser.find_element(*self.email_label).text).is_equal_to(self.email_label_text)
            assert_that(self.browser.find_element(*self.sub_label).text).is_equal_to(self.sub_label_text)
            assert_that(self.browser.find_element(*self.msg_label).text).is_equal_to(self.msg_label_text)

            self.browser.find_element(*self.name_field).send_keys("Tester Bhaai")
            self.browser.find_element(*self.email_field).send_keys("testerbhaai@gmail.com")
            self.browser.find_element(*self.sub_field).send_keys("Automation Script is Running...")
            self.browser.find_element(*self.msg_field).send_keys("Hi, Don't reply to this message. Have a good day.")

            self.browser.find_element(*self.send_btn).click()
            time.sleep(1)

            WebDriverWait(self.browser, 15).until(
                EC.presence_of_element_located((By.XPATH, self.success_msg)))
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((By.XPATH, self.success_msg),
                                                                                   self.success_msg_text))
