from selenium.webdriver import ActionChains

from utils.config import *


class WooProductCompare:
    widget = '//*[@id="post-264859"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Woo Product Compare'
    doc_link = '//*[@id="post-264859"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section/div/div' \
               '/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "WOO PRODUCT COMPARE"

    title_header = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                              f'/div/div/div/div/div/div/div/table/tbody/tr[2]/th/div/span[2]'
    price_header = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                              f'/div/div/div/div/div/div/div/table/tbody/tr[3]/th/div/span[2]'
    availability_header = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                     f'/div/div/div/div/div/div/div/div/table/tbody/tr[4]/th/div/span[2]'
    weight_header = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                               f'/div/div/div/div/div/div/div/table/tbody/tr[5]/th/div/span[2]'
    dimension_header = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                  f'/div/div/div/div/div/div/div/div/table/tbody/tr[6]/th/div/span[2]'
    color_header = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                              f'/div/div/div/div/div/div/div/table/tbody/tr[7]/th/div/span[2]'
    add_to_cart_header = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                                    f'/div/div/div/div/div/div/div/div/table/tbody/tr[8]/th/div/span[2]'

    img_1 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div/div' \
                       f'/div/div/div/div/div/table/tbody/tr[1]/td[1]/span/span/img'
    title_1 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                         f'/div/div/div/div/div/div/table/tbody/tr[2]/td[1]'
    price_1 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                         f'/div/div/div/div/div/div/table/tbody/tr[3]/td[1]'
    availability_1 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                                f'/div/div/div/div/div/div/div/table/tbody/tr[4]/td[1]/span/span'
    weight_1 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                          f'/div/div/div/div/div/div/table/tbody/tr[5]/td[1]/span/span'
    dimension_1 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                             f'/div/div/div/div/div/div/table/tbody/tr[6]/td[1]/span/span'
    color_1 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div/div' \
                         f'/div/div/div/div/div/table/tbody/tr[7]/td[1]/span'
    add_to_cart_1 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                               f'/div/div/div/div/div/div/div/table/tbody/tr[8]/td[1]/span/a'

    img_2 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div/div' \
                       f'/div/div/div/div/div/table/tbody/tr[1]/td[2]/span/span/img'
    title_2 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div/div' \
                         f'/div/div/div/div/div/table/tbody/tr[2]/td[2]/span'
    price_2 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                         f'/div/div/div/div/div/div/table/tbody/tr[3]/td[2]'
    availability_2 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                                f'/div/div/div/div/div/div/div/table/tbody/tr[4]/td[2]/span/span'
    weight_2 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                          f'/div/div/div/div/div/div/table/tbody/tr[5]/td[2]/span/span'
    dimension_2 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                             f'/div/div/div/div/div/div/table/tbody/tr[6]/td[2]/span/span'
    color_2 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div/div' \
                         f'/div/div/div/div/div/table/tbody/tr[7]/td[2]/span'
    add_to_cart_2 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                               f'/div/div/div/div/div/div/div/table/tbody/tr[8]/td[2]/span/a'

    img_3 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div/div' \
                       f'/div/div/div/div/div/table/tbody/tr[1]/td[3]/span/span/img'
    title_3 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                         f'/div/div/div/div/div/div/table/tbody/tr[2]/td[3]'
    price_3 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                         f'/div/div/div/div/div/div/table/tbody/tr[3]/td[3]'
    availability_3 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                                f'/div/div/div/div/div/div/div/table/tbody/tr[4]/td[3]/span/span'
    weight_3 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                          f'/div/div/div/div/div/div/table/tbody/tr[5]/td[3]/span/span'
    dimension_3 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div' \
                             f'/div/div/div/div/div/div/table/tbody/tr[6]/td[3]/span/span'
    color_3 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div/div' \
                         f'/div/div/div/div/div/table/tbody/tr[7]/td[3]/span'
    add_to_cart_3 = f'//*[@id="post-264859"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div' \
                               f'/div/div/div/div/div/div/div/table/tbody/tr[8]/td[3]/span/a'

    title_header_text = "Title"
    price_header_text = "Price"
    availability_header_text = "Availability"
    weight_header_text = "Weight"
    dimension_header_text = "Dimension"
    color_header_text = "Color"
    add_to_cart_header_text = "Add to cart"

    title_1_text = "Sports shoe for men"
    price_1_text = "£99.00"
    availability_1_text = "In stock"
    weight_1_text = "-"
    dimension_1_text = "N/A"
    color_1_text = "Black, Colourful"
    add_to_cart_1_text = "Add to cart"

    title_2_text = "Casual Shoe for men"
    price_2_text = "£80.00"
    availability_2_text = "In stock"
    weight_2_text = "-"
    dimension_2_text = "N/A"
    color_2_text = "Black, Colourful"
    add_to_cart_2_text = "Add to cart"

    title_3_text = "Super Running Shoe"
    price_3_text = "£60.00"
    availability_3_text = "In stock"
    weight_3_text = "-"
    dimension_3_text = "N/A"
    color_3_text = "Colourful"
    add_to_cart_3_text = "Add to cart"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(woo_product_compare)

    def check_table(self, title, title_text, price, price_text, availability, availability_text, weight, weight_text,
                    dimension, dimension_text, color, color_text, add_to_cart, add_to_cart_text):
        assert_that(self.browser.find_element(By.XPATH, title).text).is_equal_to(title_text)
        assert_that(self.browser.find_element(By.XPATH, price).text).is_equal_to(price_text)
        assert_that(self.browser.find_element(By.XPATH, availability).text).is_equal_to(availability_text)
        assert_that(self.browser.find_element(By.XPATH, weight).text).is_equal_to(weight_text)
        assert_that(self.browser.find_element(By.XPATH, dimension).text).is_equal_to(dimension_text)
        assert_that(self.browser.find_element(By.XPATH, color).text).is_equal_to(color_text)
        atc = self.browser.find_element(By.XPATH, add_to_cart)
        assert_that(atc.text).is_equal_to(add_to_cart_text)
        cursor = ActionChains(self.browser)
        cursor.move_to_element(atc).perform()

    def check_image(self, img):
        if self.browser.find_element(By.XPATH, img).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("image is not visible")

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1128)")
            time.sleep(.5)

            self.check_table(self.title_1, self.title_1_text, self.price_1, self.price_1_text, self.availability_1,
                             self.availability_1_text, self.weight_1, self.weight_1_text, self.dimension_1,
                             self.dimension_1_text, self.color_1, self.color_1_text, self.add_to_cart_1,
                             self.add_to_cart_1_text)
            self.check_image(self.img_1)

            self.check_table(self.title_2, self.title_2_text, self.price_2, self.price_2_text, self.availability_2,
                             self.availability_2_text, self.weight_2, self.weight_2_text, self.dimension_2,
                             self.dimension_2_text, self.color_2, self.color_2_text, self.add_to_cart_2,
                             self.add_to_cart_2_text)
            self.check_image(self.img_2)

            self.check_table(self.title_3, self.title_3_text, self.price_3, self.price_3_text, self.availability_3,
                             self.availability_3_text, self.weight_3, self.weight_3_text, self.dimension_3,
                             self.dimension_3_text, self.color_3, self.color_3_text, self.add_to_cart_3,
                             self.add_to_cart_3_text)
            self.check_image(self.img_3)
