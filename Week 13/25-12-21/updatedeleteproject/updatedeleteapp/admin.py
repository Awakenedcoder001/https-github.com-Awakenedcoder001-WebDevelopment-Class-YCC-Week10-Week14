from django.contrib import admin
from updatedeleteapp.models import Update_Delete

# Register your models here.

class Update_DeleteAdmin(admin.ModelAdmin):

	list_display=('sid','susn','name','sage','sgender','scourse')

admin.site.register(Update_Delete, Update_DeleteAdmin)
