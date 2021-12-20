from selenium.webdriver import ActionChains

from utils.config import *


class PostBlock:
    widget = '//*[@id="post-1347"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Post Block'
    doc_link = '//*[@id="post-1347"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a'
    doc_name = "POST BLOCK"
    # # Post 1
    # post_1_media = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[1]')
    # post_1_overlay_icon = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[1]/div[1]/i')
    # post_1_title = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[2]/header/h2/a')
    # post_1_des = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[2]/div/div/p')
    # post_1_author = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[3]/div[2]/div[1]/a')
    # post_1_date = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[3]/div[2]/div[2]/time')
    # # Post 2
    # post_2_media = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[1]')
    # post_2_overlay_icon = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[1]/div[1]/i')
    # post_2_title = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[2]/header/h2/a')
    # post_2_des = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[2]/div/div/p')
    # post_2_author = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[3]/div[2]/div[1]/a')
    # post_2_date = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[3]/div[2]/div[2]/time')

    # Post 1
    post_1_media = f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[1]'
    post_1_overlay_icon = f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[1]/div[1]/i'
    post_1_title = f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[2]/header/h2/a'
    post_1_des = f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[2]/div/div/p'
    post_1_author = f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[3]/div[2]/div[1]/a'
    post_1_date = f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[3]/div[2]/div[2]/time'
    # Post 2
    post_2_media = f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[1]'
    post_2_overlay_icon = f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[1]/div[1]/i'
    post_2_title = f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[2]/header/h2/a'
    post_2_des = f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[2]/div/div/p'
    post_2_author = f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[3]/div[2]/div[1]/a'
    post_2_date = f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[3]/div[2]/div[2]/time'

    # Article
    article_title = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                               f'/div/div/div/div/div/div[1]/div/h1')
    article_date = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                              f'/div/div/div/div/div/div[2]/div/ul/li[1]/a/span[2]')
    article_author = (By.XPATH, f'//*[@id="content"]/div[1]/div/div/h2')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(post_block)

    def check_post(self, title, date):
        assert_that(self.browser.find_element(*self.article_title).text).is_equal_to(title)
        assert_that(self.browser.find_element(*self.article_date).text).is_equal_to(date)

    def check_author(self, author):
        assert_that(self.browser.find_element(*self.article_author).text).is_equal_to(author)

    def check_visibility(self, media, icon):
        cursor = ActionChains(self.browser)
        post_media_1 = self.browser.find_element(By.XPATH, media)
        cursor.move_to_element(post_media_1).perform()
        time.sleep(.5)
        if self.browser.find_element(By.XPATH, icon).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to(0)

    def check_widget_post(self, post, author, date, media, icon):
        self.check_visibility(media, icon)
        p_title = self.browser.find_element(By.XPATH, post).text
        p_author = self.browser.find_element(By.XPATH, author).text
        p_date = self.browser.find_element(By.XPATH, date).text

        self.browser.find_element(By.XPATH, post).click()
        self.check_post(p_title, p_date)
        self.browser.back()
        time.sleep(1)
        self.browser.find_element(By.XPATH, author).click()
        self.check_author(p_author)
        self.browser.back()
        time.sleep(1)

        self.browser.execute_script("window.scrollTo(0, 1150)")
        time.sleep(.5)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1150)")

            self.check_widget_post(self.post_1_title, self.post_1_author, self.post_1_date, self.post_1_media,
                                   self.post_1_overlay_icon)
            self.check_widget_post(self.post_2_title, self.post_2_author, self.post_2_date, self.post_2_media,
                                   self.post_2_overlay_icon)

