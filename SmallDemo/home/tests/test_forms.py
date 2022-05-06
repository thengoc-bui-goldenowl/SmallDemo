from django.test import TestCase
from home.forms import DevForm, ProjectForm, UpdateDevForm, DetailDevForm, \
    DetailProjectForm, UpdateProjectForm


class TestForms(TestCase):
    data_dev={
            'first_name': 'testfirstname',
            'last_name': 'testlastname',
            'language': 'python',
            'active': False

        }
    data_project={
            'name': 'testfirstname',
            'des': 'testlastname',
            'start_date': '2022-02-02',
            'end_date': '2011-02-02',
        
        }
    def test_dev_form_valid_data(self):
        form = DevForm(data=self.data_dev)
        self.assertTrue(form.is_valid)

    def test_dev_form_no_data(self):
        form = DevForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_project_form_valid_data(self):
        form = ProjectForm(data=self.data_project)
        self.assertTrue(form.is_valid)

    def test_project_form_no_data(self):
        form = ProjectForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    def test_update_project_form_valid_data(self):
        form = UpdateProjectForm(data=self.data_project)
        self.assertTrue(form.is_valid)

    def test__update_project_form_no_data(self):
        form = UpdateProjectForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)
         # dev field can be null

    def test_update_dev_form_valid_data(self):
        form = UpdateDevForm(data=self.data_dev)
        self.assertTrue(form.is_valid)

    def test_update_dev_form_no_data(self):
        form = UpdateDevForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
        # active field can be null

    def test_detail_project_form_valid_data(self):
        form = DetailProjectForm(data=self.data_project)
        self.assertTrue(form.is_valid)

    def test__detail_project_form_no_data(self):
        form = DetailProjectForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

    def test_detail_dev_form_valid_data(self):
        form = DetailDevForm(data=self.data_dev)
        self.assertTrue(form.is_valid)

    def test_detail_dev_form_no_data(self):
        form = DetailDevForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
         # active field can be null

