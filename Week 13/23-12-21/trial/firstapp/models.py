from django.db import models

# Create your models here.
class StudentDetails(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	gender = models.CharField(max_length=50)
	did = models.CharField(primary_key=True,max_length=50)
	course = models.CharField(max_length=50)

	class Meta:
		verbose_name = "StudentDetails"
		verbose_name_plural = "StudentDetails"

	def __str__(self):
		return self.name