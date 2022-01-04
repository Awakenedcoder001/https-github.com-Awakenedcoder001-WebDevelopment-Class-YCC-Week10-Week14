from django.db import models

# Create your models here.
class Personal_Details(models.Model):
	usn = models.CharField(primary_key=True,max_length=50)
	name = models.CharField(max_length=40)
	age = models.IntegerField()
	gender = models.CharField(max_length=70)
	location = models.CharField(max_length=80)


	class Meta:
		verbose_name = "Personal_Details"
		verbose_name_plural = "Personal_Detailss"

	def __str__(self):
		return self.usn
