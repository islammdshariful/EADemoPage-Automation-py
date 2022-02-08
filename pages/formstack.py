from selenium.webdriver import Keys

from utils.config import *


class Formstack(Helper):
    widget = '//*[@id="post-259465"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Formstack'
    doc_link = '//*[@id="post-259465"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "FORMSTACK"

    title = (By.XPATH, f'//*[@id="fsSection94545411"]/div[1]/h2')
    des = (By.XPATH, f'//*[@id="fsSection94545411"]/div[1]/div')

    name_label = (By.XPATH, f'//*[@id="label94545412"]')
    fname_field = (By.XPATH, f'//*[@id="field94545412-first"]')
    lname_field = (By.XPATH, f'//*[@id="field94545412-last"]')
    address_label = (By.XPATH, f'//*[@id="label94545413"]')
    address_field = (By.XPATH, f'//*[@id="field94545413-address"]')
    hphone_label = (By.XPATH, f'//*[@id="label94545414"]')
    hphone_field = (By.XPATH, f'//*[@id="field94545414"]')
    wphone_label = (By.XPATH, f'//*[@id="label94545415"]')
    wphone_field = (By.XPATH, f'//*[@id="field94545415"]')
    email_label = (By.XPATH, f'//*[@id="label94545416"]')
    email_field = (By.XPATH, f'//*[@id="field94545416"]')
    comment_label = (By.XPATH, f'//*[@id="label94545417"]')
    comment_field = (By.XPATH, f'//*[@id="field94545417"]')

    fname_bottom_label = (By.XPATH, f'//*[@id="fsCell94545412"]/div[1]/div[1]/label')
    lname_bottom_label = (By.XPATH, f'//*[@id="fsCell94545412"]/div[1]/div[2]/label')
    address_bottom_label = (By.XPATH, f'//*[@id="fsCell94545413"]/div[1]/div/label')

    submit_btn = (By.XPATH, f'//*[@id="fsSubmitButton3799616"]')

    success_msg = f'//*[@id="post-1300"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                  f'/div/div/div/div/div/div/div/div/div'
    success_msg_text = "Thanks for contacting us! We will get in touch with you shortly."

    name_label_text = "Name*"
    fname_bottom_label_text = "First Name"
    lname_bottom_label_text = "Last Name"
    address_bottom_label_text= "Address*"
    address_label_text = "Address Line 1"
    hphone_label_text = "Home Phone*"
    wphone_label_text = "Work Phone"
    email_label_text = "Email*"
    comment_label_text = "Comments"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.formstack)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 905)")
                time.sleep(1)

                assert_that(self.browser.find_element(*self.name_label).text).is_equal_to(self.name_label_text)
                assert_that(self.browser.find_element(*self.fname_bottom_label).text).\
                    is_equal_to(self.fname_bottom_label_text)
                assert_that(self.browser.find_element(*self.lname_bottom_label).text). \
                    is_equal_to(self.lname_bottom_label_text)
                assert_that(self.browser.find_element(*self.fname_bottom_label).text). \
                    is_equal_to(self.fname_bottom_label_text)
                assert_that(self.browser.find_element(*self.address_label).text).\
                    is_equal_to(self.address_bottom_label_text)
                assert_that(self.browser.find_element(*self.hphone_label).text).is_equal_to(self.hphone_label_text)
                assert_that(self.browser.find_element(*self.wphone_label).text).is_equal_to(self.wphone_label_text)
                assert_that(self.browser.find_element(*self.email_label).text).is_equal_to(self.email_label_text)
                assert_that(self.browser.find_element(*self.comment_label).text).is_equal_to(self.comment_label_text)

                self.browser.find_element(*self.fname_field).send_keys("Tester")
                self.browser.find_element(*self.lname_field).send_keys("Bhaai")
                self.browser.find_element(*self.address_field).send_keys("planet Earth, Universe Level 7")
                self.browser.find_element(*self.hphone_field).send_keys("01234567890")
                self.browser.find_element(*self.wphone_field).send_keys("09876543210")
                self.browser.find_element(*self.email_field).send_keys("testerbhaai@gmail.com")
                self.browser.find_element(*self.comment_field).send_keys("Automation Script is Running...\nHi, Don't reply"
                                                                         " to this message. Have a good day.")

                # self.browser.find_element(*self.submit_btn).click()
                #
                # WebDriverWait(self.browser, 15).until(
                #     EC.presence_of_element_located((By.XPATH, self.success_msg)))
                # WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((By.XPATH, self.success_msg),
                #                                                                        self.success_msg_text))