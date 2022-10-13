from pages.basepage import BasePage
from utils.config import *


class PostList(BasePage, Helper):
    widget = '//*[@id="post-2322"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Smart Post List'
    doc_link = '//*[@id="post-2322"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "SMART POST LIST"

    search = (By.ID, f'search_field')
    search_icon = (By.XPATH, f'//*[@id="post-list-search-form-312f98e8"]/i')
    search_result_title = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div'
                                     f'/div/div/div/div/div/div[1]/div[2]/div/div[1]/h6/a')

    all = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div/div/div/div'
                     f'/div/div[1]/div[1]/a[1]')
    elementor = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div/div/div'
                           f'/div/div/div[1]/div[1]/a[2]')
    essential_addons = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div'
                                  f'/div/div/div/div/div[1]/div[1]/a[3]')
    wordpress = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div/div/div'
                           f'/div/div/div[1]/div[1]/a[4]')

    post_1_title = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div' \
                              f'/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/h2/a')
    post_1_date = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div' \
                             f'/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[1]/span')
    post_1_img = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div/div' \
                            f'/div/div/div/div[2]/div/div[1]/div/div[1]/img')

    post_2_title = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div/div/div' \
                              f'/div/div/div[2]/div/div[6]/div/div[2]/h2/a')
    post_2_date = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div/div/div' \
                             f'/div/div/div[2]/div/div[6]/div/div[2]/div[1]/span')
    post_2_img = (By.XPATH, f'//*[@id="post-2322"]/div/div/div/div/section[2]/div/div/div/div/div' \
                            f'/div/div/div/div[2]/div/div[6]/div/div[1]/img')

    # Article
    article_title = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                               f'/div/div/div/div/div/div[1]/div/h1')
    article_date = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                              f'/div/div/div/div/div/div[2]/div/ul/li[1]/a/span[2]')

    scroll = (By.XPATH, "//div[@class='elementor-element elementor-element-1220b3b1 "
                        "elementor-widget elementor-widget-heading']"
                        "//div[@class='elementor-widget-container']")

    def __init__(self, browser):
        super().__init__(browser)

    def check_widget_post(self, post, date, img):
        self.move_cursor_to(post)
        self.is_visible(img, "Post Image is not visible.")
        post_title = self.get_element_text(post)
        published_date = self.get_element_text(date)
        self.do_click(post)

        """Match post meta"""
        self.check_text_matches_with(self.article_title, post_title)
        self.check_text_matches_with(self.article_date, published_date)
        self.go_back()

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.post_list)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1133)
                # All
                self.do_click(self.all)
                time.sleep(1)
                self.check_widget_post(self.post_1_title, self.post_1_date, self.post_1_img)
                self.check_widget_post(self.post_2_title, self.post_2_date, self.post_2_img)
                # Elementor
                self.scroll_to_element(self.scroll)
                self.do_click(self.elementor)
                time.sleep(1)
                self.check_widget_post(self.post_1_title, self.post_1_date, self.post_1_img)
                self.do_click(self.elementor)
                time.sleep(1)
                self.check_widget_post(self.post_2_title, self.post_2_date, self.post_2_img)
                # Essential Addons
                self.scroll_to_element(self.scroll)
                self.do_click(self.essential_addons)
                time.sleep(1)
                self.check_widget_post(self.post_1_title, self.post_1_date, self.post_1_img)
                self.do_click(self.essential_addons)
                time.sleep(1)
                self.check_widget_post(self.post_2_title, self.post_2_date, self.post_2_img)
                # WordPress
                self.scroll_to_element(self.scroll)
                self.do_click(self.wordpress)
                time.sleep(1)
                self.check_widget_post(self.post_1_title, self.post_1_date, self.post_1_img)
                self.do_click(self.wordpress)
                time.sleep(1)
                self.check_widget_post(self.post_2_title, self.post_2_date, self.post_2_img)

                # Search
                self.reload_page()
                self.scroll_to_element(self.scroll)
                self.is_visible(self.search_icon, "Search Icon not Visible.")
                """Search post"""
                self.do_send_keys(self.search, "Essential Addons")
                time.sleep(4)
                title = self.get_element_text(self.search_result_title)
                self.do_click(self.search_result_title)
                self.check_text_matches_with(self.article_title, title)
                self.go_back()
