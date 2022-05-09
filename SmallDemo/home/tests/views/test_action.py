from urllib import response
from django.test import TestCase, Client, TransactionTestCase
from django.urls import reverse
from home.models import Project, ProjectDev, Dev
import json


class TestCreates(TransactionTestCase):
    def setUp(self):
        self.client = Client()
        self.project1 = Project.objects.create(
            name="project1",
            des="Nothing",
            start_date="2022-04-04",
            end_date="2022-05-05",
            cost=120
        )
        self.dev1 = Dev.objects.create(
            first_name="John",
            last_name="Joe",
            language="python",
            active=False
        )
        self.dev_id = self.dev1.id
        self.project_id = self.project1.id

    def test_home_get(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, "f")

    def test_dev_create_get(self):
        response = self.client.get(reverse('create_dev'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'popup.html')
        self.assertContains(response, "f")

    def test_dev_create_post(self):
        data={
            'active': 'on',
            'first_name': 'Squid',
            'last_name': 'Doe',
            'language': 'C++',
            'project': str(self.project_id)
        }
        data=json.dumps(data)
        response = self.client.post(reverse('create_dev'), data, content_type='application/json' )
        self.assertEqual(Dev.objects.count(), 2)
        self.assertEquals(self.dev1.first_name, "John")
        self.assertEquals(response.status_code, 200)

    def test_project_create_get(self):
        response = self.client.get(reverse('create_project'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'popup.html')
        self.assertContains(response, "f")

    def test_project_create_post(self):
        data={
            'name': "NameTest",
            'des': 'Description',
            'start_date': '2001-02-02',
            'end_date': '2002-02-02',
            'cost': '2500',
            'dev': str(self.dev_id)
        }
        data=json.dumps(data)
        response = self.client.post(reverse('create_project'), data, content_type='application/json')
        self.assertEqual(Project.objects.count(), 2)
        self.assertEquals(self.project1.name, "project1")
        self.assertEquals(response.status_code, 200)

    def test_autocomplete_dev_get(self):
        response = self.client.get(reverse('dev_autocomplete'),data={'term':'j'})
        self.assertEquals(response.status_code, 200)
        
    def test_autocomplete_project_get(self):
        response = self.client.get(reverse('project_autocomplete'),data={'term':'p'})
        self.assertEquals(response.status_code, 200)  

    def test_project_search_name_autocomplete_get(self):
        response = self.client.get(reverse('project_search_name_autocomplete'),data={'term':'p'})
        self.assertEquals(response.status_code, 200) 

    def test_dev_search_name_autocomplete_get(self):
        response = self.client.get(reverse('dev_search_name_autocomplete'),data={'term':'p'})
        self.assertEquals(response.status_code, 200) 

    def test_detail_dev_get(self):
        response = self.client.get(reverse('detail_dev', args=(self.dev_id,)))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail.html')
        self.assertContains(response, "project")

    def test_detail_project_get(self):
        response = self.client.get(
            reverse('detail_project', args=(self.project_id,)))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail.html')
        self.assertContains(response, "project")

    def test_update_dev_get(self):
        response = self.client.get(reverse('dev_update', args=(self.dev_id,)))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dev/updatedev.html')
        self.assertContains(response, "project")
        self.assertContains(response, "f")
    #!!!!!!!!!!!!!!!!!!

    def test_update_dev_patch(self):
        new_project=Project.objects.create(
            name="project1",
            des="Nothing",
            start_date="2022-04-04",
            end_date="2022-05-05",
            cost=120
        )
        self.project1.dev.add(self.dev1)
        data={'active':'on',
        'first_name':'Squid',
        'last_name':'Doe',
        'language':'C++',
        'projects':str(new_project.id)}
        data=json.dumps(data)
        response = self.client.patch(reverse('dev_update', args=(
            self.dev_id,)), data, format="json")
        self.assertEqual(Dev.objects.get(id=self.dev_id).first_name, 'Squid')
        self.assertEquals(response.status_code, 200)

    def test_update_dev_delete(self):
        # dev=self.dev1.id
        self.assertEqual(Dev.objects.count(), 1)
        response = self.client.delete(
            reverse('dev_update', args=(self.dev_id,)))
        self.assertEqual(Dev.objects.count(), 0)
        self.assertEquals(response.status_code, 200)

    # update project
    def test_update_project_get(self):
        project = self.project_id
        response = self.client.get(reverse('project_update', args=(project,)))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/updateproject.html')
        self.assertContains(response, "project")
        self.assertContains(response, "f")

    #!!!!!!!!!!!!!!!!!!
    def test_update_project_patch(self):
        new_dev1=Dev.objects.create(
            first_name="Kalm",
            last_name="Joe",
            language="python",
            active=True
        )
        self.project1.dev.add(self.dev1)
        data = {"name":"TestProjectName",
        "des":"Nothing",
        "start_date":"2000-02-02",
        "end_date":"2001-02-02",
        "cost":"1250",
        "devs":str(new_dev1.id)}
        data=json.dumps(data)
        response = self.client.patch(
            reverse('project_update', args=(self.project_id,)), data, format="json")
        self.assertEqual(Project.objects.get(
            id=self.project_id).name, 'TestProjectName')
        self.assertEquals(response.status_code, 200)

    def test_update_project_delete(self):
        self.assertEqual(Project.objects.count(), 1)
        response = self.client.delete(
            reverse('project_update', args=(self.project_id,)))
        self.assertEqual(Project.objects.count(), 0)
        self.assertEquals(response.status_code, 200)

    def test_search_date_project_get(self):
        data={'start_date':'2022-04-03','end_date':'2022-05-06'}
        project = self.project_id
        response = self.client.get(
            reverse('project_search_date'),data, format="json")
        self.assertTemplateUsed(response, 'project/projectpage.html')
        self.assertEquals(
            response.context['data'][0]['name'], self.project1.name)
        self.assertEquals(response.status_code, 200)

    def test_search_name_project_get(self):
        project = self.project_id
        response = self.client.get(
            reverse('project_search_name'), {'qry':'pr'}, format="json")
        self.assertTemplateUsed(response, 'project/projectpage.html')
        self.assertEquals(response.context['data'][0].name, self.project1.name)
        self.assertEquals(response.status_code, 200)

    def test_search_name_dev_get(self):
        dev = self.dev_id
        response = self.client.get(reverse('dev_search_name'), {'qry':'o'}, format="json")
        self.assertTemplateUsed(response, 'dev/devpage.html')
        self.assertEquals(
            response.context['data'][0].first_name, self.dev1.first_name)
        self.assertEquals(response.status_code, 200)

    def test_lang_get(self):
        response = self.client.get(reverse('language', args=('vi',)))
        self.assertEquals(response.status_code, 200)
