from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome_message(request):
	msg="<h1>Hi Zangmo, How do you do?</h1> <p> Momo is bae</p>"
	return HttpResponse(msg)