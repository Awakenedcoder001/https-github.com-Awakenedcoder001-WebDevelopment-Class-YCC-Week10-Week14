from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Greetings(request):
	msg="<h1> Hello World</h1> /n <p>Welcome to Django</p>"
	return HttpResponse(msg)


