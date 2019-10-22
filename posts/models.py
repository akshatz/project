# Create your models here.
from django.db import models


# Create your models here.
class Posts(models.Model):
    email = models.EmailField()
    postdescription = models.CharField(max_length=500)


class Likes(models.Model):
    like = models.IntegerField()


class Comments(models.Model):
    commentdescription = models.CharField(max_length=500)