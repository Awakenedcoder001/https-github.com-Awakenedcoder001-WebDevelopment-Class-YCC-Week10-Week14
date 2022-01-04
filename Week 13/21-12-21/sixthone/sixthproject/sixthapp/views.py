from django.shortcuts import render
import datetime

# Create your views here.
def message_greetings(request):
	date=datetime.datetime.now();
	print(date)
	msg="Hope you have a lovely day ahead"
	my_dict={'date':date,'msg':msg}
	return render(request, 'sixthapp/display.html',context=my_dict)
