from selenium.webdriver import ActionChains

from utils.config import *


class FlipCarousel:
    widget = '//*[@id="post-1616"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Flip Carousel'
    doc_link = '//*[@id="post-1616"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "FLIP CAROUSEL"

    flip_1 = (By.XPATH, f'//*[@id="post-1616"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div'
                        f'/div/div/div/div/div/div/ul/li[1]/div/img')
    flip_2 = (By.XPATH, f'//*[@id="post-1616"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div'
                        f'/div/div/div/div/div/div/ul/li[2]/div/img')
    flip_3 = (By.XPATH, f'//*[@id="post-1616"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div'
                        f'/div/div/div/div/div/div/ul/li[3]/div/img')
    flip_4 = (By.XPATH, f'//*[@id="post-1616"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div'
                        f'/div/div/div/div/div/div/ul/li[4]/div/img')
    flip_5 = (By.XPATH, f'//*[@id="post-1616"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div'
                        f'/div/div/div/div/div/div/ul/li[5]/div/img')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(flip_carousel)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 905)")
            self.browser.find_element(*self.flip_2).click()
            time.sleep(.5)
            self.browser.find_element(*self.flip_1).click()
            time.sleep(.5)
            self.browser.find_element(*self.flip_2).click()
            time.sleep(.5)
            self.browser.find_element(*self.flip_3).click()
            time.sleep(.5)
            self.browser.find_element(*self.flip_4).click()
            time.sleep(.5)
            self.browser.find_element(*self.flip_5).click()