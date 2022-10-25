from pages.basepage import BasePage
from utils.config import *


class TeamMemberCarousel(BasePage, Helper):
    widget = '//*[@id="post-2946"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = "Team Members Carousel"
    doc_link = '//*[@id="post-2946"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/' \
               'section/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "TEAM MEMBER CAROUSEL"

    next_button = (By.XPATH, f'//*[@id="post-2946"]/div/div/div/div/section[2]/div/div/div'
                             f'/div/div/div/div/div/div[2]')
    prev_button = (By.XPATH, f'//*[@id="post-2946"]/div/div/div/div/section[2]/div/div/div'
                             f'/div/div/div/div/div/div[3]')

    mem_1_name = (By.XPATH, f'//*[@id="swiper-container-29a9b4d7"]/div/div[7]/div/div[2]/h4')
    mem_1_pos = (By.XPATH, f'//*[@id="swiper-container-29a9b4d7"]/div/div[7]/div/div[2]/div')
    mem_1_img = (By.XPATH, f'//*[@id="swiper-container-29a9b4d7"]/div/div[7]/div/div[1]/img')
    mem_1_soc_fb = (By.XPATH, f'//*[@id="swiper-container-29a9b4d7"]/div/div[7]/div/div[1]/div'
                              f'/div/div/ul/li[1]/a/span/span')
    mem_1_soc_tw = (By.XPATH, f'//*[@id="swiper-container-29a9b4d7"]/div/div[7]/div/div[1]/div'
                              f'/div/div/ul/li[2]/a/span/span')
    mem_1_soc_lk = (By.XPATH, f'//*[@id="swiper-container-29a9b4d7"]/div/div[7]/div/div[1]/div'
                              f'/div/div/ul/li[3]/a/span/span')

    mem_name_text = "Henry Fayowl"
    mem_pos_text = "UX Experts"

    mem_2_name = (By.XPATH, f'//*[@id="swiper-container-29a9b4d7"]/div/div[9]/div/div[2]/h4')
    mem_2_pos = (By.XPATH, f'//*[@id="swiper-container-29a9b4d7"]/div/div[9]/div/div[2]/div')
    mem_2_img = (By.XPATH, f'//*[@id="swiper-container-29a9b4d7"]/div/div[9]/div/div[1]/img')
    mem_2_soc_fb = (By.XPATH, f'//*[@id="swiper-container-29a9b4d7"]/div/div[9]/div/div[1]/div'
                              f'/div/div/ul/li[1]/a/span/span')
    mem_2_soc_tw = (By.XPATH, f'//*[@id="swiper-container-29a9b4d7"]/div/div[9]/div/div[1]/div'
                              f'/div/div/ul/li[2]/a/span/span')
    mem_2_soc_lk = (By.XPATH, f'//*[@id="swiper-container-29a9b4d7"]/div/div[9]/div/div[1]/div'
                              f'/div/div/ul/li[3]/a/span/span')

    dot_1 = (By.XPATH, f'//*[@id="post-2946"]/div/div/div/div/section[5]/div/div/div/div'
                       f'/div/div/div/div/div[2]/span[1]')
    dot_2 = (By.XPATH, f'//*[@id="post-2946"]/div/div/div/div/section[5]/div/div/div/div'
                       f'/div/div/div/div/div[2]/span[2]')
    dot_3 = (By.XPATH, f'//*[@id="post-2946"]/div/div/div/div/section[5]/div/div/div/div'
                       f'/div/div/div/div/div[2]/span[3]')

    mem_3_name = (By.XPATH, f'//*[@id="swiper-container-60695a44"]/div/div[4]/div/div[2]/h4')
    mem_3_name_text = "Jemes Barber"
    mem_3_pos = (By.XPATH, f'//*[@id="swiper-container-60695a44"]/div/div[4]/div/div[2]/div[1]')
    mem_3_pos_text = "Beard Trimmer"
    mem_3_img = (By.XPATH, f'//*[@id="swiper-container-60695a44"]/div/div[4]/div/div[1]/img')
    mem_3_soc_fb = (By.XPATH, f'//*[@id="swiper-container-60695a44"]/div/div[4]/div/div[2]/div[2]'
                              f'/ul/li[1]/a/span/span')
    mem_3_soc_tw = (By.XPATH, f'//*[@id="swiper-container-60695a44"]/div/div[4]/div/div[2]/div[2]'
                              f'/ul/li[2]/a/span/span')
    mem_3_soc_lk = (By.XPATH, f'//*[@id="swiper-container-60695a44"]/div/div[4]/div/div[2]/div[2]'
                              f'/ul/li[3]/a/span/span')

    mem_4_name = (By.XPATH, f'//*[@id="swiper-container-60695a44"]/div/div[8]/div/div[2]/h4')
    mem_4_name_text = "Deen Mustachio"
    mem_4_pos = (By.XPATH, f'//*[@id="swiper-container-60695a44"]/div/div[8]/div/div[2]/div[1]')
    mem_4_pos_text = "Mustache Experts"
    mem_4_img = (By.XPATH, f'//*[@id="swiper-container-60695a44"]/div/div[8]/div/div[1]/img')
    mem_4_soc_fb = (By.XPATH, f'//*[@id="swiper-container-60695a44"]/div/div[8]/div/div[2]/div[2]'
                              f'/ul/li[1]/a/span/span')
    mem_4_soc_tw = (By.XPATH, f'//*[@id="swiper-container-60695a44"]/div/div[8]/div/div[2]/div[2]'
                              f'/ul/li[2]/a/span/span')
    mem_4_soc_lk = (By.XPATH, f'//*[@id="swiper-container-60695a44"]/div/div[8]/div/div[2]/div[2]'
                              f'/ul/li[3]/a/span/span')

    scroll_to_1 = (By.XPATH, '//*[@id="post-2946"]/div/div/div/div/section[2]/div/div/div/div/div/section'
                             '/div/div/div[2]/div/div/div[1]/div/h3')
    scroll_to_2 = (By.XPATH, '//*[@id="post-2946"]/div/div/div/div/section[5]/div/div/div/div/div/section'
                             '/div/div/div[2]/div/div/div[1]/div/h3')

    def __init__(self, browser):
        super().__init__(browser)

    def member_card(self, img_locator, social_fb_locator, social_tw_locator, social_li_locator, name_locator, name_txt,
                    pos_locator, pos_txt, dot=None):
        """Check member information"""
        self.check_text_matches_with(name_locator, name_txt)
        self.check_text_matches_with(pos_locator, pos_txt)

        self.move_cursor_to(img_locator)
        if dot is not None:
            self.do_click(dot)
        self.cursor.move_to_element(self.get_element(social_fb_locator)).\
            move_to_element(self.get_element(social_tw_locator)). \
            move_to_element(self.get_element(social_li_locator)).perform()

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.team_members_carousel)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to_element(self.scroll_to_1)
                """Check carousel 1"""
                self.member_card(self.mem_1_img, self.mem_1_soc_fb,
                                 self.mem_1_soc_tw, self.mem_1_soc_lk,
                                 self.mem_1_name, self.mem_name_text,
                                 self.mem_1_pos, self.mem_pos_text)
                """Clicking navigation arrows"""
                self.do_click(self.prev_button, click_after_wait='yes')
                self.do_click(self.prev_button, click_after_wait='yes')
                self.do_click(self.next_button, click_after_wait='yes')
                self.do_click(self.next_button, click_after_wait='yes')
                """Check carousel 2"""
                self.member_card(self.mem_2_img, self.mem_2_soc_fb,
                                 self.mem_2_soc_tw, self.mem_2_soc_lk,
                                 self.mem_2_name, self.mem_name_text,
                                 self.mem_2_pos, self.mem_pos_text)
                """Go to next carousel"""
                self.scroll_to_element(self.scroll_to_2)
                """Click on navigation dot"""
                self.do_click(self.dot_1, click_after_wait='yes')
                self.scroll_to_element(self.scroll_to_2)
                self.member_card(self.mem_3_img, self.mem_3_soc_fb,
                                 self.mem_3_soc_tw, self.mem_3_soc_lk,
                                 self.mem_3_name, self.mem_3_name_text,
                                 self.mem_3_pos, self.mem_3_pos_text, self.dot_1)
                """Click on navigation dot"""
                self.do_click(self.dot_2, click_after_wait='yes')
                """Click on navigation dot"""
                self.do_click(self.dot_3, click_after_wait='yes')
                self.scroll_to_element(self.scroll_to_2)
                self.member_card(self.mem_4_img, self.mem_4_soc_fb,
                                 self.mem_4_soc_tw, self.mem_4_soc_lk,
                                 self.mem_4_name, self.mem_4_name_text,
                                 self.mem_4_pos, self.mem_4_pos_text, self.dot_3)
