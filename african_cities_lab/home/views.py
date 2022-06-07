# from django.shortcuts import render
# from multiprocessing import context

from django.apps import apps
from django.views import generic
from wagtail.core.models import Locale


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = "home/home.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_lang = Locale.get_active()
        # Get current language
        blog_model = apps.get_model("home.BlogPage")
        # Get last 3 news articles
        latest_article = (
            blog_model.objects.filter(locale=current_lang)
            .live()
            .public()
            .order_by("-first_published_at")[:3]
        )
        context["blog"] = latest_article
        context["moocs"] = []
        context["topics"] = []
        return context