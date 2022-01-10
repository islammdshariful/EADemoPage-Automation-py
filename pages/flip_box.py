from selenium.webdriver import ActionChains

from utils.config import *


class FlipBox:
    widget = '//*[@id="post-1519"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = "Flip Box"
    DOC_LINK = '//*[@id="post-1519"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/' \
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
        self.browser = browser

    def load(self):
        self.browser.get(flip_box)

    def testcase(self):
        c = CheckText(self.browser)

        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.DOC_LINK, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1023)")
            time.sleep(1)

            front_header_ele = self.browser.find_element(*self.BOX_FRONT_HEADER)

            if self.browser.find_element(*self.BOX_FRONT_HEADER).is_displayed():
                assert_that(front_header_ele.text).is_equal_to(self.BOX_FRONT_HEADER_TEXT)
                print("Front header is visible")

            cursor = ActionChains(self.browser)

            box_1_element = self.browser.find_element(*self.BOX_1)

            cursor.move_to_element(box_1_element).perform()

            back_header_ele = self.browser.find_element(*self.BOX_BACK_HEADER)
            back_des_ele = self.browser.find_element(*self.BOX_BACK_DES)

            if self.browser.find_element(*self.BOX_BACK_HEADER).is_displayed():
                print("Back header is visible")
                if self.browser.find_element(*self.BOX_BACK_DES).is_displayed():
                    assert_that(back_header_ele.text).is_equal_to(self.BOX_BACK_HEADER_TEXT)
                    assert_that(back_des_ele.text).is_equal_to(self.BOX_DES_TEXT)
                    print("Back description is visible")

            box_2_element = self.browser.find_element(*self.BOX_2)
            cursor.move_to_element(box_2_element).perform()




