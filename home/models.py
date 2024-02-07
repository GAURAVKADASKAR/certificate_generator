from django.db import models
from django.contrib.auth.models import User
class certificate(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    student_email=models.EmailField(unique=True)
    student_name=models.CharField(max_length=100)
class name(models.Model):
    student_name=models.CharField(max_length=100)
    
