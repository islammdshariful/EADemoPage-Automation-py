from utils.config import *


class ParticleEffect(BasePage, Helper):
    widget = '//*[@id="post-4577"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
             '/div/div/div[1]/div/h2'
    widget_name = 'Particles'
    doc_link = '//*[@id="post-4577"]/div/div/div/div/section[1]/div[3]/div/div[2]/div/div/section/div/div/div[2]' \
               '/div/div/div[3]/div/div/a/span/span'
    doc_name = "EA PARTICLES"

    def __init__(self, browser):
        super().__init__(browser)

    def run(self):
        with soft_assertions():
            """Go to page"""
            self.go_to(self.particle_effect)
            """Checking widget name"""
            self.check_widget_name(self.widget, self.widget_name)
            if self.check_doc:
                """Checking widget's documentation"""
                self.check_documents(self.doc_link, self.doc_name)
            else:
                self.scroll_to(1137)

                self.cursor.move_by_offset(100, 100).perform()

                self.cursor.move_by_offset(100, 50).perform()

                self.scroll_to(2121)

                self.cursor.move_by_offset(10, 100).perform()

                self.cursor.move_by_offset(10, 50).perform()

                self.scroll_to(3108)
                for i in range(3108, 5632, 100):
                    self.browser.execute_script("window.scrollTo(0, " + str(i) + ")")
