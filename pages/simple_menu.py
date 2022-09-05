from pages.basepage import BasePage
from utils.config import *


class SimpleMenu(BasePage, Helper):
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
    v_elementor_menu = (By.XPATH, f'//*[@id="menu-advanced-menu-7"]/li[2]/ul/li[3]')
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

    def horizontal_menu(self):
        self.do_click(self.h_home)
        self.go_back()
        self.move_cursor_to(self.h_elementor)
        """Move cursor to sub menus"""
        self.cursor.move_to_element(self.get_element(self.h_elementor)). \
            move_to_element(self.get_element(self.h_elementor_woo_slider)). \
            move_to_element(self.get_element(self.h_elementor_woo_grid)). \
            move_to_element(self.get_element(self.h_elementor_woo_compare)). \
            move_to_element(self.get_element(self.h_elementor_woo_carousel)). \
            move_to_element(self.get_element(self.h_elementor_call_action)). \
            move_to_element(self.get_element(self.h_blog)). \
            move_to_element(self.get_element(self.h_support)).perform()
        """Click a sub menu items"""
        self.reload_page()
        self.move_cursor_to(self.h_elementor)
        self.cursor.move_to_element(self.get_element(self.h_elementor)). \
            move_to_element(self.get_element(self.h_elementor_woo_slider)).click().perform()
        self.check_widget_name(self.ea_p_s, self.ea_p_s_text)
        self.go_back()

    def vertical_menu(self):
        self.do_click(self.v_home)
        self.go_back()
        self.scroll_to(4061)
        self.move_cursor_to(self.v_elementor)
        self.do_click(self.v_expand_button)
        """Move cursor to sub menus"""
        self.cursor.move_to_element(self.get_element(self.v_elementor_accordion)).\
            move_to_element(self.get_element(self.v_elementor_map)).\
            move_to_element(self.get_element(self.v_elementor_menu)).\
            move_to_element(self.get_element(self.v_elementor_tabs)).\
            move_to_element(self.get_element(self.v_elementor_cal_form)).\
            move_to_element(self.get_element(self.v_elementor_call_action)). \
            move_to_element(self.get_element(self.v_elementor_form_7)). \
            move_to_element(self.get_element(self.v_elementor_ticker)). \
            move_to_element(self.get_element(self.v_support)). \
            move_to_element(self.get_element(self.v_blog)). \
            move_to_element(self.get_element(self.v_contact)).perform()
        """Click a sub menu items"""
        self.move_cursor_to_and_click(self.v_elementor_accordion)
        self.check_widget_name(self.adv_acor, self.adv_acor_text)
        self.go_back()

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.simple_menu)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(905)
                self.horizontal_menu()
                self.scroll_to(4044)
                self.vertical_menu()
