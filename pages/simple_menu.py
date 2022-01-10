import time

from assertpy import soft_assertions, assert_that
from selenium.webdriver import ActionChains
# from src.testproject.sdk.drivers.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils.config import *


class SimpleMenu:
    widget = '//*[@id="post-267411"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = "Simple Menu"
    DOC_LINK = f'//*[@id="post-267411"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               f'/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_link = f'//*[@id="post-267411"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/' \
               f'section/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "SIMPLE MENU"

    # Horizontal Layouts
    H_HOME = (By.XPATH, f'//*[@id="menu-item-267446"]')
    H_ELEMENTOR = (By.XPATH, f'//*[@id="menu-item-267450"]')
    H_ELEMENTOR_WOO_SLIDER = (By.XPATH, f'//*[@id="menu-item-267452"]')
    H_ELEMENTOR_WOO_GRID = (By.XPATH, f'//*[@id="menu-item-267453"]')
    H_ELEMENTOR_WOO_COMPARE = (By.XPATH, f'//*[@id="menu-item-267454"]')
    H_ELEMENTOR_WOO_CAROUSEL = (By.XPATH, f'//*[@id="menu-item-267455"]')
    H_ELEMENTOR_CALL_ACTION = (By.XPATH, f'//*[@id="menu-item-267552"]')
    H_SIMPLE_MENU = (By.XPATH, f'//*[@id="menu-item-267445"]')
    H_BLOG = (By.XPATH, f'//*[@id="menu-item-267449"]')
    H_SUPPORT = (By.XPATH, f'//*[@id="menu-item-267447"]')

    # Vertical Layouts
    V_HOME = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[1]')
    V_ELEMENTOR = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]')
    V_EXPAND_BUTTON = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/span')
    V_ELEMENTOR_ACCORDION = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[1]')
    V_ELEMENTOR_MAP = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[2]')
    V_ELEMENTOR_MANU = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[3]')
    V_ELEMENTOR_TABS = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[4]')
    V_ELEMENTOR_CAL_FORM = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[5]')
    V_ELEMENTOR_CALL_ACTION = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[6]')
    V_ELEMENTOR_FORM_7 = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[7]')
    V_ELEMENTOR_TICKER = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[8]')
    V_SIMPLE_MENU = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[3]')
    V_BLOG = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[4]')
    V_SUPPORT = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[5]')
    V_CONTACT = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[5]')

    ea_p_s = f'//*[@id="post-266629"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             f'/div/div/div[2]/div/div/div[1]/div/h2'
    ea_p_s_text = "Woo Product Slider"

    adv_acor = f'//*[@id="post-2453"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]/div' \
               f'/div/div[1]/div/h2'
    adv_acor_text = "Advanced Accordion"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(simple_menu)

    def testcase(self):
        c = CheckText(self.browser)
        # with soft_assertions():
        c.check_widget_name(self.widget, self.widget_name)
        if check_doc:
            c.check_doc(self.DOC_LINK, self.doc_name)
        self.browser.execute_script("window.scrollTo(0, 905)")
        time.sleep(1)

        self.browser.find_element(*self.H_HOME).click()
        self.browser.back()

        cursor = ActionChains(self.browser)

        h_ele_ele = self.browser.find_element(*self.H_ELEMENTOR)
        h_ele_woo_slider = self.browser.find_element(*self.H_ELEMENTOR_WOO_SLIDER)
        h_ele_woo_grid = self.browser.find_element(*self.H_ELEMENTOR_WOO_GRID)
        h_ele_woo_compare = self.browser.find_element(*self.H_ELEMENTOR_WOO_COMPARE)
        h_ele_woo_carousel = self.browser.find_element(*self.H_ELEMENTOR_WOO_CAROUSEL)
        h_ele_woo_action = self.browser.find_element(*self.H_ELEMENTOR_CALL_ACTION)
        h_blog = self.browser.find_element(*self.H_BLOG)
        h_support = self.browser.find_element(*self.H_SUPPORT)

        cursor.move_to_element(h_ele_ele).move_to_element(h_ele_woo_slider). \
            move_to_element(h_ele_woo_grid).move_to_element(h_ele_woo_compare). \
            move_to_element(h_ele_woo_carousel).move_to_element(h_ele_woo_action). \
            move_to_element(h_blog).move_to_element(h_support).perform()

        cursor.move_to_element(h_ele_ele).move_to_element(h_ele_woo_slider).click().perform()
        c.check_widget_name(self.ea_p_s, self.ea_p_s_text)
        self.browser.back()

        self.browser.execute_script("window.scrollTo(0, 3971)")
        self.browser.find_element(*self.V_HOME).click()
        self.browser.back()

        self.browser.execute_script("window.scrollTo(0, 3971)")
        cursor = ActionChains(self.browser)

        v_ele_ele = self.browser.find_element(*self.V_ELEMENTOR)
        v_ele_accordion = self.browser.find_element(*self.V_ELEMENTOR_ACCORDION)
        v_ele_map = self.browser.find_element(*self.V_ELEMENTOR_MAP)
        v_ele_menu = self.browser.find_element(*self.V_ELEMENTOR_ACCORDION)
        v_ele_tab = self.browser.find_element(*self.V_ELEMENTOR_TABS)
        v_ele_caldera_form = self.browser.find_element(*self.V_ELEMENTOR_CAL_FORM)
        v_ele_action = self.browser.find_element(*self.V_ELEMENTOR_CALL_ACTION)
        v_ele_cf7 = self.browser.find_element(*self.V_ELEMENTOR_FORM_7)
        v_ele_ticker = self.browser.find_element(*self.V_ELEMENTOR_TICKER)
        v_ele_support = self.browser.find_element(*self.V_SUPPORT)
        v_ele_blog = self.browser.find_element(*self.V_BLOG)
        v_ele_contact_us = self.browser.find_element(*self.V_CONTACT)

        cursor.move_to_element(v_ele_ele).perform()
        self.browser.find_element(*self.V_EXPAND_BUTTON).click()

        cursor.move_to_element(v_ele_accordion).move_to_element(v_ele_map).move_to_element(v_ele_menu). \
            move_to_element(v_ele_tab).move_to_element(v_ele_caldera_form).move_to_element(v_ele_action). \
            move_to_element(v_ele_cf7).move_to_element(v_ele_ticker).move_to_element(v_ele_support).\
            move_to_element(v_ele_blog).move_to_element(v_ele_contact_us).perform()

        cursor.move_to_element(v_ele_accordion).click().perform()
        c.check_widget_name(self.adv_acor, self.adv_acor_text)
        self.browser.back()
