from django.shortcuts import render
import datetime

# Create your views here.

def welcome_msg(request):
	date=datetime.datetime.now();
	hour = int(date.strftime('%H'))
	

	msg=None

	name = "Tandin"

	if hour < 12:
		msg = "Good Morning"

	elif hour < 16:
		msg = "Good Afternoon"

	elif hour < 20:
		msg = "Goog Evening"

	else:
		msg = "Good Night"



	my_dict={"date":date,"msg":msg,"name":name}
	return render(request,'tenthapp/display.html',context=my_dict)