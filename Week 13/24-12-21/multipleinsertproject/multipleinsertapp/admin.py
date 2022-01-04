from django.contrib import admin
from multipleinsertapp.models import Student_Details 
# Register your models here.
class Student_DetailsAdmin(admin.ModelAdmin):
	'''
	Admin view for Student_Details
	'''
	list_display = ('sid','sname','sage','dob', 'gender','course')

admin.site.register(Student_Details, Student_DetailsAdmin)


