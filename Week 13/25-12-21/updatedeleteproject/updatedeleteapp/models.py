from django.db import models

# Create your models here.
class Update_Delete(models.Model):
	sid = models.AutoField(primary_key = True)
	susn = models.CharField(unique= True, max_length=50)
	name = models.CharField(max_length = 50)
	sage = models.IntegerField()
	sgender = models.CharField(max_length = 50)
	scourse = models.CharField(max_length = 50)

	class Meta:
		verbose_name = "Update_Delete"
		verbose_name_plural = "Update_Deletes"

	def __str__(self):
		return str(self.sid)
