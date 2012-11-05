from django.db import models


class Post(models.Model):
    heading = models.CharField(max_length=255)
    body = models.TextField()
    visible = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
