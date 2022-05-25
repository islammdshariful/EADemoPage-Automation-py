from selenium.webdriver import ActionChains, Keys

from utils.config import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PostGrid(Helper):
    widget = '//*[@id="post-1345"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Post Grid'
    doc_link = '//*[@id="post-1345"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "POST GRID"

    # Post 1
    post_1_media = f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[1]/div/div/div[1]/div[2]'
    post_1_overlay_icon = f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[1]/div/div/div[1]/div[1]/i'
    post_1_title = f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[1]/div/div/div[2]/header/h2/a'
    post_1_author = f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[1]/div/div/div[2]/div/span[1]/a'
    post_1_date = f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[1]/div/div/div[2]/div/span[2]/time'
    # Post 2
    post_2_media = f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[6]/div/div/div[1]/div[2]'
    post_2_overlay_icon = f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[6]/div/div/div[1]/div[1]/i'
    post_2_title = f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[6]/div/div/div[2]/header/h2/a'
    post_2_author = f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[6]/div/div/div[2]/div/span[1]/a'
    post_2_date = f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[6]/div/div/div[2]/div/span[2]/time'
    # Post 3
    post_3_media = f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[11]/div/div/div[2]/header/h2/a'
    post_3_overlay_icon = f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[11]/div/div/div[1]/div[1]/i'
    post_3_title = f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[11]/div/div/div[2]/header/h2/a'
    post_3_author = f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[11]/div/div/div[2]/div/span[1]/a'
    post_3_date = f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[11]/div/div/div[2]/div/span[2]/time'

    load_more_btn = (By.ID, f'eael-load-more-btn-4d645e5c')

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
        self.browser.get(self.post_grid)

    def check_post(self, title, date):
        assert_that(self.browser.find_element(*self.article_title).text).is_equal_to(title)
        assert_that(self.browser.find_element(*self.article_date).text).is_equal_to(date)

    def check_author(self, author):
        assert_that(self.browser.find_element(*self.article_author).text).is_equal_to(author)

    def check_visibility_of_post(self, media, icon):
        cursor = ActionChains(self.browser)
        post_media_1 = self.browser.find_element(By.XPATH, media)
        cursor.move_to_element(post_media_1).perform()
        time.sleep(1)

        self.check_visibility(icon, "Icon is not visible.")

    def check_widget_post(self, post, author, date, media, icon):
        self.check_visibility_of_post(media, icon)
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

        self.browser.execute_script("window.scrollTo(0, 1037)")
        time.sleep(.5)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1037)")
                time.sleep(1)

                self.check_widget_post(self.post_1_title, self.post_1_author, self.post_1_date, self.post_1_media,
                                       self.post_1_overlay_icon)
                self.check_widget_post(self.post_2_title, self.post_2_author, self.post_2_date, self.post_2_media,
                                       self.post_2_overlay_icon)
                self.browser.find_element(*self.load_more_btn).click()

                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.post_3_title)))

                self.browser.execute_script("window.scrollTo(0, 2142)")
                time.sleep(1)

                # self.check_visibility_of_post(self.post_3_media, self.post_3_overlay_icon)
                p_title = self.browser.find_element(By.XPATH, self.post_3_title).text
                p_date = self.browser.find_element(By.XPATH, self.post_3_date).text

                self.browser.find_element(By.XPATH, self.post_3_title).click()
                self.check_post(p_title, p_date)
                self.browser.back()
                time.sleep(1)
