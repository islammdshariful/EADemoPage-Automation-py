from pages.AB_sample import Sample
from pages.advanced_accordion import AdvancedAccordion
from pages.advanced_tabs import AdvancedTabs
from pages.creative_button import CreativeButton
from pages.dual_color_headline import DualColorHeading
from pages.event_calendar import EventCalendar
from pages.flip_box import FlipBox
from pages.info_box import InfoBox
from pages.logo_carousel import LogoCarousel
from pages.protected_content import ProtectedContent
from pages.simple_menu import SimpleMenu
from pages.static_product import StaticProduct
from pages.sticky_video import StickyVideo
from pages.team_members import TeamMember
from pages.team_members_carousel import TeamMemberCarousel
from pages.testimonial_slider import TestimonialSlider
from pages.testimonials import Testimonial
from pages.tooltip import ToolTip


def test_widgets(browser):
    t = Testimonial(browser)
    t.load()
    t.testcase()
    # sv = StickyVideo(browser)
    # sv.load()
    # sv.testcase()
    # tt = ToolTip(browser)
    # tt.load()
    # tt.testcase()
    # pc = ProtectedContent(browser)
    # pc.load()
    # pc.testcase()
    # ts = TestimonialSlider(browser)
    # ts.load()
    # ts.testcase()
    # at = AdvancedTabs(browser)
    # at.load()
    # at.testcase()
    # adva = AdvancedAccordion(browser)
    # adva.load()
    # adva.testcase()
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
