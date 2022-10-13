from utils.config import *


class AdvancedTooltip(BasePage, Helper):
    widget = '//*[@id="post-5622"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'Advanced Tooltip'
    doc_link = '//*[@id="post-5622"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA ADVANCED TOOLTIP"

    card = (By.XPATH, f'//*[@id="eael-section-tooltip-4b0da25c"]/div/div/div')
    tooltip = (By.XPATH, f'//*[@id="tippy-1"]/div')
    tooltip_text = "Save 10% in Basic Plan"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.advanced_tooltip)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1002)

                self.move_cursor_to(self.card)
                self.is_visible(self.tooltip, "Tooltip is not visible.")

                self.check_text_matches_with(self.tooltip, self.tooltip_text)
