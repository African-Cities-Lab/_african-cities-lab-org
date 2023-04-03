from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", TemplateView.as_view(template_name="home/about.html"), name="about"),
    path(
        "events/",
        TemplateView.as_view(template_name="home/event_index_page.html"),
        name="events",
    ),
    path(
        "gdpr/",
        TemplateView.as_view(template_name="home/static_gdpr.html"),
        name="gdpr",
    ),
    path(
        "terms-conditions/",
        TemplateView.as_view(template_name="home/static_terms.html"),
        name="terms-conditions",
    ),
    path(
        "contact/",
        TemplateView.as_view(template_name="home/static_contact.html"),
        name="contact",
    ),
    path(
        "moocs/",
        TemplateView.as_view(template_name="home/moocs.html"),
        name="moocs",
    ),
    path(
        "integration-of-open-data-and-artificial-intelligence-in-the-development-of-smart-cities-in-Africa/",
        TemplateView.as_view(template_name="home/events/1st_webinar.html"),
        name="integration-of-open-data-and-artificial-intelligence-in-the-development-of-smart-cities-in-Africa",
    ),
    path(
        "african-cities-what-role-for-the-youth/",
        TemplateView.as_view(template_name="home/events/2nd_webinar.html"),
        name="african-cities-what-role-for-the-youth",
    ),
    path(
        "how-to-build-resilient-african-cities/",
        TemplateView.as_view(template_name="home/events/3rd_webinar.html"),
        name="how-to-build-resilient-african-cities",
    ),
    path(
        "webinar-registration/",
        TemplateView.as_view(template_name="home/webinar_form.html"),
        name="webinar-registration",
    ),
    path("webinar-subscribe/", views.subscribe_webinar, name="subscribe-webinar"),
    path(
        "acc-2023/",
        TemplateView.as_view(template_name="home/events/civa/civa.html"),
        name="acc-2023",
    ),
    path(
        "acc-2023-agenda/",
        TemplateView.as_view(template_name="home/events/civa/agenda.html"),
        name="acc-agenda",
    ),
    path(
        "acc-2023-speakers/",
        TemplateView.as_view(template_name="home/events/civa/speakers.html"),
        name="acc-speakers",
    ),
    path(
        "acc-2023-sponsors/",
        TemplateView.as_view(template_name="home/events/civa/sponsors.html"),
        name="acc-sponsors",
    ),
    path(
        "acc-2023-contact/",
        TemplateView.as_view(template_name="home/events/civa/contact.html"),
        name="acc-informations",
    ),
    path(
        "acc-2023-registration/",
        TemplateView.as_view(template_name="home/events/civa/form.html"),
        name="acc-registration",
    ),
    path(
        "acc-2023-special-guests/",
        TemplateView.as_view(template_name="home/events/civa/guests.html"),
        name="acc-guests",
    ),
    path(
        "acc-2023-commitee/",
        TemplateView.as_view(template_name="home/events/civa/commitee.html"),
        name="acc-commitee",
    ),
    path(
        "acc-2023-call-for-papers/",
        TemplateView.as_view(template_name="home/events/civa/call-for-paper.html"),
        name="acc-papers",
    ),
    path(
        "acc-2023-call-for-papers-details/",
        TemplateView.as_view(template_name="home/events/civa/cfp-details.html"),
        name="cfp-details",
    ),
    path(
        "acc-2023-call-for-poster-demos/",
        TemplateView.as_view(template_name="home/events/civa/call-for-poster.html"),
        name="cfpd-details",
    ),
    path(
        "acc-2023-call-for-workshops-tutorials/",
        TemplateView.as_view(template_name="home/events/civa/call-for-workshops.html"),
        name="cfwt-details",
    ),
    path(
        "acc-2023-call-for-doctoral-consortium/",
        TemplateView.as_view(template_name="home/events/civa/call-for-doctoral.html"),
        name="cfdc-details",
    ),
    path(
        "newsletter/",
        TemplateView.as_view(template_name="home/newsletter.html"),
        name="newsletter",
    ),

    ########
    path("newsletter/submission/", views.newsletter_submission, name="suscribe-newsletter"),

    path("moocs/subscribe/", views.subscribe_moocs, name="subscribe-moocs"),
]
