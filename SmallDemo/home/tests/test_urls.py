from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from home.views import *


class TestUrls(TestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, Home)

    def test_create_project_url_is_resolved(self):
        url = reverse('create_project')
        self.assertEqual(resolve(url).func.view_class, CreateProject)

    def test_create_dev_is_resolved(self):
        url = reverse('create_dev')
        self.assertEqual(resolve(url).func.view_class, CreateDev)

    def test_project_page_url_is_resolved(self):
        url = reverse('project_page')
        self.assertEqual(resolve(url).func.view_class, ProjectPage)

    def test_dev_page_url_is_resolved(self):
        url = reverse('dev_page')
        self.assertEqual(resolve(url).func.view_class, DevPage)

    def test_project_update_url_is_resolved(self):
        url = reverse('project_update', args=(20,))
        self.assertEqual(resolve(url).func.view_class, UpdateProject)

    def test_dev_update_url_is_resolved(self):
        url = reverse('dev_update', args=(20,))
        self.assertEqual(resolve(url).func.view_class, UpdateDev)

    def test_detail_project_url_is_resolved(self):
        url = reverse('detail_project', args=(3,))
        self.assertEqual(resolve(url).func.view_class, DetailProject)

    def test_detail_dev_url_is_resolved(self):
        url = reverse('detail_dev', args=(3,))
        self.assertEqual(resolve(url).func.view_class, DetailDev)

    def test_dev_autocomplete_url_is_resolved(self):
        url = reverse('dev_autocomplete')
        self.assertEqual(resolve(url).func.view_class, DevAutocomplete)

    def test_project_autocomplete_url_is_resolved(self):
        url = reverse('project_autocomplete')
        self.assertEqual(resolve(url).func.view_class, ProjectAutocomplete)

    def test_project_search_name_url_is_resolved(self):
        url = reverse('project_search_name')
        self.assertEqual(resolve(url).func.view_class, SearchNameProject)

    def test_project_search_date_url_is_resolved(self):
        url = reverse('project_search_date')
        self.assertEqual(resolve(url).func.view_class, SearchDateProject)

    def test_dev_search_name_url_is_resolved(self):
        url = reverse('dev_search_name')
        self.assertEqual(resolve(url).func.view_class, SearchNameDev)

    def test_language_url_is_resolved(self):
        url = reverse('language', args=('vi',))
        self.assertEqual(resolve(url).func.view_class, Language)

    def test_count_display_url_is_resolved(self):
        url = reverse('count_display', args=(5,))
        self.assertEqual(resolve(url).func.view_class, CountDisplay)