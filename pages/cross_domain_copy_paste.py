from selenium.webdriver import ActionChains

from utils.config import *


class CrossDomainCopyPaste:
    widget = '//*[@id="post-271333"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Cross-Domain Copy Paste'
    doc_link = '//*[@id="post-271333"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA CROSS-DOMAIN COPY PASTE"

    img = f'//*[@id="post-271333"]/div/div/div/div/section[3]/div[2]/div/div/div/div/section' \
          f'/div/div/div/div/div/div/div/div/img'
    src = "https://aadhmqulyo.cloudimg.io/v7/essential-addons.com/elementor/wp-content/uploads/2021/12/Section-1.gif"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(cross_domain_copy_paste)

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_widget_name(self.widget, self.widget_name)
            if check_doc:
                c.check_doc(self.doc_link, self.doc_name)

            self.browser.execute_script("window.scrollTo(0, 1038)")
            img_src = self.browser.find_element(By.XPATH, self.img)
            assert_that(img_src.get_attribute("src")).is_equal_to(self.src)

            ic = ImageComparison(self.browser)

            # This is for downloading the gif
            # ic.download_gif(self.img, "CrossDomainCopyPaste")

            ic.download_gif_comparison(self.img, "CrossDomainCopyPaste")
