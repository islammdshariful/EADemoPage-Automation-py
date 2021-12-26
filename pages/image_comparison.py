from selenium.webdriver import ActionChains

from utils.config import *


class ImageComparison:
    widget = '//*[@id="post-17"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Image Comparison'
    doc_link = '//*[@id="post-17"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "IMAGE COMPARISON"

    handle = (By.XPATH, f'//*[@id="eael-image-comparison-23558b85"]/div[2]')


    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(image_comparison)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1082)")
            time.sleep(1)
            cursor = ActionChains(self.browser)
            element = self.browser.find_element(*self.handle)
            cursor.click_and_hold(element).drag_and_drop_by_offset(element, 1376, 1598)
            # cursor.drag_and_drop_by_offset(element, 1376, 1598)
            self.browser.execute_script("document.getElementsByClassName('twentytwenty-handle').style = 'left: 978.5px;';")