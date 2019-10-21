from django.contrib.auth.models import User
from django.db import models


class Posts(models.Model):
    email = models.EmailField()
    postdescription = models.CharField(max_length=500)


class Likes(models.Model):
    like = models.IntegerField()


class Comments(models.Model):
    commentdescription = models.CharField(max_length=500)
