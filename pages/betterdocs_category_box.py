from utils.config import *


class BetterdocsCategoryBox(BasePage, Helper):
    widget = '//*[@id="post-255913"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'BetterDocs Category Box'
    doc_link = '//*[@id="post-255913"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "BETTERDOCS CATEGORY BOX"

    icon_1 = (By.XPATH, f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[1]/div/div[1]/img')
    title_1 = (By.XPATH, f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[1]/div/h2')
    count_1 = (By.XPATH, f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[1]/div/div[2]')
    count_title_1 = (By.XPATH, f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[1]/div/div[2]/span[2]')

    icon_2 = (By.XPATH, f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[6]/div/div[1]/img')
    title_2 = (By.XPATH, f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[6]/div/h2')
    count_2 = (By.XPATH, f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[6]/div/div[2]')
    count_title_2 = (By.XPATH, f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[6]/div/div[2]/span[2]')

    title_1_text = "Getting Started"
    count_1_text = "7articles"

    title_2_text = "Dynamic Content Elements"
    count_2_text = "11articles"

    betterdocs_entry_heading = (By.XPATH, f'//*[@id="main"]/div/div[1]/h3')

    def __init__(self, browser):
        super().__init__(browser)

    def box_layout(self, icon, title, title_text, count, count_text):
        self.is_visible(icon, "Icon is not visible")
        self.check_text_matches_with(title, title_text)
        self.check_text_matches_with(count, count_text)
        name = self.get_element_text(title)
        self.do_click(title)
        self.check_text_matches_with(self.betterdocs_entry_heading, name)
        self.go_back()
        self.scroll_to(856)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.betterdocs_category_box)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(856)
                self.box_layout(self.icon_1, self.title_1, self.title_1_text, self.count_1, self.count_1_text)
                self.box_layout(self.icon_2, self.title_2, self.title_2_text, self.count_2, self.count_2_text)

