from selenium.webdriver import ActionChains

from utils.config import *


class LearndashCourseList:
    widget = '//*[@id="post-255262"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'LearnDash Course List'
    doc_link = '//*[@id="post-255262"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "LEARNDASH COURSE LIST"

    course_title_1 = f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                         f'/div[1]/div/div[2]/h4'
    course_img_1 = f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                              f'/div[1]/div/a/img'
    course_des_1 = f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                              f'/div[1]/div/div[2]/div/p'
    course_price_1 = f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                                f'/div[1]/div/div[1]'

    course_title_2 = f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                         f'/div[2]/div/div[2]/h4'
    course_img_2 = f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                              f'/div[2]/div/a/img'
    course_des_2 = f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                              f'/div[2]/div/div[2]/div/p'
    course_price_2 = f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                                f'/div[2]/div/div[1]'

    course_title_3 = f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                         f'/div[3]/div/div[2]/h4'
    course_img_3 = f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                              f'/div[3]/div/a/img'
    course_des_3 = f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                              f'/div[3]/div/div[2]/div/p'
    course_price_3 = f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                                f'/div[3]/div/div[1]'
    course_title_text_1 = "Communication Master Class-Complete Guide To Be An Expert"
    course_des_text = "In iOS, interface elements layouts can configured change shape size …"
    course_price_text_1 = "$67"

    course_title_text_2 = "CSS Master Course-The Complete Guide Of 2020"
    course_price_text_2 = "$55"

    course_title_text_3 = "UI & UX Web Design Master Course-Strategy, Design & Development"
    course_price_text_3 = "$65"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(learndash_course_list)

    def course(self, title, title_text, des, des_text, price, price_text, img):
        cursor = ActionChains(self.browser)
        ttl = self.browser.find_element(By.XPATH, title)
        cursor.move_to_element(ttl).perform()
        assert_that(ttl.text).is_equal_to(title_text)
        assert_that(self.browser.find_element(By.XPATH, des).text).is_equal_to(des_text)
        assert_that(self.browser.find_element(By.XPATH, price).text).is_equal_to(price_text)

        if self.browser.find_element(By.XPATH, img).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Image is not visible")

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 946)")
            self.course(self.course_title_1, self.course_title_text_1, self.course_des_1, self.course_des_text,
                        self.course_price_1, self.course_price_text_1, self.course_img_1)

            self.course(self.course_title_2, self.course_title_text_2, self.course_des_2, self.course_des_text,
                        self.course_price_2, self.course_price_text_2, self.course_img_2)

            self.course(self.course_title_3, self.course_title_text_3, self.course_des_3, self.course_des_text,
                        self.course_price_3, self.course_price_text_3, self.course_img_3)
