from wagtail.tests.utils import WagtailPageTests

from .models import (
    AboutUsPage,
    ContactPage,
    FlatPage,
    GetInvolvedPage,
    HomePage,
    NewsIndexPage,
    NewsPage,
    OnlineCoursesPage,
    TrainingProgramsPage,
)


class FlatPageTests(WagtailPageTests):
    def test_can_create_a_page(self):
        self.assertCanCreateAt(FlatPage, FlatPage)


class HomePageTests(WagtailPageTests):
    def test_can_create_pages(self):
        self.assertCanCreateAt(HomePage, AboutUsPage)
        self.assertCanCreateAt(HomePage, OnlineCoursesPage)
        self.assertCanCreateAt(HomePage, TrainingProgramsPage)
        self.assertCanCreateAt(HomePage, GetInvolvedPage)
        self.assertCanCreateAt(HomePage, ContactPage)
        self.assertCanNotCreateAt(HomePage, FlatPage)
        self.assertCanCreateAt(HomePage, NewsIndexPage)
        self.assertCanCreateAt(NewsIndexPage, NewsPage)
