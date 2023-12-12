from django.db import models

# Create your models here.

class About(models.Model):
  name = models.CharField(max_length=100)
  keterangan = models.TextField()
  
  def __str__(self):
    return f"{self.name}"

class Home(models.Model):
  About = models.ForeignKey(About, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  keterangan = models.TextField()
  
  def __str__(self):
    return f"{self.name}"