from django.shortcuts import render

# Create your views here.
def views_one(request):
	return render(request,'firstapp/view1.html')

def views_two(request):
	return render(request,'firstapp/views2.html')
