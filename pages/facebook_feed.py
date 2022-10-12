from utils.config import *


class FacebookFeed(BasePage, Helper):
    widget = '//*[@id="post-1840"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Facebook Feed'
    doc_link = '//*[@id="post-1840"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "FACEBOOK FEED"

    avatar_1 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/header/div/a[1]/img')
    name_1 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/header/div/a[2]/p')
    date_1 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/header/a')
    des_1 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/div[1]/p')
    img_1 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/div[2]/a/img')
    des_url_1 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/div[2]/div/p[1]')
    des_title_1 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/div[2]/div/h2')
    des_bottom_content_1 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/div[2]/div/p[2]')
    like_icon_1 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/footer/div/span[1]/i')
    like_count_1 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/footer/div/span[1]/text()')
    comment_icon_1 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/footer/div/span[2]/i')
    comment_count_1 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[1]/div/footer/div/span[2]/text()')

    avatar_2 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/header/div/a[1]/img')
    name_2 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/header/div/a[2]/p')
    date_2 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/header/a')
    des_2 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/div[1]/p')
    img_2 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/div[2]/a/img')
    des_url_2 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/div[2]/div/p[1]')
    des_title_2 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/div[2]/div/h2')
    des_bottom_content_2 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/div[2]/div/p[2]')
    like_icon_2 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/footer/div/span[1]/i')
    like_count_2 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/footer/div/span[1]/text()')
    comment_icon_2 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/footer/div/span[2]/i')
    comment_count_2 = (By.XPATH, f'//*[@id="eael-facebook-feed-1ba7c6e5"]/div[3]/div/footer/div/span[2]/text()')

    def __init__(self, browser):
        super().__init__(browser)

    def check_post(self, avatar, name, date, des, img, url, title, des_bottom, like, comment):
        self.is_visible(avatar, "Avatar is not visible")
        self.is_visible(date, "Date is not visible")

        self.check_text_matches_with(name, "WPDeveloper")
        self.is_visible(des, "Description is not visible")
        self.is_visible(img, "Image is not visible")
        # self.check_visibility(url, "URL is not visible")
        # self.check_visibility(title, "Title is not visible")
        # self.check_visibility(des_bottom, "Bottom is not visible")
        self.is_visible(like, "Like is not visible")
        self.is_visible(comment, "Comment is not visible")

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.facebook_feed)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(982)

                self.check_post(self.avatar_1, self.name_1, self.date_1, self.des_1, self.img_1, self.des_url_1,
                                self.des_title_1, self.des_bottom_content_1, self.like_icon_1, self.comment_icon_1)
                self.check_post(self.avatar_2, self.name_2, self.date_2, self.des_2, self.img_2, self.des_url_2,
                                self.des_title_2, self.des_bottom_content_2, self.like_icon_2, self.comment_icon_2)
