from django.db import models
import datetime
# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    phone_number = models.IntegerField()
    badge_color = models.CharField(max_length=20)
    email = models.EmailField(max_length=70,blank=True,unique=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name 
    
class Subtask(models.Model):
    description = models.CharField(max_length=200)
    state = models.BooleanField(default=False)
    
    def __str__(self):
        return self.description

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    due_date = models.DateField((), default=datetime.date.today)
    category = models.CharField(max_length=50)
    prio = models.PositiveSmallIntegerField(default=1)
    status = models.CharField(max_length=40)
    assigned_to = models.ManyToManyField(Contact)
    subtasks = models.ManyToManyField(Subtask)
    
    
    def __str__(self):
        return self.title
    
    

    

    