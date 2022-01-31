# from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


# Create your models here.
class HomePage(Page):
    template = "home/home.html"

    subpage_types = [
        "home.AboutPage",
        "home.OnlineCoursesPage",
        "home.TrainingProgramsPage",
        "home.GetInvolvedPage",
        "home.ContactPage",
    ]
    parent_page_type = [
        "wagtailcore.Page",
    ]
    max_count = 1


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


class AboutPage(FlatPage):
    """FlatPage page model."""

    template = "home/about.html"

    parent_page_type = [
        "home.HomePage",
    ]


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
