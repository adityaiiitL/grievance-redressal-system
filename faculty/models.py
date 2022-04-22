from django.db import models
from student.models import Student
# Create your models here.
class Faculty(models.Model):
    faculty_id = models.AutoField
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    contact = models.EmailField(max_length=200) 
    parent = models.ForeignKey('self', blank = True, on_delete=models.CASCADE)

class Complain(models.Model): 
    complain_id = models.AutoField
    heading = models.CharField(max_length=300)
    description = models.CharField(max_length=5000)
    registered_to = models.ForeignKey('faculty', on_delete=models.CASCADE)
    user = models.ForeignKey(Student, on_delete=models.CASCADE)