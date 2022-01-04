from django.shortcuts import render
import datetime
# Create your views here.

def greetingmessage(request):
	date=datetime.datetime.now().year
	msg="Goodmorning"
	my_dict={'date':date,'msg':msg}
	return render(request,"seventhapp/display7.html",context=my_dict)
