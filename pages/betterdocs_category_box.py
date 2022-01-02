from selenium.webdriver import ActionChains

from utils.config import *


class BetterdocsCategoryBox:
    widget = '//*[@id="post-255913"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'BetterDocs Category Box'
    doc_link = '//*[@id="post-255913"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "BETTERDOCS CATEGORY BOX"

    icon_1 = f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[1]/div/div[1]/img'
    title_1 = f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[1]/div/h2'
    count_1 = f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[1]/div/div[2]'
    count_title_1 = f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[1]/div/div[2]/span[2]'

    icon_2 = f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[6]/div/div[1]/img'
    title_2 = f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[6]/div/h2'
    count_2 = f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[6]/div/div[2]'
    count_title_2 = f'//*[@id="eael-bd-cat-box-5655788f"]/div/a[6]/div/div[2]/span[2]'

    title_1_text = "Getting Started"
    count_1_text = "7articles"

    title_2_text = "Dynamic Content Elements"
    count_2_text = "10articles"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(betterdocs_category_box)

    def box_layout(self, icon, title, title_text, count, count_text):
        if self.browser.find_element(By.XPATH, icon).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Icon is not visible")

        assert_that(self.browser.find_element(By.XPATH, title).text).is_equal_to(title_text)
        assert_that(self.browser.find_element(By.XPATH, count).text).is_equal_to(count_text)
        name = self.browser.find_element(By.XPATH, title).text
        self.browser.find_element(By.XPATH, title).click()
        assert_that(self.browser.find_element(By.XPATH, f'//*[@id="main"]/div/div[1]/h3').text).is_equal_to(name)
        self.browser.back()
        time.sleep(1)
        self.browser.execute_script("window.scrollTo(0, 856)")

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 856)")
            self.box_layout(self.icon_1, self.title_1, self.title_1_text, self.count_1, self.count_1_text)
            self.box_layout(self.icon_2, self.title_2, self.title_2_text, self.count_2, self.count_2_text)

