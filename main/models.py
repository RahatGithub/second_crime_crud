from django.db import models

# Create your models here.
class Case(models.Model):
    id = models.AutoField(primary_key=True)
    case_code = models.CharField(max_length=11)
    location = models.CharField(max_length=300)
    desc = models.CharField(max_length=5000)
    status = models.CharField(max_length=200)
    reporter_name = models.CharField(max_length=50)
    reporter_phone = models.CharField(max_length=20)
    investigator_code = models.CharField(max_length=11)


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    message = models.CharField(max_length=5000)