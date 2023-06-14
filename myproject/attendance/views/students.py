from django.views import generic
from ..models.students import Students

class StudentListView (generic.ListView):
    model= Students
    context_object_name= 'students_list'
    template_name= 'attendance/students/student_list.html'

class StudentDetailView (generic.DetailView):
    model= Students
    context_object_name= 'student_detail'
    template_name= 'attendance/students/student_detail.html'

class StudentCreateView (generic.CreateView):
    model= Students
    fields= [
        'fname',
        'lname',
        'document_type',
        'document_number',
        'cohorte_id'
    ]
    template_name= 'attendance/students/student_forms.html'