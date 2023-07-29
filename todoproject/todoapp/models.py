from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)

# register

# date

