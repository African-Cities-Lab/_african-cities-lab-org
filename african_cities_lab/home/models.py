from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Locale, Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

NEWS_SUMMARY_MAX_LENGTH = 500


class HomePage(Page):
    template = "home/home.html"

    subpage_types = [
        "home.AboutUsPage",
        "home.OnlineCoursesPage",
        "home.TrainingProgramsPage",
        "home.GetInvolvedPage",
        "home.ContactPage",
        "home.NewsIndexPage",
    ]
    parent_page_type = [
        "wagtailcore.Page",
    ]
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        print("it's get_context")
        context = super().get_context(request, *args, **kwargs)
        # Get current language
        current_lang = Locale.get_active()
        # Get last 4 news articles
        latest_news = (
            NewsPage.objects.filter(locale=current_lang)
            .live()
            .public()
            .order_by("-first_published_at")[:4]
        )
        context["news"] = latest_news
        return context


class FlatPage(Page):
    """FlatPage page model."""

    template = "home/flat_page.html"
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
    parent_page_type = [
        "home.HomePage",
    ]


class AboutUsPage(Page):
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


class OnlineCoursesPage(FlatPage):
    """Online Courses page model."""

    template = "home/courses.html"

    parent_page_type = [
        "home.HomePage",
    ]


class TrainingProgramsPage(FlatPage):
    """Training programs page model."""

    template = "home/programs.html"

    parent_page_type = [
        "home.HomePage",
    ]


class GetInvolvedPage(FlatPage):
    """Get Involved page model."""

    template = "home/get_involved.html"

    parent_page_type = [
        "home.HomePage",
    ]


class ContactPage(FlatPage):
    """Contact page model."""

    template = "home/contact.html"

    parent_page_type = [
        "home.HomePage",
    ]
    max_count = 1


class NewsIndexPage(Page):

    subpage_types = ["home.NewsPage"]
    parent_page_type = [
        "home.HomePage",
    ]
    max_count = 1


class NewsPage(Page):
    summary = models.CharField(max_length=NEWS_SUMMARY_MAX_LENGTH)
    main_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.PROTECT,
    )
    date = models.DateField()
    body = StreamField(
        [
            ("heading", blocks.CharBlock(form_classname="full title")),
            ("paragraph", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
        ]
    )

    content_panels = Page.content_panels + [
        FieldPanel("summary"),
        ImageChooserPanel("main_image"),
        FieldPanel("date"),
        StreamFieldPanel("body", classname="full"),
    ]

    parent_page_type = [
        "home.NewsIndexPage",
    ]

    def __str__(self):
        return self.title
