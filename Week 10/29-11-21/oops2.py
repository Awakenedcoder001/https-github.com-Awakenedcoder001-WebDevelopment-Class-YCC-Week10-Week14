class EmployeeDetails(object): 
 """docstring for ClassName""" 
 def __init__(self,name,age): 
  self.emp_name=name 
  self.emp_age=age 
 
 
 def display(self,gender): 
  self.emp_gender=gender 
  print(f"AGE OF THE EMPLOYEE IS : {self.emp_age}") 
   
 print(f"NAME OF THE EMPLOYEE IS : {self.emp_name} ") 
emp_obj1=EmployeeDetails(name="Pemba",age=30) 
 
emp_obj1.display("Male") 
 
print(f"GENDER OF THE EMPLOYEE IS : {emp_obj1.emp_gender}")


#Traceback (most recent call last): 
  File "D:\Python\OOPS\accessingvariables.py", line 1, in <module> 
    class EmployeeDetails(object): 
  File "D:\Python\OOPS\accessingvariables.py", line 12, in EmployeeDetails 
    print(f"NAME OF THE EMPLOYEE IS : {self.emp_name} ") 
NameError: name 'self' is not defined