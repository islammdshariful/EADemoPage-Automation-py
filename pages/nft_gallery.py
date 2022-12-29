from utils.config import *


class NFTGallery(BasePage, Helper):
    widget = "//h2[normalize-space()='NFT Gallery']"
    widget_name = 'NFT Gallery'
    doc_link = "//a[@class='elementor-button-link elementor-button elementor-size-md']"
    doc_name = "EA NFT GALLERY"

    item_1 = f"//div[@id='eael-nft-gallery-6d9f4889']/div[1]"
    item_1_chain = (By.XPATH, item_1 + f"/div[1]")
    item_1_image = (By.XPATH, item_1 + f"/div[2]")
    item_1_title = (By.XPATH, item_1 + f"/div[3]/div[1]/h3")
    item_1_price = (By.XPATH, item_1 + f"/div[3]/div[1]/div[1]")
    item_1_creator_img = (By.XPATH, item_1 + f"/div[3]/div[1]/div[2]/div[1]")
    item_1_creator_name_label = (By.XPATH, item_1 + f"/div[3]/div[1]/div[2]/div[2]/div[1]/span")
    item_1_creator_name = (By.XPATH, item_1 + f"/div[3]/div[1]/div[2]/div[2]/div[2]/a")
    item_1_last_sale_label = (By.XPATH, item_1 + f"/div[3]/div[1]/div[3]/p/span[1]")
    item_1_last_sale = (By.XPATH, item_1 + f"/div[3]/div[1]/div[3]/p/span[2]")
    item_1_button = (By.XPATH, item_1 + f"/div[3]/div[2]/button/a")

    item_2 = f"//div[@id='eael-nft-gallery-6d9f4889']/div[8]"
    item_2_chain = (By.XPATH, item_2 + f"/div[1]")
    item_2_image = (By.XPATH, item_2 + f"/div[2]")
    item_2_title = (By.XPATH, item_2 + f"/div[3]/div[1]/h3")
    item_2_price = (By.XPATH, item_2 + f"/div[3]/div[1]/div[1]")
    item_2_creator_img = (By.XPATH, item_2 + f"/div[3]/div[1]/div[2]/div[1]")
    item_2_creator_name_label = (By.XPATH, item_2 + f"/div[3]/div[1]/div[2]/div[2]/div[1]/span")
    item_2_creator_name = (By.XPATH, item_2 + f"/div[3]/div[1]/div[2]/div[2]/div[2]/a")
    item_2_last_sale_label = (By.XPATH, item_2 + f"/div[3]/div[1]/div[3]/p/span[1]")
    item_2_last_sale = (By.XPATH, item_2 + f"/div[3]/div[1]/div[3]/p/span[2]")
    item_2_button = (By.XPATH, item_2 + f"/div[3]/div[2]/button/a")

    nft_title = (By.CSS_SELECTOR, '.item--title')
    nft_price = (By.CSS_SELECTOR, '.Price--amount')
    nft_creator = (By.CSS_SELECTOR, "[data-testid='phoenix-header']")

    scroll = (By.CSS_SELECTOR, '.elementor-element-7d8e5375')

    def __init__(self, browser):
        super().__init__(browser)

    def check_item(self, image, chain, name, price, creator_image, creator_name_label, creator_name, last_sale,
                   button, *last_sale_label):
        self.is_visible(self.item_1_image, 'NFT 1 image is not visible')
        self.is_visible(creator_image, 'NFT 1 Creator avatar is not visible')
        item_name = self.get_element_text(name)
        price = self.get_element_text(price)
        creator = self.get_element_text(creator_name)
        self.check_text_matches_with(creator_name_label, 'Creator')

        if len(self.browser.find_elements(*last_sale_label)) > 0:
            self.check_text_matches_with(last_sale_label, 'Last sale:')
            self.is_visible(last_sale, 'Last sale data is not showing')
        self.move_cursor_to(image)
        self.is_visible(chain, 'NFT 1 Chain not visible')
        self.check_text_matches_with(button, 'View Details')
        self.close_nx_popup()
        self.move_cursor_to(image)
        self.do_click(button)
        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[1])
        self.check_text_matches_with(self.nft_title, item_name)
        self.check_text_matches_with(self.nft_price, price)
        self.browser.close()
        self.browser.switch_to.window(windows[0])
        self.close_nx_popup()
        self.do_click(creator_name)
        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[1])
        self.check_text_matches_with(self.nft_creator, creator)
        self.browser.close()
        self.browser.switch_to.window(windows[0])

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.nft_gallery)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to_element(self.scroll)
                self.check_item(self.item_1_image, self.item_1_chain, self.item_1_title, self.item_1_price,
                                self.item_1_creator_img, self.item_1_creator_name_label, self.item_1_creator_name,
                                self.item_1_last_sale, self.item_1_button, *self.item_1_last_sale_label)

                self.scroll_to_element(self.item_1_last_sale_label)

                self.check_item(self.item_2_image, self.item_2_chain, self.item_2_title, self.item_2_price,
                                self.item_2_creator_img, self.item_2_creator_name_label, self.item_2_creator_name,
                                self.item_2_last_sale, self.item_2_button, *self.item_2_last_sale_label)

