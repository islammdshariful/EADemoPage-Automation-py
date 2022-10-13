from utils.config import *


class WoocommerceProductCollections(BasePage, Helper):
    widget = '//*[@id="post-4588"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Woo Product Collection'
    doc_link = '//*[@id="post-4588"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA WOO PRODUCT COLLECTIONS"

    img_1 = (By.XPATH, f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                       f'/div/div/div[1]/div/div/div/div/div/a/img')
    title_1 = (By.XPATH, f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                         f'/div/div/div[1]/div/div/div/div/div/a/div/div/span')
    cat_1 = (By.XPATH, f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                       f'/div/div/div[1]/div/div/div/div/div/a/div/div/h2')

    img_2 = (By.XPATH, f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                       f'/div/div/div[2]/div/div/div/div/div/a/img')
    title_2 = (By.XPATH, f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                         f'/div/div/div[2]/div/div/div/div/div/a/div/div/span')
    cat_2 = (By.XPATH, f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                       f'/div/div/div[2]/div/div/div/div/div/a/div/div/h2')

    img_3 = (By.XPATH, f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                       f'/div/div/div[3]/div/div/div/div/div/a/img')
    title_3 = (By.XPATH, f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                         f'/div/div/div[3]/div/div/div/div/div/a/div/div/span')
    cat_3 = (By.XPATH, f'//*[@id="post-4588"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                       f'/div/div/div[3]/div/div/div/div/div/a/div/div/h2')

    title_text = "Collections"
    cat_1_text = "Men"
    cat_2_text = "Women"
    cat_3_text = "Shoe"

    shop_page = (By.XPATH, f'//*[@id="main"]/header/h1')

    def __init__(self, browser):
        super().__init__(browser)

    def check_collections(self, img, title, title_text, cat, cat_text):
        self.is_visible(img, "Image is not visible.")
        self.move_cursor_to(img)
        self.check_text_matches_with(title, title_text)
        self.check_text_matches_with(cat, cat_text)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.woocommerce_product_collections)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(895)

                self.check_collections(self.img_1, self.title_1, self.title_text, self.cat_1, self.cat_1_text)
                self.check_collections(self.img_2, self.title_2, self.title_text, self.cat_2, self.cat_2_text)
                self.check_collections(self.img_3, self.title_3, self.title_text, self.cat_3, self.cat_3_text)

                cat = self.get_element_text(self.cat_3)
                self.do_click(self.cat_3)
                self.check_text_matches_with(self.shop_page, cat)
                self.go_back()
                self.scroll_to(895)
