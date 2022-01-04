from django.contrib import admin
from nightapp.models import Personal_Details

# Register your models here.
class Personal_DetailsAdmin(admin.ModelAdmin):

	list_display = ('usn','name','age','gender','location')

admin.site.register(Personal_Details, Personal_DetailsAdmin)