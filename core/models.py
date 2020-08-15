from django.db import models
from datetime import datetime


class Blog(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.title

class Registration(models.Model):
    name = models.CharField(max_length=100)
    emailaddress = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class Rank(models.Model):
    name = models.CharField(max_length=100)
    points = models.CharField(max_length=100)
    rank = models.CharField(max_length=10)

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

class Question(models.Model):
    username = models.CharField(max_length=100)
    question = models.CharField(max_length=200)

class Profile_info(models.Model):
    username = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    questions = models.CharField(max_length=100)
    blog = models.CharField(max_length=100)



