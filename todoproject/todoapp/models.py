from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django import forms

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
# date
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    my_date_field = forms.DateField(input_formats=['%d-%m-%Y'])

# register


