from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=64)
    age = models.SmallIntegerField()
