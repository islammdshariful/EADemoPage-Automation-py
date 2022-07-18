from selenium.webdriver import ActionChains, Keys

from utils.config import *


class DynamicGallery(Helper):
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

    all_post_1_title = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[2]/h2/a'
    all_post_1_des = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[2]/p'
    all_post_1_img = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[1]/img'

    all_post_2_title = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[3]/div[1]/div[2]/h2/a'
    all_post_2_des = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[3]/div[1]/div[2]/p'
    all_post_2_img = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[3]/div[1]/div[1]/img'

    all_post_3_title = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[6]/div/div[2]/h2/a'
    all_post_3_des = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[6]/div[1]/div[2]/p'
    all_post_3_img = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[6]/div[1]/div[1]/img'

    all_post_4_title = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[12]/div/div[2]/h2/a'
    all_post_4_des = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[12]/div[1]/div[2]/p'
    all_post_4_img = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[12]/div[1]/div[1]/img'

    ele_post_1_title = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[2]/h2/a'
    ele_post_1_des = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[2]/p'
    ele_post_1_img = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[1]/img'

    ele_post_2_title = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[3]/div[1]/div[2]/h2/a'
    ele_post_2_des = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[3]/div[1]/div[2]/p'
    ele_post_2_img = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[3]/div[1]/div[1]/img'

    wp_post_1_title = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[2]/h2/a'
    wp_post_1_des = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[2]/p'
    wp_post_1_img = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[1]/div[1]/div[1]/img'

    wp_post_2_title = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[4]/div[1]/div[2]/h2/a'
    wp_post_2_des = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[4]/div[1]/div[2]/p'
    wp_post_2_img = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[4]/div[1]/div[1]/img'

    tm_post_1_title = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[2]/div[1]/div[2]/h2/a'
    tm_post_1_des = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[2]/div[1]/div[2]/p'
    tm_post_1_img = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[2]/div[1]/div[1]/img'

    tm_post_2_title = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[8]/div/div[2]/h2/a'
    tm_post_2_des = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[8]/div[1]/div[2]/p'
    tm_post_2_img = f'//*[@id="eael-filter-gallery-wrapper-3990f5c"]/div[2]/div[8]/div[1]/div[1]/img'

    load_more_btn = (By.ID, f'eael-load-more-btn-3990f5c')

    # Article
    article_title = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                               f'/div/div/div/div/div/div[1]/div/h1')
    article_date = (By.XPATH, f'//*[@id="page"]/div[1]/div/section/div/div/div[1]/div/div/section[1]'
                              f'/div/div/div/div/div/div[2]/div/ul/li[1]/a/span[2]')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.dynamic_gallery)

    def check_widget_post(self, post, des, img):
        cursor = ActionChains(self.browser)
        post_title = self.browser.find_element(By.XPATH, post)

        cursor.move_to_element(post_title).perform()
        self.check_visibility(des, "Galary Description is not visible")
        self.check_visibility(img, "Galary Image is not visible")

        p_title = post_title.text

        post_title.click()
        assert_that(self.browser.find_element(*self.article_title).text).is_equal_to(p_title)
        self.browser.back()
        time.sleep(1)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 905)")
                time.sleep(1)

                # All
                self.browser.find_element(*self.all).click()
                time.sleep(1)
                self.check_widget_post(self.all_post_1_title, self.all_post_1_des, self.all_post_1_img)
                self.browser.execute_script("window.scrollTo(0, 1439)")
                time.sleep(1)
                self.check_widget_post(self.all_post_3_title, self.all_post_3_des, self.all_post_3_img)
                self.browser.execute_script("window.scrollTo(0, 1450)")
                time.sleep(2)
                self.browser.find_element(*self.load_more_btn).click()
                time.sleep(1)
                self.browser.execute_script("window.scrollTo(0, 2018)")
                time.sleep(1)
                self.check_widget_post(self.all_post_4_title, self.all_post_4_des, self.all_post_4_img)
                self.browser.execute_script("window.scrollTo(0, 905)")
                time.sleep(1)
                # Elementor
                self.browser.find_element(*self.elementor).click()
                time.sleep(1)
                self.check_widget_post(self.ele_post_1_title, self.ele_post_1_des, self.ele_post_1_img)
                self.browser.find_element(*self.elementor).click()
                time.sleep(1)
                self.check_widget_post(self.ele_post_2_title, self.ele_post_2_des, self.ele_post_2_img)
                # WordPress
                self.browser.find_element(*self.wordpress).click()
                time.sleep(1)
                self.browser.execute_script("window.scrollTo(0, 1439)")
                time.sleep(1)
                self.browser.find_element(*self.load_more_btn).click()
                time.sleep(1)
                # self.check_widget_post(self.wp_post_1_title, self.wp_post_1_des, self.wp_post_1_img)
                # self.browser.find_element(*self.wordpress).click()
                # time.sleep(1)
                # self.check_widget_post(self.wp_post_2_title, self.wp_post_2_des, self.wp_post_2_img)
                # Templates
                self.browser.execute_script("window.scrollTo(0, 905)")
                time.sleep(1)
                self.browser.find_element(*self.templates).click()
                time.sleep(1)
                self.browser.execute_script("window.scrollTo(0, 1439)")
                time.sleep(1)
                self.browser.find_element(*self.load_more_btn).click()
                time.sleep(1)
                # self.check_widget_post(self.tm_post_1_title, self.tm_post_1_des, self.tm_post_1_img)
                # self.browser.find_element(*self.templates).click()
                # time.sleep(1)
                # self.browser.find_element(*self.load_more_btn).click()
                # time.sleep(1)
                # self.check_widget_post(self.tm_post_2_title, self.tm_post_2_des, self.tm_post_2_img)