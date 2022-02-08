from selenium.webdriver import ActionChains, Keys

from utils.config import *


class FlipBox(Helper):
    widget = '//*[@id="post-1519"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = "Flip Box"
    doc_link = '//*[@id="post-1519"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/' \
               'div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "FLIP BOX"
    BOX_1 = (By.XPATH, f'//*[@id="post-1519"]/div/div/div/div/section[2]/div/div/div/div/div/section['
                     f'2]/div/div/div[1]/div/div/div/div/div')
    BOX_2 = (By.XPATH, f'//*[@id="post-1519"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                       f'/div/div/div[2]/div/div')
    BOX_FRONT_HEADER = (By.XPATH, f'//*[@id="post-1519"]/div/div/div/div/section[2]/div/div/div/div/div/section['
                                  f'2]/div/div/div[1]/div/div/div/div/div/a/div[1]/div/div/div/h2')
    BOX_BACK_HEADER = (By.XPATH, f'//*[@id="post-1519"]/div/div/div/div/section[2]/div/div/div/div/div/section['
                          f'2]/div/div/div[1]/div/div/div/div/div/a/div[2]/div/div/div/h2')
    BOX_BACK_DES = (By.XPATH, f'//*[@id="post-1519"]/div/div/div/div/section[2]/div/div/div/div/div/section['
                         f'2]/div/div/div[1]/div/div/div/div/div/a/div[2]/div/div/div/div[2]/p[2]')

    BOX_FRONT_HEADER_TEXT = "Interface Design"
    BOX_BACK_HEADER_TEXT = "Style Your Flip Box Exclusively"
    BOX_DES_TEXT = "Add your preferred content or use saved templates here, choose your 'Icon Type', " \
                   "add title, select title tag for front & back, set your content position, alignment " \
                   "and style your Flip Box the way you want.    "

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.flip_box)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 1023)")
                time.sleep(1)

                front_header_ele = self.browser.find_element(*self.BOX_FRONT_HEADER)

                if self.browser.find_element(*self.BOX_FRONT_HEADER).is_displayed():
                    assert_that(front_header_ele.text).is_equal_to(self.BOX_FRONT_HEADER_TEXT)

                cursor = ActionChains(self.browser)

                box_1_element = self.browser.find_element(*self.BOX_1)

                cursor.move_to_element(box_1_element).perform()

                back_header_ele = self.browser.find_element(*self.BOX_BACK_HEADER)
                back_des_ele = self.browser.find_element(*self.BOX_BACK_DES)

                if self.browser.find_element(*self.BOX_BACK_HEADER).is_displayed():
                    if self.browser.find_element(*self.BOX_BACK_DES).is_displayed():
                        assert_that(back_header_ele.text).is_equal_to(self.BOX_BACK_HEADER_TEXT)
                        assert_that(back_des_ele.text).is_equal_to(self.BOX_DES_TEXT)

                box_2_element = self.browser.find_element(*self.BOX_2)
                cursor.move_to_element(box_2_element).perform()




