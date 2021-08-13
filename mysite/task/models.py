from django.db import models

# Create your models here.
class tugas(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=225)