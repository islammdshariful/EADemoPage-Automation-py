from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import *


class InteractiveCircle(Helper):
    widget = '//*[@id="post-271398"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Interactive Circle'
    doc_link = '//*[@id="post-271398"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA INTERACTIVE CIRCLE"

    item_1_icon = f"//div[@class='eael-circle-item elementor-repeater-item-daade21']" \
                  f"//i[@class='fas fa-leaf']"
    item_1_title = f"//div[@class='eael-circle-item elementor-repeater-item-daade21']//" \
                   f"span[@class='eael-circle-btn-txt'][normalize-space()='Item 1']"
    item_1_des = f"//div[@class='eael-circle-item elementor-repeater-item-daade21']//" \
                 f"div[@class='eael-circle-btn-content eael-circle-item-1 active']"

    item_2_icon = f"//div[@class='eael-circle-item elementor-repeater-item-ee5d844']" \
                  f"//i[@class='fas fa-comment']"
    item_2_title = f"//div[@class='eael-circle-item elementor-repeater-item-ee5d844']//" \
                   f"span[@class='eael-circle-btn-txt'][normalize-space()='Item 2']"
    item_2_des = f"//div[@class='eael-circle-btn-content eael-circle-item-2 active']"

    item_3_icon = f"//div[@class='eael-circle-item elementor-repeater-item-9077b74']//" \
                  f"i[@class='fas fa-map-marker-alt']"
    item_3_title = f"//div[@class='eael-circle-item elementor-repeater-item-9077b74']//" \
                   f"span[@class='eael-circle-btn-txt'][normalize-space()='Item 3']"
    item_3_des = f"//div[@class='eael-circle-btn-content eael-circle-item-3 active']"

    item_4_icon = f"//div[@class='eael-circle-item elementor-repeater-item-b5c66d9']//" \
                  f"i[@class='fas fa-rocket']"
    item_4_title = f"//div[@class='eael-circle-item elementor-repeater-item-b5c66d9']//" \
                   f"span[@class='eael-circle-btn-txt'][normalize-space()='Item 4']"
    item_4_des = f"//div[@class='eael-circle-btn-content eael-circle-item-4 active']"

    item_5_icon = f"//div[@class='eael-circle-item elementor-repeater-item-ff78a5b']//" \
                  f"i[@class='fas fa-hourglass-half']"
    item_5_title = f"//div[@class='eael-circle-item elementor-repeater-item-ff78a5b']//" \
                   f"span[@class='eael-circle-btn-txt'][normalize-space()='Item 5']"
    item_5_des = f"//div[@class='eael-circle-btn-content eael-circle-item-5 active']"

    item_6_icon = f"//div[@class='eael-circle-item elementor-repeater-item-f32b657']//i[@class='fas fa-tag']"
    item_6_title = f"//div[@class='eael-circle-item elementor-repeater-item-f32b657']//" \
                   f"span[@class='eael-circle-btn-txt'][normalize-space()='Item 6']"
    item_6_des = f"//div[@class='eael-circle-btn-content eael-circle-item-6 active']"

    item_1_title_text = "Item 1"
    item_1_des_text = "Present your content in an attractive Circle layout item 1. You can highlight key information " \
                      "with click or hover effects and style it as per your preference."
    item_2_title_text = "Item 2"
    item_2_des_text = "Present your content in an attractive Circle layout item 2. You can highlight key information " \
                      "with click or hover effects and style it as per your preference."
    item_3_title_text = "Item 3"
    item_3_des_text = "Present your content in an attractive Circle layout item 3. You can highlight key information " \
                      "with click or hover effects and style it as per your preference."
    item_4_title_text = "Item 4"
    item_4_des_text = "Present your content in an attractive Circle layout item 4. You can highlight key information " \
                      "with click or hover effects and style it as per your preference."
    item_5_title_text = "Item 5"
    item_5_des_text = "Present your content in an attractive Circle layout item 5. You can highlight key information " \
                      "with click or hover effects and style it as per your preference."
    item_6_title_text = "Item 6"
    item_6_des_text = "Present your content in an attractive Circle layout item 6. You can highlight key information " \
                      "with click or hover effects and style it as per your preference."

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.interactive_circle)

    def check_circle(self, icon, title, des, title_text, des_text):
        self.browser.find_element(By.XPATH, title).click()
        time.sleep(.5)
        if self.browser.find_element(By.XPATH, icon).is_displayed():
            assert_that(1).is_equal_to(1)
        else:
            assert_that(1).is_equal_to("Icon not displaying")

        assert_that(self.browser.find_element(By.XPATH, title).text).is_equal_to(title_text)
        assert_that(self.browser.find_element(By.XPATH, des).text).is_equal_to(des_text)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 890)")
                time.sleep(1)

                self.check_circle(self.item_1_icon, self.item_1_title, self.item_1_des, self.item_1_title_text,
                                  self.item_1_des_text)
                self.check_circle(self.item_2_icon, self.item_2_title, self.item_2_des, self.item_2_title_text,
                                  self.item_2_des_text)
                self.check_circle(self.item_3_icon, self.item_3_title, self.item_3_des, self.item_3_title_text,
                                  self.item_3_des_text)
                self.check_circle(self.item_4_icon, self.item_4_title, self.item_4_des, self.item_4_title_text,
                                  self.item_4_des_text)
                self.check_circle(self.item_5_icon, self.item_5_title, self.item_5_des, self.item_5_title_text,
                                  self.item_5_des_text)
                self.check_circle(self.item_6_icon, self.item_6_title, self.item_6_des, self.item_6_title_text,
                                  self.item_6_des_text)
