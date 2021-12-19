from selenium.webdriver import ActionChains

from utils.config import *


class PostBlock:
    widget = '//*[@id="post-1347"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Post Block'
    doc_link = '//*[@id="post-1347"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a'
    doc_name = "POST BLOCK"
    # Post 1
    post_1_media = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[1]')
    post_1_overlay_icon = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[1]/div[1]/i')
    post_1_title = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[2]/header/h2/a')
    post_1_des = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[2]/div/div/p')
    post_1_author = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[3]/div[2]/div[1]/a')
    post_1_date = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[1]/div/div/div[3]/div[2]/div[2]/time')
    # Post 2
    post_2_media = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[1]')
    post_2_overlay_icon = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[1]/div[1]/i')
    post_2_title = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[2]/header/h2/a')
    post_2_des = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[2]/div/div/p')
    post_2_author = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[3]/div[2]/div[1]/a')
    post_2_date = (By.XPATH, f'//*[@id="eael-post-block-4c6c0c0c"]/div/article[5]/div/div/div[3]/div[2]/div[2]/time')
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

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1150)")

            cursor = ActionChains(self.browser)
            post_media_1 = self.browser.find_element(*self.post_1_media)
            post_media_2 = self.browser.find_element(*self.post_2_media)

            cursor.move_to_element(post_media_1).perform()
            time.sleep(.5)
            if self.browser.find_element(*self.post_1_overlay_icon).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to(0)

            cursor.move_to_element(post_media_2).perform()
            time.sleep(.5)
            if self.browser.find_element(*self.post_1_des).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to(0)

            title_1 = self.browser.find_element(*self.post_1_title).text
            author_1 = self.browser.find_element(*self.post_1_author).text
            date_1 = self.browser.find_element(*self.post_1_date).text

            self.browser.find_element(*self.post_1_title).click()
            self.check_post(title_1, date_1)
            self.browser.back()
            time.sleep(1)
            self.browser.find_element(*self.post_1_author).click()
            self.check_author(author_1)
            self.browser.back()
            time.sleep(1)

            self.browser.execute_script("window.scrollTo(0, 1150)")
            time.sleep(.5)

            title_2 = self.browser.find_element(*self.post_2_title).text
            author_2 = self.browser.find_element(*self.post_2_author).text
            date_2 = self.browser.find_element(*self.post_2_date).text

            if self.browser.find_element(*self.post_2_des).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to(0)
            self.browser.find_element(*self.post_2_title).click()
            self.check_post(title_2, date_2)
            self.browser.back()
            time.sleep(1)
            self.browser.find_element(*self.post_2_author).click()
            self.check_author(author_2)
            self.browser.back()
            time.sleep(1)
