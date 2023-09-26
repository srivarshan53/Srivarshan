from django.db import models

# Create your models here.
class skills(models.Model):
    skillname = models.CharField(max_length=100)
    skilldesc = models.TextField()
    
class project(models.Model):
    name = models.CharField(max_length=100)
    apptype = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    link = models.CharField(max_length=100)

