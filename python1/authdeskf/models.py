from django.db import models

# Create your models here.
class Post(models.Model):
    body = models.TextField()
    dttm_add = models.DataTimeField(auto_now=True)
    author= models.CharField(max_length=255)
    title = models.CharField(max_length=255)
