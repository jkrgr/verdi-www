from django.db import models


class Post(models.Model):
    heading = models.CharField(max_length=255)
    body = models.TextField()