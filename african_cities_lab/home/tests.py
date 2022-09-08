from wagtail.tests.utils import WagtailPageTests

from .models import (
    FlatPage,
    HomePage,
)
class FlatPageTests(WagtailPageTests):
    def test_can_create_a_page(self):
        self.assertCanCreateAt(FlatPage, FlatPage)
class HomePageTests(WagtailPageTests):
    def test_can_create_pages(self):
        self.assertCanNotCreateAt(HomePage, FlatPage)
