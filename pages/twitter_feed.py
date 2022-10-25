from utils.config import *


class TwitterFeed(BasePage, Helper):
    widget = '//*[@id="post-2899"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Twitter Feed'
    doc_link = '//*[@id="post-2899"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "TWITTER FEED"

    img_1 = (By.XPATH, f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                       f'/div[1]/div[1]/div/div[1]/a[1]/img')
    icon_1 = (By.XPATH, f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                        f'/div[1]/div[1]/div/div[1]/a[2]/i')
    author_1 = (By.XPATH, f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                          f'/div[1]/div[1]/div/div[1]/a[2]/span')
    content_1 = (By.XPATH, f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/'
                           f'div[1]/div[1]/div/div[2]/p')
    read_more_1 = (By.XPATH, f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div'
                             f'/div[1]/div[1]/div/div[2]/a')

    img_2 = (By.XPATH, f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[1]'
                       f'/div[3]/div/div[1]/a[1]/img')
    icon_2 = (By.XPATH, f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[1]'
                        f'/div[3]/div/div[1]/a[2]/i')
    author_2 = (By.XPATH, f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[1]'
                          f'/div[3]/div/div[1]/a[2]/span')
    content_2 = (By.XPATH, f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[1]'
                           f'/div[3]/div/div[2]/p')
    read_more_2 = (By.XPATH, f'//*[@id="post-2899"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div[1]'
                             f'/div[3]/div/div[2]/a')

    def __init__(self, browser):
        super().__init__(browser)

    def check_post(self, img, icon, author, content, read_more):
        # self.is_visible(img, "Image is not visible")
        self.is_visible(icon, "Icon is not visible")

        self.check_text_matches_with(author, "WPDeveloper")

        self.is_visible(content, "Content is not visible")
        self.check_text_matches_with(read_more, "Read More")

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.twitter_feed)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1004)

                self.check_post(self.img_1, self.icon_1, self.author_1, self.content_1, self.read_more_1)
                self.check_post(self.img_2, self.icon_2, self.author_2, self.content_2, self.read_more_2)
