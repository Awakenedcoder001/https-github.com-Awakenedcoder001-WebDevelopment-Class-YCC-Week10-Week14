from django.contrib import admin
from formsapp.models import FormDetails

# Register your models here.
class FormDetailsAdmin(admin.ModelAdmin):

	list_display = ('usn','name','age','stream','section')

admin.site.register(FormDetails,FormDetailsAdmin)
