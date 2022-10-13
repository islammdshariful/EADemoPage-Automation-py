from utils.config import *


class InstagramFeed(BasePage, Helper):
    widget = '//*[@id="post-25"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Instagram Feed'
    doc_link = '//*[@id="post-25"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "INSTAGRAM FEED"
    author_1 = (By.XPATH, f'//*[@id="eael-instafeed-1db29dc0"]/div[1]/div/header/div/a[1]/img')
    name_1 = (By.XPATH, f'//*[@id="eael-instafeed-1db29dc0"]/div[1]/div/header/div/a[2]/p')
    icon_1 = (By.XPATH, f'//*[@id="eael-instafeed-1db29dc0"]/div[1]/div/header/span/i')
    img_1 = (By.XPATH, f'//*[@id="eael-instafeed-1db29dc0"]/div[1]/div/a/img')

    author_2 = (By.XPATH, f'//*[@id="eael-instafeed-1db29dc0"]/div[8]/div/header/div/a[1]/img')
    name_2 = (By.XPATH, f'//*[@id="eael-instafeed-1db29dc0"]/div[8]/div/header/div/a[2]/p')
    icon_2 = (By.XPATH, f'//*[@id="eael-instafeed-1db29dc0"]/div[8]/div/header/span/i')
    img_2 = (By.XPATH, f'//*[@id="eael-instafeed-1db29dc0"]/div[8]/div/a/img')

    def __init__(self, browser):
        super().__init__(browser)

    def check_post(self, author, icon, image, name):
        self.is_visible(author, "Author is not visible")
        self.is_visible(icon, "Icon is not visible")
        self.is_visible(image, "Image is not visible")

        self.check_text_matches_with(name, "Essential Addons")

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.instagram_feed)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(905)

                self.check_post(self.author_1, self.icon_1, self.img_1, self.name_1)
                time.sleep(.5)
                self.check_post(self.author_2, self.icon_2, self.img_2, self.name_2)