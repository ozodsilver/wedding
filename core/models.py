from django.db import models

# Create your models here.
class Appeal(models.Model):
    name = models.TextField()
    presence = models.BooleanField()


