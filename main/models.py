from django.db import models


class Person(models.Model):
    username = models.CharField(max_length=15)
    email = models.CharField()
    password = models.CharField()
