from pages.flip_box import FlipBox
from pages.simple_menu import SimpleMenu


def test_widgets(browser):
    # smp = SimpleMenu(browser)
    # smp.load()
    # smp.testcase()
    fpb = FlipBox(browser)
    fpb.load()
    fpb.testcase()

    browser.quit()
