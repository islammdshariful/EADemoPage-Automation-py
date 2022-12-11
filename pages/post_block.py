from pages.basepage import BasePage
from utils.config import *


class PostBlock(BasePage, Helper):
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

    scroll = (By.XPATH, f"//div[@class='elementor-element elementor-element-1a7f19a0 elementor-widget "
                        f"elementor-widget-text-editor']")

    def __init__(self, browser):
        super().__init__(browser)

    def check_widget_post(self, post, author, des, date, media, icon):
        """Check post description"""
        self.is_visible(des, "Description is not visible.")
        self.move_cursor_to(media)
        self.is_visible(icon, "Icon is not visible.")
        post_title = self.get_element_text(post)
        author_name = self.get_element_text(author)
        published_date = self.get_element_text(date)
        self.do_click(post)
        """Match post meta"""""
        self.check_text_matches_with(self.article_title, post_title)
        self.check_text_matches_with(self.article_date, published_date)
        self.go_back()
        self.do_click(author)
        """Match author name"""
        self.check_text_matches_with(self.article_author, author_name)
        self.go_back()

        self.scroll_to(1150)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.post_block)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to_element(self.scroll)

                self.check_widget_post(self.post_1_title, self.post_1_author, self.post_1_des,
                                       self.post_1_date, self.post_1_media, self.post_1_overlay_icon)
                self.check_widget_post(self.post_2_title, self.post_2_author, self.post_1_des,
                                       self.post_2_date, self.post_2_media, self.post_2_overlay_icon)

