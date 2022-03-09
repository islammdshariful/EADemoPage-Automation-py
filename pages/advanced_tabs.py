import time

from selenium.webdriver import ActionChains, Keys

from utils.config import *


class AdvancedTabs(Helper):
    widget = '//*[@id="post-2436"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Advanced Tabs'
    doc_link = '//*[@id="post-2436"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "ADVANCED TABS"

    tab_1_icon = (By.XPATH, f"//div[@id='eael-advance-tabs-73ca6f31']//li[@id='philosophy']//*[name()='svg']")
    tab_1 = (By.XPATH, f"//ul[@class='eael-tab-top-icon']//span[@class='eael-tab-title title-after-icon']"
                       f"[normalize-space()='PHILOSOPHY']")
    tab_1_text = "PHILOSOPHY"
    tab_1_des = (By.XPATH, f"//div[@id='eael-advance-tabs-6012d12c']//div[@id='philosophy-tab']")
    tab_des_text = "Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus. Praesent elementum feugiat dignissim. Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus. Praesent elementum feugiat dignissim. Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam."
    tab_nested_ver_des_text = "Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus. Praesent elementum feugiat dignissim. Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus. Praesent elementum feugiat dignissim. Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus. Praesent elementum feugiat dignissim."
    tab_nested_hor_des_text = "Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus. Praesent elementum feugiat dignissim. Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus. Praesent elementum feugiat dignissim. Nunc placerat mi id nisi interdum mollis. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. Praesent pharetra, justo ut scelerisque mattis, leo quam aliquet diam, congue laoreet elit metus eget diam. Proin ac metus diam. In quis scelerisque velit. Proin pellentesque neque ut scelerisque dapibus."

    tab_2_icon = (By.XPATH, f"//li[@id='mission']//*[name()='svg']")
    tab_2 = (By.XPATH, f"//span[normalize-space()='MISSION']")
    tab_2_text = "MISSION"
    tab_2_1 = (By.XPATH, f"//div[@id='eael-advance-tabs-798ca354']//span[@class='eael-tab-title title-after-icon']"
                         f"[normalize-space()='Easy To Use']")
    tab_2_1_text = "Easy To Use"
    tab_2_1_des = (By.XPATH, f"//div[@id='eael-advance-tabs-798ca354']//div[@id='easy-to-use-tab']")
    tab_2_2 = (By.XPATH, f"//div[@id='eael-advance-tabs-798ca354']//span[@class='eael-tab-title title-after-icon']"
                         f"[normalize-space()='Mission & Vision']")
    tab_2_2_text = "Mission & Vision"
    tab_2_2_des = (By.XPATH, f"//div[@id='eael-advance-tabs-798ca354']//div[@id='mission-vision-tab']")
    tab_2_3 = (By.XPATH, f"//div[@id='eael-advance-tabs-798ca354']//span[@class='eael-tab-title title-after-icon']"
                         f"[normalize-space()='Goals']")
    tab_2_3_text = "Goals"
    tab_2_3_des = (By.XPATH, f"//div[@id='eael-advance-tabs-798ca354']//div[@id='goals-tab']")
    tab_2_4 = (By.XPATH, f"//div[@id='eael-advance-tabs-798ca354']//span[@class='eael-tab-title title-after-icon']"
                         f"[normalize-space()='Privacy Policy']")
    tab_2_4_text = "Privacy Policy"
    tab_2_4_des = (By.XPATH, f"//div[@id='eael-advance-tabs-798ca354']//div[@id='privacy-policy-tab']")

    tab_3_icon = (By.XPATH, f"//li[@id='vision']//*[name()='svg']")
    tab_3 = (By.XPATH, f"//span[normalize-space()='VISION']")
    tab_3_text = "VISION"
    tab_3_1 = (By.XPATH, f"//ul[@class='eael-tab-top-icon']//span[@class='eael-tab-title title-after-icon']"
                         f"[normalize-space()='Easy To Use']")
    tab_3_1_text = "Easy To Use"
    tab_3_1_des = (By.XPATH, f"//div[@id='eael-advance-tabs-3a353666']//div[@id='easy-to-use-tab']")
    tab_3_2 = (By.XPATH, f"//ul[@class='eael-tab-top-icon']//span[@class='eael-tab-title title-after-icon']"
                         f"[normalize-space()='Mission & Vision']")
    tab_3_2_text = "Mission & Vision"
    tab_3_2_des = (By.XPATH, f"//div[@id='eael-advance-tabs-3a353666']//div[@id='mission-vision-tab']")
    tab_3_3 = (By.XPATH, f"//ul[@class='eael-tab-top-icon']//span[@class='eael-tab-title title-after-icon']"
                         f"[normalize-space()='Goals']")
    tab_3_3_text = "Goals"
    tab_3_3_des = (By.XPATH, f"//div[@id='eael-advance-tabs-3a353666']//div[@id='goals-tab']")
    tab_3_4 = (By.XPATH, f"//ul[@class='eael-tab-top-icon']//span[@class='eael-tab-title title-after-icon']"
                         f"[normalize-space()='Privacy Policy']")
    tab_3_4_text = "Privacy Policy"
    tab_3_4_des = (By.XPATH, f"//div[@id='eael-advance-tabs-3a353666']//div[@id='privacy-policy-tab']")

    tab_4_icon = (By.XPATH, f"//body/div[@class='eael-offcanvas-container eael-offcanvas-container-b1d375a']/"
                            f"div[@id='page']/div[@id='content']/div[@class='flexia-wrapper flexia-blank-container']"
                            f"/div[@id='primary']/main[@id='main']/article[@id='post-2436']/div[@class='entry-content']"
                            f"/div[@class='elementor elementor-2436']/div[@class='elementor-inner']"
                            f"/div[@class='elementor-section-wrap']/section[@class='elementor-section "
                            f"elementor-top-section elementor-element elementor-element-6e7ab82b elementor-"
                            f"section-content-middle elementor-reverse-mobile elementor-section-boxed elementor-"
                            f"section-height-default elementor-section-height-default']/div[@class='elementor-"
                            f"container elementor-column-gap-default']/div[@class='elementor-row']/div[@class='"
                            f"elementor-column elementor-col-100 elementor-top-column elementor-element elementor-"
                            f"element-5bc509eb']/div[@class='elementor-column-wrap elementor-element-populated']/"
                            f"div[@class='elementor-widget-wrap']/div[@class='elementor-element elementor-element-"
                            f"6012d12c elementor-widget elementor-widget-eael-adv-tabs']/div[@class='elementor-widget"
                            f"-container']/div[@id='eael-advance-tabs-6012d12c']/div[@class='eael-tabs-nav']/"
                            f"ul[@class='eael-tab-top-icon']/li[4]//*[name()='svg']")
    tab_4 = (By.XPATH, f"//ul[@class='eael-tab-top-icon']//span[@class='eael-tab-title title-after-icon']"
                       f"[normalize-space()='GOALS']")
    tab_4_text = "GOALS"
    tab_4_des = (By.XPATH, f"//body/div[@class='eael-offcanvas-container eael-offcanvas-container-b1d375a']/div[@id='"
                           f"page']/div[@id='content']/div[@class='flexia-wrapper flexia-blank-container']/div[@id='"
                           f"primary']/main[@id='main']/article[@id='post-2436']/div[@class='entry-content']/div"
                           f"[@class='elementor elementor-2436']/div[@class='elementor-inner']/div[@class='"
                           f"elementor-section-wrap']/section[@class='elementor-section elementor-top-section "
                           f"elementor-element elementor-element-6e7ab82b elementor-section-content-middle "
                           f"elementor-reverse-mobile elementor-section-boxed elementor-section-height-default "
                           f"elementor-section-height-default']/div[@class='elementor-container elementor-column-"
                           f"gap-default']/div[@class='elementor-row']/div[@class='elementor-column elementor-col-"
                           f"100 elementor-top-column elementor-element elementor-element-5bc509eb']/div[@class="
                           f"'elementor-column-wrap elementor-element-populated']/div[@class='elementor-widget-wrap']"
                           f"/div[@class='elementor-element elementor-element-6012d12c elementor-widget elementor-"
                           f"widget-eael-adv-tabs']/div[@class='elementor-widget-container']/div[@id='eael-advance-"
                           f"tabs-6012d12c']/div[@class='eael-tabs-content']/div[4]")

    tab_5_icon = (By.XPATH, f"//li[@id='privacy']//*[name()='svg']")
    tab_5 = (By.XPATH, f"//span[normalize-space()='PRIVACY']")
    tab_5_text = "PRIVACY"
    tab_5_des = (By.XPATH, f"//div[@id='privacy-tab']")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.advanced_tabs)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 2378)")
                time.sleep(1)
                # self.wait_for_bar_to_come()

                assert_that(self.browser.find_element(*self.tab_1).text).is_equal_to(self.tab_1_text)
                self.browser.find_element(*self.tab_1).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.tab_1_des).text).is_equal_to(self.tab_des_text)

                assert_that(self.browser.find_element(*self.tab_2).text).is_equal_to(self.tab_2_text)
                time.sleep(.5)
                self.browser.find_element(*self.tab_2).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.tab_2_1).text).is_equal_to(self.tab_2_1_text)
                self.browser.find_element(*self.tab_2_1).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.tab_2_1_des).text).is_equal_to(self.tab_nested_ver_des_text)

                assert_that(self.browser.find_element(*self.tab_2_2).text).is_equal_to(self.tab_2_2_text)
                self.browser.find_element(*self.tab_2_2).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.tab_2_2_des).text).is_equal_to(self.tab_nested_ver_des_text)

                assert_that(self.browser.find_element(*self.tab_2_3).text).is_equal_to(self.tab_2_3_text)
                self.browser.find_element(*self.tab_2_3).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.tab_2_3_des).text).is_equal_to(self.tab_nested_ver_des_text)

                assert_that(self.browser.find_element(*self.tab_2_4).text).is_equal_to(self.tab_2_4_text)
                self.browser.find_element(*self.tab_2_4).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.tab_2_4_des).text).is_equal_to(self.tab_nested_ver_des_text)

                assert_that(self.browser.find_element(*self.tab_3).text).is_equal_to(self.tab_3_text)
                self.browser.find_element(*self.tab_3).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.tab_3_1).text).is_equal_to(self.tab_2_1_text)
                self.browser.find_element(*self.tab_3_1).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.tab_3_1_des).text).is_equal_to(self.tab_nested_hor_des_text)

                assert_that(self.browser.find_element(*self.tab_3_2).text).is_equal_to(self.tab_3_2_text)
                self.browser.find_element(*self.tab_3_2).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.tab_3_2_des).text).is_equal_to(self.tab_nested_hor_des_text)

                assert_that(self.browser.find_element(*self.tab_3_3).text).is_equal_to(self.tab_3_3_text)
                self.browser.find_element(*self.tab_3_3).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.tab_3_3_des).text).is_equal_to(self.tab_nested_hor_des_text)

                assert_that(self.browser.find_element(*self.tab_3_4).text).is_equal_to(self.tab_3_4_text)
                self.browser.find_element(*self.tab_3_4).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.tab_3_4_des).text).is_equal_to(self.tab_nested_hor_des_text)

                assert_that(self.browser.find_element(*self.tab_4).text).is_equal_to(self.tab_4_text)
                self.browser.find_element(*self.tab_4).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.tab_4_des).text).is_equal_to(self.tab_des_text)

                assert_that(self.browser.find_element(*self.tab_5).text).is_equal_to(self.tab_5_text)
                self.browser.find_element(*self.tab_5).click()
                time.sleep(.5)
                assert_that(self.browser.find_element(*self.tab_5_des).text).is_equal_to(self.tab_des_text)




