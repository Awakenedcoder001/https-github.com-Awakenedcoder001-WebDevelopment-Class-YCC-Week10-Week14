from django.shortcuts import render

# Create your views here.
def github_view(request):

	count=request.session.get('count',0)

	#update the count value
	new_count = count + 1 

	#request.sessions is nothing but a dictionary variable(inside which we have a KEY called count )
	#value for the key is called 'count' and the value is 'new_count'
	request.session['count'] = new_count


	session_date = request.session.get_expiry_date()

	session_age = request.session.get_expiry_age()

	return render(request,'githubapp/display.html',context={"count":new_count,"sessionage":session_age,"sessiondate":session_date})