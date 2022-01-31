from utils.config import *


class TwitterFeed(Helper):
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
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.twitter_feed)

    def check_post(self, img, icon, author, content, read_more):
        time.sleep(.5)
        self.check_visibility(img, "Image is not visible")
        self.check_visibility(icon, "Icon is not visible")

        assert_that(self.browser.find_element(By.XPATH, author).text).is_equal_to("WPDeveloper")

        self.check_visibility(content, "Content is not visible")
        assert_that(self.browser.find_element(By.XPATH, read_more).text).is_equal_to("Read More")

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1004)")
            time.sleep(1)

            self.check_post(self.img_1, self.icon_1, self.author_1, self.content_1, self.read_more_1)
            self.check_post(self.img_2, self.icon_2, self.author_2, self.content_2, self.read_more_2)