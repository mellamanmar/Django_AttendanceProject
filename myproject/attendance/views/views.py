from django.shortcuts import render

# Create your views here.

from ..models.students import Students
from ..models.cohorte import Cohorte

def index(request):
    """Function to home site"""
    cohortes= Cohorte.objects.all()
    students= Students.objects.all()

    return render(
        request,
        'attendance/index.html',
        context=
        {
            "cohortes":cohortes,
            "students":students
        }
    )
