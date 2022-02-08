from selenium.webdriver import Keys

from utils.config import *


class InstagramFeed(Helper):
    widget = '//*[@id="post-25"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Instagram Feed'
    doc_link = '//*[@id="post-25"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "INSTAGRAM FEED"
    author_1 = f'//*[@id="eael-instafeed-1db29dc0"]/div[1]/div/header/div/a[1]/img'
    name_1 = f'//*[@id="eael-instafeed-1db29dc0"]/div[1]/div/header/div/a[2]/p'
    icon_1 = f'//*[@id="eael-instafeed-1db29dc0"]/div[1]/div/header/span/i'
    img_1 = f'//*[@id="eael-instafeed-1db29dc0"]/div[1]/div/a/img'

    author_2 = f'//*[@id="eael-instafeed-1db29dc0"]/div[8]/div/header/div/a[1]/img'
    name_2 = f'//*[@id="eael-instafeed-1db29dc0"]/div[8]/div/header/div/a[2]/p'
    icon_2 = f'//*[@id="eael-instafeed-1db29dc0"]/div[8]/div/header/span/i'
    img_2 = f'//*[@id="eael-instafeed-1db29dc0"]/div[8]/div/a/img'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.instagram_feed)

    def check_post(self, author, icon, image, name):
        self.check_visibility(author, "Author is not visible")
        self.check_visibility(icon, "Icon is not visible")
        self.check_visibility(image, "Image is not visible")

        assert_that(self.browser.find_element(By.XPATH, name).text).is_equal_to("Essential Addons")

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 905)")
                self.check_post(self.author_1, self.icon_1, self.img_1, self.name_1)
                time.sleep(.5)
                self.check_post(self.author_2, self.icon_2, self.img_2, self.name_2)