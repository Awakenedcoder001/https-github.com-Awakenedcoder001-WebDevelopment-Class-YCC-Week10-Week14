class EmployeeDetails: 
 @staticmethod 
 def static_variables(): 
  EmployeeDetails.company_name="TCC" 
  print(f"NAME OF THE COMAPNAY IS : {EmployeeDetails.company_name}") 
 
s1=EmployeeDetails() 
#Calling a sctaic method using Object Refrence 
s1.static_variables() 
print(EmployeeDetails.__dict__)