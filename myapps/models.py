from django.db import models

# Create your models here.

class About(models.Model):
  name = models.CharField(max_length=100)
  keterangan = models.TextField()
  
class Home(models.Model):
  name = models.CharField(max_length=255)
  
class Blog(models.Model):
  name = models.CharField(max_length=255)
  keterangan = models.TextField()
