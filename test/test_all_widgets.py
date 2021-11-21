from pages.creative_button import CreativeButton
from pages.event_calendar import EventCalendar
from pages.flip_box import FlipBox
from pages.simple_menu import SimpleMenu
from pages.static_product import StaticProduct


def test_widgets(browser):
    # smp = SimpleMenu(browser)
    # smp.load()
    # smp.testcase()
    # fpb = FlipBox(browser)
    # fpb.load()
    # fpb.testcase()
    # cb = CreativeButton(browser)
    # cb.load()
    # cb.testcase()
    # sp = StaticProduct(browser)
    # sp.load()
    # sp.testcase()
    evc = EventCalendar(browser)
    evc.load()
    evc.testcase()

    browser.quit()
