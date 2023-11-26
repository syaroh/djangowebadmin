from django.db import models

# Create your models here.

class About(models.Model):
  name = models.CharField(max_length=100)
  keterangan = models.TextField()
  
  def __str__(self):
    return f"{self.name}"

class Home(models.Model):
  name = models.CharField(max_length=255)
  keterangan = models.TextField()
  
  def __str__(self):
    return f"{self.name}"
  
class Blog(models.Model):
  name = models.CharField(max_length=255)
  keterangan = models.TextField()
  

  def __str__(self):
    return f"{self.name}"