from django.shortcuts import render

# Create your views here.
def Thimphu(request):
	name = "Burger Point"
	budget = "Average"
	return render(request,'touristapp/Thimphu.html',context={"name":name,"budget":budget})


def Paro(request):
	name = "NAB"
	reason = "Only draftbeer in the country"
	budgetrange = "Average"

	return render(request,'touristapp/Paro.html',context={"name":name,"reason":reason,"budgetrange":budgetrange})
