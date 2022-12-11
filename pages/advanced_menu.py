import time

from selenium.webdriver import ActionChains, Keys

from pages.basepage import BasePage
from utils.config import *


class AdvancedMenu(BasePage, Helper):
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

    scroll = (By.XPATH, f'//*[@id="post-4584"]/div/div/div/div/section[16]')

    def __init__(self, browser):
        super().__init__(browser)

    def horizontal_menu(self):
        """Checking Horizontal Menu"""
        """Checking all menu items' name"""
        self.check_text_matches_with(self.h_home, self.h_home_text)
        self.check_text_matches_with(self.h_elementor, self.h_elementor_text)
        self.check_text_matches_with(self.h_support, self.h_support_text)
        self.check_text_matches_with(self.h_blog, self.h_blog_text)
        self.check_text_matches_with(self.h_contact, self.h_contact_text)
        """Go to Homepage via menu"""
        self.do_click(self.h_home)
        self.check_widget_name(self.ea_l_p, self.ea_l_p_text)
        """Navigating Back"""
        self.go_back()
        self.browser.execute_script("window.scrollTo(0, 934)")
        time.sleep(1)
        """Move cursor to Element item"""
        self.move_cursor_to(self.h_elementor)
        """Checking all sub menu items name"""
        self.check_text_matches_with(self.h_elementor_accor, self.h_elementor_accor_text)
        self.check_text_matches_with(self.h_elementor_map, self.h_elementor_map_text)
        self.check_text_matches_with(self.h_elementor_menu, self.h_elementor_menu_text)
        self.check_text_matches_with(self.h_elementor_tab, self.h_elementor_tab_text)
        self.check_text_matches_with(self.h_elementor_calderaform, self.h_elementor_calderaform_text)
        self.check_text_matches_with(self.h_elementor_calltoaction, self.h_elementor_calltoaction_text)
        self.check_text_matches_with(self.h_elementor_cf7, self.h_elementor_cf7_text)
        self.check_text_matches_with(self.h_elementor_ticker, self.h_elementor_ticker_text)

        """Moving cursor to all the sub menus"""
        self.cursor.move_to_element(self.get_element(self.h_elementor)).move_to_element(
            self.get_element(self.h_elementor_accor)).move_to_element(
            self.get_element(self.h_elementor_map)).move_to_element(
            self.get_element(self.h_elementor_menu)).move_to_element(
            self.get_element(self.h_elementor_tab)).move_to_element(
            self.get_element(self.h_elementor_calderaform)).move_to_element(
            self.get_element(self.h_elementor_calltoaction)).move_to_element(
            self.get_element(self.h_elementor_cf7)).move_to_element(
            self.get_element(self.h_elementor_ticker)).perform()
        """Navigating to a sub menu item"""
        self.cursor.move_to_element(self.get_element(self.h_elementor)).move_to_element(
            self.get_element(self.h_elementor_accor)).click().perform()
        self.check_widget_name(self.adv_acor, self.adv_acor_text)
        self.go_back()
        """Moving cursor to other menu items"""
        self.cursor.move_to_element(self.get_element(self.h_support)).move_to_element(
            self.get_element(self.h_blog)).move_to_element(
            self.get_element(self.h_contact)).perform()

        self.browser.execute_script("window.scrollTo(0, 3158)")
        time.sleep(1)

    def vertical_menu(self):
        """Checking Vertical Menu"""
        """Checking all menu items' name"""
        self.scroll_to_element(self.scroll)
        self.check_text_matches_with(self.v_home, self.v_home_text)
        self.check_text_matches_with(self.v_elementor, self.v_elementor_text)
        self.check_text_matches_with(self.v_support, self.v_support_text)
        self.check_text_matches_with(self.v_blog, self.v_blog_text)
        self.check_text_matches_with(self.v_contact, self.v_contact_text)
        """Go to Homepage via menu"""
        self.do_click(self.v_home)
        self.check_widget_name(self.ea_l_p, self.ea_l_p_text)
        """Navigating Back"""
        self.go_back()
        self.scroll_to_element(self.scroll)
        time.sleep(1)
        """Expanding sub menus"""
        self.do_click(self.v_toogle)
        time.sleep(.5)
        """Checking all sub menu items name"""
        self.check_text_matches_with(self.v_elementor_accor, self.v_elementor_accor_text)
        self.check_text_matches_with(self.v_elementor_map, self.v_elementor_map_text)
        self.check_text_matches_with(self.v_elementor_menu, self.v_elementor_menu_text)
        self.check_text_matches_with(self.v_elementor_tab, self.v_elementor_tab_text)
        self.check_text_matches_with(self.v_elementor_calderaform, self.v_elementor_calderaform_text)
        self.check_text_matches_with(self.v_elementor_calltoaction, self.v_elementor_calltoaction_text)
        self.check_text_matches_with(self.v_elementor_cf7, self.v_elementor_cf7_text)
        self.check_text_matches_with(self.v_elementor_ticker, self.v_elementor_ticker_text)
        """Moving cursor to all the sub menus"""
        self.cursor.move_to_element(self.get_element(self.v_elementor)).move_to_element(
            self.get_element(self.v_elementor_accor)).move_to_element(
            self.get_element(self.v_elementor_map)).move_to_element(
            self.get_element(self.v_elementor_menu)).move_to_element(
            self.get_element(self.v_elementor_tab)).move_to_element(
            self.get_element(self.v_elementor_calderaform)).move_to_element(
            self.get_element(self.v_elementor_calltoaction)).move_to_element(
            self.get_element(self.v_elementor_cf7)).move_to_element(
            self.get_element(self.v_elementor_ticker)).perform()
        self.do_click(self.v_toogle)
        time.sleep(1)
        """Click to a sub menu item"""
        self.do_click(self.v_toogle)
        time.sleep(1)
        self.cursor.move_to_element(self.get_element(self.v_elementor_accor)).click().perform()
        time.sleep(.5)
        self.check_widget_name(self.adv_acor, self.adv_acor_text)
        self.go_back()
        """Moving cursor to other menu items"""
        self.cursor.move_to_element(self.get_element(self.v_support)).move_to_element(
            self.get_element(self.v_blog)).move_to_element(
            self.get_element(self.v_contact)).perform()

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.advanced_menu)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(934)

                """Check horizontal menu"""
                self.horizontal_menu()

                """Check vertical menu"""
                self.vertical_menu()
