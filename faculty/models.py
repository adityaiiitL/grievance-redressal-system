from django.contrib.auth.models import User
from django.db import models
from django.forms import DateTimeField
import datetime
from datetime import timezone
from django.utils import timezone
from student.models import Student
from django.utils.timezone import now
# Create your models here.
class Faculty(models.Model):
    faculty_id = models.AutoField
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    contact = models.EmailField(max_length=200) 
    parent = models.ForeignKey('self', blank = True, default=" ",null=True, on_delete=models.CASCADE)
    
class Complain(models.Model): 
    complain_id = models.AutoField
    heading = models.CharField(max_length=300)
    description = models.CharField(max_length=5000)
    registered_to = models.ForeignKey('faculty', on_delete=models.CASCADE)
    complain_response_date = models.DateTimeField(default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(max_length=1,default=" ",null=True)
