from django.contrib import admin
from adminapp.models import EmployeeDetails
# Register your models here.
class EmployeeDetailsAdmin(admin.ModelAdmin):
#'''Admin View for EmployeeDetails'''
	list_display = ('empid','empname','empdesignation','empdepartment','empage','empbloodgroup','empemailid')

admin.site.register(EmployeeDetails, EmployeeDetailsAdmin)
#admin.site.registration(EmployeeDetails,EmployeeDetailsAdmin)
