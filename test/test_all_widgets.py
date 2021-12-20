from pages.AB_sample import Sample
from pages.advanced_accordion import AdvancedAccordion
from pages.advanced_data_table import AdvancedDataTable
from pages.advanced_menu import AdvancedMenu
from pages.advanced_tabs import AdvancedTabs
from pages.content_toggle import ContentToggle
from pages.creative_button import CreativeButton
from pages.dual_color_headline import DualColorHeading
from pages.event_calendar import EventCalendar
from pages.feature_list import FeatureList
from pages.flip_box import FlipBox
from pages.info_box import InfoBox
from pages.logo_carousel import LogoCarousel
from pages.offcanvas_content import OffCanvas
from pages.post_block import PostBlock
from pages.protected_content import ProtectedContent
from pages.simple_menu import SimpleMenu
from pages.static_product import StaticProduct
from pages.sticky_video import StickyVideo
from pages.team_members import TeamMember
from pages.team_members_carousel import TeamMemberCarousel
from pages.testimonial_slider import TestimonialSlider
from pages.testimonials import Testimonial
from pages.tooltip import ToolTip

# ------------------------------------------------
# CONTENT ELEMENTS
# ------------------------------------------------

def test_content_toggle(browser):
    ct = ContentToggle(browser)
    ct.load()
    ct.testcase()

def test_advanced_menu(browser):
    am = AdvancedMenu(browser)
    am.load()
    am.testcase()

def test_off_canvas(browser):
    oc = OffCanvas(browser)
    oc.load()
    oc.testcase()

def test_feature_list(browser):
    fl = FeatureList(browser)
    fl.load()
    fl.testcase()

def testimonial(browser):
    t = Testimonial(browser)
    t.load()
    t.testcase()

# def test_sticky_video(browser):
#     sv = StickyVideo(browser)
#     sv.load()
#     sv.testcase()


def test_tooltip(browser):
    tt = ToolTip(browser)
    tt.load()
    tt.testcase()


def test_protected_content(browser):
    pc = ProtectedContent(browser)
    pc.load()
    pc.testcase()


def test_testimonial_slide(browser):
    ts = TestimonialSlider(browser)
    ts.load()
    ts.testcase()


def test_advanced_tab(browser):
    at = AdvancedTabs(browser)
    at.load()
    at.testcase()


def test_advanced_accordion(browser):
    adva = AdvancedAccordion(browser)
    adva.load()
    adva.testcase()


def test_team_member(browser):
    tc = TeamMember(browser)
    tc.load()
    tc.testcase()


def test_infobox(browser):
    ib = InfoBox(browser)
    ib.load()
    ib.testcase()


def test_dual_color_heading(browser):
    dc = DualColorHeading(browser)
    dc.load()
    dc.testcase()


def test_logo_carousel(browser):
    lc = LogoCarousel(browser)
    lc.load()
    lc.testcase()


def test_team_member_carousle(browser):
    tmc = TeamMemberCarousel(browser)
    tmc.load()
    tmc.testcase()


def test_simple_menu(browser):
    smp = SimpleMenu(browser)
    smp.load()
    smp.testcase()


def test_flip_box(browser):
    fpb = FlipBox(browser)
    fpb.load()
    fpb.testcase()


def test_creative_button(browser):
    cb = CreativeButton(browser)
    cb.load()
    cb.testcase()


def test_static_product(browser):
    sp = StaticProduct(browser)
    sp.load()
    sp.testcase()

# def test_event_calender(browser):
#     evc = EventCalendar(browser)
#     evc.load()
#     evc.testcase()

# ------------------------------------------------
# DYNAMIC CONTENT ELEMENTS
# ------------------------------------------------

# def test_advanced_data_table(browser):
#     adt = AdvancedDataTable(browser)
#     adt.load()
#     adt.testcase()

# def test_post_block(browser):
#     pb = PostBlock(browser)
#     pb.load()
#     pb.testcase()