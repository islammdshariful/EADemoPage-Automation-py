from pages.basepage import BasePage
from utils.config import *


class ProtectedContent(BasePage, Helper):
    widget = '//*[@id="post-3712"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Protected Content'
    doc_link = '//*[@id="post-3712"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA PROTECTED CONTENT"

    message = (By.XPATH, f'//*[@id="post-3712"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                         f'/div/div/div[2]/div/div/div/div/div[1]/div/p')
    message_text = "This section is password protected. So use 1234 to access the content."
    password = (By.XPATH, f'//*[@id="eael_protected_content_form_3d01145b"]/input[1]')
    button = (By.XPATH, f'//*[@id="eael_protected_content_form_3d01145b"]/input[3]')
    img = (By.XPATH, f'//*[@id="eael-protected-content-render-3d01145b"]/div/div/div/section/div/div/div/div/div/'
                     f'div[1]/div/div/img')
    title = (By.XPATH, f'//*[@id="eael-protected-content-render-3d01145b"]/div/div/div/section'
                       f'/div/div/div/div/div/div[2]/div/h2')
    title_text = "Ya! You Have Typed The Right Password"
    des = (By.XPATH, f'//*[@id="eael-protected-content-render-3d01145b"]/div/div/div/section'
                     f'/div/div/div/div/div/div[3]/div/div')
    des_text = "Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or " \
               "web designs. The passage is attributed to an unknown typesetter in the 15th century who is thought" \
               " to have scrambled parts of Cicero’s De Finibus Bonorum et Malorum for use in a type specimen book."

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.protected_content)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(603)
                """Help text"""
                self.check_text_matches_with(self.message, self.message_text)
                """Enter credentials"""
                self.browser.find_element(*self.password).click()
                self.do_click(self.password)
                self.clear_field(self.password)
                self.do_send_keys(self.password, "1234")
                self.do_click(self.button)
                """Checking protected contents"""
                self.is_visible(self.img, "Image is not visible.")
                self.check_text_matches_with(self.title, self.title_text)
                self.check_text_matches_with(self.des, self.des_text)
