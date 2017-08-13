from django.test import TestCase
from todo.models import todo


class TestModelClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        # Set up non-modified objects used by all test methods
        todo.objects.create(title="test", description="test description",
                            done=False)

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_title_verbose_name(self):
        print("test title verbose name")
        t = todo.objects.get(id=1)
        title_field_label = t._meta.get_field('title').verbose_name
        self.assertEquals(title_field_label, 'title')

    def test_todo_str(self):
        t = todo.objects.get(id=1)
        expected_object_name = '%s, %s, %s' % (t.title, t.description, t.done)
        self.assertEquals(expected_object_name, str(t))
