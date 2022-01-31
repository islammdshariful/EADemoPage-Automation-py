from utils.config import *


class FluentForms(Helper):
    widget = '//*[@id="post-260959"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'Fluent Forms'
    doc_link = '//*[@id="post-260959"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[4]/div/div/a/span/span'
    doc_name = "FLUENT FORMS"

    name_label = (By.XPATH, f'//*[@id="fluentform_1"]/div[1]/div[1]/label')
    name_field = (By.XPATH, f'//*[@id="ff_1_input_text"]')
    email_label = (By.XPATH, f'//*[@id="fluentform_1"]/div[2]/div[1]/label')
    email_field = (By.XPATH, f'//*[@id="ff_1_email"]')
    sub_label = (By.XPATH, f'//*[@id="fluentform_1"]/div[3]/div[1]/label')
    sub_field = (By.XPATH, f'//*[@id="ff_1_input_text_1"]')
    message_label = (By.XPATH, f'//*[@id="fluentform_1"]/div[4]/div[1]/label')
    message_field = (By.XPATH, f'//*[@id="ff_1_description"]')

    send_message_btn = (By.XPATH, f'//*[@id="fluentform_1"]/div[5]/button')

    success_msg = f'//*[@id="fluentform_1_success"]'
    success_msg_text = "Thank you for your message. We will get in touch with you shortly"

    name_label_text = "YOUR NAME (REQUIRED)"
    email_label_text = "YOUR EMAIL (REQUIRED)"
    sub_label_text = "SUBJECT"
    message_label_text = "YOUR MESSAGE"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.fluent_forms)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 997)")
            time.sleep(1)

            assert_that(self.browser.find_element(*self.name_label).text).is_equal_to(self.name_label_text)
            assert_that(self.browser.find_element(*self.email_label).text).is_equal_to(self.email_label_text)
            assert_that(self.browser.find_element(*self.sub_label).text).is_equal_to(self.sub_label_text)
            assert_that(self.browser.find_element(*self.message_label).text).is_equal_to(self.message_label_text)

            self.browser.find_element(*self.name_field).send_keys("Tester Bhaai")
            self.browser.find_element(*self.email_field).send_keys("testerbhaai@gmail.com")
            self.browser.find_element(*self.sub_field).send_keys("Automation Script is Running...")
            self.browser.find_element(*self.message_field).send_keys("Hi, Don't reply to this message. Have a good day.")

            self.browser.find_element(*self.send_message_btn).click()

            WebDriverWait(self.browser, 15).until(
                EC.presence_of_element_located((By.XPATH, self.success_msg)))
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((By.XPATH, self.success_msg),
                                                                                   self.success_msg_text))