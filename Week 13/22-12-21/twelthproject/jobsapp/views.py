from django.shortcuts import render


# Create your views here.
def salt_is_bae(request):
	name = "Tandin"
	msg = "Congratulation you made it to google"
	my_dict={"name":name, "msg":msg}
	return render(request,'jobsapp/salt_is_bae.html',context=my_dict)

def pornhub_company(request):
	name = "Tshewang"
	msg = "I knew you could do it "
	my_dict = {"name":name,"msg":msg}
	return render(request,'jobsapp/pornhub_company.html',context=my_dict)

def youtube_company(request):
	name = "Sonam"
	msg = "Time to shine"
	my_dict={"name": name,"msg":msg}
	return render(request,'jobsapp/youtube_company.html',context=my_dict)