from selenium.webdriver import Keys

from utils.config import *


class LightboxModal(Helper, Snapshot):
    widget = '//*[@id="post-40"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Lightbox & Modal'
    doc_link = '//*[@id="post-40"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "LIGHTBOX & MODAL"

    button = (By.XPATH, f'//*[@id="post-40"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]/div/div/div[4]'
                        f'/div/div/div/div/div[1]/div')
    cross_btn = (By.XPATH, f"//button[normalize-space()='×']")
    img = f'/html/body/div[2]/div/div[1]/div/div/img'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.lightbox_modal)

    def testcase(self):
        with soft_assertions():
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.browser.execute_script("window.scrollTo(0, 903)")
                time.sleep(1)
                self.browser.find_element(*self.button).click()
                time.sleep(1)
                self.check_visibility(self.img, "Image is not visible.")

                # this is for download image
                # self.download_image(self.img, "LightboxModal")

                self.download_image_comparison(self.img, "LightboxModal")

                self.browser.find_element(*self.cross_btn).click()
