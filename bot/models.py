from django.db import models

class userInfo(models.Model):
  username = models.TextField()
  password = models.TextField()