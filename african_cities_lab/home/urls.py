from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="home/home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="home/about.html"), name="about"),
    path(
        "courses/",
        TemplateView.as_view(template_name="home/courses.html"),
        name="courses",
    ),
    path(
        "programs/",
        TemplateView.as_view(template_name="home/programs.html"),
        name="programs",
    ),
    path(
        "get-involved/",
        TemplateView.as_view(template_name="home/get_involved.html"),
        name="get-involved",
    ),
    # path("news/", TemplateView.as_view(template_name="home/news.html"), name="news"),
    path(
        "contact/",
        TemplateView.as_view(template_name="home/contact.html"),
        name="contact",
    ),
    # AUTHENTIFICATION
    path("login/", TemplateView.as_view(template_name="home/login.html"), name="login"),
    path(
        "register/",
        TemplateView.as_view(template_name="home/register.html"),
        name="register",
    ),
]
