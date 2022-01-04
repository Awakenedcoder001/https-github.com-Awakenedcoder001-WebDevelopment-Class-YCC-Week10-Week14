from django.db import models

# Create your models here.
class Register_Form(models.Model):
	fname = models.CharField(max_length = 50)
	lname = models.CharField(max_length = 50)
	email = models.CharField(unique=True,max_length=40)
	address = models.CharField(max_length=60)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)

	class META:
		verbose_name = "Register_Form"
		verbose_name_plural= "Register_Forms"


	def __str__(self):
		return self.fname
