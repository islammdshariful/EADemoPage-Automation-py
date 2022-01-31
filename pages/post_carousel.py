from utils.config import *


class PostCarousel(Helper):
    widget = '//*[@id="post-2944"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Post Carousel'
    doc_link = '//*[@id="post-2944"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "POST CAROUSEL"

    dot_1 = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[3]/span[1]'
    dot_2 = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[3]/span[2]'
    dot_3 = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[3]/span[3]'
    dot_4 = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[3]/span[4]'

    post_1_title = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[4]/article/div/div/div[2]/header/h2/a'
    post_1_author = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[4]/article/div/div/div[4]/div[2]/div[1]/a'
    post_1_date = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[4]/article/div/div/div[4]/div[2]/div[2]/time'
    post_1_img = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[4]/article/div/div/div[1]/div[1]/a'

    post_2_title = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[5]/article/div/div/div[2]/header/h2/a'
    post_2_author = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[5]/article/div/div/div[4]/div[2]/div[1]/a'
    post_2_date = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[5]/article/div/div/div[4]/div[2]/div[2]/time'
    post_2_img = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[5]/article/div/div/div[1]/div[1]/a'

    post_3_title = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[6]/article/div/div/div[2]/header/h2/a'
    post_3_author = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[6]/article/div/div/div[4]/div[2]/div[1]/a'
    post_3_date = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[6]/article/div/div/div[4]/div[2]/div[2]/time'
    post_3_img = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[6]/article/div/div/div[1]/div[1]/a'

    post_4_title = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[7]/article/div/div/div[2]/header/h2/a'
    post_4_author = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[7]/article/div/div/div[4]/div[2]/div[1]/a'
    post_4_date = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[7]/article/div/div/div[4]/div[2]/div[2]/time'
    post_4_img = f'//*[@id="eael-post-grid-3a6ac8e4"]/div[1]/div/div[7]/article/div/div/div[1]/div[1]/a'

    # Article
    article_title = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                               f'/div/div/div/div/div/div[1]/div/h1')
    article_date = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                              f'/div/div/div/div/div/div[2]/div/ul/li[1]/a/span[2]')
    article_author = (By.XPATH, f'//*[@id="content"]/div[1]/div/div/h2')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.post_carousel)

    def check_post(self, title, date):
        assert_that(self.browser.find_element(*self.article_title).text).is_equal_to(title)
        assert_that(self.browser.find_element(*self.article_date).text).is_equal_to(date)

    def check_author(self, author):
        assert_that(self.browser.find_element(*self.article_author).text).is_equal_to(author)

    def check_widget_post(self, post, author, date, img, dot):
        p_title = self.browser.find_element(By.XPATH, post).text
        p_author = self.browser.find_element(By.XPATH, author).text
        p_date = self.browser.find_element(By.XPATH, date).text

        self.browser.find_element(By.XPATH, post).click()
        self.check_post(p_title, p_date)
        self.browser.back()
        time.sleep(1)
        self.browser.find_element(By.XPATH, self.dot_3).click()
        self.browser.find_element(By.XPATH, dot).click()
        time.sleep(.5)
        self.browser.find_element(By.XPATH, author).click()
        self.check_author(p_author)
        self.browser.back()
        time.sleep(1)
        self.browser.execute_script("window.scrollTo(0, 957)")
        time.sleep(1)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 957)")
            time.sleep(1)
            self.browser.find_element(By.XPATH, self.dot_3).click()
            time.sleep(.5)
            self.browser.find_element(By.XPATH, self.dot_1).click()
            time.sleep(.5)
            self.check_widget_post(self.post_1_title, self.post_1_author, self.post_1_date,
                                   self.post_1_img, self.dot_1)

            self.browser.find_element(By.XPATH, self.dot_2).click()
            time.sleep(.5)
            self.browser.find_element(By.XPATH, self.dot_3).click()
            time.sleep(.5)

            self.browser.find_element(By.XPATH, self.dot_4).click()
            time.sleep(.5)
            self.check_widget_post(self.post_4_title, self.post_4_author, self.post_4_date,
                                   self.post_4_img, self.dot_4)