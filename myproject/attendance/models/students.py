from django.db import models
from .cohorte import Cohorte
from django.urls import reverse

class Students(models.Model):
    fname= models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    DOCUMENT_TYPE_CHOICE=(
        ("CC", " Cédula de Ciudadanía"),
        ("PPT", "Permiso de Protección Temporal"),
        ("CE", "Cédula de Extranjería"),
        ("TI", "Tarjeta de Identidad"),
    )
    document_type= models.CharField(max_length=5, choices= DOCUMENT_TYPE_CHOICE, default= "CC")
    document_number= models.IntegerField(default=0)
    cohorte_id= models.ForeignKey(Cohorte, null= True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.fname +" "+ self.lname
    
    def get_absolute_url(self):
        return reverse("student_detail", args=[str(self.id)])
    
    