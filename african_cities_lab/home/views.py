# from django.shortcuts import render
# from multiprocessing import context

from django.http import HttpResponse
from unicodedata import category
from django.apps import apps
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views import generic
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from django.utils.datastructures import MultiValueDictKeyError
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
        return context
    
    
def _moocs_registered(email, merge_fields=None):
    """
    Contains code handling the communication to the mailchimp api
    to create a contact/member in an audience/list.
    """
    mailchimp = Client()
    mailchimp.set_config(
        {
            "api_key": settings.MAILCHIMP_API_KEY,
            "server": settings.MAILCHIMP_DATA_CENTER,
        }
    )

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    if merge_fields is not None:
        member_info["merge_fields"] = merge_fields

    try:
        response = mailchimp.lists.add_list_member(
            settings.MAILCHIMP_MOOCS_LIST_ID, member_info
        )
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))
        
    
def moocs_registered(request):
    if request.method == "POST":
        email = request.POST["EMAIL"]
        merge_fields = {
            "MOOCS": request.POST["MOOCS"],
            "LNAME": request.POST["LNAME"],
            "FNAME": request.POST["FNAME"],
            "INSTITUT": request.POST["INSTITUT"],
            "FUNCTION": request.POST["FUNCTION"],
            "COUNTRY": request.POST["COUNTRY"],
        }
            
        _moocs_registered(email, merge_fields)  # function to access mailchimp
        messages.success(
            request, _("Thank you for registering. We have just sent you an email with the webinar link.Please check your mailbox or spam folder if you haven't received it yet.")
        )  # message
    return HttpResponse("/")
  

def _webinar_subscription_en(email, merge_fields=None):
    """
    Contains code handling the communication to the mailchimp api
    to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config(
        {
            "api_key": settings.MAILCHIMP_API_KEY,
            "server": settings.MAILCHIMP_DATA_CENTER,
        }
    )

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    if merge_fields is not None:
        member_info["merge_fields"] = merge_fields

    try:
        response = mailchimp.lists.add_list_member(
            settings.MAILCHIMP_WEBINAR_EN_LIST_ID, member_info
        )
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))
        
        
def _webinar_subscription_fr(email, merge_fields=None):
    """
    Contains code handling the communication to the mailchimp api
    to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config(
        {
            "api_key": settings.MAILCHIMP_API_KEY,
            "server": settings.MAILCHIMP_DATA_CENTER,
        }
    )

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    if merge_fields is not None:
        member_info["merge_fields"] = merge_fields

    try:
        response = mailchimp.lists.add_list_member(
            settings.MAILCHIMP_WEBINAR_FR_LIST_ID, member_info
        )
        print(f'API call successful: {response.status}')
    except ApiClientError as error:
        print(f'An exception occurred: {error.text}')     
        
class WebinarSubscription(generic.TemplateView):
    
    def subscribe(request):
        if request.method == "POST":
            email = request.POST["EMAIL"]
            merge_fields = {
                "LNAME": request.POST["LNAME"],
                "FNAME": request.POST["FNAME"],
                "INSTITUT": request.POST["INSTITUT"],
                "FUNCTION": request.POST["FUNCTION"],
                "TITLE": request.POST["TITLE"],
                "COUNTRY": request.POST["COUNTRY"],
                "LINKEDIN": request.POST["LINKEDIN"],
            }
            
            if request.POST["site_language"] == "en":
                _webinar_subscription_en(email, merge_fields)  # function to access mailchimp
                messages.success(
                    request, _("Thank you for your registration! A confirmation email has been sent to you, please check your mailbox or your spam.")
                )  # message
                
            if request.POST["site_language"] == "fr":
                _webinar_subscription_fr(email, merge_fields)  # function to access mailchimp
                messages.success(
                    request, _("Merci de votre inscription ! Un mail de confirmation vous a été envoyé, veuillez consulter votre boîte mail ou vos spams.")
                )  # message

        return render(
            request,
            "home/webinar_form.html",
            context={"title": _("Subscribe to the webinar")},
        )


