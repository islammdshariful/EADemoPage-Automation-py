from pages.basepage import BasePage
from utils.config import *


class AdvancedAccordion(BasePage, Helper):
    widget = '//*[@id="post-2453"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Advanced Accordion'
    doc_link = '//*[@id="post-2453"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "ADVANCED ACCORDION"
    accor_1_icon = (By.XPATH, f'//*[@id="font-awesome-icons-used"]/i[1]')
    accor_1_title = (By.XPATH, f"//div[@id='eael-adv-accordion-73d0d346']//span[@class='eael-accordion-tab-title']"
                               f"[normalize-space()='Font Awesome Icons Used']")
    accor_1_title_text = "Font Awesome Icons Used"
    accor_1_des = (By.XPATH, f'//*[@id="elementor-tab-content-1941"]/p')
    accor_1_des_text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio, neque qui velit." \
                       " Magni dolorum quidem ipsam eligendi, totam, facilis laudantium cum accusamus ullam " \
                       "voluptatibus commodi numquam, error, est. Ea, consequatur."
    accor_2_icon = (By.XPATH, f'//*[@id="free-demo-content-installations"]/i[1]')
    accor_2_title = (By.XPATH, f"//div[@id='eael-adv-accordion-73d0d346']//span[@class='eael-accordion-tab-title']"
                               f"[normalize-space()='Free Demo Content Installations']")
    accor_2_title_text = "Free Demo Content Installations"
    accor_2_des = (By.XPATH, f'//*[@id="elementor-tab-content-1942"]/p[2]')
    accor_2_des_text = "Netflix has struck a deal set up a permanent production base at Shepperton Studios, " \
                       "home to films from Alien to Mary Poppins Returns."
    accor_3_icon = (By.XPATH, f'//*[@id="visual-page-builder"]/i[1]')
    accor_3_title = (By.XPATH, f"//div[@id='eael-adv-accordion-73d0d346']//span[@class='eael-accordion-tab-title']"
                               f"[normalize-space()='Visual Page Builder']")
    accor_3_title_text = "Visual Page Builder"
    accor_3_des = (By.XPATH, f'//*[@id="elementor-tab-content-1943"]/p[2]')
    accor_3_des_text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio, neque qui velit. " \
                       "Magni dolorum quidem ipsam eligendi, totam, facilis laudantium cum accusamus ullam " \
                       "voluptatibus commodi numquam, error, est. Ea, consequatur."

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.advanced_accordion)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1047)
                """Check accordion title"""
                self.check_text_matches_with(self.accor_1_title, self.accor_1_title_text)
                self.check_text_matches_with(self.accor_2_title, self.accor_2_title_text)
                self.check_text_matches_with(self.accor_3_title, self.accor_3_title_text)
                """Check accordion icon"""
                self.is_visible(self.accor_1_icon, "Accordion 1 icon is not visible")
                self.is_visible(self.accor_2_icon, "Accordion 2 icon is not visible")
                self.is_visible(self.accor_3_icon, "Accordion 3 icon is not visible")
                """Click on accordion tab 2"""
                self.move_cursor_and_click(self.accor_2_title)
                """Check accordion tab 2's description"""
                self.check_text_matches_with(self.accor_2_des, self.accor_2_des_text)
                """Checking if other tabs are closed"""
                if not self.is_displaying(*self.accor_1_des):
                    if not self.is_displaying(*self.accor_3_des):
                        pass
                    else:
                        assert_that(1).is_equal_to("Tab three open, FAILED")
                else:
                    assert_that(1).is_equal_to("Tab one open, FAILED")
                """Click on accordion tab 3"""
                self.move_cursor_and_click(self.accor_3_title)
                """Check accordion tab 3's description"""
                self.check_text_matches_with(self.accor_3_des, self.accor_3_des_text)
                """Checking if other tabs are closed"""
                if not self.is_displaying(*self.accor_1_des):
                    if not self.is_displaying(*self.accor_2_des):
                        pass
                    else:
                        assert_that(1).is_equal_to("Tab two open, FAILED")

                else:
                    assert_that(1).is_equal_to("Tab one open, FAILED")
                """Click on accordion tab 2"""
                self.move_cursor_and_click(self.accor_1_title)
                """Check accordion tab 2's description"""
                self.check_text_matches_with(self.accor_1_des, self.accor_1_des_text)
                """Checking if other tabs are closed"""
                if not self.is_displaying(*self.accor_2_des):
                    if not self.is_displaying(*self.accor_3_des):
                        pass
                    else:
                        assert_that(1).is_equal_to("Tab three open, FAILED")
                else:
                    assert_that(1).is_equal_to("Tab two open, FAILED")



