from utils.config import *


class PostGrid(BasePage, Helper):
    widget = '//*[@id="post-1345"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Post Grid'
    doc_link = '//*[@id="post-1345"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "POST GRID"

    # Post 1
    post_1_media = (By.XPATH, f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[1]/div/div/div[1]/div[2]')
    post_1_overlay_icon = (By.XPATH, f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[1]/div/div/div[1]/div[1]/i')
    post_1_title = (By.XPATH, f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[1]/div/div/div[2]/header/h2/a')
    post_1_author = (By.XPATH, f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[1]/div/div/div[2]/div/div[2]/span['
                               f'1]/a')
    post_1_date = (By.XPATH, f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[1]/div/div/div[2]/div/div[2]/span['
                             f'2]/time')
    # Post 2
    post_2_media = (By.XPATH, f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[6]/div/div/div[1]/div[2]')
    post_2_overlay_icon = (By.XPATH, f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[6]/div/div/div[1]/div[1]/i')
    post_2_title = (By.XPATH, f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[6]/div/div/div[2]/header/h2/a')
    post_2_author = (By.XPATH, f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[6]/div/div/div[2]/div/div[2]/span['
                               f'1]/a')
    post_2_date = (By.XPATH, f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[6]/div/div/div[2]/div/div[2]/span['
                             f'2]/time')
    # Post 3
    post_3_media = (By.XPATH, f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[12]/div/div/div[1]/div[2]')
    post_3_overlay_icon = (By.XPATH, f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[12]/div/div/div[1]/div[1]/i')
    post_3_title = (By.XPATH, f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[12]/div/div/div[2]/header/h2/a')
    post_3_author = (By.XPATH, f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[12]/div/div/div[2]/div/div['
                               f'2]/span[1]/a')
    post_3_date = (By.XPATH, f'//*[@id="eael-post-grid-4d645e5c"]/div[1]/article[12]/div/div/div[2]/div/div[2]/span['
                             f'2]/time')

    load_more_btn = (By.ID, f'eael-load-more-btn-4d645e5c')

    # Article
    article_title = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                               f'/div/div/div/div/div/div[1]/div/h1')
    article_date = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                              f'/div/div/div/div/div/div[2]/div/ul/li[1]/a/span[2]')
    article_author = (By.XPATH, f'//*[@id="content"]/div[1]/div/div/h2')

    def __init__(self, browser):
        super().__init__(browser)

    def load(self):
        self.browser.get(self.post_grid)

    def check_widget_post(self, post, author, date, media, icon):
        self.move_cursor_to(media)
        self.is_visible(icon, "Icon is not visible.")
        post_title = self.get_element_text(post)
        published_date = self.get_element_text(date)
        self.do_click(post)
        """Match post meta"""""
        self.check_text_matches_with(self.article_title, post_title)
        self.check_text_matches_with(self.article_date, published_date)
        self.go_back()
        if author is not None:
            author_name = self.get_element_text(author)
            self.do_click(author)
            """Match author name"""
            self.check_text_matches_with(self.article_author, author_name)
            self.go_back()

        self.scroll_to(1037)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.post_grid)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1037)

                self.check_widget_post(self.post_1_title, self.post_1_author, self.post_1_date, self.post_1_media,
                                       self.post_1_overlay_icon)
                self.check_widget_post(self.post_2_title, self.post_2_author, self.post_2_date, self.post_2_media,
                                       self.post_2_overlay_icon)
                self.do_click(self.load_more_btn)

                self.scroll_to(2142)
                self.check_widget_post(post=self.post_3_title, author=None, date=self.post_3_date,
                                       media=self.post_3_media, icon=self.post_3_overlay_icon)
