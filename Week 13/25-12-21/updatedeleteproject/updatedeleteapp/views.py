from django.shortcuts import render, redirect 
from updatedeleteapp.models import Update_Delete

# Create your views here.
def select_operation(request): #display coursese
	data=Update_Delete.objects.all()
	my_dict={'data':data}

	return render(request,"updatedeleteapp/display.html",context=my_dict)

def update_operation(request):
	data=Update_Delete.objects.filter(sid=1).update(sage=105)
	#data.save()
	return redirect('/select/')#redirect()----inside(django)---and in django it exsists in the S(shortcuts

def delete_operation(request):
	delete=Update_Delete.objects.filter(sid=2).delete()
	return redirect('/select/')

