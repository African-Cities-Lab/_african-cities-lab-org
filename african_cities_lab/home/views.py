# from django.shortcuts import render
# from multiprocessing import context
import json
from unicodedata import category

from django.apps import apps
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.translation import gettext_lazy as _
from django.views import generic
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
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


def _subscribe(email, list_id, merge_fields=None):
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
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print(f"API call successful: {response}")
        return response["status"]
    except ApiClientError as error:
        print(f"An exception occurred: {error.text}")
        if json.loads(error.text)["title"] == "Member Exists":
            return "exists"


def subscribe_moocs(request):
    if request.method == "POST":
        email = request.POST["EMAIL"]
        merge_fields = {
            "NAME": request.POST["NAME"],
        }

        status = _subscribe(email, settings.MAILCHIMP_MOOCS_LIST_ID, merge_fields)
        if status == "subscribed":
            messages.success(
                request, _("Thank you! Your registration has been successful.")
            )  # message
        elif status == "exists":
            messages.info(
                request,
                _(
                    "Your email is already registered, please check your mailbox or your spam. Thank you!"
                ),
            )  # message

    return render(request, "home/home.html")


def subscribe_webinar(request):
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
            list_id = settings.MAILCHIMP_WEBINAR_EN_LIST_ID
        else:  # "fr"
            list_id = settings.MAILCHIMP_WEBINAR_FR_LIST_ID

        status = _subscribe(email, list_id, merge_fields)
        if status == "subscribed":
            messages.success(
                request,
                _(
                    "Thank you for registering! A confirmation email has been sent to you, please check your mailbox or your spam."
                ),
            )  # message
        elif status == "exists":
            messages.info(
                request,
                _(
                    "Your email is already registered, please check your mailbox or your spam. Thank you!"
                ),
            )  # message

    return render(
        request,
        "home/webinar_form.html",
        context={"title": _("Subscribe to the webinar")},
    )


def newsletter(request): 
    
    if request.method == "POST":
        email = request.POST["EMAIL"] 

        if request.POST["site_language"] == "en":
            list_id = settings.MAILCHIMP_NEWSLETTER_EN_ID
        else:  # "fr"
            list_id = settings.MAILCHIMP_NEWSLETTER_FR_ID

        status = _subscribe(email, list_id)
        if status == "subscribed":
            messages.success(
                request,
                _(
                    "Thank you for subscribed to the ACL newsletter."
                ),
            )  # message
        elif status == "exists":
            messages.info(
                request,
                _(
                    "Your email is already subscribed. Thank you!"
                ),
            )  # message

    return JsonResponse(request)
