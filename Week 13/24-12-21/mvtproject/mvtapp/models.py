from django.db import models

# Create your models here.
class Webdevelopment_Details(models.Model):
	did = models.CharField(primary_key=True,max_length=50)
	name = models.CharField(max_length=50)
	age = models.integerField()
	phone_no = models.BigIntegerField(unique=True)
	gender = models.CharField(max_length=50)
	
