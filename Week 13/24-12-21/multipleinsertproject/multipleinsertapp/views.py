from django.shortcuts import render
from multipleinsertapp.models import Student_Details

# Create your views here.
def multiple_insert(request):
	for i in range(2):
		sid = int(input("Enter the ID : "))
		name = input("Enter the name : ")
		age = int(input("Enter the age : "))
		dob = input ("Enter the DOB in DD-MM-YYYY : ")
		gender = input("Enter the gender: ")
		course = input("Enter the course : ")

		Student_Details.object.get_or_create(sid=sid,sname=name,sage=age,dob=dob,course=course)

	return render(request,'multipleinsertapp/display.html')
