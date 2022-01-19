from selenium.webdriver import ActionChains

from utils.config import *


class ContentToggle:
    widget = '//*[@id="post-2605"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Content Toggle'
    doc_link = '//*[@id="post-2605"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "CONTENT TOGGLE"
    toggle_button = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[1]/div/div[2]/label/span')
    primary_btn = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[1]/div/div[1]')
    primary_btn_text = "Single"
    secondary_btn = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[1]/div/div[3]')
    secondary_btn_text = "Unlimited"

    p_1_title = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                           f'/div/div/div/div/div/div/div/div/div/div[2]/h2')
    p_1_title_text = "Single"
    p_1_price = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                           f'/div/div/div/div/div/div/div/div/div/div[1]/span[1]/span')
    p_1_price_text = "$49.50"
    p_1_month = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                           f'/div/div/div/div/div/div/div/div/div/div[1]/span[2]')
    p_1_month_text = "Permonth"
    p_1_item_1_icon = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                                 f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[1]/span/i')
    p_1_item_1 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section/div/div/div/'
                            f'div/div/div/div/div/div/div[3]/ul/li[1]')
    p_1_item_1_text = "Unlimited calls"

    p_1_item_2 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[2]')
    p_1_item_2_text = "Free hosting"

    p_1_item_3 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[3]')
    p_1_item_3_text = "500 MB of storage space"

    p_1_item_4 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[4]')
    p_1_item_4_text = "500 MB Bandwidth"

    p_1_item_5 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[5]')
    p_1_item_5_text = "24/7 support"

    p_1_button = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[1]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[4]/a')

    # Secondary
    s_1_title = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                           f'/div/div/div/div/div/div/div/div/div/div[2]/h2')
    s_1_title_text = "Unlimited"
    s_1_price = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                           f'/div/div/div/div/div/div/div/div/div/div[1]/span[1]/span')
    s_1_price_text = "$89.50"
    s_1_month = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                           f'/div/div/div/div/div/div/div/div/div/div[1]/span[2]')
    s_1_month_text = "Permonth"
    s_1_item_1_icon = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                                 f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[1]/span/i')
    s_1_item_1 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section/div/div/div/'
                            f'div/div/div/div/div/div/div[3]/ul/li[1]')
    s_1_item_1_text = "Unlimited calls"

    s_1_item_2 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[2]')
    s_1_item_2_text = "Free hosting"

    s_1_item_3 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[3]')
    s_1_item_3_text = "500 MB of storage space"

    s_1_item_4 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[4]')
    s_1_item_4_text = "500 MB Bandwidth"

    s_1_item_5 = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[3]/ul/li[5]')
    s_1_item_5_text = "24/7 support"

    s_1_button = (By.XPATH, f'//*[@id="eael-toggle-container-6bee69bf"]/div[2]/div[2]/div/div/section'
                            f'/div/div/div/div/div/div/div/div/div/div[4]/a')

    close_scrips_chat_btn = (By.XPATH, f'//*[@id="crisp-chatbox"]/div/a/span[1]/span/span[1]/span[1]/span')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(content_toggle)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1967)")
            wait_for_bar_to_come(self.browser)

            assert_that(self.browser.find_element(*self.primary_btn).text).is_equal_to(self.primary_btn_text)
            assert_that(self.browser.find_element(*self.secondary_btn).text).is_equal_to(self.secondary_btn_text)

            cursor = ActionChains(self.browser)
            p_title = self.browser.find_element(*self.p_1_title)
            p_btn = self.browser.find_element(*self.p_1_button)
            s_title = self.browser.find_element(*self.s_1_title)
            s_btn = self.browser.find_element(*self.s_1_button)
            cursor.move_to_element(p_title).perform()
            time.sleep(1)

            assert_that(p_title.text).is_equal_to(self.p_1_title_text)
            assert_that(self.browser.find_element(*self.p_1_price).text).is_equal_to(self.p_1_price_text)
            assert_that(self.browser.find_element(*self.p_1_month).text).is_equal_to(self.p_1_month_text)

            if self.browser.find_element(*self.p_1_item_1_icon).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to(0)

            assert_that(self.browser.find_element(*self.p_1_item_1).text).is_equal_to(self.p_1_item_1_text)
            assert_that(self.browser.find_element(*self.p_1_item_2).text).is_equal_to(self.p_1_item_2_text)
            assert_that(self.browser.find_element(*self.p_1_item_3).text).is_equal_to(self.p_1_item_3_text)
            assert_that(self.browser.find_element(*self.p_1_item_4).text).is_equal_to(self.p_1_item_4_text)
            assert_that(self.browser.find_element(*self.p_1_item_5).text).is_equal_to(self.p_1_item_5_text)

            cursor.move_to_element(p_btn).perform()

            self.browser.find_element(*self.toggle_button).click()
            time.sleep(.5)

            cursor.move_to_element(s_title).perform()
            # time.sleep(1)

            assert_that(s_title.text).is_equal_to(self.s_1_title_text)
            assert_that(self.browser.find_element(*self.s_1_price).text).is_equal_to(self.s_1_price_text)
            assert_that(self.browser.find_element(*self.s_1_month).text).is_equal_to(self.s_1_month_text)

            if self.browser.find_element(*self.s_1_item_1_icon).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to(0)

            assert_that(self.browser.find_element(*self.s_1_item_1).text).is_equal_to(self.s_1_item_1_text)
            assert_that(self.browser.find_element(*self.s_1_item_2).text).is_equal_to(self.s_1_item_2_text)
            assert_that(self.browser.find_element(*self.s_1_item_3).text).is_equal_to(self.s_1_item_3_text)
            assert_that(self.browser.find_element(*self.s_1_item_4).text).is_equal_to(self.s_1_item_4_text)
            assert_that(self.browser.find_element(*self.s_1_item_5).text).is_equal_to(self.s_1_item_5_text)

            cursor.move_to_element(s_btn).perform()


