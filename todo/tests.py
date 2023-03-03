from django.test import TestCase
from .models import Todo

class TodoModelTestCase(TestCase):

    def setUp(self):
        self.todo = Todo.objects.create(
            name='Test Todo',
            description='Test Todo Description',
            due_date='2022-12-31',
            status='todo',
            priority='yes',
            category='WORK'
        )

    def test_todo_name(self):
        self.assertEqual(self.todo.name, 'Test Todo')

    def test_todo_description(self):
        self.assertEqual(self.todo.description, 'Test Todo Description')

    def test_todo_due_date(self):
        self.assertEqual(str(self.todo.due_date), '2022-12-31')

    def test_todo_status(self):
        self.assertEqual(self.todo.status, 'todo')

    def test_todo_priority(self):
        self.assertEqual(self.todo.priority, 'yes')

    def test_todo_category(self):
        self.assertEqual(self.todo.category, 'WORK')