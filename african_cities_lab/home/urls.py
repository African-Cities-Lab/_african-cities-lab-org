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
    path("integration-of-open-data-and-artificial-intelligence-in-the-development-of-smart-cities-in-Africa/", 
         TemplateView.as_view(template_name="home/events/1st_webinar.html"), 
         name="integration-of-open-data-and-artificial-intelligence-in-the-development-of-smart-cities-in-Africa"
    ),
    path("youth-and-urban-planning-challenges-and-roles-of-youth-in-the-development-of-the-african-city/", 
         TemplateView.as_view(template_name="home/events/2nd_webinar.html"), 
         name="youth-and-urban-planning-challenges-and-roles-of-youth-in-the-development-of-the-african-city"
    ),
    path("webinar-subscribe/", views.subscribe, name="subscribe"),
    # path(
    #   "contact/",
    #   TemplateView.as_view(template_name="home/contact.html"),
    #   name="contact",
    # ),
    path(
        "the-international-conference-of-african-cities-2023/",
        TemplateView.as_view(template_name="home/events/civa/civa.html"),
        name="the-international-conference-of-african-cities-2023",
    ),
    path(
        "the-international-conference-of-african-cities-2023-agenda/",
        TemplateView.as_view(template_name="home/events/civa/agenda.html"),
        name="civa-agenda",
    ),
    path(
        "the-international-conference-of-african-cities-2023-speakers/",
        TemplateView.as_view(template_name="home/events/civa/speakers.html"),
        name="civa-speakers",
    ),
    path(
        "the-international-conference-of-african-cities-2023-sponsors/",
        TemplateView.as_view(template_name="home/events/civa/sponsors.html"),
        name="civa-sponsors",
    ),
    path(
        "the-international-conference-of-african-cities-2023-travel-information/",
        TemplateView.as_view(template_name="home/events/civa/travel_info.html"),
        name="civa-travel-information",
    ),
    
    # Moocs url
    path(
        "moocs/introduction-to-sanitazation-economy-systems-markets/",
        TemplateView.as_view(template_name="home/moocs/introduction_to_sanitazation_economy_systems_markets.html"),
        name="introduction-to-sanitazation-economy-systems-markets",
    ),
    path(
        "moocs/urban-data-management-for-smart-city-developpement-in-africa/",
        TemplateView.as_view(template_name="home/moocs/urban_data_management_for_smart_city_developpement_in_africa.html"),
        name="urban-data-management-for-smart-city-developpement-in-africa",
    ),
    path(
        "moocs/eco-construction-en-afrique/",
        TemplateView.as_view(template_name="home/moocs/eco_construction_en_afrique.html"),
        name="eco-construction-en-afrique",
    ),
    path(
        "moocs/making-housing-work-in-african-cities/",
        TemplateView.as_view(template_name="home/moocs/making_housing_work_in_african_cities.html"),
        name="making-housing-work-in-african-cities",
    ),
    path(
        "moocs/how-can-cities-in-africa-be-smarter/",
        TemplateView.as_view(template_name="home/moocs/how_can_cities_in_africa_be_smarter.html"),
        name="how-can-cities-in-africa-be-smarter",
    ),
    path(
        "moocs/what-can-food-tell-us-about-cities-in-africa/",
        TemplateView.as_view(template_name="home/moocs/what_can_food_tell_us_about_cities_in_africa.html"),
        name="what-can-food-tell-us-about-cities-in-africa",
    ),
    path(
        "moocs/la-fabrique-urbaine-collective/",
        TemplateView.as_view(template_name="home/moocs/la_fabrique_urbaine_collective.html"),
        name="la-fabrique-urbaine-collective",
    ),
    path(
        "moocs/urban-economic-development-in-the-context-of-climate-change/",
        TemplateView.as_view(template_name="home/moocs/urban_economic_development_in_the_context_of_climate_change.html"),
        name="urban-economic-development-in-the-context-of-climate-change",
    ),
    path(
        "moocs/digital-governance-for-a-better-public-participation-and-urban-services-delivery-in-african-cities/",
        TemplateView.as_view(template_name="home/moocs/digital_governance_for_a_better_public_participation_and_urban_services_delivery_in_african_cities.html"),
        name="digital-governance-for-a-better-public-participation-and-urban-services-delivery-in-african-cities",
    ),
    path(
        "moocs/le-solaire-photovoltaïque-et-ses-applications-au-profit-du-developpement-urbain/",
        TemplateView.as_view(template_name="home/moocs/le_solaire_photovoltaïque_et_ses_applications_au_profit_du_developpement_urbain.html"),
        name="le-solaire-photovoltaïque-et-ses-applications-au-profit-du-developpement-urbain",
    ),
    path(
        "moocs/sustainable-urban-systems/",
        TemplateView.as_view(template_name="home/moocs/sustainable_urban_systems.html"),
        name="sustainable-urban-systems",
    ),
    path(
        "moocs/habitat-resilient/",
        TemplateView.as_view(template_name="home/moocs/habitat_resilient.html"),
        name="habitat-resilient",
    ),
    path(
        "moocs/urban-ai/",
        TemplateView.as_view(template_name="home/moocs/urban_ai.html"),
        name="urban-ai",
    ),
    
]
