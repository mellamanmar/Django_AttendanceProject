from django.db import models
from .students import Students


class Attendance(models.Model):
    status= models.BooleanField(default= False)
    excuse= models.BooleanField(default= False)
    excuse_support= models.CharField(max_length= 50)
    date= models.DateField(auto_now= True)
    student= models.ForeignKey(Students,on_delete= models.CASCADE)

    