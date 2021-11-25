from assertpy import soft_assertions, assert_that
from selenium.webdriver.common.by import By

demo_page = "https://essential-addons.com/elementor/demos/"
base_url = "https://essential-addons.com/elementor/"
simple_menu = base_url + "simple-menu/"
flip_box = base_url + "flip-box/"
create_button = base_url + "creative-buttons/"
static_product = base_url + "static-product/"
event_calendar = base_url + "event-calendar/"
team_members_carousel = base_url + "team-members-carousel/"
logo_carousel = base_url + "logo-carousel/"
dual_color_heading = base_url + "dual-color-headline/"
info_box = base_url + "info-box/"
team_members = base_url + "team-members/"
advanced_accordion = base_url + "advanced-accordion/"
advanced_tabs = base_url + "advanced-tabs/"
testimonial_slider = base_url + "testimonial-slider/"
protected_content = base_url + "protected-content/"
tooltip = base_url + "tooltip/"
sticky_video = base_url + "sticky-video/"
testimonials = base_url + "testimonials/"
feature_list = base_url + "feature-list/"

check_doc = False
# check_doc = True
display = 1


class CheckText:
    HEADING = (By.ID, f'betterdocs-entry-title')

    WIDGET_TITLE = (By.XPATH, f'//*[@id="post-266629"]/div/div/div/div/section[1]/div[3]/div/div['
                              f'2]/div/div/section/div/div/div[2]/div/div/div[1]/div/h2')

    def __init__(self, browser):
        self.browser = browser

    def check_doc(self, link, name):
        self.browser.find_element(By.XPATH, link).click()
        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[1])
        ele = self.browser.find_element(*self.HEADING)

        assert_that(ele.text).is_equal_to(name)
        # try:
        #     assert ele.text == txt
        # except AssertionError:
        #     print("Assertion failed. Actual value is %s" % ele.text)

        self.browser.close()
        self.browser.switch_to.window(windows[0])

    def check_widget_name(self, locator, name):
        with soft_assertions():
            assert_that(self.browser.find_element(By.XPATH, locator).text).is_equal_to(name)


