from selenium.webdriver import ActionChains

from utils.config import *


class SimpleMenu(Helper):
    widget = '//*[@id="post-267411"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = "Simple Menu"
    doc_link = f'//*[@id="post-267411"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               f'/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "SIMPLE MENU"

    # Horizontal Layouts
    h_home = (By.XPATH, f'//*[@id="menu-item-267446"]')
    h_elementor = (By.XPATH, f'//*[@id="menu-item-267450"]')
    h_elementor_woo_slider = (By.XPATH, f'//*[@id="menu-item-267452"]')
    h_elementor_woo_grid = (By.XPATH, f'//*[@id="menu-item-267453"]')
    h_elementor_woo_compare = (By.XPATH, f'//*[@id="menu-item-267454"]')
    h_elementor_woo_carousel = (By.XPATH, f'//*[@id="menu-item-267455"]')
    h_elementor_call_action = (By.XPATH, f'//*[@id="menu-item-267552"]')
    h_simple_menu = (By.XPATH, f'//*[@id="menu-item-267445"]')
    h_blog = (By.XPATH, f'//*[@id="menu-item-267449"]')
    h_support = (By.XPATH, f'//*[@id="menu-item-267447"]')

    # Vertical Layouts
    v_home = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[1]')
    v_elementor = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]')
    v_expand_button = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/span')
    v_elementor_accordion = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[1]')
    v_elementor_map = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[2]')
    v_elementor_manu = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[3]')
    v_elementor_tabs = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[4]')
    v_elementor_cal_form = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[5]')
    v_elementor_call_action = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[6]')
    v_elementor_form_7 = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[7]')
    v_elementor_ticker = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[8]')
    v_simple_menu = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[3]')
    v_blog = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[4]')
    v_support = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[5]')
    v_contact = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[5]')

    ea_p_s = f'//*[@id="post-266629"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             f'/div/div/div[2]/div/div/div[1]/div/h2'
    ea_p_s_text = "Woo Product Slider"

    adv_acor = f'//*[@id="post-2453"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]/div' \
               f'/div/div[1]/div/h2'
    adv_acor_text = "Advanced Accordion"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.simple_menu)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)
            self.browser.execute_script("window.scrollTo(0, 905)")
            time.sleep(1)

            self.browser.find_element(*self.h_home).click()
            self.browser.back()

            cursor = ActionChains(self.browser)

            h_ele_ele = self.browser.find_element(*self.h_elementor)
            h_ele_woo_slider = self.browser.find_element(*self.h_elementor_woo_slider)
            h_ele_woo_grid = self.browser.find_element(*self.h_elementor_woo_grid)
            h_ele_woo_compare = self.browser.find_element(*self.h_elementor_woo_compare)
            h_ele_woo_carousel = self.browser.find_element(*self.h_elementor_woo_carousel)
            h_ele_woo_action = self.browser.find_element(*self.h_elementor_call_action)
            h_blog = self.browser.find_element(*self.h_blog)
            h_support = self.browser.find_element(*self.h_support)

            cursor.move_to_element(h_ele_ele).move_to_element(h_ele_woo_slider). \
                move_to_element(h_ele_woo_grid).move_to_element(h_ele_woo_compare). \
                move_to_element(h_ele_woo_carousel).move_to_element(h_ele_woo_action). \
                move_to_element(h_blog).move_to_element(h_support).perform()

            cursor.move_to_element(h_ele_ele).move_to_element(h_ele_woo_slider).click().perform()
            self.check_widget_name(self.ea_p_s, self.ea_p_s_text)
            self.browser.back()

            self.browser.execute_script("window.scrollTo(0, 3971)")
            self.browser.find_element(*self.v_home).click()
            self.browser.back()

            self.browser.execute_script("window.scrollTo(0, 3971)")
            cursor = ActionChains(self.browser)

            v_ele_ele = self.browser.find_element(*self.v_elementor)
            v_ele_accordion = self.browser.find_element(*self.v_elementor_accordion)
            v_ele_map = self.browser.find_element(*self.v_elementor_map)
            v_ele_menu = self.browser.find_element(*self.v_elementor_accordion)
            v_ele_tab = self.browser.find_element(*self.v_elementor_tabs)
            v_ele_caldera_form = self.browser.find_element(*self.v_elementor_cal_form)
            v_ele_action = self.browser.find_element(*self.v_elementor_call_action)
            v_ele_cf7 = self.browser.find_element(*self.v_elementor_form_7)
            v_ele_ticker = self.browser.find_element(*self.v_elementor_ticker)
            v_ele_support = self.browser.find_element(*self.v_support)
            v_ele_blog = self.browser.find_element(*self.v_blog)
            v_ele_contact_us = self.browser.find_element(*self.v_contact)

            cursor.move_to_element(v_ele_ele).perform()
            self.browser.find_element(*self.v_expand_button).click()

            cursor.move_to_element(v_ele_accordion).move_to_element(v_ele_map).move_to_element(v_ele_menu). \
                move_to_element(v_ele_tab).move_to_element(v_ele_caldera_form).move_to_element(v_ele_action). \
                move_to_element(v_ele_cf7).move_to_element(v_ele_ticker).move_to_element(v_ele_support).\
                move_to_element(v_ele_blog).move_to_element(v_ele_contact_us).perform()

            cursor.move_to_element(v_ele_accordion).click().perform()
            self.check_widget_name(self.adv_acor, self.adv_acor_text)
            self.browser.back()
