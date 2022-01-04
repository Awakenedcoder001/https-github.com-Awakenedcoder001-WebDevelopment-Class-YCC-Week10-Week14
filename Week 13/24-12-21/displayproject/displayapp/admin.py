from django.contrib import admin
from displayapp.models import Student_Data

# Register your models here.

#Admin view for Student_Data
class Student_DataAdmin(admin.ModelAdmin):

	list_display = ('usn','name','age','gender', 'course')

admin.site.register(Student_Data,Student_DataAdmin)
