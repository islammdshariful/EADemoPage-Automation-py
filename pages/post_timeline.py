from pages.basepage import BasePage
from utils.config import *


class PostTimeline(BasePage, Helper):
    widget = '//*[@id="post-27"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Post Timeline'
    doc_link = '//*[@id="post-27"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a'
    doc_name = "POST TIMELINE"

    post_1_title = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[1]/div[2]/a/div[3]/h2')
    post_1_des = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[1]/div[2]/a/div[2]/p')
    post_1_date = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[1]/div[2]/a/time')
    post_1_bullet = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[1]/div[1]')

    post_2_title = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[2]/div[2]/a/div[3]/h2')
    post_2_des = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[2]/div[2]/a/div[2]/p')
    post_2_date = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[2]/div[2]/a/time')
    post_2_bullet = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[2]/div[1]')

    post_3_title = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[5]/div[2]/a/div[3]/h2')
    post_3_des = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[5]/div[2]/a/div[2]/p')
    post_3_date = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[5]/div[2]/a/time')
    post_3_bullet = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[5]/div[1]')

    post_4_title = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[6]/div[2]/a/div[3]/h2')
    post_4_des = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[6]/div[2]/a/div[2]/p')
    post_4_date = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[6]/div[2]/a/time')
    post_4_bullet = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[6]/div[1]')

    post_5_title = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[12]/div[2]/a/div[3]/h2')
    post_5_des = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[12]/div[2]/a/div[2]/p')
    post_5_date = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[12]/div[2]/a/time')
    post_5_bullet = (By.XPATH, f'//*[@id="eael-post-timeline-3f78c0af"]/div/article[12]/div[1]')

    # Article
    article_title = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                               f'/div/div/div/div/div/div[1]/div/h1')
    article_date = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                              f'/div/div/div/div/div/div[2]/div/ul/li[1]/a/span[2]')
    article_author = (By.XPATH, f'//*[@id="content"]/div[1]/div/div/h2')

    load_more_btn = (By.XPATH, f'//*[@id="eael-load-more-btn-3f78c0af"]/span')

    def __init__(self, browser):
        super().__init__(browser)

    def check_post(self, title, date):
        assert_that(self.browser.find_element(*self.article_title).text.upper()).is_equal_to(title)
        assert_that(self.browser.find_element(*self.article_date).text).is_equal_to(date)

    def check_visibility_of_post(self, des, bullet):
        self.is_visible(des, "Post description is not visible.")
        self.is_visible(bullet, "Post bullet is not visible.")

    def check_widget_post(self, post, date, des, bullet):
        self.move_cursor_to(post)
        """Match post description"""
        self.is_visible(des, "Post description is not visible.")
        self.is_visible(bullet, "Post bullet is not visible.")
        post_title = self.get_element_text(post)
        published_date = self.get_element_text(date)
        """Match post publish date"""
        self.is_visible(date, "Post date is not visible.")
        self.do_click(post)
        """Match post meta"""
        assert_that(self.get_element_text(self.article_title).upper()).is_equal_to(post_title)
        self.check_text_matches_with(self.article_date, published_date)
        self.go_back()

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.post_timeline)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(989)
                self.check_widget_post(self.post_1_title, self.post_1_date, self.post_1_des, self.post_1_bullet)
                self.check_widget_post(self.post_2_title, self.post_2_date, self.post_2_des, self.post_2_bullet)
                self.scroll_to(1679)
                self.check_widget_post(self.post_3_title, self.post_3_date, self.post_3_des, self.post_3_bullet)
                self.check_widget_post(self.post_4_title, self.post_4_date, self.post_4_des, self.post_4_bullet)
                self.do_click(self.load_more_btn)
                self.scroll_to(2813)
                self.check_widget_post(self.post_5_title, self.post_5_date, self.post_5_des, self.post_5_bullet)
