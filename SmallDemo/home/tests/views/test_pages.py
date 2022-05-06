from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from home.models import Project, ProjectDev, Dev

class TestPages(TestCase):

    def setUp(self):
        self.client=Client()

    def test_dev_page_get(self):
        response= self.client.get(reverse('dev_page'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'dev/devpage.html')

    def test_project_page_get(self):
        response= self.client.get(reverse('project_page'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'project/projectpage.html')

    def test_count_display_page_get(self):
        response= self.client.get(reverse('count_display', args=(3,)))
        self.assertEquals(response.status_code,200)