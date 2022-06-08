from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel 
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmetadata.models import MetadataPageMixin

NEWS_SUMMARY_MAX_LENGTH = 500
CHARFIELD_MAX_LENGTH = 255

class HomePage(MetadataPageMixin, Page):
    template = "home/home.html"

    subpage_types = [
        "home.AboutUsPage", 
        "home.BlogIndexPage", 
        "home.EventsIndexPage",  
        "home.ContactPage",
        "home.GdprPage",
        "home.TermsPage", 
    ]
    parent_page_type = [
        "wagtailcore.Page",
    ]
    max_count = 1

class FlatPage(MetadataPageMixin, Page):
    """FlatPage page model."""

    template = "home/flat_page.html"
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
    parent_page_type = [
        "home.HomePage",
    ]
    
    
class AboutUsPage(MetadataPageMixin, Page):
    """About Us page model."""

    template = "home/about.html"

    presentation = RichTextField()
    vision = RichTextField()
    description = StreamField(
        [
            ("paragraph", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
        ]
    )

    content_panels = Page.content_panels + [
        FieldPanel("presentation"),
        FieldPanel("vision"),
        StreamFieldPanel("description", classname="full"),
    ]

    parent_page_type = [
        "home.HomePage",
    ]
    max_count = 1
    
class ContactPage(FlatPage):
    """Contact page model."""

    template = "home/contact.html"

    parent_page_type = [
        "home.HomePage",
    ]
    max_count = 1
    
class GdprPage(FlatPage):
    """GDPR page model."""

    template = "home/gdpr.html"

    parent_page_type = [
        "home.HomePage",
    ]
    max_count = 1
    
class TermsPage(FlatPage):
    """Terms & Conditions page model."""

    template = "home/terms.html"

    parent_page_type = [
        "home.HomePage",
    ]
    max_count = 1    

class BlogIndexPage(MetadataPageMixin, Page):

    subpage_types = ["home.BlogPage"]
    parent_page_type = [
        "home.HomePage",
    ]
    max_count = 1
    

class BlogPage(MetadataPageMixin, Page):
    summary = models.CharField(max_length=NEWS_SUMMARY_MAX_LENGTH)
    main_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.PROTECT,
    )
    date = models.DateField("Post date")
    body = RichTextField(blank=True) 

    content_panels = Page.content_panels + [
        FieldPanel("summary"),
        ImageChooserPanel("main_image"),
        FieldPanel("date"),
        FieldPanel("body"), 
    ]

    parent_page_type = [
        "home.BlogIndexPage",
    ]
    
    def __str__(self):
        return self.title

class EventsIndexPage(MetadataPageMixin, Page):

    subpage_types = ["home.EventPage"]
    parent_page_type = [
        "home.HomePage",
    ]
    max_count = 1

class EventPage(MetadataPageMixin, Page):
    summary = models.CharField(max_length=NEWS_SUMMARY_MAX_LENGTH)
    preview_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.PROTECT,
    )
    event_date = models.DateField() 
    event_time = models.TimeField()
    event_location = models.CharField(max_length=CHARFIELD_MAX_LENGTH)
    body = RichTextField(blank=True) 

    content_panels = Page.content_panels + [
        ImageChooserPanel("preview_image"),
        FieldPanel("summary"),
        FieldPanel("event_date"), 
        FieldPanel("event_time"),
        FieldPanel("event_location"),
        FieldPanel("body"), 
    ]

    parent_page_type = [
        "home.EventsIndexPage",
    ]
    
    def __str__(self):
        return self.title
