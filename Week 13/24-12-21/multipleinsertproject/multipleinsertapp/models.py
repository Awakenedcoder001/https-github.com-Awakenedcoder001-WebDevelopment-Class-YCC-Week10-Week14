from django.db import models

# Create your models here.
class Student_Details(models.Model):
	sid = models.CharField(primary_key= True,max_length=50)
	sname = models.CharField(max_length=50)
	sage = models.PositiveIntegerField()
	dob   = models.CharField(max_length=50)
	gender = models.CharField(max_length=50)
	course = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Student_Details"
		verbose_name_plural = "Student_Detailss" 

	def __str__(self):
		return self.name