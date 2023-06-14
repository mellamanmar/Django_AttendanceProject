from django.contrib import admin

# Register your models here.

from .models.cohorte import Cohorte
from .models.students import Students
from .models.attendance import Attendance


admin.site.register(Cohorte)
admin.site.register(Students)
admin.site.register(Attendance)