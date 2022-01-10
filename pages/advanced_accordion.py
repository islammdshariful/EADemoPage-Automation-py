import time

from selenium.webdriver import ActionChains

from utils.config import *


class AdvancedAccordion:
    widget = '//*[@id="post-2453"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Advanced Accordion'
    doc_link = '//*[@id="post-2453"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "ADVANCED ACCORDION"
    accor_1_icon = (By.XPATH, f'//*[@id="font-awesome-icons-used"]/i[1]')
    accor_1_title = (By.XPATH, f'//*[@id="font-awesome-icons-used"]/span')
    accor_1_title_text = "Font Awesome Icons Used"
    accor_1_des = (By.XPATH, f'//*[@id="elementor-tab-content-1941"]/p')
    accor_1_des_text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio, neque qui velit." \
                       " Magni dolorum quidem ipsam eligendi, totam, facilis laudantium cum accusamus ullam " \
                       "voluptatibus commodi numquam, error, est. Ea, consequatur."
    accor_2_icon = (By.XPATH, f'//*[@id="free-demo-content-installations"]/i[1]')
    accor_2_title = (By.XPATH, f'//*[@id="free-demo-content-installations"]/span')
    accor_2_title_text = "Free Demo Content Installations"
    accor_2_des = (By.XPATH, f'//*[@id="elementor-tab-content-1942"]/p[2]')
    accor_2_des_text = "Netflix has struck a deal set up a permanent production base at Shepperton Studios, " \
                       "home to films from Alien to Mary Poppins Returns."
    accor_3_icon = (By.XPATH, f'//*[@id="visual-page-builder"]/i[1]')
    accor_3_title = (By.XPATH, f'//*[@id="visual-page-builder"]/span')
    accor_3_title_text = "Visual Page Builder"
    accor_3_des = (By.XPATH, f'//*[@id="elementor-tab-content-1943"]/p[2]')
    accor_3_des_text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio, neque qui velit. " \
                       "Magni dolorum quidem ipsam eligendi, totam, facilis laudantium cum accusamus ullam " \
                       "voluptatibus commodi numquam, error, est. Ea, consequatur."

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(advanced_accordion)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1047)")
            time.sleep(1)

            accor_1 = self.browser.find_element(*self.accor_1_title)
            accor_2 = self.browser.find_element(*self.accor_2_title)
            accor_3 = self.browser.find_element(*self.accor_3_title)

            assert_that(self.browser.find_element(*self.accor_1_title).text).is_equal_to(self.accor_1_title_text)
            assert_that(self.browser.find_element(*self.accor_2_title).text).is_equal_to(self.accor_2_title_text)
            assert_that(self.browser.find_element(*self.accor_3_title).text).is_equal_to(self.accor_3_title_text)
            if self.browser.find_element(*self.accor_1_icon).is_displayed():
                print("ACCORDION 1 ICON IS VISIBLE")
                if self.browser.find_element(*self.accor_2_icon).is_displayed():
                    print("ACCORDION 2 ICON IS VISIBLE")
                    if self.browser.find_element(*self.accor_3_icon).is_displayed():
                        print("ACCORDION 3 ICON IS VISIBLE")
                    else:
                        print("ACCORDION 3 ICON IS NOT VISIBLE")
                else:
                    print("ACCORDION 2 ICON IS NOT VISIBLE")
            else:
                print("ACCORDION 1 ICON IS NOT VISIBLE")

            cursor_1 = ActionChains(self.browser)
            cursor_2 = ActionChains(self.browser)
            cursor_3 = ActionChains(self.browser)

            cursor_1.move_to_element(accor_2).click().perform()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.accor_2_des).text).is_equal_to(self.accor_2_des_text)
            if not self.browser.find_element(*self.accor_1_des).is_displayed():
                if not self.browser.find_element(*self.accor_3_des).is_displayed():
                    print("ACCORDION 2 PASSED")
                else:
                    print("ACCORDION 2 FAILED")
            else:
                print("ACCORDION 2 FAILED")

            cursor_2.move_to_element(accor_3).click().perform()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.accor_3_des).text).is_equal_to(self.accor_3_des_text)
            if not self.browser.find_element(*self.accor_1_des).is_displayed():
                if not self.browser.find_element(*self.accor_2_des).is_displayed():
                    print("ACCORDION 3 PASSED")
                else:
                    print("ACCORDION 3 FAILED")
            else:
                print("ACCORDION 3 FAILED")

            cursor_3.move_to_element(accor_1).click().perform()
            time.sleep(.5)
            assert_that(self.browser.find_element(*self.accor_1_des).text).is_equal_to(self.accor_1_des_text)
            if not self.browser.find_element(*self.accor_2_des).is_displayed():
                if not self.browser.find_element(*self.accor_3_des).is_displayed():
                    print("ACCORDION 1 PASSED")
                else:
                    print("ACCORDION 1 FAILED")
            else:
                print("ACCORDION 1 FAILED")



