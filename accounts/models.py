from django.db import models

# Create your models here.
class Reporter(models.Model):
    id = models.AutoField(primary_key=True)
    reporter_code = models.CharField(max_length=11)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cases = models.CharField(max_length=5000)

class Investigator(models.Model):
    id = models.AutoField(primary_key=True)
    investigator_code = models.CharField(max_length=11)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cases = models.CharField(max_length=5000)