from selenium.webdriver import ActionChains

from utils.config import *


class TwitterFeed:
    widget = '//*[@id="post-2899"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Twitter Feed'
    doc_link = '//*[@id="post-2899"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "TWITTER FEED"

    img_1 = f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
            f'/div[1]/div/div[1]/a[1]/img'
    icon_1 = f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
             f'/div[1]/div/div[1]/a[2]/i'
    author_1 = f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
               f'/div[1]/div/div[1]/a[2]/span'
    content_1 = f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                f'/div[1]/div/div[2]/p'
    read_more_1 = f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                 f'/div[1]/div/div[2]/a'

    img_2 = f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
            f'/div[3]/div/div[1]/a[1]/img'
    icon_2 = f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
             f'/div[3]/div/div[1]/a[2]/i'
    author_2 = f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
               f'/div[3]/div/div[1]/a[2]/span'
    content_2 = f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                f'/div[3]/div/div[2]/p'
    read_more_2 = f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                 f'/div[3]/div/div[2]/a'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(twitter_feed)

    def check_post(self, img, icon, author, content, read_more):
        time.sleep(.5)
        if self.browser.find_element(By.XPATH, img).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("image is not visible")

        if self.browser.find_element(By.XPATH, icon).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Icon is not visible")

        assert_that(self.browser.find_element(By.XPATH, author).text).is_equal_to("WPDeveloper")

        if self.browser.find_element(By.XPATH, content).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Content is not visible")

        assert_that(self.browser.find_element(By.XPATH, read_more).text).is_equal_to("Read More")

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1004)")

            self.check_post(self.img_1, self.icon_1, self.author_1, self.content_1, self.read_more_1)
            self.check_post(self.img_2, self.icon_2, self.author_2, self.content_2, self.read_more_2)