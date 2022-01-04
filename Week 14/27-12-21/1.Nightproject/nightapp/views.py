from django.shortcuts import render
from nightapp.forms import Personal_DetailsForms
from nightapp.models import Personal_Details
from django.db import connection

# Create your views here.

#1 .INSERT OPTION(Single)
def insert_operation(request):
	my_cursor = connection.cursor()

	sql_query_insert = '''insert into `nightapp_Personal_Details` values('bs009','Dophu',22,'Female','Paro')'''

	my_cursor.execute(sql_query_insert)

	records=Personal_Details.objects.all()

	my_dict = {'records':records}
	return render(request,'nightapp/display.html', context=my_dict)

#2 Delete options.(single)
def delete_operation(request):
	my_cursor = connection.cursor()

	sql_query_delete = '''DELETE FROM `nightapp_Personal_Details` WHERE `usn`="bs009"'''
	my_cursor.execute(sql_query_delete)

	records=Personal_Details.objects.all()
	my_dict = {'records':records}
	return render(request,'nightapp/display.html', context=my_dict)

#3. multi_insert_operation
def multi_insert_operation(request):
	my_cursor = connection.cursor()
															#('usn','name','age','gender','location')
	sql_query_multi_insert_operation = '''INSERT INTO `nightapp_Personal_Details` VALUES('001','Leji',25,'Female','Punakha'),('002','Meji',28,'Male','SingyeDzong')'''
	my_cursor.execute(sql_query_multi_insert_operation)

	records=Personal_Details.objects.all()
	my_dict = {'records':records}

	return render(request,'nightapp/display.html',context=my_dict)

#4.




# storage=
# if request.method == 'GET':
# 		form = Personal_DetailsForms()
# 		return render(request,'nightapp/display.html',context={"form": form})

# 	if request.method == 'POST':
# 		formdata=Personal_DetailsForms(request.POST)

# 		if format.is_valid():
# 			format.save()