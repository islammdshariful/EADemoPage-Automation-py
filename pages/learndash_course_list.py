from utils.config import *


class LearndashCourseList(BasePage, Helper):
    widget = '//*[@id="post-255262"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'LearnDash Course List'
    doc_link = '//*[@id="post-255262"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "LEARNDASH COURSE LIST"

    course_title_1 = (By.XPATH, f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                                f'/div[1]/div/div[2]/h4')
    course_img_1 = (By.XPATH, f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                              f'/div[1]/div/a/img')
    course_des_1 = (By.XPATH, f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                              f'/div[1]/div/div[2]/div/p')
    course_price_1 = (By.XPATH, f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                                f'/div[1]/div/div[1]')

    course_title_2 = (By.XPATH, f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                                f'/div[2]/div/div[2]/h4')
    course_img_2 = (By.XPATH, f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                              f'/div[2]/div/a/img')
    course_des_2 = (By.XPATH, f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                              f'/div[2]/div/div[2]/div/p')
    course_price_2 = (By.XPATH, f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                                f'/div[2]/div/div[1]')

    course_title_3 = (By.XPATH, f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                                f'/div[3]/div/div[2]/h4')
    course_img_3 = (By.XPATH, f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                              f'/div[3]/div/a/img')
    course_des_3 = (By.XPATH, f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                              f'/div[3]/div/div[2]/div/p')
    course_price_3 = (By.XPATH, f'//*[@id="post-255262"]/div/div/div/div/section[2]/div/div/div/div/div/div/div/div' \
                                f'/div[3]/div/div[1]')
    course_title_text_1 = "Communication Master Class-Complete Guide To Be An Expert"
    course_des_text = "In iOS, interface elements layouts can configured change shape size …"
    course_price_text_1 = "$67"

    course_title_text_2 = "CSS Master Course-The Complete Guide Of 2020"
    course_price_text_2 = "$55"

    course_title_text_3 = "UI & UX Web Design Master Course-Strategy, Design & Development"
    course_price_text_3 = "$65"

    def __init__(self, browser):
        super().__init__(browser)

    def course(self, title, title_text, des, des_text, price, price_text, img):
        self.move_cursor_to(title)
        self.check_text_matches_with(title, title_text)
        self.check_text_matches_with(des, des_text)
        self.check_text_matches_with(price, price_text)
        self.is_visible(img, "Image is not visible")

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.learndash_course_list)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(946)
                self.course(self.course_title_1, self.course_title_text_1, self.course_des_1, self.course_des_text,
                            self.course_price_1, self.course_price_text_1, self.course_img_1)

                self.course(self.course_title_2, self.course_title_text_2, self.course_des_2, self.course_des_text,
                            self.course_price_2, self.course_price_text_2, self.course_img_2)

                self.course(self.course_title_3, self.course_title_text_3, self.course_des_3, self.course_des_text,
                            self.course_price_3, self.course_price_text_3, self.course_img_3)
