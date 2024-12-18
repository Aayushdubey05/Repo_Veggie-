from django.db import models

# Create your models here.


class  student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField()
    address = models.TextField(null=False,blank=False,default='Mumbai')
    #primary_key = models.AutoField()#primary id 

class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return self.car_name
    