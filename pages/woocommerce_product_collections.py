from selenium.webdriver import ActionChains

from utils.config import *


class WoocommerceProductCollections:
    widget = '//*[@id="post-4588"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Woo Product Collection'
    doc_link = '//*[@id="post-4588"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = ""

    img_1 = f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
            f'/div/div/div[1]/div/div/div/div/div/a/img'
    title_1 = f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
            f'/div/div/div[1]/div/div/div/div/div/a/div/div/span'
    cat_1 = f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
          f'/div/div/div[1]/div/div/div/div/div/a/div/div/h2'

    img_2 = f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
            f'/div/div/div[2]/div/div/div/div/div/a/img'
    title_2 = f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
              f'/div/div/div[2]/div/div/div/div/div/a/div/div/span'
    cat_2 = f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
            f'/div/div/div[2]/div/div/div/div/div/a/div/div/h2'

    img_3 = f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
            f'/div/div/div[3]/div/div/div/div/div/a/img'
    title_3 = f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
              f'/div/div/div[3]/div/div/div/div/div/a/div/div/span'
    cat_3 = f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
            f'/div/div/div[3]/div/div/div/div/div/a/div/div/h2'

    title_text = "Collections"
    cat_1_text = "Men"
    cat_2_text = "Women"
    cat_3_text = "Shoe"

    shop_page = (By.XPATH, f'//*[@id="main"]/header/h1')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(woocommerce_product_collections)

    def check_collections(self, img, title, title_text, cat, cat_text):
        cursor = ActionChains(self.browser)
        if self.browser.find_element(By.XPATH, img).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Image is not visible.")

        img = self.browser.find_element(By.XPATH, img)
        cursor.move_to_element(img).perform()
        assert_that(self.browser.find_element(By.XPATH, title).text).is_equal_to(title_text)
        assert_that(self.browser.find_element(By.XPATH, cat).text).is_equal_to(cat_text)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 895)")
            time.sleep(.5)

            self.check_collections(self.img_1, self.title_1, self.title_text, self.cat_1, self.cat_1_text)
            self.check_collections(self.img_2, self.title_2, self.title_text, self.cat_2, self.cat_2_text)
            self.check_collections(self.img_3, self.title_3, self.title_text, self.cat_3, self.cat_3_text)

            cat = self.browser.find_element(By.XPATH, self.cat_3).text
            self.browser.find_element(By.XPATH, self.cat_3).click()
            assert_that(self.browser.find_element(*self.shop_page).text).is_equal_to(cat)
            self.browser.back()
            self.browser.execute_script("window.scrollTo(0, 895)")