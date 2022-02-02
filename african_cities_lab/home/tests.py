# from django.test import TestCase

from wagtail.tests.utils import WagtailPageTests

from .models import (
    AboutPage,
    ContactPage,
    FlatPage,
    GetInvolvedPage,
    HomePage,
    OnlineCoursesPage,
    TrainingProgramsPage,
)


def test_imports():
    from .models import FlatPage  # noqa: F401


class FlatPageTests(WagtailPageTests):
    def test_can_create_a_page(self):
        self.assertCanCreateAt(FlatPage, FlatPage)


class HomePageTests(WagtailPageTests):
    def test_can_create_pages(self):
        self.assertCanCreateAt(HomePage, AboutPage)
        self.assertCanCreateAt(HomePage, OnlineCoursesPage)
        self.assertCanCreateAt(HomePage, TrainingProgramsPage)
        self.assertCanCreateAt(HomePage, GetInvolvedPage)
        self.assertCanCreateAt(HomePage, ContactPage)
        self.assertCanNotCreateAt(HomePage, FlatPage)
