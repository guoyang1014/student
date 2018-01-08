from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=40)
    high = models.CharField(max_length=20)
    course = models.CharField(max_length=40)
    sex = models.CharField(max_length=20)