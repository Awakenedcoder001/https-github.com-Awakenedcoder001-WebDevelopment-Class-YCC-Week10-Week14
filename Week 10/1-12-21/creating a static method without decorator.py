#Craeting a static method without a decorator: 
class EmployeeDetails: 
 def static_variables(): 
  EmployeeDetails.company_name="TCC" 
  print(f"NAME OF THE COMAPNAY IS : {EmployeeDetails.company_name}") 
 
#Calling a static method using ClassName Refrence 
EmployeeDetails.static_variables() 
 
s1=EmployeeDetails() 
#TypeError : We can not call the static method without the decorator using Obj Refernce 
s1.static_variables()