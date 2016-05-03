from django.db import models
from django.contrib.auth.models import User
from django import forms
    # Create your models here.

class Customer(models.Model):
   user= models.OneToOneField(User,default=None,on_delete=models.CASCADE)
  # blood_group = models.CharField(max_length=30,default=None)  
   # age=models.IntegerField(default=None) 
   # email=models.EmailField(default=None	,null=False)
   # password =models.CharField(max_length=20,default=None,null=True)
  

   def __str__(self):
   		return "%s"%(self.user)   

