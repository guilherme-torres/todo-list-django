from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=255)
    finished = models.BooleanField(default=False)
