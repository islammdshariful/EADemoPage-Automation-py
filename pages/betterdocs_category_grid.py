from selenium.webdriver import ActionChains

from utils.config import *


class BetterdocsCategoryGrid(Helper):
    widget = '//*[@id="post-255888"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'BetterDocs Category Grid'
    doc_link = '//*[@id="post-255888"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "BETTERDOCS CATEGORY GRID"

    icon_1 = f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[1]/div/div[1]/div/div[1]/img'
    title_1 = f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[1]/div/div[1]/div/h2'
    title_text_1 = "Content Elements"
    count_1 = f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[1]/div/div[1]/div/div[2]'
    count_1_text = "29"
    list_icon_1 = f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[1]/div/div[2]/ul/li[1]/i'
    list_title_1 = f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[1]/div/div[2]/ul/li[1]/a'
    explore_more_btn_1 = f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[1]/div/div[3]/a'
    explore_more_btn_text = "Explore More"
    explore_more_icon_1 = f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[1]/div/div[3]/a/i'

    icon_2 = f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[5]/div/div[1]/div/div[1]/img'
    title_2 = f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[5]/div/div[1]/div/h2'
    title_text_2 = "Getting Started"
    count_2 = f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[5]/div/div[1]/div/div[2]'
    count_2_text = "7"
    list_icon_2 = f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[5]/div/div[2]/ul/li[1]/i'
    list_title_2 = f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[5]/div/div[2]/ul/li[1]/a'
    explore_more_btn_2 = f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[5]/div/div[3]/a'
    explore_more_icon_2 = f'//*[@id="eael-bd-cat-grid-36d08f5"]/div[1]/article[5]/div/div[3]/a/i'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.betterdocs_category_grid)

    def check_grid(self, icon, title, title_text, count, count_text, list, explore_btn, btn_text, btn_icon):
        self.check_visibility(icon, "Icon is not visible")

        assert_that(self.browser.find_element(By.XPATH, title).text).is_equal_to(title_text)
        assert_that(self.browser.find_element(By.XPATH, count).text).is_equal_to(count_text)
        cursor = ActionChains(self.browser)
        btn = self.browser.find_element(By.XPATH, explore_btn)
        cursor.move_to_element(btn).perform()
        assert_that(btn.text).is_equal_to(btn_text)
        self.check_visibility(btn_icon, "Button icon is not visible")

        lst_text = self.browser.find_element(By.XPATH, list).text
        self.browser.find_element(By.XPATH, list).click()
        assert_that(self.browser.find_element(By.ID, 'betterdocs-entry-title').text).is_equal_to(lst_text.upper())
        self.browser.back()
        time.sleep(1)
        self.browser.execute_script("window.scrollTo(0, 1014)")
        self.browser.find_element(By.XPATH, explore_btn).click()
        assert_that(self.browser.find_element(By.XPATH, f'//*[@id="main"]/div/div[1]/h3').text).is_equal_to(title_text)
        self.browser.back()
        time.sleep(1)
        self.browser.execute_script("window.scrollTo(0, 1014)")

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.check_documents(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1014)")
            self.check_grid(self.icon_1, self.title_1, self.title_text_1, self.count_1, self.count_1_text,
                            self.list_title_1, self.explore_more_btn_1, self.explore_more_btn_text,
                            self.explore_more_icon_1)

            self.check_grid(self.icon_2, self.title_2, self.title_text_2, self.count_2, self.count_2_text,
                            self.list_title_2, self.explore_more_btn_2, self.explore_more_btn_text,
                            self.explore_more_icon_2)
