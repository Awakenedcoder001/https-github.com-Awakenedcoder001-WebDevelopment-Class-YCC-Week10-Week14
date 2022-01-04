class EmployeeDetails: 
 @staticmethod 
 def static_variables(a,b): 
  sum=a+b 
  return sum 
   
s1=EmployeeDetails() 
#Calling a static method using Object Refrence 
result=s1.static_variables(a=10,b=20)#30 
print(result) 
 
#Calling a static method using ClassName 
sum=EmployeeDetails.static_variables(a=30,b=40) #70 
print(sum)