from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def greetings(request):
	msg1="<h1>Hello World</h1>"
	msg2="<p>Welcome to Django</p>"

	jengu=msg1+msg2
	return HttpResponse(jengu)


