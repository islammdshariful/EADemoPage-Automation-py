from selenium.webdriver import ActionChains

from utils.config import *


class FacebookFeed:
    widget = '//*[@id="post-1840"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Facebook Feed'
    doc_link = '//*[@id="post-1840"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "FACEBOOK FEED"

    avatar_1 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/header/div/a[1]/img'
    name_1 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/header/div/a[2]/p'
    date_1 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/header/a'
    des_1 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/div[1]/p'
    img_1 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/div[2]/a/img'
    des_url_1 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/div[2]/div/p[1]'
    des_title_1 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/div[2]/div/h2'
    des_bottom_content_1 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/div[2]/div/p[2]'
    like_icon_1 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/footer/div/span[1]/i'
    like_count_1 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/footer/div/span[1]/text()'
    comment_icon_1 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/footer/div/span[2]/i'
    comment_count_1 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/footer/div/span[2]/text()'

    avatar_2 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/header/div/a[1]/img'
    name_2 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/header/div/a[2]/p'
    date_2 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/header/a'
    des_2 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/div[1]/p'
    img_2 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/div[2]/a/img'
    des_url_2 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/div[2]/div/p[1]'
    des_title_2 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/div[2]/div/h2'
    des_bottom_content_2 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/div[2]/div/p[2]'
    like_icon_2 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/footer/div/span[1]/i'
    like_count_2 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/footer/div/span[1]/text()'
    comment_icon_2 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/footer/div/span[2]/i'
    comment_count_2 = f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/footer/div/span[2]/text()'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(facebook_feed)

    def check_post(self, avatar, name, date, des, img, url, title, des_bottom, like, l_count, comment, c_count):
        if self.browser.find_element(By.XPATH, avatar).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Avatar is not visible")

        assert_that(self.browser.find_element(By.XPATH, name).text).is_equal_to("WPDeveloper")

        if self.browser.find_element(By.XPATH, date).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Date is not visible")

        if self.browser.find_element(By.XPATH, des).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Description is not visible")

        if self.browser.find_element(By.XPATH, img).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Image is not visible")

        if self.browser.find_element(By.XPATH, url).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("URL is not visible")

        if self.browser.find_element(By.XPATH, title).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Title is not visible")

        if self.browser.find_element(By.XPATH, des_bottom).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Bottom Content is not visible")

        if self.browser.find_element(By.XPATH, like).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Like is not visible")

        # if self.browser.find_element(By.XPATH, l_count).is_displayed():
        #     assert_that(display).is_equal_to(1)
        # else:
        #     assert_that(display).is_equal_to("Like Count is not visible")

        if self.browser.find_element(By.XPATH, comment).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Comment is not visible")

        # if self.browser.find_element(By.XPATH, c_count).is_displayed():
        #     assert_that(display).is_equal_to(1)
        # else:
        #     assert_that(display).is_equal_to("Comment Count is not visible")

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 982)")
            self.check_post(self.avatar_1, self.name_1, self.date_1, self.des_1, self.img_1, self.des_url_1,
                            self.des_title_1, self.des_bottom_content_1, self.like_icon_1, self.like_count_1,
                            self.comment_icon_1, self.comment_count_1)
            time.sleep(.5)
            self.check_post(self.avatar_2, self.name_2, self.date_2, self.des_2, self.img_2, self.des_url_2,
                            self.des_title_2, self.des_bottom_content_2, self.like_icon_2, self.like_count_2,
                            self.comment_icon_2, self.comment_count_2)