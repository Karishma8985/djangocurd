from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    address  = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    pics = models.ImageField(upload_to='pics')
    
