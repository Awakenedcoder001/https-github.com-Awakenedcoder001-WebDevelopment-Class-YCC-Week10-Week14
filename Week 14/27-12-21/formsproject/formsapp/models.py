from django.db import models

# Create your models here.
class FormDetails(models.Model):
	usn = models.CharField(primary_key=True,max_length=50)
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	stream = models.CharField(max_length=50)
	section = models.CharField(max_length=50)

	class Meta:
		verbose_name= "FormDetails"
		verbose_name_plural= "FormDetailss"

	def __str__(self):
		return self.usn