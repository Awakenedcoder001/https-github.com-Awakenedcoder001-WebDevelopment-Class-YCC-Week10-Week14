from django.shortcuts import render
from displayapp.models import Student_Data

# Create your views here.

def insert_data(request):
	#Fetching the data in the database:
	#modelsc lastname.object.all()
	# data = student_data.object.all()	

	for i in range(2):
		usn = input("Enter your roll number : ")
		name = input("Enter the name : ")
		age = int(input("Enter the age : "))
		gender=input("Enter the Gender : ")
		course = input("Enter the course : ")

		student_data=Student_Data.objects.create(usn=usn,name=name,age=age,gender=gender,course=course)
		student_data.save()

	
	return render(request,'displayapp/inserting.html')




