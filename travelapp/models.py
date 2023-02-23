from django.db import models

# Create your models here.
class Place(models.Model):
    name= models.CharField(max_length=250)
    img= models.ImageField('pics')
    desc= models.TextField()
def __str__(self):
    return self.name
class People(models.Model):
    name1=models.CharField(max_length=250)
    img2=models.ImageField('pics')
    des=models.TextField()
def __str__(self):
    return self.name1