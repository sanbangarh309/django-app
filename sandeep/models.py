from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    image = models.FileField(upload_to='sandeep/static/img/profile/')
    about = models.TextField(null=True)
    password = models.CharField(max_length=100)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=30)
    fb = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    when = models.DateTimeField("date created", auto_now_add=True)

class Project(models.Model):
    name = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    user_id = models.IntegerField()
    image = models.FileField(upload_to='sandeep/static/img/projects/')
    about = models.TextField(null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    when = models.DateTimeField("date created", auto_now_add=True)

class History(models.Model):
    companyname = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    about = models.TextField(null=True)
    when = models.DateTimeField("date created", auto_now_add=True)
