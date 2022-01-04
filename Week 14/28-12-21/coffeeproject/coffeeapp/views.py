from django.shortcuts import render
from coffeeapp.models import Register_Form

# Create your views here.
def registration_form(request):
	if request.method == "GET":
		return render(request,'coffeeapp/register.html')

	if request.method == "POST":
		data = request.POST.dict();
		#Variablenameofdict['keyname'] keyname = name attr in html
		print(data['fname'])
		print(data['lname'])
		print(data['email'])
		print(data['state'])
		print(data['address'])
		print(data['city'])

		#Modelsname.objects.create(tableattricutes= htmlnameattribute)
		data = Register_Form.objects.create(fname=data['fname'],lname=data['lname'],email=data['email'],address=data['address'],city=data['city'],state=data['state'])
		data.save()

	return render(request,'coffeeapp/success.html',context={"data":data})

