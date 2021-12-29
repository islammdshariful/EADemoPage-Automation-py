from selenium.webdriver import ActionChains

from utils.config import *


class TwitterFeedCarousel:
    widget = '//*[@id="post-266500"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Twitter Feed Carousel'
    doc_link = '//*[@id="post-266500"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "TWITTER FEED CAROUSEL"

    dot_1 = (By.XPATH, f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[2]/'
                       f'span[1]')
    dot_2 = (By.XPATH, f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[2]/'
                         f'span[2]')
    dot_3 = (By.XPATH, f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[2]/'
                       f'span[3]')
    dot_4 = (By.XPATH, f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[2]/'
                       f'span[4]')
    dot_5 = (By.XPATH, f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[2]/'
                       f'span[5]')
    dot_6 = (By.XPATH, f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[2]/'
                       f'span[6]')
    dot_7 = (By.XPATH, f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[2]/'
                       f'span[7]')
    dot_8 = (By.XPATH, f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[2]/'
                       f'span[8]')

    img_1 = f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[1]' \
                     f'/div[1]/div/div[1]/a[1]/img'
    icon_1 = f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[1]' \
                      f'/div[1]/div/div[1]/a[2]/i'
    author_1 = f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[1]' \
                          f'/div[1]/div/div[1]/a[2]/span'
    content_1 = f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[1]' \
                         f'/div[1]/div/div[2]/p'
    readmore_1 = f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[1]' \
                          f'/div[1]/div/div[2]/a'

    img_2 = f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[1]' \
                       f'/div[10]/div/div[1]/a[1]/img'
    icon_2 = f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[1]' \
                        f'/div[10]/div/div[1]/a[2]/i'
    author_2 = f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[1]' \
                          f'/div[10]/div/div[1]/a[2]/span'
    content_2 = f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[1]' \
                           f'/div[10]/div/div[2]/p'
    readmore_2 = f'//*[@id="post-266500"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[1]' \
                            f'/div[10]/div/div[2]/a'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(twitter_feed_carousel)

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

            self.browser.execute_script("window.scrollTo(0, 904)")
            self.browser.find_element(*self.dot_3).click()
            time.sleep(.5)
            self.browser.find_element(*self.dot_4).click()
            time.sleep(.5)
            self.browser.find_element(*self.dot_5).click()
            time.sleep(.5)
            self.browser.find_element(*self.dot_6).click()
            time.sleep(.5)
            self.browser.find_element(*self.dot_1).click()
            self.check_post(self.img_1, self.icon_1, self.author_1, self.content_1, self.readmore_1)
            self.browser.find_element(*self.dot_2).click()
            time.sleep(.5)
            self.browser.find_element(*self.dot_7).click()
            time.sleep(.5)
            self.browser.find_element(*self.dot_8).click()
            self.browser.find_element(*self.dot_8).click()
            self.check_post(self.img_2, self.icon_2, self.author_2, self.content_2, self.readmore_2)
