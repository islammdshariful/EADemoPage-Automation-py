from selenium.webdriver import ActionChains

from utils.config import *


class LightboxModal:
    widget = '//*[@id="post-40"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Lightbox & Modal'
    doc_link = '//*[@id="post-40"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "LIGHTBOX & MODAL"

    button = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div/main/article/div/div/div/div/section[2]/div/div/div'
                        f'/div/div/section[2]/div/div/div[4]/div/div/div/div/div[1]/div/span')
    cross_btn = (By.XPATH, f'/html/body/div[2]/div/div[1]/div/button')
    img = f'/html/body/div[2]/div/div[1]/div/div/img'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(lightbox_modal)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 903)")
            self.browser.find_element(*self.button).click()
            time.sleep(1)
            if self.browser.find_element(By.XPATH, self.img).is_displayed():
                assert_that(display).is_equal_to(1)
            else:
                assert_that(display).is_equal_to("Image is not visible")

            ss = ImageComparison(self.browser)

            # this is for download image
            # ss.download_image(self.img, "LightboxModal")

            ss.download_image_comparison(self.img, "LightboxModal")

            self.browser.find_element(*self.cross_btn).click()