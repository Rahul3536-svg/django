from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    address = models.CharField(max_length=100)

