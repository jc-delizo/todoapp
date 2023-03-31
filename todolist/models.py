from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class ToDoItem(models.Model):
	task_name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	status = models.CharField(max_length=50, default = "pending")
	date_created = models.DateTimeField('date created')
	user= models.ForeignKey(User, on_delete = models.RESTRICT, default = "")

class EventItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)