from selenium.webdriver import ActionChains

from utils.config import *


class PostTimeline:
    widget = '//*[@id="post-27"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Post Timeline'
    doc_link = '//*[@id="post-27"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a'
    doc_name = "POST TIMELINE"

    post_1_title = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[1]/div[2]/a/div[3]/h2'
    post_1_des = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[1]/div[2]/a/div[2]/p'
    post_1_date = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[1]/div[2]/a/time'
    post_1_bullet = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[1]/div[1]'

    post_2_title = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[2]/div[2]/a/div[3]/h2'
    post_2_des = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[2]/div[2]/a/div[2]/p'
    post_2_date = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[2]/div[2]/a/time'
    post_2_bullet = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[2]/div[1]'

    post_3_title = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[5]/div[2]/a/div[3]/h2'
    post_3_des = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[5]/div[2]/a/div[2]/p'
    post_3_date = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[5]/div[2]/a/time'
    post_3_bullet = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[5]/div[1]'

    post_4_title = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[6]/div[2]/a/div[3]/h2'
    post_4_des = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[6]/div[2]/a/div[2]/p'
    post_4_date = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[6]/div[2]/a/time'
    post_4_bullet = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[6]/div[1]'

    post_5_title = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[12]/div[2]/a/div[3]/h2'
    post_5_des = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[12]/div[2]/a/div[2]/p'
    post_5_date = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[12]/div[2]/a/time'
    post_5_bullet = f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[12]/div[1]'

    # Article
    article_title = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                               f'/div/div/div/div/div/div[1]/div/h1')
    article_date = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                              f'/div/div/div/div/div/div[2]/div/ul/li[1]/a/span[2]')
    article_author = (By.XPATH, f'//*[@id="content"]/div[1]/div/div/h2')

    load_more_btn = (By.XPATH, f'//*[@id="eael-load-more-btn-3f78c0af"]/span')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(post_timeline)

    def check_post(self, title, date):
        assert_that(self.browser.find_element(*self.article_title).text.upper()).is_equal_to(title)
        assert_that(self.browser.find_element(*self.article_date).text).is_equal_to(date)

    def check_visibility(self, des, bullet):
        if self.browser.find_element(By.XPATH, des).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Post description is not showing")

        if self.browser.find_element(By.XPATH, bullet).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Post bullet is not showing")

    def check_widget_post(self, post, date, des, bullet):
        cursor = ActionChains(self.browser)
        post_title = self.browser.find_element(By.XPATH, post)

        cursor.move_to_element(post_title).perform()
        self.check_visibility(des, bullet)

        p_title = post_title.text
        p_date = ""
        if self.browser.find_element(By.XPATH, date).is_displayed():
            p_date = self.browser.find_element(By.XPATH, date).text
        else:
            assert_that(display).is_equal_to("Post date not showing")

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

            self.browser.execute_script("window.scrollTo(0, 989)")

            cursor = ActionChains(self.browser)

            # post_1 = self.browser.find_element(*self.post_1_title)
            # post_2 = self.browser.find_element(*self.post_2_title)
            # post_3 = self.browser.find_element(*self.post_3_title)
            # post_4 = self.browser.find_element(*self.post_4_title)

            self.check_widget_post(self.post_1_title, self.post_1_date, self.post_1_des, self.post_1_bullet)
            self.check_widget_post(self.post_2_title, self.post_2_date, self.post_2_des, self.post_2_bullet)
            self.check_widget_post(self.post_3_title, self.post_3_date, self.post_3_des, self.post_3_bullet)
            self.check_widget_post(self.post_4_title, self.post_4_date, self.post_4_des, self.post_4_bullet)
            self.browser.find_element(*self.load_more_btn).click()
            time.sleep(1)
            self.check_widget_post(self.post_5_title, self.post_5_date, self.post_5_des, self.post_5_bullet)



