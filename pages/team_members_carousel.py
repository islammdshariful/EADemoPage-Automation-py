import time

from selenium.webdriver import ActionChains

from utils.config import *


class TeamMemberCarousel:
    widget = '//*[@id="post-2946"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = "Team Members Carousel"
    DOC_LINK = '//*[@id="post-2946"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/' \
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

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(team_members_carousel)

    def testcase(self):
        c = CheckText(self.browser)

        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.DOC_LINK, self.doc_name)

            cursor = ActionChains(self.browser)
            scrol_ele = self.browser.find_element(By.XPATH, '//*[@id="post-2946"]/div/div/div/div/section[2]/div/div/'
                                                            'div/div/div/section/div/div/div[2]/div/div/div[1]/div/h3')
            self.browser.execute_script("arguments[0].scrollIntoView();", scrol_ele)

            mem_1 = self.browser.find_element(*self.mem_1_img)
            mem_2 = self.browser.find_element(*self.mem_2_img)

            cursor.move_to_element(mem_1).perform()
            if self.browser.find_element(*self.mem_1_soc_fb).is_displayed():
                print("MEMBER 1 FACEBOOK ICON IS VISIBLE")
                if self.browser.find_element(*self.mem_1_soc_tw).is_displayed():
                    print("MEMBER 1 TWITTER ICON IS VISIBLE")
                    if self.browser.find_element(*self.mem_1_soc_lk).is_displayed():
                        print("MEMBER 1 LINKEDIN ICON IS VISIBLE")
                    else:
                        print("MEMBER 1 LINKEDINICON IS NOT VISIBLE")
                else:
                    print("MEMBER 1 FACEBOOK ICON IS NOT VISIBLE")
            else:
                print("MEMBER 1 FACEBOOK ICON IS NOT VISIBLE")

            assert_that(self.browser.find_element(*self.mem_1_name).text).is_equal_to(self.mem_name_text)
            assert_that(self.browser.find_element(*self.mem_1_pos).text).is_equal_to(self.mem_pos_text)

            self.browser.find_element(*self.prev_button).click()
            self.browser.find_element(*self.prev_button).click()
            self.browser.find_element(*self.next_button).click()
            self.browser.find_element(*self.next_button).click()

            cursor.move_to_element(mem_2).perform()
            if self.browser.find_element(*self.mem_2_soc_fb).is_displayed():
                print("MEMBER 2 FACEBOOK ICON IS VISIBLE")
                if self.browser.find_element(*self.mem_2_soc_tw).is_displayed():
                    print("MEMBER 2 TWITTER ICON IS VISIBLE")
                    if self.browser.find_element(*self.mem_2_soc_lk).is_displayed():
                        print("MEMBER 2 LINKEDIN ICON IS VISIBLE")
                    else:
                        print("MEMBER 2 LINKEDINICON IS NOT VISIBLE")
                else:
                    print("MEMBER 2 FACEBOOK ICON IS NOT VISIBLE")
            else:
                print("MEMBER 2 FACEBOOK ICON IS NOT VISIBLE")

            assert_that(self.browser.find_element(*self.mem_2_name).text).is_equal_to(self.mem_name_text)
            assert_that(self.browser.find_element(*self.mem_2_pos).text).is_equal_to(self.mem_pos_text)

            # self.browser.execute_script("window.scrollTo(0, 3566)")
            scrol_ele_1 = self.browser.find_element(By.XPATH, '//*[@id="post-2946"]/div/div/div/div/section[5]/div/div'
                                                            '/div/div/div/section/div/div/div[2]/div/div/div[1]/div/h3')
            self.browser.execute_script("arguments[0].scrollIntoView();", scrol_ele_1)

            self.browser.find_element(*self.dot_1).click()
            time.sleep(.5)
            if self.browser.find_element(*self.mem_3_img).is_displayed():
                print("MEMBER 3 IMAGE IS VISIBLE")
            else:
                print("MEMBER 3 IMAGE IS NOT VISIBLE")
            assert_that(self.browser.find_element(*self.mem_3_name).text).is_equal_to(self.mem_3_name_text)
            assert_that(self.browser.find_element(*self.mem_3_name).text).is_equal_to(self.mem_3_pos_text)
            mem_3_fb = self.browser.find_element(*self.mem_3_soc_fb)
            mem_3_tw = self.browser.find_element(*self.mem_3_soc_tw)
            mem_3_lk = self.browser.find_element(*self.mem_3_soc_lk)
            cursor.move_to_element(mem_3_fb).move_to_element(mem_3_tw).move_to_element(mem_3_lk).perform()
            self.browser.find_element(*self.dot_2).click()
            time.sleep(.5)
            self.browser.find_element(*self.dot_3).click()
            time.sleep(.5)
            if self.browser.find_element(*self.mem_4_img).is_displayed():
                print("MEMBER 4 IMAGE IS NOT VISIBLE")
            else:
                print("MEMBER 4 IMAGE IS NOT VISIBLE")
            assert_that(self.browser.find_element(*self.mem_4_name).text).is_equal_to(self.mem_4_name_text)
            assert_that(self.browser.find_element(*self.mem_4_name).text).is_equal_to(self.mem_4_pos_text)
            mem_4_fb = self.browser.find_element(*self.mem_4_soc_fb)
            mem_4_tw = self.browser.find_element(*self.mem_4_soc_tw)
            mem_4_lk = self.browser.find_element(*self.mem_4_soc_lk)

            self.browser.execute_script("arguments[0].scrollIntoView();", scrol_ele_1)
            self.browser.find_element(*self.dot_3).click()
            time.sleep(1)
            cursor.move_to_element(mem_4_fb).move_to_element(mem_4_tw).move_to_element(mem_4_lk).perform()
            







