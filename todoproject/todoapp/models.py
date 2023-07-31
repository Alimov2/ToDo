from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django import forms
from django.contrib.auth.models import AbstractUser

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
# date
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    my_date_field = forms.DateField(input_formats=['%d-%m-%Y'])

# register

class UserProfile(AbstractUser):
    password_confirmation = models.CharField(max_length=128)
    groups = models.ManyToManyField('auth.Group', blank=True, related_name='todoapp_userprofile')
    user_permissions = models.ManyToManyField('auth.Permission', blank=True, related_name='todoapp_userprofile')

    def __str__(self):
        return self.username
