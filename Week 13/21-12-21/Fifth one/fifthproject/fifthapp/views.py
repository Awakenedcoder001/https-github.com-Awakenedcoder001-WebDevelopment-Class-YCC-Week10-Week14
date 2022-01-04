from django.shortcuts import render

# Create your views here.
def welcome_message(request):
	print(request)
	return render(request, 'fifthapp/display.html')
