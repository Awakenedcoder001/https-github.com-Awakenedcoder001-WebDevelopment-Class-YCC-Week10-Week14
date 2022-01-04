from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
	empid = models.IntegerField(primary_key=True)
	empname = models.CharField(max_length=59)
	empdesignation = models.CharField(max_length=59)
	empdepartment = models.CharField(max_length=59)
	empage = models.IntegerField(unique=True)
	empbloodgroup= models.CharField(max_length=59) 
	empemailid= models.CharField(unique=True,max_length=59)

	class Meta:
		verbose_name = "EmployeeDetails"
		verbose_name_plural = "EmployeeDetailss"

	def __str__(self):
		return self.empname +" "+str(self.empid) +""+self.empdesignation +""+self.empdepartment+""+str(self.empage)+""+self.empbloodgroup



