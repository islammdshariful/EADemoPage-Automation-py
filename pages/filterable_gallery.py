from utils.config import *


class FilterableGallery(BasePage, Helper):
    widget = '//*[@id="post-1925"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Filterable Gallery'
    doc_link = '//*[@id="post-1925"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "FILTERABLE GALLERY"

    all = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[1]/ul/li[1]')
    news = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[1]/ul/li[2]')
    updates = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[1]/ul/li[3]')
    events = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[1]/ul/li[4]')
    masonry = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[1]/ul/li[5]')

    all_control_text = 'ALL'
    news_control_text = 'NEWS'
    updates_control_text = 'UPDATES'
    events_control_text = 'EVENTS'
    masonry_control_text = 'MASONRY'

    prev_btn = (By.XPATH, f"//button[@title='Previous (Left arrow key)']")
    next_btn = (By.XPATH, f"//button[@title='Next (Right arrow key)']")
    cross_btn = (By.XPATH, f"//button[normalize-space()='×']")

    gallery_title_text = "HIGHLY DELIGHTED PRESENT"

    all_gallery_1 = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[1]')
    all_gallery_1_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[1]/div/div[2]/'
                                     f'div[2]/h5')
    all_gallery_1_icon = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[1]/div/div[2]/'
                                    f'div[2]/div/a/span/i')

    gallery_2 = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[2]')
    gallery_2_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[2]/div/div[2]/div[2]/h5')
    gallery_2_icon = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[2]/div/div[2]/div[2]/'
                                f'div/a/span/i')

    all_gallery_3 = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[8]')
    all_gallery_3_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[8]/div/div[2]/'
                                     f'div[2]/h5')
    all_gallery_3_icon = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[8]/div/div[2]/'
                                    f'div[2]/div/a/span/i')

    news_gallery_1 = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[1]')
    news_gallery_1_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[1]/div/div[2]/'
                                      f'div[2]/h5')
    news_gallery_1_icon = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[1]/div/div[2]/'
                                     f'div[2]/div/a/span/i')

    news_gallery_2 = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[5]')
    news_gallery_2_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[5]/div/div[2]/'
                                      f'div[2]/h5')
    news_gallery_2_icon = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[5]/div/div[2]/'
                                     f'div[2]/div/a/span/i')

    updates_gallery_1 = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[2]')
    updates_gallery_1_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[2]/div/div[2]/'
                                         f'div[2]/h5')
    updates_gallery_1_icon = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[2]/div/div[2]/'
                                        f'div[2]/div/a/span/i')

    updates_gallery_2 = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[6]')
    updates_gallery_2_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[6]/div/div[2]/'
                                         f'div[2]/h5')
    updates_gallery_2_icon = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[6]/div/div[2]/'
                                        f'div[2]/div/a/span/i')

    events_gallery_1 = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[3]')
    events_gallery_1_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[3]/div/div[2]/'
                                        f'div[2]/h5')
    events_gallery_1_icon = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[3]/div/div[2]/'
                                       f'div[2]/div/a/span/i')

    events_gallery_2 = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[7]')
    events_gallery_2_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[7]/div/div[2]/'
                                        f'div[2]/h5')
    events_gallery_2_icon = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[7]/div/div[2]/'
                                       f'div[2]/div/a/span/i')

    masonry_gallery_1 = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[4]')
    masonry_gallery_1_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[4]/div/div[2]/'
                                         f'div[2]/h5')
    masonry_gallery_1_icon = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[4]/div/div[2]/'
                                        f'div[2]/div/a/span/i')

    masonry_gallery_2 = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[8]')
    masonry_gallery_2_title = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[8]/div/div[2]/'
                                         f'div[2]/h5')
    masonry_gallery_2_icon = (By.XPATH, f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[8]/div/div[2]/'
                                        f'div[2]/div/a/span/i')

    scroll = (By.CSS_SELECTOR, 'h3.elementor-heading-title')

    def __init__(self, browser):
        super().__init__(browser)

    def open_gallery(self, gallery, title, title_text, icon):
        time.sleep(.5)
        self.move_cursor_to(gallery)
        self.check_text_matches_with(title, title_text)
        self.is_visible(icon, "Icon is not visible.")
        self.do_click(icon)
        self.do_click(self.next_btn)
        self.do_click(self.prev_btn)
        self.do_click(self.cross_btn)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.filterable_gallery)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to_element(self.scroll)
                self.check_text_matches_with(self.all, self.all_control_text)
                self.check_text_matches_with(self.news, self.news_control_text)
                self.check_text_matches_with(self.updates, self.updates_control_text)
                self.check_text_matches_with(self.events, self.events_control_text)
                self.check_text_matches_with(self.masonry, self.masonry_control_text)

                """Filter Gallery: All"""
                self.do_click(self.all)
                self.open_gallery(self.all_gallery_1, self.all_gallery_1_title, self.gallery_title_text,
                                  self.all_gallery_1_icon)

                self.open_gallery(self.all_gallery_3, self.all_gallery_3_title, self.gallery_title_text,
                                  self.all_gallery_3_icon)
                self.scroll_to_element(self.scroll)
                """Filter Gallery: News"""
                self.do_click(self.news)
                self.open_gallery(self.news_gallery_1, self.news_gallery_1_title, self.gallery_title_text,
                                  self.news_gallery_1_icon)
                self.open_gallery(self.news_gallery_2, self.news_gallery_2_title, self.gallery_title_text,
                                  self.news_gallery_2_icon)
                self.scroll_to_element(self.scroll)
                """Filter Gallery: Updates"""
                self.do_click(self.updates)
                self.open_gallery(self.updates_gallery_1, self.updates_gallery_1_title, self.gallery_title_text,
                                  self.updates_gallery_1_icon)
                self.open_gallery(self.updates_gallery_2, self.updates_gallery_2_title, self.gallery_title_text,
                                  self.updates_gallery_2_icon)
                self.scroll_to_element(self.scroll)
                """Filter Gallery: Events"""
                self.do_click(self.events)
                self.open_gallery(self.events_gallery_1, self.events_gallery_1_title, self.gallery_title_text,
                                  self.events_gallery_1_icon)
                self.open_gallery(self.events_gallery_2, self.events_gallery_2_title, self.gallery_title_text,
                                  self.events_gallery_2_icon)
                self.scroll_to_element(self.scroll)
                """Filter Gallery: Masonry"""
                self.do_click(self.masonry)
                self.open_gallery(self.masonry_gallery_1, self.masonry_gallery_1_title, self.gallery_title_text,
                                  self.masonry_gallery_1_icon)
                self.open_gallery(self.masonry_gallery_2, self.masonry_gallery_2_title, self.gallery_title_text,
                                  self.masonry_gallery_2_icon)

