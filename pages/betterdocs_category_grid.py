from utils.config import *


class BetterdocsCategoryGrid(BasePage, Helper):
    widget = '//*[@id="post-255888"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'BetterDocs Category Grid'
    doc_link = '//*[@id="post-255888"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "BETTERDOCS CATEGORY GRID"

    icon_1 = (By.XPATH, f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[1]/div/div[1]/div/div[1]/img')
    title_1 = (By.XPATH, f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[1]/div/div[1]/div/h2')
    title_text_1 = "Content Elements"
    count_1 = (By.XPATH, f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[1]/div/div[1]/div/div[2]')
    count_1_text = "29"
    list_icon_1 = (By.XPATH, f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[1]/div/div[2]/ul/li[1]/i')
    list_title_1 = (By.XPATH, f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[1]/div/div[2]/ul/li[1]/a')
    explore_more_btn_1 = (By.XPATH, f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[1]/div/div[3]/a')
    explore_more_btn_text = "Explore More"
    explore_more_icon_1 = (By.XPATH, f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[1]/div/div[3]/a/i')

    icon_2 = (By.XPATH, f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[5]/div/div[1]/div/div[1]/img')
    title_2 = (By.XPATH, f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[5]/div/div[1]/div/h2')
    title_text_2 = "Getting Started"
    count_2 = (By.XPATH, f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[5]/div/div[1]/div/div[2]')
    count_2_text = "7"
    list_icon_2 = (By.XPATH, f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[5]/div/div[2]/ul/li[1]/i')
    list_title_2 = (By.XPATH, f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[5]/div/div[2]/ul/li[1]/a')
    explore_more_btn_2 = (By.XPATH, f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[5]/div/div[3]/a')
    explore_more_icon_2 = (By.XPATH, f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[5]/div/div[3]/a/i')

    betterdocs_entry_title = (By.ID, 'betterdocs-entry-title')
    betterdocs_entry_heading = (By.XPATH, f'//*[@id="main"]/div/div[1]/h3')

    def __init__(self, browser):
        super().__init__(browser)

    def check_grid(self, icon, title, title_text, count, count_text, list, explore_btn, btn_text, btn_icon):
        self.is_visible(icon, "Icon is not visible")
        self.check_text_matches_with(title, title_text)
        self.check_text_matches_with(count, count_text)
        self.move_cursor_to(explore_btn)
        self.check_text_matches_with(explore_btn, btn_text)
        self.is_visible(btn_icon, "Button icon is not visible")

        list_text = self.get_element_text(list)
        self.do_click(list)
        self.check_text_matches_with(self.betterdocs_entry_title, list_text.upper())
        self.go_back()
        self.scroll_to(1050)

        self.do_click(explore_btn)
        self.check_text_matches_with(self.betterdocs_entry_heading, title_text)
        self.go_back()
        self.scroll_to(1050)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.betterdocs_category_grid)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1014)
                self.check_grid(self.icon_1, self.title_1, self.title_text_1, self.count_1, self.count_1_text,
                                self.list_title_1, self.explore_more_btn_1, self.explore_more_btn_text,
                                self.explore_more_icon_1)

                self.check_grid(self.icon_2, self.title_2, self.title_text_2, self.count_2, self.count_2_text,
                                self.list_title_2, self.explore_more_btn_2, self.explore_more_btn_text,
                                self.explore_more_icon_2)
