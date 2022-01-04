class EmployeeDetails(object): 
 """docstring for ClassName""" 
 def __init__(self,name,age): 
  #Creating the Instance variables inside the constructor 
  self.emp_name=name 
  self.emp_age=age 
 
 def display(self,gender): 
  #Creating Instance Variaboe inside Instace method 
  self.emp_gender=gender 
  print(f"NAME OF THE EMPLOYEE IS : {self.emp_name} ") 
  print(f"AGE OF THE EMPLOYEE IS : {self.emp_age}") 
  print(f"GENDER OF THE EMPLOYEE IS : {self.emp_gender}") 
 
emp_obj1=EmployeeDetails(name="Pemba",age=30) 
#Syntax for checking instance variables outside the class 
#objrefernce.__dict__ 
 
print(emp_obj1.__dict__) 
 
emp_obj1.display(gender="Male") 
print(emp_obj1.__dict__) 
 
#Craete the instance variable outside the class. 
#objrefernce.varabiablename = objectvalue 
 
emp_obj1.weight=65.5 
print(emp_obj1.__dict__)