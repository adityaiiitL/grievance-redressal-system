from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField
    student = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    
