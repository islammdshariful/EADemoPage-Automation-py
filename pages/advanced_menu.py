import time

from selenium.webdriver import ActionChains

from utils.config import *


class AdvancedMenu(Helper):
    widget = '//*[@id="post-4584"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Advanced Menu'
    doc_link = '//*[@id="post-4584"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA ADVANCED MENU"

    h_home = (By.XPATH, f'/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]'
                        f'/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]')
    h_home_text = "Home"
    h_elementor = (By.XPATH, f'//*[@id="menu-item-4843"]')
    h_elementor_text = "Elements"
    h_elementor_accor = (By.XPATH, f'//*[@id="menu-item-4844"]')
    h_elementor_accor_text = "Advanced Accordion for Elementor"
    h_elementor_map = (By.XPATH, f'//*[@id="menu-item-4845"]')
    h_elementor_map_text = "Advanced Google Map for Elementor"
    h_elementor_menu = (By.XPATH, f'//*[@id="menu-item-4846"]')
    h_elementor_menu_text = "Advanced Menu"
    h_elementor_tab = (By.XPATH, f'//*[@id="menu-item-4847"]')
    h_elementor_tab_text = "Advanced Tabs for Elementor"
    h_elementor_calderaform = (By.XPATH, f'//*[@id="menu-item-4848"]')
    h_elementor_calderaform_text = "Caldera Forms"
    h_elementor_calltoaction = (By.XPATH, f'//*[@id="menu-item-4849"]')
    h_elementor_calltoaction_text = "Call To Action"
    h_elementor_cf7 = (By.XPATH, f'//*[@id="menu-item-4850"]')
    h_elementor_cf7_text = "Contact Form 7"
    h_elementor_ticker = (By.XPATH, f'//*[@id="menu-item-4851"]')
    h_elementor_ticker_text = "Content Ticker"
    h_support = (By.XPATH, f'//*[@id="menu-item-4859"]')
    h_support_text = "Support"
    h_blog = (By.XPATH, f'//*[@id="menu-item-4861"]')
    h_blog_text = "Blog"
    h_contact = (By.XPATH, f'//*[@id="menu-item-4862"]')
    h_contact_text = "Contact Us"

    v_home = (By.XPATH, f'//*[@id="menu-advanced-menu-9"]/li[1]')
    v_home_text = "Home"
    v_elementor = (By.XPATH, f'//*[@id="menu-advanced-menu-9"]/li[2]')
    v_elementor_text = "Elements"
    v_toogle = (By.XPATH, f'//*[@id="menu-advanced-menu-9"]/li[2]/span')
    v_elementor_accor = (By.XPATH, f'//*[@id="menu-advanced-menu-9"]/li[2]/ul/li[1]')
    v_elementor_accor_text = "Advanced Accordion for Elementor"
    v_elementor_map = (By.XPATH, f'//*[@id="menu-advanced-menu-9"]/li[2]/ul/li[2]')
    v_elementor_map_text = "Advanced Google Map for Elementor"
    v_elementor_menu = (By.XPATH, f'//*[@id="menu-advanced-menu-9"]/li[2]/ul/li[3]')
    v_elementor_menu_text = "Advanced Menu"
    v_elementor_tab = (By.XPATH, f'//*[@id="menu-advanced-menu-9"]/li[2]/ul/li[4]')
    v_elementor_tab_text = "Advanced Tabs for Elementor"
    v_elementor_calderaform = (By.XPATH, f'//*[@id="menu-advanced-menu-9"]/li[2]/ul/li[5]')
    v_elementor_calderaform_text = "Caldera Forms"
    v_elementor_calltoaction = (By.XPATH, f'//*[@id="menu-advanced-menu-9"]/li[2]/ul/li[6]')
    v_elementor_calltoaction_text = "Call To Action"
    v_elementor_cf7 = (By.XPATH, f'//*[@id="menu-advanced-menu-9"]/li[2]/ul/li[7]')
    v_elementor_cf7_text = "Contact Form 7"
    v_elementor_ticker = (By.XPATH, f'//*[@id="menu-advanced-menu-9"]/li[2]/ul/li[8]')
    v_elementor_ticker_text = "Content Ticker"
    v_support = (By.XPATH, f'//*[@id="menu-advanced-menu-9"]/li[3]')
    v_support_text = "Support"
    v_blog = (By.XPATH, f'//*[@id="menu-advanced-menu-9"]/li[4]')
    v_blog_text = "Blog"
    v_contact = (By.XPATH, f'//*[@id="menu-advanced-menu-9"]/li[5]')
    v_contact_text = "Contact Us"

    ea_l_p = f'//*[@id="post-1334"]/div/div/div/div/section[1]/div/div/div/div/div/section/div/div/div[1]/div/div' \
             f'/div[3]/div/h2'
    ea_l_p_text = "Most Popular Elements Library For Elementor"

    adv_acor = f'//*[@id="post-2453"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]/div' \
               f'/div/div[1]/div/h2'
    adv_acor_text = "Advanced Accordion"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.advanced_menu)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 934)")
            time.sleep(1)
            assert_that(self.browser.find_element(*self.h_home).text).is_equal_to(self.h_home_text)
            assert_that(self.browser.find_element(*self.h_elementor).text).is_equal_to(self.h_elementor_text)
            assert_that(self.browser.find_element(*self.h_support).text).is_equal_to(self.h_support_text)
            assert_that(self.browser.find_element(*self.h_blog).text).is_equal_to(self.h_blog_text)
            assert_that(self.browser.find_element(*self.h_contact).text).is_equal_to(self.h_contact_text)
            self.browser.find_element(*self.h_home).click()
            self.check_widget_name(self.ea_l_p, self.ea_l_p_text)
            self.browser.back()
            time.sleep(1)
            self.browser.execute_script("window.scrollTo(0, 934)")
            time.sleep(1)
            cursor = ActionChains(self.browser)
            h_ele = self.browser.find_element(*self.h_elementor)
            h_ele_accor = self.browser.find_element(*self.h_elementor_accor)
            h_ele_map = self.browser.find_element(*self.h_elementor_map)
            h_ele_menu = self.browser.find_element(*self.h_elementor_menu)
            h_ele_tab = self.browser.find_element(*self.h_elementor_tab)
            h_ele_calderaform = self.browser.find_element(*self.h_elementor_calderaform)
            h_ele_calltoaction = self.browser.find_element(*self.h_elementor_calltoaction)
            h_ele_cf7 = self.browser.find_element(*self.h_elementor_cf7)
            h_ele_ticker = self.browser.find_element(*self.h_elementor_ticker)
            cursor.move_to_element(h_ele).perform()

            assert_that(h_ele_accor.text).is_equal_to(self.h_elementor_accor_text)
            assert_that(h_ele_map.text).is_equal_to(self.h_elementor_map_text)
            assert_that(h_ele_menu.text).is_equal_to(self.h_elementor_menu_text)
            assert_that(h_ele_tab.text).is_equal_to(self.h_elementor_tab_text)
            assert_that(h_ele_calderaform.text).is_equal_to(self.h_elementor_calderaform_text)
            assert_that(h_ele_calltoaction.text).is_equal_to(self.h_elementor_calltoaction_text)
            assert_that(h_ele_cf7.text).is_equal_to(self.h_elementor_cf7_text)
            assert_that(h_ele_ticker.text).is_equal_to(self.h_elementor_ticker_text)

            cursor.move_to_element(h_ele).move_to_element(h_ele_accor).move_to_element(h_ele_map).\
                move_to_element(h_ele_menu).move_to_element(h_ele_tab).move_to_element(h_ele_calderaform).\
                move_to_element(h_ele_calltoaction).move_to_element(h_ele_cf7).move_to_element(h_ele_ticker).perform()

            cursor.move_to_element(h_ele).move_to_element(h_ele_accor).click().perform()
            self.check_widget_name(self.adv_acor, self.adv_acor_text)
            self.browser.back()
            time.sleep(1)
            h_sup = self.browser.find_element(*self.h_support)
            h_blog = self.browser.find_element(*self.h_blog)
            h_cont = self.browser.find_element(*self.h_contact)
            cursor.move_to_element(h_sup).move_to_element(h_blog).move_to_element(h_cont).perform()

            self.browser.execute_script("window.scrollTo(0, 3158)")
            time.sleep(1)

            # Vertical Tabs
            assert_that(self.browser.find_element(*self.v_home).text).is_equal_to(self.v_home_text)
            assert_that(self.browser.find_element(*self.v_elementor).text).is_equal_to(self.v_elementor_text)
            assert_that(self.browser.find_element(*self.v_support).text).is_equal_to(self.v_support_text)
            assert_that(self.browser.find_element(*self.v_blog).text).is_equal_to(self.v_blog_text)
            assert_that(self.browser.find_element(*self.v_contact).text).is_equal_to(self.v_contact_text)
            self.browser.find_element(*self.v_home).click()
            self.check_widget_name(self.ea_l_p, self.ea_l_p_text)
            self.browser.back()
            time.sleep(1)
            self.browser.execute_script("window.scrollTo(0, 3158)")
            time.sleep(1)
            self.browser.find_element(*self.v_toogle).click()
            time.sleep(.5)

            # v_ele = self.browser.find_element(*self.v_elementor)
            v_ele_accor = self.browser.find_element(*self.v_elementor_accor)
            v_ele_map = self.browser.find_element(*self.v_elementor_map)
            v_ele_menu = self.browser.find_element(*self.v_elementor_menu)
            v_ele_tab = self.browser.find_element(*self.v_elementor_tab)
            v_ele_calderaform = self.browser.find_element(*self.v_elementor_calderaform)
            v_ele_calltoaction = self.browser.find_element(*self.v_elementor_calltoaction)
            v_ele_cf7 = self.browser.find_element(*self.v_elementor_cf7)
            v_ele_ticker = self.browser.find_element(*self.v_elementor_ticker)

            assert_that(v_ele_accor.text).is_equal_to(self.v_elementor_accor_text)
            assert_that(v_ele_map.text).is_equal_to(self.v_elementor_map_text)
            assert_that(v_ele_menu.text).is_equal_to(self.v_elementor_menu_text)
            assert_that(v_ele_tab.text).is_equal_to(self.v_elementor_tab_text)
            assert_that(v_ele_calderaform.text).is_equal_to(self.v_elementor_calderaform_text)
            assert_that(v_ele_calltoaction.text).is_equal_to(self.v_elementor_calltoaction_text)
            assert_that(v_ele_cf7.text).is_equal_to(self.v_elementor_cf7_text)
            assert_that(v_ele_ticker.text).is_equal_to(self.v_elementor_ticker_text)

            cursor.move_to_element(v_ele_accor).move_to_element(v_ele_map). \
                move_to_element(v_ele_menu).move_to_element(v_ele_tab).move_to_element(v_ele_calderaform). \
                move_to_element(v_ele_calltoaction).move_to_element(v_ele_cf7).move_to_element(v_ele_ticker).perform()

            self.browser.find_element(*self.v_toogle).click()
            time.sleep(1)
            self.browser.find_element(*self.v_toogle).click()

            cursor.move_to_element(v_ele_accor).click().perform()
            time.sleep(.5)
            self.check_widget_name(self.adv_acor, self.adv_acor_text)
            self.browser.back()
            time.sleep(1)
            v_sup = self.browser.find_element(*self.v_support)
            v_blog = self.browser.find_element(*self.v_blog)
            v_cont = self.browser.find_element(*self.v_contact)

            cursor.move_to_element(v_sup).move_to_element(v_blog).move_to_element(v_cont).perform()




