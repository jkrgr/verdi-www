from django.db import models
from  django.contrib.auth.admin import User



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    position = models.CharField(max_length=255)

