# from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


# Create your models here.
class FlatPage(Page):
    """FlatPage page model."""

    template = "home/flat_page.html"
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
