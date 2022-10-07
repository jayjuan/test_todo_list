from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.task)