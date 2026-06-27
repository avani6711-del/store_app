from django.db import models

# Create your models here.
class CustomerModel(models.Model):
    name=models.CharField()
    age=models.IntegerField()
    phone=models.IntegerField()
    email=models.TextField(max_length=200)
    address=models.TextField()
    password=models.CharField(max_length=8)
    confrim_password=models.CharField(max_length=8)

def __str__(self):
    return self.name
