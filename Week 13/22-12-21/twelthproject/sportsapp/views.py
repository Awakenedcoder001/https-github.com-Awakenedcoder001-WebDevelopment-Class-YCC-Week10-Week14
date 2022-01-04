from django.shortcuts import render

# Create your views here.
def WWE_Wrestler(request):
	name = "Reymysterio"
	History = "Looks like a butterfly stings like a bee in WWE since 2004"
	return render(request,'sportsapp/WWE_Wrestler.html',context={"name":name, "History":History})

def Esports_Gamers(request):
	name = "Dendi"
	Team = "Navi"
	Fame = "TI1"
	return render(request,'sportsapp/Esports_Gamers.html',context={"name":name, "Team":Team, "Fame":Fame})

def Dance_off(request):
	name = "Ranveer kapoor"
	country = "India"
	Profession = "Actor"
	return render(request,'sportsapp/Dance_off.html',context={"name":name,"country":country,"Profession":Profession})
