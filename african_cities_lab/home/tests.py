# from django.test import TestCase

from wagtail.tests.utils import WagtailPageTests

from .models import FlatPage


def test_imports():
    from .models import FlatPage  # noqa: F401


class FlatPageTests(WagtailPageTests):
    def test_can_create_a_page(self):
        self.assertCanCreateAt(FlatPage, FlatPage)
