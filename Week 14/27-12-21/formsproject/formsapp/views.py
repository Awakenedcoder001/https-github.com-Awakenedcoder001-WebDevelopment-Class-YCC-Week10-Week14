from django.shortcuts import render
from formsapp.forms import FormDetailsForm
from formsapp.models import FormDetails

# Create your views here.

def form_display(request):
	if request.method =='GET':
		#creating the object of the form from the displaying the form on the web browser
		form=FormDetailsForm()
		return render(request,'formsapp/display.html',context={"form":form})

def form_accept(request):
	if request.method == 'POST':
		#Fetching the data from the browser using request.POST
		form=FormDetailsForm(request.POST)
		
		if form.is_valid():
			form.save()

	form = FormDetailsForm()
	return render(request,'formsapp/display.html',context={"form":form})