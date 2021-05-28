from django.db import models

# Create your models here.
class Member(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length = 20)
    major = models.CharField(max_length = 40)
    year = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField(max_length = 60)
