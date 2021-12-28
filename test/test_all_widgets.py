from pages.AB_sample import Sample
from pages.advanced_accordion import AdvancedAccordion
from pages.advanced_data_table import AdvancedDataTable
from pages.advanced_google_map import AdvancedGoogleMap
from pages.advanced_menu import AdvancedMenu
from pages.advanced_search import AdvancedSearch
from pages.advanced_tabs import AdvancedTabs
from pages.call_to_action import CallToAction
from pages.content_ticker import ContentTicker
from pages.content_timeline import ContentTimeline
from pages.content_toggle import ContentToggle
from pages.countdown import Countdown
from pages.creative_button import CreativeButton
from pages.data_table import DataTable
from pages.divider import Divider
from pages.dual_color_headline import DualColorHeading
from pages.dynamic_gallery import DynamicGallery
from pages.event_calendar import EventCalendar
from pages.fancy_text import FancyText
from pages.feature_list import FeatureList
from pages.filterable_gallery import FilterableGallery
from pages.flip_box import FlipBox
from pages.image_hotspots import ImageHotspots
from pages.image_scroller import ImageScroller
from pages.info_box import InfoBox
from pages.interactive_cards import InteractiveCards
from pages.interactive_circle import InteractiveCircle
from pages.interactive_promo import InteractivePromo
from pages.logo_carousel import LogoCarousel
from pages.offcanvas_content import OffCanvas
from pages.one_page_nav import OnePageNav
from pages.post_block import PostBlock
from pages.post_carousel import PostCarousel
from pages.post_grid import PostGrid
from pages.post_list import PostList
from pages.post_timeline import PostTimeline
from pages.price_menu import PriceMenu
from pages.pricing_table import PricingTable
from pages.protected_content import ProtectedContent
from pages.simple_menu import SimpleMenu
from pages.static_product import StaticProduct
from pages.sticky_video import StickyVideo
from pages.team_members import TeamMember
from pages.team_members_carousel import TeamMemberCarousel
from pages.testimonial_slider import TestimonialSlider
from pages.testimonials import Testimonial
from pages.tooltip import ToolTip
from pages.counter import Counter
from pages.image_comparison import ImageComparison


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


def test_advanced_search(browser):
    ads = AdvancedSearch(browser)
    ads.load()
    ads.testcase()


# ------------------------------------------------
# DYNAMIC CONTENT ELEMENTS
# ------------------------------------------------

def test_advanced_data_table(browser):
    adt = AdvancedDataTable(browser)
    adt.load()
    adt.testcase()


def test_post_block(browser):
    pb = PostBlock(browser)
    pb.load()
    pb.testcase()


def test_post_timeline(browser):
    ptl = PostTimeline(browser)
    ptl.load()
    ptl.testcase()


def test_smart_post_list(browser):
    spl = PostList(browser)
    spl.load()
    spl.testcase()


def test_google_map(browser):
    gm = AdvancedGoogleMap(browser)
    gm.load()
    gm.testcase()


def test_content_ticker(browser):
    ct = ContentTicker(browser)
    ct.load()
    ct.testcase()


def test_content_timeline(browser):
    ct = ContentTimeline(browser)
    ct.load()
    ct.testcase()


def test_dynamic_gallery(browser):
    dg = DynamicGallery(browser)
    dg.load()
    dg.testcase()


def test_post_grid(browser):
    pg = PostGrid(browser)
    pg.load()
    pg.testcase()


def test_data_table(browser):
    dt = DataTable(browser)
    dt.load()
    dt.testcase()


def test_post_carousel(browser):
    pc = PostCarousel(browser)
    pc.load()
    pc.testcase()


# ------------------------------------------------
# MARKETING ELEMENTS
# ------------------------------------------------

def test_pricing_table(browser):
    pt = PricingTable(browser)
    pt.load()
    pt.testcase()


def test_call_to_action(browser):
    cta = CallToAction(browser)
    cta.load()
    cta.testcase()


def test_price_menu(browser):
    pm = PriceMenu(browser)
    pm.load()
    pm.testcase()


# ------------------------------------------------
# CREATIVE ELEMENTS
# ------------------------------------------------

def test_interactive_promo(browser):
    ip = InteractivePromo(browser)
    ip.load()
    ip.testcase()


def test_interactive_cards(browser):
    ic = InteractiveCards(browser)
    ic.load()
    ic.testcase()


def test_one_page_nav(browser):
    opn = OnePageNav(browser)
    opn.load()
    opn.testcase()


# def test_image_comparison(browser):
#     ic = ImageComparison(browser)
#     ic.load()
#     ic.testcase()


def test_filterable_gallery(browser):
    fg = FilterableGallery(browser)
    fg.load()
    fg.testcase()


def test_interactive_circle(browser):
    ic = InteractiveCircle(browser)
    ic.load()
    ic.testcase()


def test_image_hotspots(browser):
    ih = ImageHotspots(browser)
    ih.load()
    ih.testcase()


def test_image_scroller(browser):
    imgs = ImageScroller(browser)
    imgs.load()
    imgs.testcase()


def test_divider(browser):
    d = Divider(browser)
    d.load()
    d.testcase()


def test_fancy_text(browser):
    ft = FancyText(browser)
    ft.load()
    ft.testcase()


def test_counter(browser):
    c = Counter(browser)
    c.load()
    c.testcase()


def test_countdown(browser):
    c = Countdown(browser)
    c.load()
    c.testcase()

