from selenium.webdriver import ActionChains

from utils.config import *


class PostList:
    widget = '//*[@id="post-2322"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Smart Post List'
    doc_link = '//*[@id="post-2322"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "SMART POST LIST"

    search = (By.ID, f'search_field')
    search_icon = (By.XPATH, f'//*[@id="post-list-search-form-312f98e8"]/i')
    search_result_title = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div'
                                     f'/div/div/div/div/div/div[1]/div[2]/div/div[1]/h6/a')

    all = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div/div/div/div'
                     f'/div/div[1]/div[1]/a[1]')
    elementor = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div/div/div'
                           f'/div/div/div[1]/div[1]/a[2]')
    essential_addons = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div'
                                  f'/div/div/div/div/div[1]/div[1]/a[3]')
    wordpress = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div/div/div'
                           f'/div/div/div[1]/div[1]/a[4]')

    post_1_title = f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div' \
                   f'/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/h2/a'
    post_1_date = f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div' \
                                       f'/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[1]/span'
    post_1_img = f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div/div' \
                                      f'/div/div/div/div[2]/div/div[1]/div/div[1]/img'

    post_2_title = f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div/div/div' \
                                        f'/div/div/div[2]/div/div[6]/div/div[2]/h2/a'
    post_2_date = f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div/div/div' \
                                       f'/div/div/div[2]/div/div[6]/div/div[2]/div[1]/span'
    post_2_img = f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div/div' \
                                      f'/div/div/div/div[2]/div/div[6]/div/div[1]/img'

    # Article
    article_title = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                               f'/div/div/div/div/div/div[1]/div/h1')
    article_date = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                              f'/div/div/div/div/div/div[2]/div/ul/li[1]/a/span[2]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(post_list)

    def check_post(self, title, date):
        assert_that(self.browser.find_element(*self.article_title).text).is_equal_to(title)
        assert_that(self.browser.find_element(*self.article_date).text).is_equal_to(date)

    def check_visibility(self, img):
        if self.browser.find_element(By.XPATH, img).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Post Image is not showing")

    def check_widget_post(self, post, date, img):
        cursor = ActionChains(self.browser)
        post_title = self.browser.find_element(By.XPATH, post)

        cursor.move_to_element(post_title).perform()
        self.check_visibility(img)

        p_title = post_title.text
        p_date = self.browser.find_element(By.XPATH, date).text

        post_title.click()
        self.check_post(p_title, p_date)
        self.browser.back()
        time.sleep(1)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1133)")

            # All
            self.browser.find_element(*self.all).click()
            time.sleep(1)
            self.check_widget_post(self.post_1_title, self.post_1_date, self.post_1_img)
            time.sleep(1)
            self.check_widget_post(self.post_2_title, self.post_2_date, self.post_2_img)
            # Elementor
            self.browser.find_element(*self.elementor).click()
            time.sleep(1)
            self.check_widget_post(self.post_1_title, self.post_1_date, self.post_1_img)
            self.browser.find_element(*self.elementor).click()
            time.sleep(1)
            self.check_widget_post(self.post_2_title, self.post_2_date, self.post_2_img)
            # Essential Addons
            self.browser.find_element(*self.essential_addons).click()
            time.sleep(1.5)
            self.check_widget_post(self.post_1_title, self.post_1_date, self.post_1_img)
            self.browser.find_element(*self.essential_addons).click()
            time.sleep(1.5)
            self.check_widget_post(self.post_2_title, self.post_2_date, self.post_2_img)
            # WordPress
            self.browser.find_element(*self.wordpress).click()
            time.sleep(1.5)
            self.check_widget_post(self.post_1_title, self.post_1_date, self.post_1_img)
            self.browser.find_element(*self.wordpress).click()
            time.sleep(1.5)
            self.check_widget_post(self.post_2_title, self.post_2_date, self.post_2_img)

            # Search
            if self.browser.find_element(*self.search_icon).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to("Search Icon not Visible")
            self.browser.find_element(*self.search).send_keys("Essential Addons")
            time.sleep(2)
            title = self.browser.find_element(*self.search_result_title).text
            self.browser.find_element(*self.search_result_title).click()
            assert_that(self.browser.find_element(*self.article_title).text).is_equal_to(title)
            self.browser.back()


