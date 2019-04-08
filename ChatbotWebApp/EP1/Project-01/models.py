from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# This is a model of the table we have created. file_name, location, description are all
# the column names


class Post(models.Model):
    post = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class File_Details(models.Model):
    file_name = models.CharField(max_length=200, default='insert a file name')
    location = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='insert a description for this file')

    def __str__(self):
        return self.file_name


class Ticket(models.Model):
    queue = models.CharField()
    description = models.TextField(blank=True, null=True)
    priority = models.CharField()
    email = models.EmailField()
