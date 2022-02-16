from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import *


class FilterableGallery(Helper):
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

    prev_btn = (By.XPATH, f'/html/body/div[2]/div/button[1]')
    next_btn = (By.XPATH, f'/html/body/div[2]/div/button[2]')
    cross_btn = (By.XPATH, f'/html/body/div[2]/div/div[1]/div/button')

    gallery_title_text = "HIGHLY DELIGHTED PRESENT"

    all_gallery_1 = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[1]'
    all_gallery_1_title = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[1]/div/div[2]/div[2]/h5'
    all_gallery_1_icon = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[1]/div/div[2]/div[2]/div/a/span/i'

    gallery_2 = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[2]'
    gallery_2_title = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[2]/div/div[2]/div[2]/h5'
    gallery_2_icon = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[2]/div/div[2]/div[2]/div/a/span/i'

    all_gallery_3 = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[8]'
    all_gallery_3_title = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[8]/div/div[2]/div[2]/h5'
    all_gallery_3_icon = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[8]/div/div[2]/div[2]/div/a/span/i'

    news_gallery_1 = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[1]'
    news_gallery_1_title = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[1]/div/div[2]/div[2]/h5'
    news_gallery_1_icon = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[1]/div/div[2]/div[2]/div/a/span/i'

    news_gallery_2 = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[5]'
    news_gallery_2_title = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[5]/div/div[2]/div[2]/h5'
    news_gallery_2_icon = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[5]/div/div[2]/div[2]/div/a/span/i'

    updates_gallery_1 = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[2]'
    updates_gallery_1_title = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[2]/div/div[2]/div[2]/h5'
    updates_gallery_1_icon = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[2]/div/div[2]/div[2]/div/a/span/i'

    updates_gallery_2 = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[6]'
    updates_gallery_2_title = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[6]/div/div[2]/div[2]/h5'
    updates_gallery_2_icon = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[6]/div/div[2]/div[2]/div/a/span/i'

    events_gallery_1 = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[3]'
    events_gallery_1_title = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[3]/div/div[2]/div[2]/h5'
    events_gallery_1_icon = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[3]/div/div[2]/div[2]/div/a/span/i'

    events_gallery_2 = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[7]'
    events_gallery_2_title = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[7]/div/div[2]/div[2]/h5'
    events_gallery_2_icon = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[7]/div/div[2]/div[2]/div/a/span/i'

    masonry_gallery_1 = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[4]'
    masonry_gallery_1_title = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[4]/div/div[2]/div[2]/h5'
    masonry_gallery_1_icon = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[4]/div/div[2]/div[2]/div/a/span/i'

    masonry_gallery_2 = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[8]'
    masonry_gallery_2_title = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[8]/div/div[2]/div[2]/h5'
    masonry_gallery_2_icon = f'//*[@id="eael-filter-gallery-wrapper-66fe3cdd"]/div[2]/div[8]/div/div[2]/div[2]/div/a/span/i'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.filterable_gallery)

    def open_gallery(self, gallery, title, title_text, icon):
        cursor = ActionChains(self.browser)
        element = self.browser.find_element(By.XPATH, gallery)
        cursor.move_to_element(element).perform()
        cursor.reset_actions()
        time.sleep(1)
        assert_that(self.browser.find_element(By.XPATH, title).text).is_equal_to(title_text)
        self.check_visibility(icon, "Icon is not visible.")
        self.browser.find_element(By.XPATH, icon).click()
        time.sleep(.5)
        self.browser.find_element(*self.next_btn).click()
        time.sleep(.5)
        self.browser.find_element(*self.prev_btn).click()
        time.sleep(1)
        self.browser.find_element(*self.cross_btn).click()

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1061)")
                time.sleep(1)

                WebDriverWait(self.browser, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='nx-bar-inner']")))

                self.browser.find_element(*self.all).click()
                time.sleep(.5)
                self.open_gallery(self.all_gallery_1, self.all_gallery_1_title, self.gallery_title_text, self.all_gallery_1_icon)
                time.sleep(.5)
                self.open_gallery(self.all_gallery_3, self.all_gallery_3_title, self.gallery_title_text, self.all_gallery_3_icon)

                self.browser.find_element(*self.news).click()
                time.sleep(.5)
                self.open_gallery(self.news_gallery_1, self.news_gallery_1_title, self.gallery_title_text, self.news_gallery_1_icon)
                time.sleep(.5)
                self.open_gallery(self.news_gallery_2, self.news_gallery_2_title, self.gallery_title_text, self.news_gallery_2_icon)

                self.browser.find_element(*self.updates).click()
                time.sleep(.5)
                self.open_gallery(self.updates_gallery_1, self.updates_gallery_1_title, self.gallery_title_text, self.updates_gallery_1_icon)
                time.sleep(.5)
                self.open_gallery(self.updates_gallery_2, self.updates_gallery_2_title, self.gallery_title_text, self.updates_gallery_2_icon)

                self.browser.find_element(*self.events).click()
                time.sleep(.5)
                self.open_gallery(self.events_gallery_1, self.events_gallery_1_title, self.gallery_title_text, self.events_gallery_1_icon)
                time.sleep(.5)
                self.open_gallery(self.events_gallery_2, self.events_gallery_2_title, self.gallery_title_text, self.events_gallery_2_icon)

                self.browser.find_element(*self.masonry).click()
                time.sleep(.5)
                self.open_gallery(self.masonry_gallery_1, self.masonry_gallery_1_title, self.gallery_title_text, self.masonry_gallery_1_icon)
                time.sleep(.5)
                self.open_gallery(self.masonry_gallery_2, self.masonry_gallery_2_title, self.gallery_title_text, self.masonry_gallery_2_icon)

