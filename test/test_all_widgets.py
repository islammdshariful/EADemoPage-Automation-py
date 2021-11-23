from pages.AB_sample import Sample
from pages.advanced_accordion import AdvancedAccordion
from pages.creative_button import CreativeButton
from pages.dual_color_headline import DualColorHeading
from pages.event_calendar import EventCalendar
from pages.flip_box import FlipBox
from pages.info_box import InfoBox
from pages.logo_carousel import LogoCarousel
from pages.simple_menu import SimpleMenu
from pages.static_product import StaticProduct
from pages.team_members import TeamMember
from pages.team_members_carousel import TeamMemberCarousel


def test_widgets(browser):
    adva = AdvancedAccordion(browser)
    adva.load()
    adva.testcase()
    # tc = TeamMember(browser)
    # tc.load()
    # tc.testcase()
    # ib = InfoBox(browser)
    # ib.load()
    # ib.testcase()
    # dc = DualColorHeading(browser)
    # dc.load()
    # dc.testcase()
    # lc = LogoCarousel(browser)
    # lc.load()
    # lc.testcase()
    # tmc = TeamMemberCarousel(browser)
    # tmc.load()
    # tmc.testcase()
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
    # evc = EventCalendar(browser)
    # evc.load()
    # evc.testcase()
    # do = Sample(browser)
    # do.load()
    # do.do_something()

    browser.quit()
