from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="home/home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="home/about.html"), name="about"),
]
