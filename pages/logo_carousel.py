import time

from selenium.webdriver import ActionChains

from utils.config import *


class LogoCarousel:
    widget = '//*[@id="post-2942"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = "Logo Carousel"
    DOC_LINK = '//*[@id="post-2942"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "LOGO CAROUSEL"

    dot_1 = (By.XPATH, f'//*[@id="post-2942"]/div/div/div/div/section[2]/div/div/div'
                       f'/div/div/div/div/div/div[2]/span[1]')

    dot_2 = (By.XPATH, f'//*[@id="post-2942"]/div/div/div/div/section[2]/div/div/div/div'
                       f'/div/div/div/div/div[2]/span[6]')

    img_1 = (By.XPATH, f'//*[@id="post-2942"]/div/div/div/div/section[2]/div/div/div/div'
                       f'/div/div/div/div/div[1]/div/div[7]/div/div/a/img')
    img_2 = (By.XPATH, f'//*[@id="post-2942"]/div/div/div/div/section[2]/div/div/div/div'
                       f'/div/div/div/div/div[1]/div/div[17]/div/div/a/img')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(logo_carousel)

    def testcase(self):
        c = CheckText(self.browser)

        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.DOC_LINK, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 943)")
            time.sleep(1)

            self.browser.find_element(*self.dot_1).click()

            cursor = ActionChains(self.browser)
            logo_1 = self.browser.find_element(*self.img_1)
            logo_2 = self.browser.find_element(*self.img_2)

            cursor.move_to_element(logo_1).perform()

            self.browser.find_element(*self.dot_2).click()
            cursor.move_to_element(logo_2).perform()



