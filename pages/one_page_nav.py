from utils.config import *


class OnePageNav(BasePage, Helper):
    widget = '//*[@id="post-2958"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'One Page Navigation'
    doc_link = '//*[@id="post-2958"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "ONE PAGE NAVIGATION"

    nav_1 = (By.XPATH, f'//*[@id="eael-one-page-nav-2221bcee"]/li[1]')
    nav_1_title = (By.XPATH, f'//*[@id="eael-one-page-nav-2221bcee"]/li[1]/span/span')
    nav_2 = (By.XPATH, f'//*[@id="eael-one-page-nav-2221bcee"]/li[2]')
    nav_2_title = (By.XPATH, f'//*[@id="eael-one-page-nav-2221bcee"]/li[2]/span/span')
    nav_3 = (By.XPATH, f'//*[@id="eael-one-page-nav-2221bcee"]/li[3]')
    nav_3_title = (By.XPATH, f'//*[@id="eael-one-page-nav-2221bcee"]/li[3]/span/span')
    nav_4 = (By.XPATH, f'//*[@id="eael-one-page-nav-2221bcee"]/li[4]')
    nav_4_title = (By.XPATH, f'//*[@id="eael-one-page-nav-2221bcee"]/li[4]/span/span')
    nav_5 = (By.XPATH, f'//*[@id="eael-one-page-nav-2221bcee"]/li[5]')
    nav_5_title = (By.XPATH, f'//*[@id="eael-one-page-nav-2221bcee"]/li[5]/span/span')
    nav_1_title_text = "Home"
    nav_2_title_text = "Features"
    nav_3_title_text = "Services"
    nav_4_title_text = "Pricing Plans"
    nav_5_title_text = "Blog"

    nav_1_content = (By.XPATH, f'//*[@id="hero-area"]/div/div/div/div/div/section/div/div/div/div/div/div[1]/div/h3')
    nav_1_content_text = "Create One Page Navigation"

    nav_2_content = (By.XPATH, f'//*[@id="features-section"]/div/div/div/div/div/section[1]/div/div/div/div/div/'
                               f'div[1]/div/h3')
    nav_2_content_text = "Customize Within Minutes"

    nav_3_content = (By.XPATH, f'//*[@id="services-section"]/div/div/div/div/div/section[1]/div/div/div/div/div/' \
                               'div/div/h3')
    nav_3_content_text = "Create Beautiful Single Page Website"

    nav_4_content = (By.XPATH, f'//*[@id="pricing-plans-section"]/div/div/div/div/div/section/div/div/div/div/div/'
                               f'div/div/h3')
    nav_4_content_text = "Flexible Pricing for Everyone"

    nav_5_content = (By.XPATH, f'//*[@id="blog-posts-section"]/div/div/div/div/div/section[1]/div/div/div/div/div/' \
                               'div/div/h3')
    nav_5_content_text = "Our Latest Blogs"

    def __init__(self, browser):
        super().__init__(browser)

    def check_navigation(self, nav, nav_title, nav_title_text, locator, text):
        self.move_cursor_to(nav)
        self.check_text_matches_with(nav_title, nav_title_text)
        self.do_click(nav)

        if self.is_displaying(*locator):
            self.check_text_matches_with(locator, text)
        else:
            assert_that("Navigation is working").is_equal_to("Navigation is not working")

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.one_page_nav)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(905)

                self.check_navigation(self.nav_1, self.nav_1_title, self.nav_1_title_text, self.nav_1_content,
                                      self.nav_1_content_text)
                self.check_navigation(self.nav_2, self.nav_2_title, self.nav_2_title_text, self.nav_2_content,
                                      self.nav_2_content_text)
                self.check_navigation(self.nav_3, self.nav_3_title, self.nav_3_title_text, self.nav_3_content,
                                      self.nav_3_content_text)
                self.check_navigation(self.nav_4, self.nav_4_title, self.nav_4_title_text, self.nav_4_content,
                                      self.nav_4_content_text)
                self.check_navigation(self.nav_5, self.nav_5_title, self.nav_5_title_text, self.nav_5_content,
                                      self.nav_5_content_text)
