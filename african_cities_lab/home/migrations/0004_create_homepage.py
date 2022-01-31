# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from wagtail.core.models import Locale
from african_cities_lab.home.models import FlatPage
from wagtail_localize.models import LocaleSynchronization

from django.conf import settings

def create_homepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    Page = apps.get_model('wagtailcore.Page')
    Site = apps.get_model('wagtailcore.Site')
    HomePage = apps.get_model('home.HomePage')

    # Delete the default homepage
    Page.objects.filter(id=2).delete()

    english = Locale.objects.get()


    # Create content type for homepage model
    homepage_content_type, __ = ContentType.objects.get_or_create(
        model='homepage', app_label='home')

    # Create a new homepage
    homepage = HomePage.objects.create(
        title="Home",
        slug='home',
        content_type=homepage_content_type,
        path='00010001',
        depth=2,
        numchild=0,
        url_path='/home/',
        locale_id=1,
    )

    # Create a site with the new homepage set as the root
    Site.objects.create(
        hostname='localhost', root_page=homepage, is_default_site=True)

    for lang_code, label in settings.LANGUAGES:
        if settings.LANGUAGE_CODE != lang_code:
            if not Locale.objects.filter(language_code=lang_code).exists():
                lang_locale = Locale.objects.create(language_code=lang_code)
            if not LocaleSynchronization.objects.filter(locale=lang_locale, sync_from=english).exists():
                LocaleSynchronization.objects.create(locale=lang_locale, sync_from=english)

class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize', '__latest__'),
        ('wagtailsearch', '__latest__'),
        ('home', '0003_homepage'),
    ]

    operations = [
        migrations.RunPython(create_homepage),
    ]
