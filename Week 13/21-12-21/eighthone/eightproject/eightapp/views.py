from django.shortcuts import render
import datetime

# Create your views here.
def greetings(request):
	date=datetime.datetime.now();
	hour=int(date.strftime("%H"))

	greeting = None
	if hour < 12:
		greeting = "Good Morning"
	elif hour < 16:
		greeting = "Good Afternoon"
	elif hour < 20 :
		greeting = "Good Evening"
	else:
		greeting = "Good Night"


	my_dict={'date':date,'greeting':greeting}
	return render(request,"eightapp/display.html",context=my_dict)	
