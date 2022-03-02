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
        news_model = apps.get_model("home.NewsPage")
        # Get last 4 news articles
        latest_news = (
            news_model.objects.filter(locale=current_lang)
            .live()
            .public()
            .order_by("-first_published_at")[:4]
        )
        context["news"] = latest_news
        return context
