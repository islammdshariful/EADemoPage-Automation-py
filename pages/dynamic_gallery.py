from utils.config import *


class DynamicGallery(BasePage, Helper):
    widget = '//*[@id="post-260882"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Dynamic Gallery'
    doc_link = '//*[@id="post-260882"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "DYNAMIC FILTERABLE GALLERY"

    all = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[1]/ul/li[1]')
    elementor = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[1]/ul/li[2]')
    wordpress = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[1]/ul/li[3]')
    templates = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[1]/ul/li[4]')

    all_post_1_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[2]/h2/a')
    all_post_1_des = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[2]/p')
    all_post_1_img = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[1]/img')

    all_post_2_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[3]/div[1]/div[2]/h2/a')
    all_post_2_des = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[3]/div[1]/div[2]/p')
    all_post_2_img = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[3]/div[1]/div[1]/img')

    all_post_3_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[6]/div/div[2]/h2/a')
    all_post_3_des = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[6]/div[1]/div[2]/p')
    all_post_3_img = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[6]/div[1]/div[1]/img')

    all_post_4_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[12]/div/div[2]/h2/a')
    all_post_4_des = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[12]/div[1]/div[2]/p')
    all_post_4_img = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[12]/div[1]/div[1]/img')

    ele_post_1_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[2]/h2/a')
    ele_post_1_des = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[2]/p')
    ele_post_1_img = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[1]/img')

    ele_post_2_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[3]/div[1]/div[2]/h2/a')
    ele_post_2_des = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[3]/div[1]/div[2]/p')
    ele_post_2_img = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[3]/div[1]/div[1]/img')

    wp_post_1_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[2]/h2/a')
    wp_post_1_des = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[2]/p')
    wp_post_1_img = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[1]/img')

    wp_post_2_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[4]/div[1]/div[2]/h2/a')
    wp_post_2_des = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[4]/div[1]/div[2]/p')
    wp_post_2_img = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[4]/div[1]/div[1]/img')

    tm_post_1_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[2]/div[1]/div[2]/h2/a')
    tm_post_1_des = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[2]/div[1]/div[2]/p')
    tm_post_1_img = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[2]/div[1]/div[1]/img')

    tm_post_2_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[8]/div/div[2]/h2/a')
    tm_post_2_des = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[8]/div[1]/div[2]/p')
    tm_post_2_img = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[8]/div[1]/div[1]/img')

    load_more_btn = (By.ID, f'eael-load-more-btn-3990f5c')

    # Article
    article_title = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                               f'/div/div/div/div/div/div[1]/div/h1')
    article_date = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                              f'/div/div/div/div/div/div[2]/div/ul/li[1]/a/span[2]')

    def __init__(self, browser):
        super().__init__(browser)

    def check_widget_post(self, post, des, img):
        self.move_cursor_to(post)
        self.is_visible(des, "Gallery Description is not visible")
        self.is_visible(img, "Gallery Image is not visible")

        post_title = self.get_element_text(post)
        self.do_click(post)
        assert_that(self.browser.find_element(*self.article_title).text).is_equal_to(post_title)
        self.go_back()

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.dynamic_gallery)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(905)
                # All
                self.do_click(self.all)
                self.check_widget_post(self.all_post_1_title, self.all_post_1_des, self.all_post_1_img)
                self.scroll_to(1439)
                self.check_widget_post(self.all_post_3_title, self.all_post_3_des, self.all_post_3_img)
                self.scroll_to(1450)
                self.do_click(self.load_more_btn)
                self.scroll_to(2018)
                self.check_widget_post(self.all_post_4_title, self.all_post_4_des, self.all_post_4_img)
                # Elementor
                self.scroll_to(905)
                self.do_click(self.elementor)
                self.scroll_to(1439)
                self.do_click(self.load_more_btn)
                # WordPress
                self.scroll_to(905)
                self.do_click(self.wordpress)
                self.scroll_to(1439)
                self.do_click(self.load_more_btn)
                # Templates
                self.scroll_to(905)
                self.do_click(self.templates)
                self.scroll_to(1439)
                self.do_click(self.load_more_btn)
