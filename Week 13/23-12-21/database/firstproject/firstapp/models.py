from django.db import models

# Create your models here.
class StudentDetails(models,Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	gender = models.CharField(max_length=40)
	did = models.CharField(max_length=40)
	course = models.CharField(max_length=40)

class Meta:
	verboose_name = "StudentDetails"
	verboose_name = "StudentDetailss"
def __str__(self):
	return self.name