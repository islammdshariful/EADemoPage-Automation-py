from pages.basepage import BasePage
from utils.config import *


class ToolTip(BasePage, Helper):
    widget = '//*[@id="post-2455"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
             '/div/div/div[2]/div/div/div[1]/div/h2'
    widget_name = 'Tooltip'
    doc_link = '//*[@id="post-2455"]/div/div/div/div/section[1]/div[4]/div/div[2]/div/div/section' \
               '/div/div/div[2]/div/div/div[3]/div/div/a'
    doc_name = "TOOLTIP"

    tooltip_1_img = (By.XPATH, f'//*[@id="post-2455"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                               f'/div/div/div[1]/div/div/div/div/div/span[1]/img')
    tooltip_1 = (By.XPATH, f'//*[@id="post-2455"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                           f'/div/div/div[1]/div/div/div/div/div/span[2]')
    tooltip_1_text = "Search Engine Optimization"

    tooltip_2_img = (By.XPATH, f'//*[@id="post-2455"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]' \
                               f'/div/div/div[2]/div/div/div/div/div/span[1]/img')
    tooltip_2 = (By.XPATH, f'//*[@id="post-2455"]/div/div/div/div/section[2]/div/div/div/div/div/section[2]'
                           f'/div/div/div[2]/div/div/div/div/div/span[2]')
    tooltip_2_text = "Search Engine Optimization"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.tooltip)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1010)
                """Check image visibility"""
                self.is_visible(self.tooltip_1_img, "Tool Tip 1 image is not visible.")
                self.is_visible(self.tooltip_2_img, "Tool Tip 2 image is not visible.")
                """Move to image 1"""
                self.move_cursor_to(self.tooltip_1_img)
                """Check image 1 tooltip"""
                self.check_text_matches_with(self.tooltip_1, self.tooltip_1_text)
                """Move to image 2"""
                self.move_cursor_to(self.tooltip_2_img)
                """Check image 2 tooltip"""
                self.check_text_matches_with(self.tooltip_2, self.tooltip_2_text)
