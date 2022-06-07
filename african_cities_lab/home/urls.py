from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", 
         TemplateView.as_view(template_name="home/about.html"), 
         name="about"
    ),  
    #path("blog/", 
     #    TemplateView.as_view(template_name="home/blog_index_page.html"),
     #    name="blog"),
     #path("events/", 
      #    TemplateView.as_view(template_name="home/events_index_page.html"),
      #    name="events"),
     #path(
     #   "contact/",
     #   TemplateView.as_view(template_name="home/contact.html"),
     #   name="contact",
    #), 
]
