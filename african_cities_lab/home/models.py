from django import forms
from django.db import models

from django.shortcuts import render

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.snippets.models import register_snippet

from wagtail.core import blocks
from wagtail.core.models import Page, Locale
from wagtail.core.fields import RichTextField, StreamField

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

from wagtailmetadata.models import MetadataPageMixin
from wagtail.contrib.routable_page.models import RoutablePageMixin, route


class HomePage(MetadataPageMixin, Page):
    template = "home/home.html"

    subpage_types = [
        "home.BlogIndexPage",
        "home.FlatPage",
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
    
class BlogIndexPage(MetadataPageMixin, Page):

    subpage_types = ["home.BlogPage"]
    parent_page_type = [
        "home.HomePage",
    ]
    max_count = 1

    def get_context(self, request):

        # Get current language
        current_lang = Locale.get_active()

        # Get categories
        categories = BlogCategory.objects.filter(language=current_lang).all()

        # Update template context
        context = super().get_context(request)
        context["categories"] = categories
        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        "BlogPage",
        related_name="tagged_items",
        on_delete=models.CASCADE
    )

class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Get current language
        current_lang = Locale.get_active()
        # Filter by tag
        tag = request.GET.get("tag")
        blogpages = BlogPage.objects.filter(tags__name=tag, locale=current_lang).live().public()

        # Update template context
        context = super().get_context(request)
        context["blogpages"] = blogpages
        return context

class BlogPage(MetadataPageMixin, Page):
    summary = models.CharField(max_length=255)
    main_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.PROTECT,
    )
    date = models.DateField("Post date")
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('BlogCategory', blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("date"),
            FieldPanel("tags"),
            FieldPanel("categories", widget=forms.CheckboxSelectMultiple),
        ], heading="Blog details"),
        FieldPanel("summary"),
        ImageChooserPanel("main_image"),
        FieldPanel("body"),

    ]

    parent_page_type = [
        "home.BlogIndexPage",
    ]

    def __str__(self):
        return self.title


class LangChoices(models.TextChoices):
        ENGLISH = "English",
        FRENCH = "French"

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    language = models.TextField(
        max_length=10,
        choices=LangChoices.choices,
        default=LangChoices.ENGLISH,
    )
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        null=True,
        max_length=255,
        help_text="A slug to identify posts by this category",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("language", widget=forms.Select),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "blog categories"
        ordering = ["name"]
