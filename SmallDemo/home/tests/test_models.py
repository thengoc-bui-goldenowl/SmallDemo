from urllib import response
from django.test import TestCase, Client, TransactionTestCase
from django.urls import reverse
from home.models import Project, ProjectDev, Dev


class TestModels(TransactionTestCase):
    def setUp(self):
        self.client=Client()
        self.project1=Project.objects.create(
            name="project1",
            des="Nothing",
            start_date="2022-04-04",
            end_date="2022-05-05",
            cost=120
        )
        self.dev1= Dev.objects.create(
            first_name= "John",
            last_name= "Joe",
            language="python",
            active=False
        )

    def test_dev_create(self):
        self.assertEqual(Dev.objects.filter(first_name="John").count(),1)

    def test_project_create(self):
        self.assertEqual(Project.objects.all().count(),1)
    
    def test_projectdev_create(self):
        log=ProjectDev.objects.create(project=self.project1,
        dev=self.dev1,
        status=True)
        self.assertEqual(ProjectDev.objects.count(),1)
    def test_add_dev_to_project(self):
        self.project1.dev.add(self.dev1)
        self.project1.save()
        self.assertEqual(Project.objects.filter(dev__id=self.dev1.id).count(),1)
        