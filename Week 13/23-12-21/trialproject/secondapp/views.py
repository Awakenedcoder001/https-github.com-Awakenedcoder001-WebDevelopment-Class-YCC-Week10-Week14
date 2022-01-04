from django.shortcuts import render

# Create your views here.
def views_one(request):
	return render(request,'secondapp/viewone.html')

def views_two(request):
	return render(request,'secondapp/viewstwo.html')
