import pytest

from pages.nft_gallery import NFTGallery
from pages.wp_forms import Wpforms
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
from pages.image_comparison import Snapshot, ImageComparison
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
@pytest.mark.flaky(reruns=1)
def test_content_toggle(init_driver):
    content_toggle = ContentToggle(init_driver)
    content_toggle.run()


@pytest.mark.flaky(reruns=1)
def test_advanced_menu(init_driver):
    advanced_menu = AdvancedMenu(init_driver)
    advanced_menu.run()


@pytest.mark.flaky(reruns=1)
def test_off_canvas(init_driver):
    off_canvas = OffCanvas(init_driver)
    off_canvas.run()


@pytest.mark.flaky(reruns=1)
def test_feature_list(init_driver):
    feature_list = FeatureList(init_driver)
    feature_list.run()


@pytest.mark.flaky(reruns=1)
def test_testimonial(init_driver):
    testimonial = Testimonial(init_driver)
    testimonial.run()


@pytest.mark.flaky(reruns=1)
def test_sticky_video(init_driver):
    sticky_video = StickyVideo(init_driver)
    sticky_video.run()


@pytest.mark.flaky(reruns=1)
def test_tooltip(init_driver):
    tool_tip = ToolTip(init_driver)
    tool_tip.run()


@pytest.mark.flaky(reruns=1)
def test_protected_content(init_driver):
    protected_content = ProtectedContent(init_driver)
    protected_content.run()


@pytest.mark.flaky(reruns=1)
def test_testimonial_slide(init_driver):
    testimonial_slide = TestimonialSlider(init_driver)
    testimonial_slide.run()


@pytest.mark.flaky(reruns=1)
def test_advanced_tab(init_driver):
    advanced_tab = AdvancedTabs(init_driver)
    advanced_tab.run()


@pytest.mark.flaky(reruns=1)
def test_advanced_accordion(init_driver):
    advanced_accordion = AdvancedAccordion(init_driver)
    advanced_accordion.run()


@pytest.mark.flaky(reruns=1)
def test_team_member(init_driver):
    team_member = TeamMember(init_driver)
    team_member.run()


@pytest.mark.flaky(reruns=1)
def test_infobox(init_driver):
    infobox = InfoBox(init_driver)
    infobox.run()


@pytest.mark.flaky(reruns=1)
def test_dual_color_heading(init_driver):
    dual_color_heading = DualColorHeading(init_driver)
    dual_color_heading.run()


@pytest.mark.flaky(reruns=1)
def test_logo_carousel(init_driver):
    logo_carousel = LogoCarousel(init_driver)
    logo_carousel.run()


@pytest.mark.flaky(reruns=1)
def test_team_member_carousel(init_driver):
    team_member_carousel = TeamMemberCarousel(init_driver)
    team_member_carousel.run()


@pytest.mark.flaky(reruns=1)
def test_simple_menu(init_driver):
    simple_menu = SimpleMenu(init_driver)
    simple_menu.run()


@pytest.mark.flaky(reruns=1)
def test_flip_box(init_driver):
    flip_box = FlipBox(init_driver)
    flip_box.run()


@pytest.mark.flaky(reruns=1)
def test_creative_button(init_driver):
    creative_button = CreativeButton(init_driver)
    creative_button.run()


@pytest.mark.flaky(reruns=1)
def test_static_product(init_driver):
    static_product = StaticProduct(init_driver)
    static_product.run()


@pytest.mark.flaky(reruns=1)
def test_event_calender(init_driver):
    event_calender = EventCalendar(init_driver)
    event_calender.run()


@pytest.mark.flaky(reruns=1)
def test_advanced_search(init_driver):
    advanced_search = AdvancedSearch(init_driver)
    advanced_search.run()


# ------------------------------------------------------------------------------------------------
# DYNAMIC CONTENT ELEMENTS
# --------------------------
# ----------------------------------------------------------------------
@pytest.mark.flaky(reruns=1)
def test_advanced_data_table(init_driver):
    advanced_data_table = AdvancedDataTable(init_driver)
    advanced_data_table.run()


@pytest.mark.flaky(reruns=1)
def test_post_block(init_driver):
    post_block = PostBlock(init_driver)
    post_block.run()


# def test_nft_gallery(init_driver):
#     nft_gallery = NFTGallery(init_driver)
#     nft_gallery.run()


@pytest.mark.flaky(reruns=1)
def test_post_timeline(init_driver):
    post_timeline = PostTimeline(init_driver)
    post_timeline.run()


@pytest.mark.flaky(reruns=1)
def test_smart_post_list(init_driver):
    smart_post_list = PostList(init_driver)
    smart_post_list.run()


@pytest.mark.flaky(reruns=1)
def test_google_map(init_driver):
    google_map = AdvancedGoogleMap(init_driver)
    google_map.run()


@pytest.mark.flaky(reruns=1)
def test_content_ticker(init_driver):
    content_ticker = ContentTicker(init_driver)
    content_ticker.run()


@pytest.mark.flaky(reruns=1)
def test_content_timeline(init_driver):
    content_timeline = ContentTimeline(init_driver)
    content_timeline.run()


@pytest.mark.flaky(reruns=1)
def test_dynamic_gallery(init_driver):
    dynamic_gallery = DynamicGallery(init_driver)
    dynamic_gallery.run()


@pytest.mark.flaky(reruns=1)
def test_post_grid(init_driver):
    post_grid = PostGrid(init_driver)
    post_grid.run()


@pytest.mark.flaky(reruns=1)
def test_data_table(init_driver):
    data_table = DataTable(init_driver)
    data_table.run()


@pytest.mark.flaky(reruns=1)
def test_post_carousel(init_driver):
    post_carousel = PostCarousel(init_driver)
    post_carousel.run()


# ------------------------------------------------------------------------------------------------
# MARKETING ELEMENTS
# --------------------------
# ----------------------------------------------------------------------
@pytest.mark.flaky(reruns=1)
def test_pricing_table(init_driver):
    pricing_table = PricingTable(init_driver)
    pricing_table.run()


@pytest.mark.flaky(reruns=1)
def test_call_to_action(init_driver):
    call_to_action = CallToAction(init_driver)
    call_to_action.run()


@pytest.mark.flaky(reruns=1)
def test_price_menu(init_driver):
    price_menu = PriceMenu(init_driver)
    price_menu.run()


# ------------------------------------------------------------------------------------------------
# CREATIVE ELEMENTS
# --------------------------
# ----------------------------------------------------------------------
@pytest.mark.flaky(reruns=1)
def test_interactive_promo(init_driver):
    interactive_promo = InteractivePromo(init_driver)
    interactive_promo.run()


@pytest.mark.flaky(reruns=1)
def test_interactive_cards(init_driver):
    interactive_cards = InteractiveCards(init_driver)
    interactive_cards.run()


@pytest.mark.flaky(reruns=1)
def test_one_page_nav(init_driver):
    one_page_nav = OnePageNav(init_driver)
    one_page_nav.run()


@pytest.mark.flaky(reruns=1)
def test_image_comparison(init_driver):
    image_comparison = ImageComparison(init_driver)
    image_comparison.run()


@pytest.mark.flaky(reruns=1)
def test_filterable_gallery(init_driver):
    filterable_gallery = FilterableGallery(init_driver)
    filterable_gallery.run()


@pytest.mark.flaky(reruns=1)
def test_interactive_circle(init_driver):
    interactive_circle = InteractiveCircle(init_driver)
    interactive_circle.run()


@pytest.mark.flaky(reruns=1)
def test_image_hotspots(init_driver):
    image_hotspots = ImageHotspots(init_driver)
    image_hotspots.run()


@pytest.mark.flaky(reruns=1)
def test_image_scroller(init_driver):
    image_scroller = ImageScroller(init_driver)
    image_scroller.run()


@pytest.mark.flaky(reruns=1)
def test_divider(init_driver):
    divider = Divider(init_driver)
    divider.run()


@pytest.mark.flaky(reruns=1)
def test_fancy_text(init_driver):
    fancy_text = FancyText(init_driver)
    fancy_text.run()


@pytest.mark.flaky(reruns=1)
def test_counter(init_driver):
    counter = Counter(init_driver)
    counter.run()


@pytest.mark.flaky(reruns=1)
def test_countdown(init_driver):
    countdown = Countdown(init_driver)
    countdown.run()


@pytest.mark.flaky(reruns=1)
def test_lightbox_modal(init_driver):
    lightbox_modal = LightboxModal(init_driver)
    lightbox_modal.run()


@pytest.mark.flaky(reruns=1)
def test_flip_carousel(init_driver):
    flip_carousel = FlipCarousel(init_driver)
    flip_carousel.run()


@pytest.mark.flaky(reruns=1)
def test_progress_bar(init_driver):
    progress_bar = ProgressBar(init_driver)
    progress_bar.run()


@pytest.mark.flaky(reruns=1)
def test_image_accordion(init_driver):
    image_accordion = ImageAccordion(init_driver)
    image_accordion.run()


# ------------------------------------------------------------------------------------------------
# FORM STYLER ELEMENTS
# --------------------------
# ----------------------------------------------------------------------
@pytest.mark.flaky(reruns=1)
def test_contact_form_7(init_driver):
    contact_form_7 = ContactForm7(init_driver)
    contact_form_7.run()


@pytest.mark.flaky(reruns=1)
def test_wp_forms(init_driver):
    wp_forms = Wpforms(init_driver)
    wp_forms.run()


@pytest.mark.flaky(reruns=1)
def test_ninja_forms(init_driver):
    ninja_forms = NinjaForms(init_driver)
    ninja_forms.run()


@pytest.mark.flaky(reruns=1)
def test_mailchimp(init_driver):
    mailchimp = Mailchimp(init_driver)
    mailchimp.run()


@pytest.mark.flaky(reruns=1)
def test_caldera_forms(init_driver):
    caldera_forms = CalderaForms(init_driver)
    caldera_forms.run()


@pytest.mark.flaky(reruns=1)
def test_fluent_forms(init_driver):
    fluent_forms = FluentForms(init_driver)
    fluent_forms.run()


@pytest.mark.flaky(reruns=1)
def test_we_forms(init_driver):
    we_forms = Weforms(init_driver)
    we_forms.run()


@pytest.mark.flaky(reruns=1)
def test_formstack(init_driver):
    formstack = Formstack(init_driver)
    formstack.run()


# @pytest.mark.flaky(reruns=1)
# def test_gravity_forms(init_driver):
#     gravity_forms = GravityForms(init_driver)
#     gravity_forms.run()


@pytest.mark.flaky(reruns=1)
def test_login_register_form(init_driver):
    login_register_form = LoginRegisterForm(init_driver)
    login_register_form.run()


# ------------------------------------------------------------------------------------------------
# SOCIAL ELEMENTS
# --------------------------
# ----------------------------------------------------------------------
@pytest.mark.flaky(reruns=1)
def test_twitter_feed_carousel(init_driver):
    twitter_feed_carousel = TwitterFeedCarousel(init_driver)
    twitter_feed_carousel.run()


@pytest.mark.flaky(reruns=1)
def test_twitter_feed(init_driver):
    twitter_feed = TwitterFeed(init_driver)
    twitter_feed.run()


@pytest.mark.flaky(reruns=1)
def test_instagram_feed(init_driver):
    instagram_feed = InstagramFeed(init_driver)
    instagram_feed.run()


@pytest.mark.flaky(reruns=1)
def test_facebook_feed(init_driver):
    facebook_feed = FacebookFeed(init_driver)
    facebook_feed.run()


# ------------------------------------------------------------------------------------------------
# LEARNDASH ELEMENTS
# --------------------------
# ----------------------------------------------------------------------
@pytest.mark.flaky(reruns=1)
def test_learndash_course_list(init_driver):
    learndash_course_list = LearndashCourseList(init_driver)
    learndash_course_list.run()


# ------------------------------------------------------------------------------------------------
# DOCUMENTATION ELEMENTS
# --------------------------
# ----------------------------------------------------------------------
@pytest.mark.flaky(reruns=1)
def test_betterdocs_category_grid(init_driver):
    betterdocs_category_grid = BetterdocsCategoryGrid(init_driver)
    betterdocs_category_grid.run()


@pytest.mark.flaky(reruns=1)
def test_betterdocs_category_box(init_driver):
    betterdocs_category_box = BetterdocsCategoryBox(init_driver)
    betterdocs_category_box.run()


@pytest.mark.flaky(reruns=1)
def test_betterdocs_search_form(init_driver):
    betterdocs_category_box = BetterdocsSearchForm(init_driver)
    betterdocs_category_box.run()


# ------------------------------------------------------------------------------------------------
# WOOCOMMERCE ELEMENTS
# --------------------------
# ----------------------------------------------------------------------
@pytest.mark.flaky(reruns=1)
def test_woo_cart(init_driver):
    cart = WooCart(init_driver)
    cart.run()


@pytest.mark.flaky(reruns=1)
def test_woo_product_slider(init_driver):
    product_slider = WooProductSlider(init_driver)
    product_slider.run()


@pytest.mark.flaky(reruns=1)
def test_woo_product_carousel(init_driver):
    product_carousel = WooProductCarousel(init_driver)
    product_carousel.run()


@pytest.mark.flaky(reruns=1)
def test_woo_product_gallery(init_driver):
    product_gallery = WooProductGallery(init_driver)
    product_gallery.run()


@pytest.mark.flaky(reruns=1)
def test_woo_product_compare(init_driver):
    product_compare = WooProductCompare(init_driver)
    product_compare.run()


@pytest.mark.flaky(reruns=1)
def test_woocommerce_product_collections(init_driver):
    product_collections = WoocommerceProductCollections(init_driver)
    product_collections.run()


@pytest.mark.flaky(reruns=1)
def test_woo_product_grid(init_driver):
    product_grid = WooProductGrid(init_driver)
    product_grid.run()


@pytest.mark.flaky(reruns=1)
def test_woo_checkout(init_driver):
    checkout = WooCheckout(init_driver)
    checkout.run()


# ------------------------------------------------------------------------------------------------
# EXTENSIONS
# ------------------------------------------------------------------------------------------------


@pytest.mark.flaky(reruns=1)
def test_cross_domain_copy_paste(init_driver):
    cross_domain_copy_paste = CrossDomainCopyPaste(init_driver)
    cross_domain_copy_paste.run()


@pytest.mark.flaky(reruns=1)
def test_scroll_to_top(init_driver):
    scroll_to_top = ScrollToTop(init_driver)
    scroll_to_top.run()


@pytest.mark.flaky(reruns=1)
def test_content_protection(init_driver):
    content_protection = ContentProtection(init_driver)
    content_protection.run()


@pytest.mark.flaky(reruns=1)
def test_table_of_content(init_driver):
    table_of_content = TableOfContent(init_driver)
    table_of_content.run()


@pytest.mark.flaky(reruns=1)
def test_advanced_tooltip(init_driver):
    advanced_tooltip = AdvancedTooltip(init_driver)
    advanced_tooltip.run()

# @pytest.mark.flaky(reruns=1)
# def test_duplicator(init_driver):
#     duplicator = Duplicator(init_driver)
#     duplicator.run()

# @pytest.mark.flaky(reruns=1)
# def test_parallax_scrolling(init_driver):
#     parallax = ParallaxScrolling(init_driver)
#     parallax.run()

# @pytest.mark.flaky(reruns=1)
# def test_reading_progress(init_driver):
#     reading_progress = ReadingProgress(init_driver)
#     reading_progress.run()

# @pytest.mark.flaky(reruns=1)
# def test_particle_effect(init_driver):
#     particle = ParticleEffect(init_driver)
#     particle.run()
