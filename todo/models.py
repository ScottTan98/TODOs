from django.db import models

# Create your models here.
class Todo(models.Model):
    STATUS_TYPE = [
        ('todo', 'To do'),
        ('in_progress', 'In progress'),
        ('done', 'Done'),
    ]

    PRIORITY_TYPE = [
        ('yes', 'YES'),
        ('no', 'NO')
    ]

    CATEGORY_TYPE = [
        ('WORK', 'Work'),
        ('PERSONAL', 'Personal'),
        ('SHOPPING', 'Shopping'),
        ('OTHER', 'Other')
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_TYPE)
    priority = models.CharField(max_length=20, null=True , choices=PRIORITY_TYPE)
    category = models.CharField(max_length=20, null=True, choices=CATEGORY_TYPE)

    def __str__(self):
        return self.name