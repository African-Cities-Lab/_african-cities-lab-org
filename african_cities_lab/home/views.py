# from django.shortcuts import render
from django.views import generic


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = "pages/home.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
