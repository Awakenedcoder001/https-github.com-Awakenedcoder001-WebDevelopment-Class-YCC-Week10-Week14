from django.db import models
GENDERCHOICES=[
	("Male","Male"),
	("Female","Female"),
	("Others", "Others"),
	("Animals","Animals")
]

# Create your models here.
class Student_Data(models.Model):
	usn = models.CharField(primary_key=True,max_length=50)
	name= models.CharField(max_length=50)
	age = models.IntegerField()
	gender = models.CharField(choices = GENDERCHOICES,max_length=50,default=1)
	course = models.CharField(max_length=50)


	class Meta:
		verbose_name="Student_Data"
		verbose_name_plural = "Student_Datas"

	def __str__(self):
		return self.usn






