from pages.Wpforms import Wpforms
from pages.advanced_accordion import AdvancedAccordion
from pages.advanced_data_table import AdvancedDataTable
from pages.advanced_google_map import AdvancedGoogleMap
from pages.advanced_menu import AdvancedMenu
from pages.advanced_search import AdvancedSearch
from pages.advanced_tabs import AdvancedTabs
from pages.advanced_tooltip import AdvancedTooltip
from pages.betterdocs_category_box import BetterdocsCategoryBox
from pages.betterdocs_category_grid import BetterdocsCategoryGrid
from pages.betterdocs_search_form import BetterdocsSearchForm
from pages.caldera_forms import CalderaForms
from pages.call_to_action import CallToAction
from pages.contact_form_7 import ContactForm7
from pages.content_protection import ContentProtection
from pages.content_ticker import ContentTicker
from pages.content_timeline import ContentTimeline
from pages.content_toggle import ContentToggle
from pages.countdown import Countdown
from pages.creative_button import CreativeButton
from pages.cross_domain_copy_paste import CrossDomainCopyPaste
from pages.data_table import DataTable
from pages.divider import Divider
from pages.dual_color_headline import DualColorHeading
from pages.duplicator import Duplicator
from pages.dynamic_gallery import DynamicGallery
from pages.event_calendar import EventCalendar
from pages.facebook_feed import FacebookFeed
from pages.fancy_text import FancyText
from pages.feature_list import FeatureList
from pages.filterable_gallery import FilterableGallery
from pages.flip_box import FlipBox
from pages.flip_carousel import FlipCarousel
from pages.fluent_forms import FluentForms
from pages.formstack import Formstack
from pages.gravity_forms import GravityForms
from pages.image_accordion import ImageAccordion
from pages.image_hotspots import ImageHotspots
from pages.image_scroller import ImageScroller
from pages.info_box import InfoBox
from pages.instagram_feed import InstagramFeed
from pages.interactive_cards import InteractiveCards
from pages.interactive_circle import InteractiveCircle
from pages.interactive_promo import InteractivePromo
from pages.learndash_course_list import LearndashCourseList
from pages.lightbox_modal import LightboxModal
from pages.login_register_form import LoginRegisterForm
from pages.logo_carousel import LogoCarousel
from pages.mailchimp import Mailchimp
from pages.ninja_forms import NinjaForms
from pages.offcanvas_content import OffCanvas
from pages.one_page_nav import OnePageNav
from pages.parallax_scrolling import ParallaxScrolling
from pages.particle_effect import ParticleEffect
from pages.post_block import PostBlock
from pages.post_carousel import PostCarousel
from pages.post_grid import PostGrid
from pages.post_list import PostList
from pages.post_timeline import PostTimeline
from pages.price_menu import PriceMenu
from pages.pricing_table import PricingTable
from pages.protected_content import ProtectedContent
from pages.reading_progress import ReadingProgress
from pages.scroll_to_top import ScrollToTop
from pages.simple_menu import SimpleMenu
from pages.static_product import StaticProduct
from pages.sticky_video import StickyVideo
from pages.table_of_content import TableOfContent
from pages.team_members import TeamMember
from pages.team_members_carousel import TeamMemberCarousel
from pages.testimonial_slider import TestimonialSlider
from pages.testimonials import Testimonial
from pages.tooltip import ToolTip
from pages.counter import Counter
from pages.image_comparison import ImageComparison
from pages.progress_bar import ProgressBar
from pages.twitter_feed import TwitterFeed
from pages.twitter_feed_carousel import TwitterFeedCarousel
from pages.weforms import Weforms
from pages.woo_cart import WooCart
from pages.woo_checkout import WooCheckout
from pages.woo_product_carousel import WooProductCarousel
from pages.woo_product_compare import WooProductCompare
from pages.woo_product_gallery import WooProductGallery
from pages.woo_product_grid import WooProductGrid
from pages.woo_product_slider import WooProductSlider
from pages.woocommerce_product_collections import WoocommerceProductCollections


# ------------------------------------------------------------------------------------------------
# CONTENT ELEMENTS
# ------------------------------------------------------------------------------------------------
def test_content_toggle(init_driver):
    content_toggle = ContentToggle(init_driver)
    content_toggle.run()


def test_advanced_menu(init_driver):
    advanced_menu = AdvancedMenu(init_driver)
    advanced_menu.run()


def test_off_canvas(init_driver):
    off_canvas = OffCanvas(init_driver)
    off_canvas.run()


def test_feature_list(init_driver):
    feature_list = FeatureList(init_driver)
    feature_list.run()


def test_testimonial(init_driver):
    testimonial = Testimonial(init_driver)
    testimonial.run()


def test_sticky_video(init_driver):
    sticky_video = StickyVideo(init_driver)
    sticky_video.run()


def test_tooltip(init_driver):
    tool_tip = ToolTip(init_driver)
    tool_tip.run()


def test_protected_content(init_driver):
    protected_content = ProtectedContent(init_driver)
    protected_content.run()


def test_testimonial_slide(init_driver):
    testimonial_slide = TestimonialSlider(init_driver)
    testimonial_slide.run()


def test_advanced_tab(init_driver):
    advanced_tab = AdvancedTabs(init_driver)
    advanced_tab.run()


def test_advanced_accordion(init_driver):
    advanced_accordion = AdvancedAccordion(init_driver)
    advanced_accordion.run()


def test_team_member(init_driver):
    team_member = TeamMember(init_driver)
    team_member.run()


def test_infobox(init_driver):
    infobox = InfoBox(init_driver)
    infobox.run()


def test_dual_color_heading(init_driver):
    dual_color_heading = DualColorHeading(init_driver)
    dual_color_heading.run()


def test_logo_carousel(init_driver):
    logo_carousel = LogoCarousel(init_driver)
    logo_carousel.run()


def test_team_member_carousel(init_driver):
    team_member_carousel = TeamMemberCarousel(init_driver)
    team_member_carousel.run()


def test_simple_menu(init_driver):
    simple_menu = SimpleMenu(init_driver)
    simple_menu.run()


def test_flip_box(init_driver):
    flip_box = FlipBox(init_driver)
    flip_box.run()


def test_creative_button(init_driver):
    creative_button = CreativeButton(init_driver)
    creative_button.run()


def test_static_product(init_driver):
    static_product = StaticProduct(init_driver)
    static_product.run()


def test_event_calender(init_driver):
    event_calender = EventCalendar(init_driver)
    event_calender.run()


def test_advanced_search(init_driver):
    advanced_search = AdvancedSearch(init_driver)
    advanced_search.run()


# ------------------------------------------------------------------------------------------------
# DYNAMIC CONTENT ELEMENTS
# ------------------------------------------------------------------------------------------------

def test_advanced_data_table(init_driver):
    advanced_data_table = AdvancedDataTable(init_driver)
    advanced_data_table.run()


def test_post_block(init_driver):
    post_block = PostBlock(init_driver)
    post_block.run()


def test_post_timeline(init_driver):
    post_timeline = PostTimeline(init_driver)
    post_timeline.run()


def test_smart_post_list(init_driver):
    smart_post_list = PostList(init_driver)
    smart_post_list.run()


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


# ------------------------------------------------------------------------------------------------
# MARKETING ELEMENTS
# ------------------------------------------------------------------------------------------------

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


# ------------------------------------------------------------------------------------------------
# CREATIVE ELEMENTS
# ------------------------------------------------------------------------------------------------

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


def test_image_comparison(browser):
    ic = ImageComparison(browser)
    ic.load()
    ic.testcase()


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


def test_lightbox_modal(browser):
    lm = LightboxModal(browser)
    lm.load()
    lm.testcase()


def test_flip_carousel(browser):
    fc = FlipCarousel(browser)
    fc.load()
    fc.testcase()


def test_progress_bar(browser):
    pb = ProgressBar(browser)
    pb.load()
    pb.testcase()


def test_image_accordion(browser):
    ia = ImageAccordion(browser)
    ia.load()
    ia.testcase()


# ------------------------------------------------------------------------------------------------
# FORM STYLER ELEMENTS
# ------------------------------------------------------------------------------------------------

def test_contact_form_7(browser):
    cf7 = ContactForm7(browser)
    cf7.load()
    cf7.testcase()


def test_wpforms(browser):
    wpf = Wpforms(browser)
    wpf.load()
    wpf.testcase()


def test_ninja_forms(browser):
    nf = NinjaForms(browser)
    nf.load()
    nf.testcase()


def test_mailchimp(browser):
    mc = Mailchimp(browser)
    mc.load()
    mc.testcase()


def test_caldera_forms(browser):
    cf = CalderaForms(browser)
    cf.load()
    cf.testcase()


def test_fluent_forms(browser):
    ff = FluentForms(browser)
    ff.load()
    ff.testcase()


def test_weforms(browser):
    wf = Weforms(browser)
    wf.load()
    wf.testcase()


def test_formstack(browser):
    fs = Formstack(browser)
    fs.load()
    fs.testcase()


def test_gravity_forms(browser):
    gf = GravityForms(browser)
    gf.load()
    gf.testcase()


def test_login_register_form(browser):
    lrf = LoginRegisterForm(browser)
    lrf.load()
    lrf.testcase()


# ------------------------------------------------------------------------------------------------
# SOCIAL ELEMENTS
# ------------------------------------------------------------------------------------------------

def test_twitter_feed_carousel(browser):
    tfc = TwitterFeedCarousel(browser)
    tfc.load()
    tfc.testcase()


def test_twitter_feed(browser):
    tf = TwitterFeed(browser)
    tf.load()
    tf.testcase()


def test_instagram_feed(browser):
    insf = InstagramFeed(browser)
    insf.load()
    insf.testcase()


def test_facebook_feed(browser):
    fac = FacebookFeed(browser)
    fac.load()
    fac.testcase()


# ------------------------------------------------------------------------------------------------
# LEARNDASH ELEMENTS
# ------------------------------------------------------------------------------------------------

def test_learndash_course_list(browser):
    learndash = LearndashCourseList(browser)
    learndash.load()
    learndash.testcase()


# ------------------------------------------------------------------------------------------------
# DOCUMENTATION ELEMENTS
# ------------------------------------------------------------------------------------------------

def test_betterdocs_category_grid(browser):
    bd = BetterdocsCategoryGrid(browser)
    bd.load()
    bd.testcase()


def test_betterdocs_category_box(browser):
    bcb = BetterdocsCategoryBox(browser)
    bcb.load()
    bcb.testcase()


def test_betterdocs_search_form(browser):
    bsf = BetterdocsSearchForm(browser)
    bsf.load()
    bsf.testcase()


# ------------------------------------------------------------------------------------------------
# WOOCOMMERCE ELEMENTS
# ------------------------------------------------------------------------------------------------

def test_woo_cart(browser):
    wc = WooCart(browser)
    wc.load()
    wc.testcase()


def test_woo_product_slider(browser):
    wps = WooProductSlider(browser)
    wps.load()
    wps.testcase()


def test_woo_product_carousel(browser):
    wpc = WooProductCarousel(browser)
    wpc.load()
    wpc.testcase()


def test_woo_product_gallery(browser):
    wpg = WooProductGallery(browser)
    wpg.load()
    wpg.testcase()


def test_woo_product_compare(browser):
    wpc = WooProductCompare(browser)
    wpc.load()
    wpc.testcase()


def test_woocommerce_product_collections(browser):
    wpc = WoocommerceProductCollections(browser)
    wpc.load()
    wpc.testcase()


def test_woo_product_grid(browser):
    wpg = WooProductGrid(browser)
    wpg.load()
    wpg.testcase()


def test_woo_checkout(browser):
    wc = WooCheckout(browser)
    wc.load()
    wc.testcase()


# ------------------------------------------------------------------------------------------------
# EXTENSIONS
# ------------------------------------------------------------------------------------------------


def test_cross_domain_copy_paste(browser):
    cdcp = CrossDomainCopyPaste(browser)
    cdcp.load()
    cdcp.testcase()


def test_scroll_to_top(browser):
    stt = ScrollToTop(browser)
    stt.load()
    stt.testcase()


def test_content_protection(browser):
    cp = ContentProtection(browser)
    cp.load()
    cp.testcase()


def test_duplicator(browser):
    d = Duplicator(browser)
    d.load()
    d.testcase()


def test_table_of_content(browser):
    toc = TableOfContent(browser)
    toc.load()
    toc.testcase()


def test_parallax_scrolling(browser):
    ps = ParallaxScrolling(browser)
    ps.load()
    ps.testcase()


def test_reading_progress(browser):
    rpb = ReadingProgress(browser)
    rpb.load()
    rpb.testcase()


# def test_particle_effect(browser):
#     pe = ParticleEffect(browser)
#     pe.load()
#     pe.testcase()


def test_advanced_tooltip(browser):
    att = AdvancedTooltip(browser)
    att.load()
    att.testcase()
