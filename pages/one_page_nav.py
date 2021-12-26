from selenium.webdriver import ActionChains

from utils.config import *


class OnePageNav:
    widget = '//*[@id="post-2958"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'One Page Navigation'
    doc_link = '//*[@id="post-2958"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "ONE PAGE NAVIGATION"

    nav_1 = (By.XPATH, f'//*[@id="eael-one-page-nav-2221bcee"]/li[1]')
    nav_2 = (By.XPATH, f'//*[@id="eael-one-page-nav-2221bcee"]/li[2]')
    nav_3 = (By.XPATH, f'//*[@id="eael-one-page-nav-2221bcee"]/li[3]')
    nav_4 = (By.XPATH, f'//*[@id="eael-one-page-nav-2221bcee"]/li[4]')
    nav_5 = (By.XPATH, f'//*[@id="eael-one-page-nav-2221bcee"]/li[5]')

    nav_1_content = f'//*[@id="hero-area"]/div/div/div/div/div/section/div/div/div/div/div/div[1]/div/h3'
    nav_1_content_text = "Create One Page Navigation"

    nav_2_content = f'//*[@id="features-section"]/div/div/div/div/div/section[1]/div/div/div/div/div/div[1]/div/h3'
    nav_2_content_text = "Customize Within Minutes"

    nav_3_content = f'//*[@id="services-section"]/div/div/div/div/div/section[1]/div/div/div/div/div/div/div/h3'
    nav_3_content_text = "Create Beautiful Single Page Website"

    nav_4_content = f'//*[@id="pricing-plans-section"]/div/div/div/div/div/section/div/div/div/div/div/div/div/h3'
    nav_4_content_text = "Flexible Pricing for Everyone"

    nav_5_content = f'//*[@id="blog-posts-section"]/div/div/div/div/div/section[1]/div/div/div/div/div/div/div/h3'
    nav_5_content_text = "Our Latest Blogs"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(one_page_nav)

    def check_visibility(self, locator, text):
        if self.browser.find_element(By.XPATH, locator).is_displayed():
            assert_that(self.browser.find_element(By.XPATH, locator).text).is_equal_to(text)
        else:
            assert_that(display).is_equal_to("Content is not Visible")

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 905)")
            self.browser.find_element(*self.nav_5).click()
            time.sleep(1)
            self.check_visibility(self.nav_5_content, self.nav_5_content_text)
            self.browser.find_element(*self.nav_3).click()
            time.sleep(1)
            self.check_visibility(self.nav_3_content, self.nav_3_content_text)
            self.browser.find_element(*self.nav_4).click()
            time.sleep(1)
            self.check_visibility(self.nav_4_content, self.nav_4_content_text)
            self.browser.find_element(*self.nav_1).click()
            time.sleep(1)
            self.check_visibility(self.nav_1_content, self.nav_1_content_text)
            self.browser.find_element(*self.nav_2).click()
            time.sleep(1)
            self.check_visibility(self.nav_2_content, self.nav_2_content_text)

